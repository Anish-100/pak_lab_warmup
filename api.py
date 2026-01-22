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
print(f'STarted')
response = client.models.generate_content(
    model="gemini-3-flash-preview",
      contents= [
           {"file_data": {
                "mime_type": "text/plain", 
                "file_uri": 'https://generativelanguage.googleapis.com/v1beta/files/6zg544t22ssc'
          }},
          {"file_data": {
                "mime_type": "text/plain", 
                "file_uri": 'https://generativelanguage.googleapis.com/v1beta/files/c63uveu246wb'
          }},
          {"file_data": {
                "mime_type": "text/plain", 
                "file_uri": 'https://generativelanguage.googleapis.com/v1beta/files/4m6zospul0qb'
          }},
          {"file_data": {
                "mime_type": "text/plain", 
                "file_uri": 'https://generativelanguage.googleapis.com/v1beta/files/1cbhevq1gldq'
          }},
            
            "I’ve attached a few de-identified doctor notes about patients getting admitted to a hospital for possible infections."
            " Create 10 synthetic notes that mimic the writing style and formatting of these examples, but also reflect the diversity"
            " of all kinds of patients and infections that a US urban hospital might see."
            "The content and patient scenarios can be anything plausible and should vary naturally throughout the notes. "
            "Ensure the notes are similar to the examples, they should all “feel” like they were part of some larger dataset that was taken from a real hospital."
            "Common diseases dataset: https://hcup-us.ahrq.gov/reports/statbriefs/sb277-Top-Reasons-Hospital-Stays-2018.pdf "
            "Ensure the tone is maintained."
            "Generate the text and separate it by a row of ########"
                ]
    )

print('Ended')
number = 5
with open (f'data/GEMINI RESPONSE {number}','w') as file:
    file.write(response.text)
    print(response.text)



