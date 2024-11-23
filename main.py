import os
import uvicorn
from openai import OpenAI
from fastapi import FastAPI
from prompt import system_prompt


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/chat")
async def chat(message: str):
    client = OpenAI(
        api_key=os.getenv("TYPHON_API_KEY"), base_url="https://api.opentyphoon.ai/v1"
    )

    chat_completion = client.chat.completions.create(
        model="typhoon-v1.5x-70b-instruct",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )

    return {"response": chat_completion.choices[0].message.content}


if __name__ == "__main__":
    uvicorn.run(app)
