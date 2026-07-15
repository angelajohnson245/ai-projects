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

# we will using more prompts
prompt1="Hi"
prompt2="I am meeting Spanish clients, Can you tell me 1 common Spanish phrases that I can use to impress them?"
prompt3="Please write a 300 word essay on the importance of AI in modern education."

prompts = [prompt1, prompt2, prompt3]



# message is a dictionary with key value pairs
# max_tokens=1000      IF I give it 100 then then it will give me only 100 tokens in the response. 
# If I give it 1000 then it will give me 1000 tokens in the response.


for prompt in prompts:
    message = {
        "role": role,
        "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages, temperature=0, max_tokens=250)
    print(response.choices[0].message.content)
    usage = response.usage
    print(f"\n\nPrompt Tokens: {usage.prompt_tokens}, "
      f"\nCompletion Tokens: {usage.completion_tokens}, "
      f"\nTotal Tokens: {usage.total_tokens}, "
      f"Finish Reason: {response.choices[0].finish_reason}\n\n")

#print(response)
