import math
from random import choice

a = int(input())
b = int(input())
s = a+b
d = a-b
d1 = a//b
choice = input("Select: s or d or d1")
if choice == s:
    print(s)
elif choice == d:
    print(d)
elif choice == d1:
    print(d1)
else:
    result = None
    print("Ну ті і пісюн")
print({result:"Ничего нет"})