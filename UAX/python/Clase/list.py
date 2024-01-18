string = "python"
lista = list(string)
print(lista)

#acceder a un elemento de la lista
print(lista[0])

#indices negativos
print(lista[-2])

#modificar un elemento de la lista(cambias una letra por otra)
lista[1] = "j"

#agregar un elemento de la lista
lista.append("a")
print(lista)

#agregar un elemento a una posicion especifica
lista.insert(0, "p")
print(lista)

#eliminar un elemento de la lista
lista.remove("y")

#eliminar ultimo elemento de la lista
lista.pop(0)
print(lista)

#devolver el ultimo elemento eliminado
print(lista.pop)
