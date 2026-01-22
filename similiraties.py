from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print(f'The api key does not exist')
else:
    print(f'Api key recieved')
