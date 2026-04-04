from fastapi import FastAPI
import uvicorn

app = FastAPI()
@app.get("/")
def calculatin (a, b, op):

    if op == "+":
     return a+b
    elif op == "-":
     return a-b
    elif op == "/":
     return a//b
    else:
     return {"Ну ті і пісюн"}

if  __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.0", port=8000)