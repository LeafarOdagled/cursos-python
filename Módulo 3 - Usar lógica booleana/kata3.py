
velocidad=49
velocidad2=20
velocidad3 = 21
Size = 26

if velocidad>25: 
    print("se acerca un asteroide demaciado rapido "+ str(velocidad)+"km/s")
else: 
    print("no hay pleigro")
    
    
    
if velocidad2>=20: 
    print("¡hay uno que se dirige a la tierra ahora a una velociadad de "+ str(velocidad2)+"km/s!")
else: 
    
    print("no hay pleigro")
    
    
    
if velocidad3>25 and Size>25:
    print("¡peligro hay un asteroide que se dirige a la tierra!")
elif velocidad3>=20:
    print("hay un destello de lluz en el cielo") 
elif Size<25:
    print("aqui no pasa nada") 
else:
    print("aqui no pasa nada")
