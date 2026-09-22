a = 0
b = 0
c = 0


while True:
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))

    op = int(input("Digite a operacao desejada: 1 - soma, 2 -substracao, 3 - multiplicacao ou 4 - divisao: "))
    if op == 1:
        c = a + b
        print("O resultado da soma e: ", c)

    elif op == 2:
        c = a - b
        print("O resultado da subtracao e: ", c)

    elif op == 3:
        c = a * b
        print("O resultado da multiplicacao e: ", c)

    elif op == 4:
        if b != 0:
            c = a / b
            print("O resultado da divisao e: ", c)
        else:
            print("Nao e possível dividir por zero.")

    else:
        print("Operacao invalida.")


    if input("Deseja continuar? (s/n): ") != "s":
        break




