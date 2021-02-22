import random

clave = input('clave numerica: ')

mensaje_binario = ''
palabra = input("ingrese texto: ")

#Opcional


for letra in palabra:
    binario = format(ord(letra), "08b")
    if mensaje_binario == '':
      mensaje_binario = binario
    else:
      mensaje_binario = mensaje_binario + " " + binario
print(mensaje_binario)

cadena_aleatoria = ''
for i in range(10):
    cadena_aleatoria += str(random.randint(0, 9))
print(cadena_aleatoria)

cadena_inicio = ''
cadena_union = clave + cadena_aleatoria

while len(cadena_inicio) != 256:
  for letra in cadena_union:
      cadena_inicio += letra
      if len(cadena_inicio) == 256:
          break

print('longitud: ', len(cadena_inicio))
print(cadena_inicio)

lista_numeros = []

for i in range(255+1):
  lista_numeros.append(i)

print('Lista de numeros')
print(lista_numeros)


lista_numeros_final = []

aux=0
for i in range(256):
  j = i + int(cadena_inicio[i])
  if j>= 255:
    j = j - 255
  #print(f'j = {i} + {cadena_inicio[i]}')
  #print(j)
  aux = lista_numeros[i]
  lista_numeros[i] = lista_numeros[j]
  lista_numeros[j] = aux

print('Lista de numeros con el cambio de orden')
print(lista_numeros)

lista_numeros_binaria = ''

for i in range(len(lista_numeros)):
  if i==len(lista_numeros)-1:
    lista_numeros_binaria += format(lista_numeros[i], "08b")
  else:
    lista_numeros_binaria += format(lista_numeros[i], "08b") + ' '

print('Lista numerica a binario')
print(lista_numeros_binaria)

