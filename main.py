from fastapi import FastAPI
import uvicorn
from PIL import Image
from google import genai
import shutil
import os

app = FastAPI()
client = genai.Client(api_key="AIzaSyBkiHTeOsHbRii1JVb5NpkRO9mGNeMJq_E")

@app.get("/")
def home():
    return {"message" : "Сервер пашет"}
@app.get("/test")
def test():
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Привет! Представься одним предложением."
    )

    return {
        "answer": response.text
    }



"""def calculatin (a, b, op):

    if op == "plus":
     return int(a)+int(b)
    elif op == "min":
     return int(a)-int(b)
    elif op == "dif":
     return int(a)//int(b)
    else:
     return {"Ну ті і пісюн"}"""

"ngrok "
if  __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

