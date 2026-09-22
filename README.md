Aqui fica o código utilizado na calculadora em linguagem de Python
Da uma olhada como ficou:

a = 0
b = 0
c = 0


while True:
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))

    op = int(input("Digite a operação desejada: 1 - Soma, 2 -Substracao, 3 - multiplicacao ou 4 - divisa0: "))
    if op == 1:
        c = a + b
        print("O resultado da soma é: ", c)

    elif op == 2:
        c = a - b
        print("O resultado da subtração é: ", c)

    elif op == 3:
        c = a * b
        print("O resultado da multiplicação é: ", c)

    elif op == 4:
        if b != 0:
            c = a / b
            print("O resultado da divisão é: ", c)
        else:
            print("Não é possível dividir por zero.")

    else:
        print("Operação inválida.")


    if input("Deseja continuar? (s/n): ") != "s":
        break
