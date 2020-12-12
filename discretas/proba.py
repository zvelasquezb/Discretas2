#Código para hallar el número de verificación de la DIAN
from itertools import permutations  
import operator
import math

lista = []
lista_multi = []
primos  = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]
cont = 0
counter=0
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
print("Su nit tiene: ",len(nit),"digitos")
print("Si solo se puede dañar un digito existen:",len(nit)*9, "errores posibles")
for i in range(0,len(nit)):
  for j in range (0,10):
    if int(nit[i:1+i])!=j:
      #print(nit[0:i]+"-"+str(j)+"-"+nit[i+1:len(nit)])
      #print(algoritmo(nit[0:i]+str(j)+nit[i+1:len(nit)]),algoritmo(nit))
      if int(algoritmo(nit[0:i]+str(j)+nit[i+1:len(nit)]))==int(algoritmo(nit)):
        counter+=1
print("Se han producido",counter,"falsos positivos con el algortmo de digito de verificacion de la Dian dentro de los",len(nit)*9
      ,"errores posibles")
print("En este caso el algoritmo resulta un:",(len(nit)*9-counter)/(len(nit)*9)*100,"% efectivo")
