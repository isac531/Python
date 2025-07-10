# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        for l in range(0,3):
            for c in range(0,3):
                if((self.matriz[l][0]+self.matriz[l][1]+self.matriz[l][2]) == 3):
                    return Tabuleiro.JOGADOR_0
                elif((self.matriz[0][c]+self.matriz[1][c]+self.matriz[2][c]) == 3):
                    return Tabuleiro.JOGADOR_0
                elif((self.matriz[0][0]+self.matriz[1][1]+self.matriz[2][2]) == 3):
                    return Tabuleiro.JOGADOR_0
                elif((self.matriz[2][0]+self.matriz[1][1]+self.matriz[0][2]) == 3):
                    return Tabuleiro.JOGADOR_0
                if((self.matriz[l][0]+self.matriz[l][1]+self.matriz[l][2]) == 12):
                    return Tabuleiro.JOGADOR_X
                elif((self.matriz[0][c]+self.matriz[1][c]+self.matriz[2][c]) == 12):
                    return Tabuleiro.JOGADOR_X
                elif((self.matriz[0][0]+self.matriz[1][1]+self.matriz[2][2]) == 12):
                    return Tabuleiro.JOGADOR_X
                elif((self.matriz[2][0]+self.matriz[1][1]+self.matriz[0][2]) == 12):
                    return Tabuleiro.JOGADOR_X

           
        return Tabuleiro.DESCONHECIDO