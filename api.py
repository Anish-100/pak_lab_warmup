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
response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="How is the weather in Irvine, California today ?")

number = 1
with open (f'data/GEMINI RESPONSE {number}','w') as file:
    file.write(response.text)
    print(response.text)



