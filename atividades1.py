materia1 = 7
materia2 = 6
materia3 = 5
podersupremo = 1

resultado = (materia1 >= 7 and materia2 >= 7 and materia3 >= 7) or podersupremo == 1


print(resultado)

# ----------------------------------------------------------------------------------------------

a = "Bom"
b = ' '
c = "Dia!"

# printa o tipo
print(type(a))
# printa a quantidade de caracteres
print(len(a))
# printa a letra que está no numero exato citado (no caso 0)
print(a[0])

# executa um intevalo fechado onde mostra apenas as caracteres pedidas
print()
print(a[:])


# junta as strings
print(a+b+c)

# printa tantas vezes a string
print(5*a)

# ---------------------------------------------------------------------------------------------------

# exercicio: programa que pegue o nome da pessoa e diga quantas letras tem e a primeira letra do nome
nome = "Marcela"
print(len(nome))
print(nome[0])

# printando o nome invertido
print(nome[::-1])

# apenas os numeros impares e pares
print(nome[1::2])


# juntar 2 strings sem a primeira letra de cada uma
nome2 = "João"

print(nome[1:] + "  " + nome2[1:])

# --------------------------------------------------------------------------------------------

# String com marcador de numero (%d numero inteiro)
idade = 18
texto = 'Marcela possui %d anos' % idade

print(texto)
#  %s string
apelido = "Maah"
texto1 = 'Meu apelido é %s' % nome2

print(texto1)

# %f números decimais
preco = 19.50
texto2 = 'O preço é %5.2f' % preco

print(texto2)
# ----------------------------------------------------------------
# usando todos juntos

texto3 = ('Meu nome é %s, tenho %d anos e estou vendendo uma camisa por %.2f') % (nome, idade, preco)

print(texto3)
# ----------------------------------------------------------------
# método mais utilizado e mais pratico
texto4 = 'Meu nome é [{:^10s}], tenho {} anos e estou vendendo uma camisa por {:.2f}' .format(nome, idade, preco)
print(texto4)

# < para esquerda, > para direita e ^ para ficar no centro

# ----------------------------------------------------------------

# método mais utilizado ainda (socorro quanto método)
texto5 = f'Meu nome é {nome}, tenho {idade} anos e estou vendendo uma camisa por {preco}'
print(texto5)

# --------------------------------------------------------------------------------------------

# # programa para escrever a idade e o nome com input no terminal
#
# x = input("Escreva seu nome:")
# y = input("Escreva sua idade:")
# texto6 = f"Seu nome é {x} e você tem {y} anos."
# print(texto6)


# num1 = int(input("Digite um número que queira somar:"))
# num2 = int(input("Digite o próximo número a se somar:"))
# print("A soma dos números é igual a", num1 + num2)

# --------------------------------------------------------------------------------------------

dias = int(input("Digite a quantidade de dias:"))
horas = int(input("Digite a quantidade de horas"))
minutos = int(input("Digite a quantidade de minutos:"))
segundos = int(input("Digite a quantidade de segundos:"))

soma = segundos + minutos*60 + horas*60*60 + dias*24*60*60
print(soma)
