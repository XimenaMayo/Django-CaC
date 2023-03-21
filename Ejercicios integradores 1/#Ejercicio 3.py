#Ejercicio 3
def contar(cadena):
    lista = cadena.split() #converitr cadena en lista
    diccionario = {} #definir diccionario
    for i in lista: #recorrer la lista y contar las palabras
        diccionario[i] = {i, lista.count(i)}
    return diccionario
cadena = "hola hola lola manola hola" # cadena de caracteres a analizar
dicc = contar(cadena)
print(dicc)


 
  


  