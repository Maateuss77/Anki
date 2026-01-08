PROMPT_TEMPLATE = """
Você é um professor de inglês nativo.
Converta a lista de palavras abaixo em um JSON Array estrito.

Regras:
1. Verbos: Se irregular, coloque [passado, particípio].
2. Tradução: Português direto.
3. Exemplo: Nível B2/C1.
4. Nota: US ou UK (se relevante).

Formato de Saída (JSON Puro):
[
  {{
    "termo": "Word",
    "traducao": "Tradução",
    "exemplo": "Sentence example",
    "ipa": "/ipa/",
    "nota": "US"
  }}
]

Palavras: {palavras}
"""