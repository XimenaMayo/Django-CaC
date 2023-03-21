#Ejercico 4
#copiar cosad de ejercicio 3.
def contar(cadena):
    lista = cadena.split()
    diccionario = {}
    for i in lista:
        diccionario[i] = {lista.count(i)}
        for i in diccionario:
            frec=max(diccionario)
            return (i, diccionario[i], frec)
        return  

cadena= 'hola hola manola hola'
maxi=contar(cadena)
print(maxi)

   