# Tuplas
mi_tupla = (2,4)
print("mi tupla: ",mi_tupla)

# Lista
mi_lista = [1, 3.1416, "carlos",mi_tupla]
print("El primer elemento de la lista:",mi_lista[0])
print("el cuarto elemento de la lista: ",mi_lista[3])
print("el cuarto elemento de la lista: ",mi_lista[2])

# Diccionarios 
mi_diccionario = {"mi_lista": mi_lista,
                  "nombre": "carlos",
                  "pi": 3.1416,
                  "tel":"313-1515300"}
print("llave para acceder a mi diccionario de mi_lista",mi_diccionario["mi_lista"])
print("llave para acceder a mi diccionario pi",mi_diccionario["pi"])
print("llave para acceder a mi diccionario de tel",mi_diccionario["tel"])
