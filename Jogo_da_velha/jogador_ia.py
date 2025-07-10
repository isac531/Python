# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int):
        for l in range(0,3):
            for c in range(0,3):  

                if((self.matriz[l][0]+self.matriz[l][1]+self.matriz[l][2]) == 2 and self.matriz[l][c] == Tabuleiro.DESCONHECIDO):
                    return(l,c)
                elif((self.matriz[0][c]+self.matriz[1][c]+self.matriz[2][c]) == 2 and self.matriz[l][c] == Tabuleiro.DESCONHECIDO):
                    return(l,c)
                elif((self.matriz[0][0]+self.matriz[1][1]+self.matriz[2][2]) == 2 and self.matriz[c][c] == Tabuleiro.DESCONHECIDO):
                    return(c,c)
                elif((self.matriz[2][0]+self.matriz[1][1]+self.matriz[0][2]) == 2 and self.matriz[c][2 - c] == Tabuleiro.DESCONHECIDO):
                    return(c,2 - c)
                elif(self.matriz[1][1] == Tabuleiro.DESCONHECIDO):
                    return(1,1)
        for l in range(0,3):
             for c in range(0,3):
                if((self.matriz[l][0]+self.matriz[l][1]+self.matriz[l][2]) == 8 and self.matriz[l][c] == Tabuleiro.DESCONHECIDO):
                    return(l,c)
                elif((self.matriz[0][c]+self.matriz[1][c]+self.matriz[2][c]) == 8 and self.matriz[l][c] == Tabuleiro.DESCONHECIDO):
                    return(l,c)
                elif((self.matriz[0][0]+self.matriz[1][1]+self.matriz[2][2]) == 8 and self.matriz[c][c] == Tabuleiro.DESCONHECIDO):
                    return(c,c)
                elif((self.matriz[2][0]+self.matriz[1][1]+self.matriz[0][2]) == 8 and self.matriz[c][2-c] == Tabuleiro.DESCONHECIDO):
                    return(c,2 - c)

        if (self.matriz[0][0] == 4 and self.matriz[2][2] == Tabuleiro.DESCONHECIDO):
            return (2, 2)
        elif (self.matriz[2][2] == 4 and self.matriz[0][0] == Tabuleiro.DESCONHECIDO):
            return (0, 0)
        elif (self.matriz[0][2] == 4 and self.matriz[2][0] == Tabuleiro.DESCONHECIDO):
            return (2, 0)
        elif (self.matriz[2][0] == 4 and self.matriz[0][2] == Tabuleiro.DESCONHECIDO):
            return (0, 2)
        elif (self.matriz[2][2] == Tabuleiro.DESCONHECIDO):
            return (2, 2)
        elif (self.matriz[0][0] == Tabuleiro.DESCONHECIDO):
            return (0, 0)
        elif (self.matriz[2][0] == Tabuleiro.DESCONHECIDO):
            return (2, 0)
        elif (self.matriz[0][2] == Tabuleiro.DESCONHECIDO):
            return (0, 2)

        lista = []
        for l in range(0,3): 
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))  
            
        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]
        
        else:
            return None
        

    