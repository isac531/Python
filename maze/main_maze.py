# -*- coding: utf-8 -*-
import time
from maze import Maze
from collections import deque

# 1. Crie uma nova pilha
# A estrutura deque é eficiente para operações de append (push) e pop em suas extremidades
pilha = deque()

# Configuração inicial do labirinto a partir do arquivo
maze_csv_path = "labirinto1.txt"
maze = Maze() 
maze.load_from_csv(maze_csv_path)

# Inicia a thread de visualização do Pygame
maze.run()

# Posiciona o jogador e o prêmio de forma aleatória no labirinto
maze.init_player()

# 2. Localize a posição inicial do jogador
posicao_inicial = maze.get_init_pos_player()

# 3. Insira sua localização na pilha
pilha.append(posicao_inicial)

caminho_encontrado = False
print("Iniciando busca pelo tesouro...")

# 4. Enquanto a pilha não estiver vazia
while pilha:
    # 5. Retire uma localização (linha, coluna) da pilha
    posicao_atual = pilha.pop()

    # 6. Mova o jogador para este local (para visualização)
    maze.mov_player(posicao_atual)
    
    # Adiciona uma pequena pausa para que seja possível visualizar o processo
    time.sleep(0.05)

    # 7. Se a posição tiver o prêmio no local então...
    if maze.find_prize(posicao_atual):
        # 8. Caminho foi encontrado
        print("Tesouro encontrado na posição:", posicao_atual)
        caminho_encontrado = True
        # 9. Retorne True (neste caso, encerramos o loop)
        break

    # 10. Caso contrário, examine se as casas adjacentes estão livres
    (linha, coluna) = posicao_atual
    
    # Ordem dos vizinhos: Norte, Sul, Leste, Oeste
    vizinhos = [
        (linha - 1, coluna), 
        (linha + 1, coluna), 
        (linha, coluna - 1), 
        (linha, coluna + 1)
    ]
    
    for proxima_posicao in vizinhos:
        # 11. Se sim insira sua posição na pilha
        if maze.is_free(proxima_posicao):
            # Adiciona o vizinho à pilha para ser explorado
            pilha.append(proxima_posicao)
            
            # Marca a célula como "parte do caminho de busca" para não ser revisitada
            # A própria função mov_player já altera o estado da célula, impedindo que is_free retorne True para ela novamente
            # Isso evita que o algoritmo entre em loops infinitos entre duas células.
            maze.mov_player(proxima_posicao)


# 12. Retorne False (se o loop terminar sem encontrar o prêmio)
if not caminho_encontrado:
    print("Não foi possível encontrar um caminho para o tesouro.")

# Mantém a janela do Pygame aberta por mais 20 segundos para visualização do resultado final
time.sleep(20)