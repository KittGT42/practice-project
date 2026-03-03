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

a = int(input())
b = int(input())
op = input("Выбор операции(+ - * /):")
print (calculatin(a, b, op))