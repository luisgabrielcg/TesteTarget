## 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
*IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;*
```
def sequencia_fibonacci(num_escolhido):
    inicio, proximo = 0, 1
  
    while inicio < num_escolhido:
        inicio, proximo = proximo, inicio + proximo
    return inicio == num_escolhido

num_escolhido = int(input("Digite um número: "))
if sequencia_fibonacci(num_escolhido):
    print("Pertence a sequência de Fibonacci.")
else:
    print("Não pertence a sequência de Fibonacci.")´´´
```
## 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
*IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;*
```
palavra = str(input("Insira uma palavra: ").lower())
print(palavra.count("a"))
```

## 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA); Ao final do processamento, qual será o valor da variável SOMA?*
```
INDICE = 12
SOMA = 0
K = 1
while K<INDICE:
    K += 1
    SOMA = SOMA+K
print(f"O resultado da soma é {SOMA}")
```

## 4) Descubra a lógica e complete o próximo elemento:
### a) 1, 3, 5, 7, <strong><code>9</code></strong>

### b) 2, 4, 8, 16, 32, 64, <strong><code>128</code></strong>

### c) 0, 1, 4, 9, 16, 25, 36, <strong><code>49</code></strong>

### d) 4, 16, 36, 64, <strong><code>100</code></strong>

### e) 1, 1, 2, 3, 5, 8, <strong><code>13</code></strong>

### f) 2,10, 12, 16, 17, 18, 19, <strong><code>20</code></strong>

## 5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  
```
Primeiramente, ligo o primeiro interruptor por alguns minutos e depois o desligo, ligando o segundo interruptor. Em seguida, vou até a sala das lâmpadas. A lâmpada acesa corresponde ao segundo interruptor, a lâmpada quente ao primeiro interruptor e a lâmpada fria ao terceiro interruptor.
```
