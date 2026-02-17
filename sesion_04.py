print("========== CALCULADORA INTELIGENTE ==========")

def calculadora(num1, num2, opcion):
    
    resultado = None  # variable interna
    
    if opcion == "1":
        resultado = num1 + num2
        print("Elegiste SUMA")
        
    elif opcion == "2":
        resultado = num1 - num2
        print("Elegiste RESTA")
        
    elif opcion == "3":
        resultado = num1 * num2
        print("Elegiste MULTIPLICACIÓN")
        
    elif opcion == "4":
        print("Elegiste DIVISIÓN")
        if num2 == 0:
            return "No es posible dividir entre cero."
        resultado = num1 / num2
        
    else:
        return "Opción inválida. Intenta nuevamente."
    
    return resultado


# Entradas del usuario
print("\n1) Sumar")
print("2) Restar")
print("3) Multiplicar")
print("4) Dividir")

opcion = input("Selecciona una opción (1-4): ").strip()

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Llamada a la función
respuesta = calculadora(num1, num2, opcion)

print("Resultado final:", respuesta)
