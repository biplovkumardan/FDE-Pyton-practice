# from UV-Env-Python-Approach 

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="Is FDE (forward deployment Engineer) role good for A Technology Architect to Switch to? Explain in 5 lines",
    model="openai/gpt-oss-20b",
)
print(response.output_text)
