idade = int(input("Digite sua idade: "))
nome = input("Digite seu nome: ")
estudante = input("Você tem carteira de estudante (sim ou não)? ")

if idade >= 65 or idade <= 21 or estudante == "Sim":
    print(f"Ok {nome}, você tem direito a meia entrada!")
else:
    print(f"{nome}, você paga inteira.")


