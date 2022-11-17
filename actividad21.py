numero =int(input('Escribe un número '))
desde = 1 #límite inferior
hasta = 10 #límite superior 

for f in range(desde, hasta + 1):
	print(f'{numero} x {f} =  {numero * f}')


#FORMA CORRECTA:
for x in range(11):
    for y in range(11):
        print(f'{x} * {y} es {x*y}')