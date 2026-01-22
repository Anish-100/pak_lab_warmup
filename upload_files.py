from dotenv import load_dotenv
import errors
from google import genai
from pathlib import Path

import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise errors.APIERROR
    
client = genai.Client()

for file_name in Path('./Imported Patient Notes').iterdir():
    print(file_name)
    my_file = client.files.upload(file=file_name,
    config = {
        'display_name': f'{file_name}'
    })
    with open('./data/uri.txt', 'a') as uri_editor:
        uri_editor.write(f'The File name:{file_name}')
        uri_editor.write(f'It\'s Gemini Name: {my_file.name}')
        uri_editor.write(f'It\'s URI: {my_file.uri}')
        uri_editor.write(f'What is returned: {my_file}')
    print(f'URI {my_file.uri}')

with open('./data/uri.txt', 'r') as file:
    content = file.read()
    lines = content.split('The File name:')

with open('./data/uri.txt', 'w') as f:
    for i, part in enumerate(lines):
        f.write(f"=== Part {i} ===\n") # Ignore Part 0
        f.write(part.strip() + '\n\n')