# Chatbot Gênis

Gênis é um chatbot dinâmico e inteligente que utiliza dados de uma planilha no Google Sheets para responder perguntas de maneira interativa. Projetado com uma interface moderna e intuitiva, ele oferece suporte a consultas em tempo real, integração com APIs e respostas aleatórias para tornar a interação mais natural.

---

## **Funcionalidades**

- **Integração com Google Sheets**: Faz consultas em tempo real a uma planilha hospedada no Google Sheets utilizando a API do Google.
- **Respostas Baseadas em Dados**: Responde perguntas relacionadas aos registros da planilha, como **nome**, **idade**, **profissão**, **cidade**, **hobby** e **salário**.
- **Respostas Randomizadas**: Oferece respostas variadas para tornar a interação mais fluida e natural.
- **Interface Gráfica Intuitiva**: Desenvolvida com **customtkinter**, proporcionando uma experiência moderna e amigável ao usuário.

---

## **Requisitos do Projeto**

- **Python**: Versão 3.8 ou superior.
- **Bibliotecas Necessárias**:
  - `requests`
  - `customtkinter`

---

## **Configuração**

### 1. **Clonar o Repositório**

Clone este repositório para o seu computador:

```bash
git clone https://github.com/seu-repositorio/chatbot-genis.git
cd chatbot-genis
```

### 2. **Configurar o Ambiente Virtual**

Crie e ative um ambiente virtual. Em seguida, instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # Para Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. **Configurar a API**

- **Passo 1**: Crie uma conta no [Google Cloud Console](https://console.cloud.google.com/).
- **Passo 2**: Ative a **Google Sheets API** no projeto.
- **Passo 3**: Gere uma **Chave de API**.
- **Passo 4**: Atualize os valores `sheet_id` e `api_key` no arquivo `chatbot.py` com os seus dados:

```python
sheet_id = "SEU_SHEET_ID"
api_key = "SUA_API_KEY"
```

- O `sheet_id` pode ser encontrado na URL da sua planilha, por exemplo:

```plaintext
https://docs.google.com/spreadsheets/d/<sheet_id>/edit
```

---

## **Como Rodar o Projeto**

Execute o arquivo principal para iniciar o chatbot:

```bash
python chatbot.py
```

A interface gráfica será exibida. Você pode inserir perguntas relacionadas aos dados da planilha para interagir com o chatbot.

---

## **Estrutura do Projeto**

```plaintext
Chatbot_Genis/
│
├── chatbot.py               # Código principal do chatbot
├── GoogleSheetsAPI.py       # Classe para integração com a API do Google Sheets
├── requirements.txt         # Lista de dependências do projeto
├── README.md                # Documentação do projeto
└── assets/                  # Pasta para imagens ou capturas de tela
```

---

## **Exemplo de Uso**

### Perguntas que o chatbot pode responder:

- "Quem é o médico?"
- "Quais são os hobbies?"
- "Qual o salário dos engenheiros?"
- "Liste os nomes."

### **Saída esperada**:

```plaintext
Você: Quem é o médico?
Gênis: Encontrei algo relacionado:
Nome: Alice, Idade: 25, Profissão: Médico, Cidade: Recife, Hobby: Jogar Vôlei, Salário: R$ 15.000,00.
```

---

## **Capturas de Tela**

Adicione capturas de tela do chatbot em funcionamento na pasta `assets/`.

---

## **Problemas Conhecidos**

- **Cabeçalhos na Planilha**: Certifique-se de que os cabeçalhos na planilha estão no formato correto.
- **Conexão com a API**: Em caso de erro de conexão, verifique a chave de API, as permissões da planilha e o alcance dos dados públicos.

---

## **Contribuições**

Contribuições são bem-vindas! Para contribuir:

1. Faça um **fork** do repositório.
2. Crie uma **branch** para a sua feature:

   ```bash
   git checkout -b feature/sua-feature
   ```

3. Faça o **commit** das alterações:

   ```bash
   git commit -m "Adicionei minha feature"
   ```

4. Envie para o repositório original:

   ```bash
   git push origin feature/sua-feature
   ```

5. Abra um **Pull Request**.

