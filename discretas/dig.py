#Código para hallar el número de verificación de la DIAN
import operator

lista = []
lista_multi = []
primos  = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]

nit = (input("Ingrese el NIT sin separadores ni espacios: "))

#Función para sumar los elementos de una lista
def sumalista(listaNum):
    s = 0
    for i in listaNum:
        s = s + i
    return s

for i in range(0,len(primos)):
  #Reversa al string del Nit ingresado
  x = list(nit)[::-1]
  #convierte a enteros la lista del Nit guardada en x
  b = [int(j) for j in x]
  y = list(primos)
  lista_multi = list(map(operator.mul, b, y))

sum = sumalista(lista_multi)
#Aplicación del algoritmo módulo 11
residuo = sum % 11

if (residuo == 0):
  print("El dígito de verificación para el NIT:", nit, "es:", residuo)
elif (residuo == 1):
  print("El dígito de verificación para el NIT:", nit, "es:", residuo)
else:
  dv = 11 - residuo
  print("El dígito de verificación para el NIT:", nit, "es:", dv)