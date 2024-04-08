manuscritos = ['E','S','O','T','I','L','I','N','I','Y','O']

frequency = {}

for manuscrito in manuscritos:
    if manuscrito in frequency:
        frequency[manuscrito] += 1
    else:
        frequency[manuscrito] = 1

print(max(frequency, key=frequency.get))

"""
Consigna:
Difícil: Los exploradores descubren un manuscrito antiguo y desean encontrar la
palabra más común en él. Implementa un programa que utilice un diccionario para
encontrar la palabra con la frecuencia más alta en el texto.
"""