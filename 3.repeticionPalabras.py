'''
repeticion de palabras en un texto
'''
repeticion = 0
tempPalabras = []

#formatear texto
texto = input("ingrese el texto: ")
texto = texto\
    .replace("?", "")\
    .replace("¿", "")\
    .replace(".", "")\
    .replace(",", "")

#procesar texto
palabras = texto.split(" ")
for palabra in palabras:
    repeticion = palabras.count(palabra)
    if(tempPalabras.count(palabra) == 0):
        print(f"{repeticion} - {palabra}")
    if (repeticion > 1):
        tempPalabras.append(palabra)

