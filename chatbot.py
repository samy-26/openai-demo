import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = "OPENAI_API_KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hi there!"}
    ]
)

print(response.choices[0].message["content"])
