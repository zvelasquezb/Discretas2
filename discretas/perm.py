#Código para hallar el número de verificación de la DIAN
from itertools import permutations  
import operator

lista = []
lista_multi = []
primos  = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]
cont = 0
r = 0

#Función para sumar los elementos de una lista
def sumalista(listaNum):
    s = 0
    for i in listaNum:
        s = s + i
    return s

def algoritmo(num):
  for i in range(0,len(primos)):
    #Reversa al string de cada permutación del Nit ingresado
    x = list(num)[::-1]
    #convierte a enteros la lista del Nit guardada en x
    b = [int(j) for j in x]
    y = list(primos)
    lista_multi = list(map(operator.mul, b, y))
  sum = sumalista(lista_multi)
  #Aplicación del algoritmo módulo 11
  residuo = sum % 11
  #return residuo
  if (residuo == 0):
    r = 0
  elif (residuo == 1):
    r = 1
  else:
    dv = 11 - residuo
    r = dv
  return r

nit = (input("Ingrese el NIT sin separadores ni espacios: "))

#print(algoritmo(nit))
#Todas las permutaciones posibles del NIT sin repeticiones
perm = permutations(nit)

for i in list(perm):
  StrA = "".join(i)
  #print(StrA)    
  #print (i)
  if (algoritmo(nit) == algoritmo(StrA)):
    cont += 1
    #print(algoritmo(nit), algoritmo(StrA))
  else:
    cont = 0
   
if cont <= 1:
  print("No se encontraron coincidencias.")
else:
  print("Se encontraron", cont, " coincidencias.")