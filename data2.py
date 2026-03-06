import os
from openai import OpenAI
# Set your OpenAI API key as an environment variable for security
# Ensure you have 'pip install openai'
#os.environ ["OPENΑΙ ΑΡΙ ΚΕΥ"] = "YOUR API KEY"
client OpenAI (api key=os.environ.get("OPENAI_API_KEY"))
def generate story (prompt):
"""Generates a short story based on a prompt using the OpenAI API."""
try:
response = client.chat.completions.create(
)
model="gpt-3.5-turbo", % or other models like gpt-4
messages=[
{"role": "system", "content": "You are a creative storyteller."},
{"role": "user", "content": prompt}
],
max tokens=200,
# Controls the length of the response
temperature=0.8,
# Controls the creativity (higher is more creative)
return response.choices[0].message.content
except Exception as e:
return f"An error occurred: {e}"
# Example usage
prompt = "Once upon a time, in a small village nestled between the mountains, a young girl"
discovered a magical key."
story = generate story (prompt)
print (story)