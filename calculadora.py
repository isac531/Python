z=0
retry = 0
exec=1
while exec == 1:

    operacao = int(input("Escolha a operação desejada: \n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n R="))

    x = int(input("Digite o Primeiro digito: \n"))
    y = int(input("Digite o Segundo digito: \n"))

    if operacao == 1:
        z = x + y
        print("O Resultado da sua conta é: ")
        print(x, '+' ,y, '=',z)
    elif operacao == 2:
        z = x - y
        print("O Resultado da sua conta é: ")
        print(x, '-' ,y, '=' ,z)
    elif operacao == 3:
        z = x * y
        print(x, '*' ,y, '=' ,z)
    elif operacao == 4:
        z = x / y
        print(x, '/' ,y, '=' ,z)



    retry = int(input('Realizar outra operação? \n 1 - Sim \n 2 - Não \n R= '))
    if retry == 1:
        exec = 1

    if retry == 2:
        exec = 0
        quit()
