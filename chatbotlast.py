from GoogleSheetsAPI import GoogleSheetsAPI
import customtkinter as ctk
import random

class Chatbot:
    def __init__(self, master, api):
        self.master = master
        self.api = api

        master.title("Gênis")
        master.geometry("600x500")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.text_area = ctk.CTkTextbox(master, width=500, height=300, wrap="word")
        self.text_area.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.text_area.insert(
            ctk.END,
            "Olá! Eu sou a Gênis, sua assistente virtual.\n"
            "Você pode perguntar sobre 'nome', 'idade', 'profissão', 'cidade', 'hobby' ou 'salário'.\n"
        )
        self.text_area.configure(state="disabled")

        self.entry = ctk.CTkEntry(master, width=400, placeholder_text="Digite sua pergunta aqui...")
        self.entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.entry.bind("<Return>", self.process_input)

        self.send_button = ctk.CTkButton(master, text="Enviar", fg_color="blue", command=self.process_input)
        self.send_button.grid(row=2, column=0, padx=20, pady=10)

    def process_input(self, event=None):
        user_input = self.entry.get().strip().lower()
        if not user_input:
            return

        self.text_area.configure(state="normal")
        self.text_area.insert(ctk.END, f"Você: {user_input}\n")

        data = self.api.fetch_data()
        if "error" in data:
            self.text_area.insert(ctk.END, f"Gênis: {data['error']}\n")
        else:
            response = self.get_bot_response(user_input, data)
            self.text_area.insert(ctk.END, f"Gênis: {response}\n")

        self.text_area.configure(state="disabled")
        self.entry.delete(0, ctk.END)

    def get_bot_response(self, user_input, data):
        random_responses = [
            "Interessante! Deixe-me verificar...",
            "Certo! Vou conferir isso para você.",
            "Um momento, vou dar uma olhada nos dados.",
        ]
        self.text_area.insert(ctk.END, random.choice(random_responses) + "\n")

        if "listar" in user_input or "quais" in user_input:
            if "nome" in user_input:
                return self.list_column(data, "Nome")
            if "profissão" in user_input:
                return self.list_column(data, "Profissão")
            if "idade" in user_input:
                return self.list_column(data, "Idade")
            if "cidade" in user_input:
                return self.list_column(data, "Cidade")
            if "hobby" in user_input:
                return self.list_column(data, "Hobby")
            if "salário" in user_input:
                return self.list_column(data, "Salário")
            return "Por favor, especifique a coluna que deseja listar."

        for item in data:
            if any(str(value).lower() in user_input for value in item.values()):
                return (
                    f"Encontrei algo relacionado:\n"
                    f"Nome: {item['Nome']}, Idade: {item['Idade']}, Profissão: {item['Profissão']}, "
                    f"Cidade: {item['Cidade']}, Hobby: {item['Hobby']}, Salário: {item['Salário']}."
                )

        return "Desculpe, não encontrei informações relacionadas à sua pergunta."

    def list_column(self, data, column_name):
        try:
            values = [item[column_name] for item in data if column_name in item]
            if values:
                return f"Os dados da coluna '{column_name}' são:\n" + "\n".join(values)
            else:
                return f"Desculpe, não encontrei dados para a coluna '{column_name}'."
        except KeyError:
            return f"Coluna '{column_name}' não encontrada."


if __name__ == "__main__":
    sheet_id = "1EDZFsOumITDewnNW0dOiHo8nTwbuHSHpmozhNzjTZQk"
    api_key = "AIzaSyCKdPa6h_JJfq75Tg-uZdHBqDc_xgKz3fw"
    api = GoogleSheetsAPI(sheet_id, api_key)

    root = ctk.CTk()
    chatbot = Chatbot(root, api)
    root.mainloop()
