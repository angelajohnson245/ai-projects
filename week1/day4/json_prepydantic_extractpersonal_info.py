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
text="My name is Angela. I bought a iphone from your store. I am facing some issues with it. Can you help me? "\
" I am facing issues with the battery. It is draining very fast. I have tried all the troubleshooting steps but nothing worked. "\
" I want to know if I can get a replacement or a refund. Please let me know what are my options. "\
" I am very disappointed with the product and the service. I hope you can resolve this issue as soon as possible. "\
" My order number is 123456. I have attached the invoice and the warranty card. Please check and get back to me. "\
" My email id is angela@example.com and my phone number is +1234567890. I am looking forward to your response. Thank you."    

prompt=f"""
This is a customer complaint email. 
Please extract personal information from the email: name, order number, email address, and phone number. {text}
"""

#message is a dictionary with key value pairs
message = {
  "role": role,
  "content" : prompt 
}
#we are sending multiple messages in a list as seen below
messages = [message]

#messages = [message1, message2]
response = client.chat.completions.create(model=model, messages=messages, temperature=2, max_tokens=250)
print(response)
print(response.choices[0].message.content)