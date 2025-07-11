from google.genai import Client
from google.genai.types import GenerateContentConfig

from model import Joins

def load_prompt(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()

def load_sql(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()

def main():
    sql = load_sql('query.sql')
    prompt = load_prompt('prompt.md')
    prompt = prompt.replace('[SQLQUERY]', sql)

    client: Client = Client()
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt,
        config=GenerateContentConfig(
            response_mime_type='application/json',
            response_schema=Joins,
        ),
    )
    print(response.text)

if __name__ == "__main__":
    main()
