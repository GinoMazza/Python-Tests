def Sumar(a, b):
     return a + b

def Restar(a, b):
     return a - b

def Multiplicar(a, b):
     return a * b

def Dividir(a, b):
     return a / b

print("----- PYTHON CALCULATOR -----")
print("1- Sumar")
print("2- Restar")
print("3- Multiplicar")
print("4- Dividir")
print("0- Salir\n")

opcion = input("Seleccione una opcion: ")
match opcion:
     case "1":
          primerNumero = float(input("Primer numero: "))
          segundoNumero = float(input("Primer numero: "))
          print("Resultado:", Sumar(primerNumero, segundoNumero))
     case "2":
          primerNumero = float(input("Primer numero: "))
          segundoNumero = float(input("Primer numero: "))
          print("Resultado:", Restar(primerNumero, segundoNumero))
     case "3":
          primerNumero = float(input("Primer numero: "))
          segundoNumero = float(input("Primer numero: "))
          print("Resultado:", Multiplicar(primerNumero, segundoNumero))
     case "4":
          primerNumero = float(input("Primer numero: "))
          segundoNumero = float(input("Primer numero: "))
          print("Resultado:", Dividir(primerNumero, segundoNumero))
     case "0":
          print("Saliendo...")
     case _:
          print("Opción no válida")