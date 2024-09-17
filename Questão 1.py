#QUESTÃO 1 - Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def sequencia_fibonacci(num_escolhido):
    inicio = 0
    proximo = 1 
  
    while inicio < num_escolhido:
        inicio, proximo = proximo, inicio + proximo
    return inicio == num_escolhido

num_escolhido = int(input("Digite um número: "))
if sequencia_fibonacci(num_escolhido):
    print("Pertence a sequência de Fibonacci.")
else:
    print("Não pertence a sequência de Fibonacci.")