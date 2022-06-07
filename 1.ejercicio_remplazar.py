'''
muestre los números del 1 al 100 en la
pantalla, sustituyendo los múltiplos de 3 por la palabra "fizz", los múltiplos de 5 por
"zumbido" y los múltiplos de ambos, es decir, los múltiplos de 3 y 5, por la palabra
"zumbido efervescente".
'''
ZUMBIDO_EFERVESCENTE = "fizz buzz"
FIZZ = "fizz"
ZUMBIDO = "buzz"

samples = [];
sample = None;

for x in range(1, 101):
    if(x%3 == 0 and x%5 == 0):
        sample = ZUMBIDO_EFERVESCENTE
    elif(x%3 == 0):
        sample = FIZZ
    elif(x%5 == 0):
        sample = ZUMBIDO
    else:
        sample = x

    samples.append(sample);

print(*samples)


