kwh = float(input("Qual a quantidade de kWh consumida? "))
tipo = input('''
--------------------------
Qual o tipo de instalação?
--------------------------
| R para residências |
| I para Indústrias  |
| C para comércios   |
--------------------------
| Digite aqui: ''')


if tipo == "R":
    if kwh > 500:
       taxa = 0.65
    else:
        taxa = 0.4
elif tipo == "C":
    if kwh > 1000:
        taxa = 0.60
    else:
        taxa = 0.55
elif tipo == "I":
    if kwh > 5000:
        taxa = 0.60
    else:
        taxa = 0.55
valor = kwh*taxa


print(f'O valor pago será de R${valor:.2f}')
