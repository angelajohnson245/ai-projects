import os
from pathlib import Path
from urllib import response
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, Field

""" CustomerInfo is a Pydantic model — a typed data container that validates input automatically.
Think of it as a schema: it defines what fields must exist and what type each field must be. 

name: str
Must be a string

Required (Field(...) means “no default, must be provided”)

Has a description used in docs, OpenAPI, or error messages

2. order_number: str
Also a required string

Useful for validating incoming order‑related payloads (API, CLI, MCP tool input, etc.)

3. email: str
Required string

Pydantic won’t validate email format automatically unless you use EmailStr, but this still enforces type correctness.

4. phone: str
Required string

Same idea: type‑checked but not format‑validated unless you add a regex or a specialized type.

Field(...) means “this field has no default and must be provided.”

"""
class CustomerInfo(BaseModel):
    name: str = Field(..., description="The customer's name")
    order_number: str = Field(..., description="The customer's order number")
    email: str = Field(..., description="The customer's email address")
    phone: str = Field(..., description="The customer's phone number")
    
schema = CustomerInfo.model_json_schema()  # Generates a JSON schema representation of the model

#Correct Groq JSON schema format
response_format = {
    "type": "json_object",
}


system_prompt = """
Please extract the following personal information from the given text and return it in valid JSON format 
provided in response_format.
"""

message_system = {
    "role": "system",   
    "content": system_prompt
}

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
" My email id is angela@example.com and my phone number is +1234567890. I am looking forward to your response. "\
" I like to visit spain next this year. My dogs name is Jack. Thank you."    

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
messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages, response_format=response_format, temperature=0, max_tokens=250 )
print(response)
print(response.choices[0].message.content)