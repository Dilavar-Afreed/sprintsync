import os
from openai import OpenAI

client = OpenAI()

def get_embedding(text: str):
    # If running in CI or tests, return fake embedding
    if os.getenv("OPENAI_API_KEY") == "dummy-key-for-ci":
        return [0.0] * 1536

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
    )

    return response.data[0].embedding