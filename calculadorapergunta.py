#Calculadora que pergunta;

continuar = "s"
resultadoSoma = -1
resultadoSub = -1
resultadoMul = -1
resultadoDiv = -1

while continuar == "s" or continuar == "S":
    print("Entre com os parâmetros solicitados.")
    operacao = input("[+, -, *, /] , escolha o sinal conforme a operação: ")
    numero1 = float(input("Digite o valor correspondente ao primeiro dado da operação: "))
    numero2 = float(input("Digite o valor correspondente ao segundo dado da operação: "))
    if operacao == "+":
        resultadoSoma = numero1 + numero2

    elif operacao == "-":
        resultadoSub = numero1 - numero2

    elif operacao == "*":
        resultadoMul = numero1 * numero2

    else:
        resultadoDiv = numero1 / numero2

    continuar = input("Deseja fazer alguma outra operação? [n] não, [s]sim ")

if resultadoSoma != -1:
    print("O resultado da soma é: ", resultadoSoma)
if resultadoSub != -1:
    print("O resultado da subtração é: ", resultadoSub)
if resultadoMul != -1:
    print("O resultado da multiplicação é: ", resultadoMul)
if resultadoDiv != -1:
    print("O resultado da divisão é: ", resultadoDiv)
