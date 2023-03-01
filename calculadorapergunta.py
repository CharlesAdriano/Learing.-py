#Calculadora que pergunta;

continuar = "s"
armazena = [0,1,2,3,4,5,6,7,8]

while continuar == "s" or continuar == "S":
    print("Entre com os parâmetros solicitados.")
    operacao = input("[+, -, *, /] , escolha o sinal conforme a operação: ")
    n = float(input("Digite o valor correspondente ao primeiro dado da operação: "))
    n1 = float(input("Digite o valor correspondente ao segundo dado da operação: "))
    if operacao == "+":
        resultado = n + n1
        armazena[0] = resultado
        print(resultado)

    if operacao == "-":
        resultado = n - n1
        armazena[1] = resultado
        print(resultado)

    if operacao == "*":
        resultado = n * n1
        armazena[2] = resultado
        print(resultado)

    if operacao == "/":
        resultado = n / n1
        aramazena[3] = resultado
        print(resultado)

    continuar = input("Deseja fazer alguma outra operação? [n] não, [s]sim ")
print("O resultado das oprações foram", armazena[1], "resultado da soma, ", armazena[0], "resultado da subtração",
armazena[2], "resultado da multiplicação e ", armazena[4], "resultado da divisão")
