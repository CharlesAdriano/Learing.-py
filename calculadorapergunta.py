#Calculadora que pergunta;

continuar = "s"
armazenaa = 00
armazenab = 00
armazenac = 00
armazenad = 00

while continuar == "s" or continuar == "S":
    print("Entre com os parâmetros solicitados.")
    operacao = input("[+, -, *, /] , escolha o sinal conforme a operação: ")
    n = float(input("Digite o valor correspondente ao primeiro dado da operação: "))
    n1 = float(input("Digite o valor correspondente ao segundo dado da operação: "))
    if operacao == "+":
        resultado = n + n1
        armazenaa = resultado

    if operacao == "-":
        resultado = n - n1
        armazenab = resultado

    if operacao == "*":
        resultado = n * n1
        armazenac = resultado

    if operacao == "/":
        resultado = n / n1
        armazenad = resultado

    continuar = input("Deseja fazer alguma outra operação? [n] não, [s]sim ")

if armazenaa != 0:
    print("Este é o resultado da soma:", armazenaa)
elif armazenab != 0:
    print("Este é o resultado da subtração:", armazenab)
elif armazenac != 0:
    print("Este é o resultado da multiplicação:", armazenac)
elif armazenad!= 0:
    print("Este é o resultado da divisão:", armazenad)

