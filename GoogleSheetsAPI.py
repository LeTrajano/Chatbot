import requests

class GoogleSheetsAPI:
    def __init__(self, sheet_id, api_key):
        self.sheet_id = sheet_id
        self.api_key = api_key

    def fetch_data(self):
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{self.sheet_id}/values/A1:F10?key={self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return self.parse_sheet_data(data)
        except requests.exceptions.RequestException as e:
            return {"error": f"Erro ao acessar a API: {e}"}

    def parse_sheet_data(self, raw_data):
        try:
            headers = raw_data["values"][0]
            rows = raw_data["values"][1:]
            return [dict(zip(headers, row)) for row in rows]
        except KeyError:
            return {"error": "Formato de dados inválido recebido da API"}
