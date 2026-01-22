from dotenv import load_dotenv
import errors
import time
from google import genai
from google.genai import types
from pathlib import Path

import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise errors.APIERROR
    
prompt = """
      # ROLE
After every 25 notes, clear our your memory regarding any generated text in the chat, and redo the below prompt:

You are a Clinical Documentation Expert. Your task is to generate synthetic hospital admission notes that are indistinguishable from real-world EHR (Electronic Health Record) data.
#TASK
Generate the FIRST BATCH (Notes 1-10) of a 500-document synthetic EHR dataset. You must maintain the exact stylistic and structural "Gold Standards" of the 4 base MDs provided.
# CONTEXT & BASELINE
Use the attached 4 base documents (Theodore Exemplified, Patrick Whoisthis, Michael Fake Sample, Andrew Notadoctor) as stylistic and structural "Gold Standards." 
This will include the varyign lengths of each document specfic to each document's style.

# OBJECTIVES
1. Create 10 synthetic documents that vary across patient demographics (elderly, SNF residents, IVDU, immigrants) and clinical scenarios (Infectious Disease focus).
2. Mirror the specific structural quirks of the 4 base MDs.
3. Ensure to maintain 1 style per document, and then rotate the style for each different document. 
4. The content and patient scenarios can be anything plausible and should vary naturally throughout the notes.
Ensure the notes are similar to the examples, they should all “feel” like they were part of some larger dataset that was taken from a real hospital.
5. Search the 500 most common scenarios faced in urban hospitals and use that as the base. Then combine it with the syntax.
6. The length of each document should be similar to 1 given example (Around 50 to 150 lines exclduing empty lines. 


# FORMATTING
- Separate each note with "########".
- Use futuristic MRNs (8 digits).
- Include standard hospital headers (Facility name, Service, Location).
"""
client = genai.Client()
print(f'Started')
for i in range(10):
      print(f'Iteration {i}')
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
            prompt
                        ],
            config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
            include_thoughts=True))
      )
      number = '1-500'
      with open (f'Warmup/data/Generated Patient Notes/Attempt {number}','a') as attempt_file:
            attempt_file.write(response.text)
            print(response.text)

      with open (f'Warmup/data/Generated Patient Notes/Attempt {number} Thoughts','a') as file:
            for part in response.candidates[0].content.parts:
                  if not part.text:
                        continue
                  if part.thought:
                        file.write("Thought summary:\n")
                        file.write(part.text)
                        file.write("\n")
                  else:
                        file.write("Answer:\n")
                        file.write(part.text)
                        file.write("\n")
      time.sleep(15)
      print(f'Ended iteration {i}')



