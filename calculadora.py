num1 = float(input("Ingrese un numero"))
operacion = str(input("Ingrese su operacion: Suma,Resta,Potencia,Raiz,Multiplicacion,Division o Porcentaje",)).strip().capitalize()

if operacion in ["Suma", "Resta", "Division", "Multiplicacion"]:
    num2 = float(input("Ingrese otro numero"))
if operacion == "Suma":
    resultado = num1 + num2
    print("Su resultado es:",resultado)
elif operacion == "Resta":
    resultado = num1 - num2
    print("Su resultado es:",resultado)
elif operacion == "Multiplicacion":
    resultado = num1 * num2
elif operacion == "Division":
    #Validacion seguridad
    if num2 !=0:
        resultado = num1 / num2
        print("Su resultado es:",resultado)
    else:
        resultado = print("Error no se puede dividir por cero")
elif operacion == "Potencia":
        exponente = float(input("Ingrese el exponente"))
        resultado = num1 ** exponente
        print("Su resultado es:",resultado)
elif operacion == "Raiz":
     if num1 < 0:
          print("Error no puede calcular la raiz de un numero negativo")
     else:
          indice = float(input("Ingrese el indice"))     
          resultado = num1 ** (1/indice)
          print("Su resultado es:",resultado)
elif operacion == "Porcentaje":
        porcentaje = int(input("Ingrese el porcentaje que desea calcular"))
        resultado = num1 * (porcentaje/100)
        print("Su resultado es:",resultado)
