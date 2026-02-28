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
print({result:"Ничего нет"})
a = int(input())
b = int(input())
op = input("Выбор операции(+ - * /):")