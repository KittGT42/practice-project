from fastapi import FastAPI
import uvicorn

app = FastAPI()
@app.get("/")
def calculatin (a, b, op):

    if op == "plus":
     return int(a)+int(b)
    elif op == "min":
     return int(a)-int(b)
    elif op == "dif":
     return int(a)//int(b)
    else:
     return {"Ну ті і пісюн"}

"ngrok "
if  __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)