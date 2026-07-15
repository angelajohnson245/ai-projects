import os
from pathlib import Path
from urllib import response
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
     raise ValueError("API not found error")

client = Groq(api_key= groq_api_key)
model = "llama-3.3-70b-versatile"
role="user"
prompt1="I sell Indo Chinese food. I am looking for a name for my food delivery app. Can you suggest me 3 names?"


message_system = {
  "role": "system", 
  "content": "You are a brand manager who can suggest me a name for my food delivery app."
}

#message is a dictionary with key value pairs
message = {
  "role": role,
  "content" : prompt 
}
#we are sending multiple messages in a list as seen below
messages = [message_system, message]

#messages = [message1, message2]
#temperature=0,    IF I give it 0 then it will give me the same response every time.
# If I give it 1 then it will give me different responses every time. 
# if I give it 0.5 then it will give me different responses but not as much as 1.

# max_tokens=1000      IF I give it 100 then then it will give me only 100 tokens in the response. 
# If I give it 1000 then it will give me 1000 tokens in the response.
# temperature of 0 is more deterministic and will give you the same response every time.
# temperature of 1 is more random and will give you different creative responses every time.
# temperature of 2 is even more random and will give you even more creative responses every time.
response = client.chat.completions.create(model=model, messages=messages, temperature=2, max_tokens=1000)
#print(response)
print(response.choices[0].message.content)