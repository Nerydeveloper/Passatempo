from random import sample
import collections
from time import sleep

jogos = []
qnt_jogos = 0

#LAÇO DE REPETIÇÃO
while qnt_jogos < 1:
    
    jogo = sample( range(1, 26), 15)
    #ORDENA JOGO EM ORDEM CRESCENTE
    jogo.sort()
    jogos.append(jogo)
    #o indice x é igual a indice já existente b da lista, delete x ou se x for igual a jogo
    lista_loterica = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[2,3,5,6,8,9,13,15,16,20,21,22,23,24,25]]
    for lista in lista_loterica:
        if lista not in jogos:
            jogos.append(jogo)
            
        else:
            qnt_jogos * 1
            print(f"Deletando {jogo}")
            sleep(1)
            del jogo
    
        


        
        

    

#ATE AQUI O PROGRAMA ME MOSTRA N QUANTIDADES DE JOGOS A DEPENDER DOS N POSSIVEIS JOGOS, 
#PRECISO ENCONTRAR UMA FORMA DE LIMITAR ISSO PARA 4 JOGOS SENDO QUE MESMO ASSIM QUERO DE 
#O PROGRAMA PERCORRA TODAS OS POSSIVEIS JOGOS
print("Você pode apostar nos seguintes jogos: ", jogos,"\n")