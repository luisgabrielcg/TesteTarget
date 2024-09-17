#QUESTÃO 2 - Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

palavra = str(input("Insira uma palavra: ").lower())
print(palavra.count("a"))