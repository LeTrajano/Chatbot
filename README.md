# Chatbot Gênis
Gênis é um chatbot inteligente que utiliza dados de uma planilha no Google Sheets para responder perguntas de forma dinâmica. Ele foi projetado para ser funcional, intuitivo e escalável, com suporte a respostas baseadas nos dados da planilha e integração com a API do Google Sheets.

### Funcionalidades
Integração com Google Sheets: Faz consultas diretas a uma planilha hospedada no Google Sheets.
Respostas baseadas em dados: Responde perguntas sobre nome, idade, profissão, cidade, hobby e salário de registros.
Respostas Randomizadas: Torna as interações mais naturais com mensagens variadas.
Interface intuitiva: Desenvolvida com customtkinter para uma experiência de usuário moderna.
Requisitos do Projeto
Python 3.8+
Bibliotecas Necessárias:
requests
customtkinter
Configuração
1. Clonar o Repositório
Baixe ou clone este projeto para o seu computador:

bash

git clone https://github.com/seu-repositorio/chatbot-genis.git
cd chatbot-genis
2. Configurar o Ambiente
Certifique-se de que possui um ambiente virtual configurado. Em seguida, instale as dependências do projeto:

bash

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Configurar a API
Crie uma conta no Google Cloud Console.
Ative a Google Sheets API no projeto.
Gere uma chave de API.
Substitua os valores de sheet_id e api_key no arquivo chatbot.py:
python

sheet_id = "SEU_SHEET_ID"
api_key = "SUA_API_KEY"
O sheet_id pode ser encontrado na URL da sua planilha Google, por exemplo:

bash

https://docs.google.com/spreadsheets/d/<sheet_id>/edit
Como Rodar o Projeto
Execute o arquivo principal:
bash

python chatbot.py
A interface gráfica será exibida. Insira perguntas relacionadas aos dados da planilha.
Estrutura do Projeto
plaintext

Chatbot_Genis/
│
├── chatbot.py               # Código principal do chatbot
├── GoogleSheetsAPI.py       # Classe para integração com a API do Google Sheets
├── requirements.txt         # Lista de dependências do projeto
├── README.md                # Documentação do projeto
└── assets/                  # Pasta para imagens ou capturas de tela
Exemplo de Uso
Perguntas que o chatbot pode responder:
"Quem é o médico?"
"Quais são os hobbies?"
"Qual o salário dos engenheiros?"
"Liste os nomes."
Saída esperada:
plaintext

Você: Quem é o médico?
Gênis: Encontrei algo relacionado:
Nome: Alice, Idade: 25, Profissão: Médico, Cidade: Recife, Hobby: Jogar Vôlei, Salário: R$ 15.000,00.
Captura de Tela

Problemas Conhecidos
Certifique-se de que os cabeçalhos na planilha estejam no formato correto.
Em caso de erro de conexão com a API, verifique a chave de API ou as permissões da planilha.
Contribuições
Contribuições são bem-vindas! Para contribuir:

Faça um fork do repositório.
Crie uma branch para a sua feature (git checkout -b feature/sua-feature).
Faça o commit das alterações (git commit -m 'Adicionei minha feature').
Envie para o repositório original (git push origin feature/sua-feature).
Abra um Pull Request.
