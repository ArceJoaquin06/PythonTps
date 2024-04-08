manuscritos = ['E','S','O','T','I','L','I','N','I','Y','O']

frequency = {}

for manuscrito in manuscritos:
    if manuscrito in frequency:
        frequency[manuscrito] += 1
    else:
        frequency[manuscrito] = 1

print(max(frequency, key=frequency.get))