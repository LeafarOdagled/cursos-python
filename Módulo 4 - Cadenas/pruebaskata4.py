text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

text2=text.split()
#print(text2)

# Define las palabras pista: average, temperature y distance suenan bien
PalabrasClave=["average", "temperature", "distance"]  
print("/////////////////////////////////////////////////////////////////////////////////////////////")


#print(str(text.find("average"))+" "+str(text.find("temperature"))+" " +str(text.find("distance")))
#print(PalabrasClave)


print("/////////////////////////////////////////////////////////////////////////////////////////////")


for palabra in text2:              #esta buscando en text 2 
    for clave in PalabrasClave:    #ahora tenemos clave que es la que esta buscando en el arreglo de palabras clave
        if clave in palabra:       #despues decimos que si clave esta en palabra imprimimos la palaba
            print(palabra)
            break                  #detenemos el for
    
    
    
print("/////////////////////////////////////////////////////////////////////////////////////////////")