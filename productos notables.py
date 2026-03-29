operacion = str(input("Ingrese el calculo que desea realizar: 1) Cuadrado de binomio\n2) Suma por su diferencia\n3) Binomio al cubo"))
opcion = int(input(operacion))
if operacion == 1:
                a = float(input("Ingrese su primer termino\n"))
                b = float(input("Ingrese su segundo termnino\n"))
                input("Ingrese si el cuadrado es positivo o negativo\n")
                if "Positivo":
                        res = (a + b)**2
                        print("El resultado del cuadrado es:",res)
                else:
                    res = (a - b)**2
                    print("El resultado de su cuadrado es:",res)
if operacion == 2:
                a = float(input("Ingrese el primer numero"))
                b = float(input("Ingrese el segundo numero"))
                res = a**2 - b**2
                print("El resultado de la suma por su diferencia es:",res)
if operacion ==3:
                a = float("Ingrese el primer numero\n")
                b = float("Ingrese el segundo numero\n")
                signo = input("El cubo es 1) Positivo o 2) Negativo")
                opcion = int(input(signo))
                if opcion ==1:
                        res = a**3 + 3*a**2*b + 3*a*b**2 + b**3
                        print("El resultado del cubo es\n:,res")
                else:
                        res = a**3 - 3*a**2*b + 3*a*b**2 - b**3
                        print("El resultado del cubo es\n:,res")