# crea un programa que pida dos numero y obtenga como resultado 
# cual de ellos es par o si ambos lo son


num1=int(input("Ingresa el primer número: "))
num2=int(input("Ingresa el segundo número: "))


if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos numeros son pares.")
elif num1 % 2 == 0:
    print("Solo el primer numero es par.")
elif num2 % 2 == 0:
    print("Solo el segundo numero es par.")
else:
    print("Ninguno de los dos numeros es par.")
