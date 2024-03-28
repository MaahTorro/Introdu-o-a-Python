# dias = int(input("Digite a quantidade de dias:"))
# horas = int(input("Digite a quantidade de horas:"))
# minutos = int(input("Digite a quantidade de minutos:"))
# segundos = int(input("Digite a quantidade de segundos:"))
#
# soma = segundos + minutos*60 + horas*60*60 + dias*24*60*60
# print(soma)

# ------------------------------------------------------------

# quilometros = float(input("Digite a quantidade de km percorridos:"))
# quantDias = int(input("Digite a quantidade de dias que o carro foi alugado:"))
#
# calculo = quantDias*60 + quilometros*0.15
# print(f"O valor a pagar é de {calculo:2.f} Km percorrido: {quilometros} e quantidade de dias rodados: {quantDias}")

# -----------------------------------------------------------------

# num1 = int(input("Digite o primeiro número:"))
# num2 = int(input("Digite o segundo número:"))
#
# if num1 != num2:
#     print("True")
# else:
#     print("False")

# ----------------------------------------------------------------------

# velocidade = float(input("Velocidade do carro:"))
# limite = 80
# multa = 5
#
# if velocidade > limite:
#     excesso = velocidade - limite
#     multa = excesso * multa
#     print(f"Sua velocidade está acima do limite. Sua multa é de R${multa}")
# else:
#     print("Boa! Você está dentro do limite de velocidade")

# ----------------------------------------------------------------------

# a = int(input("Primeiro número:"))
# b = int(input("Segundo número:"))
#
# if a > b:
#     print(f"{a} é maior que {b}")
# else:
#     print(f"{b} é maior que {a}")

# ----------------------------------------------------------------------

# numero = int(input("Digite um número:"))
#
# # numero % 2 == 0 significa que o numero é par
# if numero % 2 == 0:
#     if numero >= 100:
#         print("O número é par e maior ou igual a 100")
#     else:
#         print("O número é par e menor que 100")
#
# # numero % 2 == 1 significa que o numero é ímpar
# if numero % 2 == 1:
#     if numero >= 100:
#         print("O número é impar e maior ou igual a 100")
#     else:
#         print("O número é impar e menor que 100")

# ----------------------------------------------------------------------

nota = 50

if nota >= 90:
    print("A")
elif nota >=70 and nota < 90:
    print("B")
elif nota >=50 and nota < 70:
    print("B")
