from dotenv import load_dotenv
import errors
from google import genai
from pathlib import Path

import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise errors.APIERROR
    
# client = genai.Client()

for file in Path('./Imported Patient Notes').iterdir():
    print(file)
    # my_file = client.files.upload(file)
    # with open('uri.txt', 'r') as uri_editor:
    #     uri_editor.write(f'The File name:{file}')
    #     uri_editor.write(f'It\'s URI: {my_file.uri}')
    # print(f'URI {my_file.uri}')
