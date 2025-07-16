import time
import os

def insertion_sort(A,n):
    pivo = None

    for i in range (1,n):
        pivo = A[i]

        j = i - 1

        while j >= 0 and A[j] > pivo:
            A[j+1] = A[j]
            j = j - 1
        
        A[j+1] = pivo

    return A
        

def selection_sort(A,n):
    for i  in range (0, n - 1):
        i_min = i

        for j in range (i + 1, n):
            if(A[j] < A[i_min]):
                i_min = j
        
        if( A[i] != A[i_min]):
            temp = A[i]
            A[i] = A[i_min]
            A[i_min] = temp

    return A


entrada = None

while entrada != "q" and entrada != "Q":
    print("Selecione a Operacao Desejada:")
    print("1 - Testar Algoritmo Insertion e Selection em Conjunto")
    print("2 - Testar Algoritmo Insertion")
    print("3 - Testar Algoritmo Selection")
    print("q - Sair")
    entrada = input()

    if(entrada == "1"):
        print("Digite o Nome do Arquivo: (deve estar presente na pasta do codigo)")
        in_arquivo = input()

        if os.path.exists(in_arquivo):

            arquivo = open(in_arquivo, "r")
            dados = [int(linha) for linha in arquivo.read().splitlines()]
            arquivo.close()
        else:
            print("Arquivo Nao Encontrado!")
            continue

        print("Organizando os Dados com Insertion Sort, Aguarde.....")
        start = time.time()

        D_organizado_insertion = insertion_sort(dados.copy(),len(dados))

        end = time.time()

        ttotal_insertion = end - start

        print("Organizando os Dados com Selection Sort, Aguarde.....")

        start = time.time()

        D_organizado_selection = selection_sort(dados.copy(),len(dados))

        end = time.time()

        ttotal_selection = end - start

        print("Organizacao Concluida!")
        print(f"O Insertion Sort Levou {ttotal_insertion} Segundos!")
        print(f"O Selection Sort Levou {ttotal_selection} Segundos!")

        if(ttotal_insertion < ttotal_selection):
            print(f"O Insertion Sort foi mais rapido com a diferença de {ttotal_selection - ttotal_insertion} Segundos!")
        
        else:
            print(f"O Selection Sort foi mais rapido com a diferença de {ttotal_insertion - ttotal_selection} Segundos!")

        n_arquivo, extensao = os.path.splitext(in_arquivo)

        file_insertion = open(f"{n_arquivo}_insertion{extensao}", "w")

        file_insertion.writelines(str(linha) + '\n' for linha in D_organizado_insertion)

        file_insertion.close()



        file_selection = open(f"{n_arquivo}_selection{extensao}", "w")

        file_selection.writelines(str(linha) + '\n' for linha in D_organizado_selection)

        file_selection.close()

        print("Arquivos Organizados Salvos na Pasta.")
        continue

    elif(entrada == "2"):
        print("Digite o Nome do Arquivo: (deve estar presente na pasta do codigo)")
        in_arquivo = input()

        if os.path.exists(in_arquivo):

            arquivo = open(in_arquivo, "r")
            dados = [int(linha) for linha in arquivo.read().splitlines()]
            arquivo.close()
        else:
            print("Arquivo Nao Encontrado!")
            continue

        print("Organizando os Dados com Insertion Sort, Aguarde.....")

        start = time.time()

        D_organizado_insertion = insertion_sort(dados.copy(),len(dados))

        end = time.time()

        ttotal_insertion = end - start

        print("Organizacao Concluida!")
        print(f"O Insertion Sort Levou {ttotal_insertion} Segundos!")

        n_arquivo, extensao = os.path.splitext(in_arquivo)

        file_insertion = open(f"{n_arquivo}_insertion{extensao}", "w")

        file_insertion.writelines(str(linha) + '\n' for linha in D_organizado_insertion)

        file_insertion.close()

        print("Arquivos Organizados Salvos na Pasta.")
        continue

    elif(entrada == "3"):

        print("Digite o Nome do Arquivo: (deve estar presente na pasta do codigo)")
        in_arquivo = input()

        if os.path.exists(in_arquivo):
            arquivo = open(in_arquivo, "r")
            dados = [int(linha) for linha in arquivo.read().splitlines()]
            arquivo.close()
        else:
            print("Arquivo Nao Encontrado!")
            continue

        print("Organizando os Dados com Selection Sort, Aguarde.....")

        start = time.time()

        D_organizado_selection = selection_sort(dados.copy(),len(dados))

        end = time.time()

        ttotal_selection = end - start

        print("Organizacao Concluida!")
        print(f"O Selection Sort Levou {ttotal_selection} Segundos!")

        n_arquivo, extensao = os.path.splitext(in_arquivo)


        file_selection = open(f"{n_arquivo}_selection{extensao}", "w")

        file_selection.writelines(str(linha) + '\n' for linha in D_organizado_selection)

        file_selection.close()

        print("Arquivos Organizados Salvos na Pasta.")
        continue

        
    else:
        continue