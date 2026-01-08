import os
import json
from classes import IAagent, AnkiGenerator, Words
from dotenv import load_dotenv 
from prompts import PROMPT_TEMPLATE

load_dotenv()
API_KEY = os.getenv("API_KEY")

leitor = Words("words.txt")
lista_palavras = leitor.read_words()

if lista_palavras and API_KEY:
    print(f"Lendo {len(lista_palavras)} palavras...")

    palavras_str = ", ".join(lista_palavras)
    prompt_final = PROMPT_TEMPLATE.format(palavras=palavras_str)

    agente = IAagent(API_KEY)
    print("Consultando o Gemini...")
    json_texto = agente.gemini(prompt_final)

    try:
        cards_name = input("Digite o nome dos cards:")
        dados_estruturados = json.loads(json_texto)
        anki_gen = AnkiGenerator("Inglês Speed Notes")
        anki_gen.create_apkg(dados_estruturados, f"{cards_name}.apkg")

    except json.JSONDecodeError:
        print("Erro: A IA não retornou um JSON válido.")
        print("Resposta crua:", json_texto)
else:
    print("Verifique se o arquivo words.txt existe e se o .env está configurado.")