import os

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print(f'The api key does not exist')


