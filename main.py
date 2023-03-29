import openai

openai.organization = "org-tOGfcJUBmwrDudjbls5mZW2D"

import os

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)

# Prompt the user for input
user_input = input("Enter your question: ")

# Define the parameters for the OpenAI API request
model_engine = "davinci"
prompt = user_input
temperature = 0.01
max_tokens = 10

# Make a request to the OpenAI API
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens
)

# Get the generated response from the OpenAI API
answer = response.choices[0].text.strip()

# Display the answer to the user
print(answer)