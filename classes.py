import os
import genanki
from google import genai

class Words:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_words(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

class IAagent:
    def __init__(self, api_key, model="gemini-2.5-flash"):
        self.api_key = api_key
        self.model = model

    def gemini(self, content):
        client = genai.Client(api_key=self.api_key)
        response = client.models.generate_content(
            model=self.model, 
            contents=content,
            config={'response_mime_type': 'application/json'}
        )
        return response.text

class AnkiGenerator:
    def __init__(self, deck_name="Inglês Speed Notes"):
        self.deck_name = deck_name

        self.model_id = 1607392319 
        self.deck_id = 2059400110

        self.model = genanki.Model(
            self.model_id,
            'Modelo Flashcard Pro',
            fields=[
                {'name': 'Termo'},
                {'name': 'IPA'},
                {'name': 'Traducao'},
                {'name': 'Exemplo'},
                {'name': 'Nota'},
            ],
            templates=[{
                'name': 'Card 1',
                'qfmt': '''
                    <div style="font-family: Arial; text-align: center; font-size: 30px; font-weight: bold; color: #2c3e50;">
                        {{Termo}}
                    </div>
                    <div style="text-align: center; font-size: 18px; color: #7f8c8d; margin-top: 5px;">
                        {{IPA}}
                    </div>
                ''',
                'afmt': '''
                    {{FrontSide}}
                    <hr id=answer>
                    <div style="text-align: center; font-size: 24px; color: #27ae60; font-weight: bold;">
                        {{Traducao}}
                    </div>
                    <br>
                    <div style="font-style: italic; background-color: #f1f1f1; padding: 10px; border-radius: 5px; font-size: 18px;color:black;">
                        "{{Exemplo}}"
                    </div>
                    <div style="text-align: right; font-size: 12px; color: #c0392b; margin-top: 10px;">
                        {{Nota}}
                    </div>
                ''',
            }]
        )
        self.deck = genanki.Deck(self.deck_id, self.deck_name)

    def create_apkg(self, json_data, output_file="output.apkg"):
        for card in json_data:
            note = genanki.Note(
                model=self.model,
                fields=[
                    card.get('termo', ''),
                    card.get('ipa', ''),
                    card.get('traducao', ''),
                    card.get('exemplo', ''),
                    card.get('nota', '')
                ]
            )
            self.deck.add_note(note)
        genanki.Package(self.deck).write_to_file(output_file)
        print(f"✅ Sucesso! Arquivo '{output_file}' criado com {len(json_data)} cards.")
