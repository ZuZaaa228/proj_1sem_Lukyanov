slovar = {x: y**3 for x,y in enumerate(range(7))}
print(slovar)
del slovar[0]
del slovar[6]
print(slovar)
