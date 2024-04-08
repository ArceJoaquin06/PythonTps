inscrips = ['M','F','J','P','S','M','J','M','P']

frequency = {}

for inscrip in inscrips:
    if inscrip in frequency:
        frequency[inscrip] += 1
    else:
        frequency[inscrip] = 1

print("Frecuencia  de letras: ", frequency)