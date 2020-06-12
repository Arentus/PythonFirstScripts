# para hacer una concatenacion se usa el metodo join el cual es mas eficiente que usar el operador +
x = ';'.join(['#fff444','#000000','#e4e4e4']);

print(x)

myTuple = ("John", "Peter", "Vicky")

y = "#".join(myTuple)

print(y)

# para concatenar sin ningun separator

phrase = ''.join(['hola',' que tal'])

print(phrase)

# para partir un string

z = "darksoulsIII".partition("souls")
print(z)

departure, separator, arrival = "London:Edinburgh".partition(':')
print(departure)
print(arrival)

origin, _, destination = "Seattle-Boston".partition('-')

print(origin)
print(destination)

# para formatear un String

formattedString = "La edad de {0} es {1}".format('Bobby',3)

print(formattedString)

ftS2 = "La edad de {0} es {1}. El cumplea;os de {0} es el {2}".format('Bobby',3,24)

print(ftS2)

"Reticulating spline {} of {}".format(4,23)

"Current position {latitude} {longitude}".format(latitude="60N",longitude="5E")

"Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=(65.2,23.1,82.2))

# interpolation string format
value = 4 * 20
f'The value is {value}'

import datetime
f'La hora actual es {datetime.datetime.now().isoformat()}'