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
prompt="How are you darling?"


message_system = {
  "role": "system", 
  "content": "You are my girlfriend."
}

#message is a dictionary with key value pairs
message = {
  "role": role,
  "content" : prompt 
}
#we are sending multiple messages in a list as seen below
messages = [message_system, message]

#messages = [message1, message2]
response = client.chat.completions.create(model=model, messages=messages)
#print(response)
print(response.choices[0].message.content)