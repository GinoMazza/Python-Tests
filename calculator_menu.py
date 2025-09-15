# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
import os
import time


class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        return a / b

    def mostrar_menu(self):
        os.system("cls")
        print("----- PYTHON CALCULATOR -----")
        print("1- Sumar")
        print("2- Restar")
        print("3- Multiplicar")
        print("4- Dividir")
        print("0- Salir\n")
        opcion = input("Seleccione una opcion: ")
        match opcion:
            case "1":
                primer_numero = float(input("Primer numero: "))
                segundo_numero = float(input("Segundo numero: "))
                print("Resultado:", self.sumar(primer_numero, segundo_numero))
                input()
                os.system("cls")
                self.mostrar_menu()
            case "2":
                primer_numero = float(input("Primer numero: "))
                segundo_numero = float(input("Segundo numero: "))
                print("Resultado:", self.restar(primer_numero, segundo_numero))
                input()
                os.system("cls")
                self.mostrar_menu()
            case "3":
                primer_numero = float(input("Primer numero: "))
                segundo_numero = float(input("Segundo numero: "))
                print("Resultado:", self.multiplicar(
                    primer_numero, segundo_numero))
                input()
                os.system("cls")
                self.mostrar_menu()
            case "4":
                primer_numero = float(input("Primer numero: "))
                segundo_numero = float(input("Segundo numero: "))
                print("Resultado:", self.dividir(
                    primer_numero, segundo_numero))
                input()
                os.system("cls")
                self.mostrar_menu()
            case "0":
                os.system("cls")
                print("Saliendo...")
                time.sleep(1)
                return
            case _:
                print("Opción no válida")
                input()
                os.system("cls")
                self.mostrar_menu()


calc = Calculadora()
calc.mostrar_menu()
