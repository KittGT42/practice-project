from fastapi import FastAPI


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
     result = None
     print("Ну ті і пісюн")

a = int(input("Перша змінна:"))
b = int(input("Друга змінна:"))
op = input("Выбор операции(+ - * /):")
print (calculatin(a, b, op))