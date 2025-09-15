import math

# ------ STRINGS ------
nombre = "Gino"
apellido = "Mazza"

# Length
print("--- Length ---")
largo_nombre = len(nombre)
print(largo_nombre)

# Indexes
print("--- Indexes ---")
print(nombre[0])
print(nombre[-1])
print(nombre[0:2])
print(nombre[0:])
print(nombre[:2])
print(nombre[:])

# Escape Sequences
# \"  poner comilla en string
# \'  poner comilla simple en string
# \\  poner contrabarra en string
# \n  nueva linea

# Formatted Strings
print("--- Formatted String ---")
print(f"Hola {nombre} {apellido}")

# String Methods
print("--- String Methods ---")
print(nombre.upper())  # todo a mayusculas
print(nombre.lower())  # todo a minusculas
print(nombre.title())  # primera letra en mayusculas
print(nombre.strip())  # saca espacios al principio y al final
print(nombre.lstrip())  # saca espacios al principio
print(nombre.rstrip())  # saca espacios al final
print(nombre.find("n"))  # da el index de el caracter en el string, -1 si no esta
# reemplaza todo el primer string por el segundo
print(nombre.replace("o", "i"))
print("Gin" in nombre)  # da true si el parametro esta en el string
print("Gin" not in nombre)  # da true si el parametro no esta en el string

# ------ NUMEROS ------
primero = 10
segundo = 5

# Operaciones
print("--- Number Operations ---")
print(primero + segundo)  # suma
print(primero - segundo)  # resta
print(primero * segundo)  # producto
print(primero / segundo)  # division que devuelve float (con coma)
print(primero // segundo)  # da un int en lugar de float (redondea)
print(primero % segundo)  # modulo
print(primero ** segundo)  # potencia

# Number Methods (Muchos son del module math, buscar documentacion)
print("--- Number Methods ---")
print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))

#------ TYPE CONVERSION ------
print("--- Type Conversion ---")
x = "1"
print(int(x))
print(float(x))
print(bool(x)) # da false solamente si es: "", 0, None 
print(str(x))

#------ CONDITIONALS ------
# if, elif, else
print("--- Conditionals ---")
temperature = 35
if temperature > 30:
    print("It's hot")
elif temperature > 20:
    print("It's warm")
else:
    print("It's cold")

# Ternary Operator
age = 12
message = "Grown" if age >= 18 else "Child"
print(message)

#------ LOGICAL OPERATORS ------
print("--- Logical Operators ---")
print(True and False)
print(True or False)
print(not True)

#------ FOR LOOPS ------
print("--- For Loops ---")
for i in range(3):
    print("Iteration (Range numero solo)", i)

for j in range(1, 4):
    print("Iteration (Range entre a y b)", j)

for k in range(1, 8, 2):
    print("Iteration (Range tercer parametro aumento)", k)

# For..Else
successfull = False
for i in range(3):
    print("Attempt", i)
    if successfull:
        print("Successfull!")
        break
else: # se ejecuta solo si el for termina sin early termination
    print("Attempted 3 times and failed")
