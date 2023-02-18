#Calculadora que pergunta;

continuar = "s"

while continuar == "s" or continuar == "S":
    print("Entre com os parâmetros solicitados.")
    operacao = input("[+, -, *, /] , escolha o sinal conforme a operação: ")
    n = float(input("Digite o valor correspondente ao primeiro dado da operação: "))
    n1 = float(input("Digite o valor correspondente ao segundo dado da operação: "))
    if operacao == "+":
        resultado = n + n1
        print(resultado)
    if operacao == "-":
        resultado = n - n1
        print(resultado)
    if operacao == "*":
        resultado = n * n1
        print(resultado)
    if operacao == "/":
        resultado = n / n1
        print(resultado)
    continuar = input("Deseja fazer alguma outra operação? [n] não, [s]sim ")
    
