# apiRestv1
v1

Aplicação de Cliente > Entrega 

comandos para rodar api:
[
cd api
python -m venv venv
# No Windows use: .\venv\Scripts\activate
# No Linux/Mac use: source venv/bin/activate
pip install -r requirements.txt

uvicorn app.main:app --reload
]python version needs to be 3.12.13 or older(3.13 falta alguma coisa e o pip isntall não funciona)

comandos para rodar front 
[
cd client
npm install
npm start
]
