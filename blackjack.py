from random import choice, sample 

print("Juguemos blackjack.")

cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
}
for carta, valor in cartas.items():
    print("El valor de esta carta {} es {}".format(carta, valor))
lista_cartas = list(cartas)
print("Tus cartas son: ", end=" ")
carta1 = choice(lista_cartas)  
carta2 = choice(lista_cartas)
print(carta1, carta2)
total = cartas[carta1] + cartas[carta2]
print("Tu total es: ", total)
while total < 21:
    print("¿Quieres otra carta? (s/n): ", end=" ")
    respuesta = input()
    if respuesta == "s":
        carta = choice(lista_cartas)
        print("Tu carta es: ", carta)
        total += cartas[carta]
        print("Tu total es: ", total)
    else:
        break
if total == 21:
    print("¡Ganaste!")
elif total > 21:
    print("Perdiste.")
else:
    print("Tu total es: ", total)

print("La banca recibe dos cartas.")
carta1 = choice(lista_cartas)
carta2 = choice(lista_cartas)
print("La banca tiene: ", carta1, carta2)
total_banca = cartas[carta1] + cartas[carta2]
print("El total de la banca es: ", total_banca)
while total_banca < 17:
    carta = choice(lista_cartas)
    print("La banca recibe: ", carta)
    total_banca += cartas[carta]
    print("El total de la banca es: ", total_banca)
if total_banca > 21:
    print("¡Ganaste!")

    
