monedas = {'Euro': '€', 'dollar': '$', 'yen': '¥'}

divisa = input('Ingresa una divisa ')
print(monedas.get(divisa.title(), 'La divisa no se encuentra'))
    