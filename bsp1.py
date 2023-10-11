import math

def function1(var1, var2):
    erg = math.sqrt(var1**2 + var2**2)
    return erg

input1 = int(input("Bitte geben Sie die erste Zahl ein: "))
input2 = int(input("Bitte geben Sie die zweite Zahl ein: "))
       
e = function1(input1, input2)

u = e + input1 + input2

print("Das Ergebnis lautet: ", u)
