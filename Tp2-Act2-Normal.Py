power = int(input("Ingresa la cantidad de tu poder: "))
life = int(input("Ingresa la cantidad de vida de tu adversario: "))

if power > life:
  print("Derrotaste a tu enemigo!")
elif power == life: 
  print("Empate! tu y tu adversario empataron y se dieron cuenta la cantidad de cosas en común que tienen los dos y deciden formar una familia")
elif power < life: 
  print("Tu enemigo te derrotó!")