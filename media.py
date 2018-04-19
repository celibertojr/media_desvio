#encoding: utf-8
import os
import numpy as np
import math

#lista apenas os arquivos txt da pasta
pasta = "/Users/Luiz/Desktop/ler dados/evolucao/"
caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
arquivos_txt = [arq for arq in arquivos if arq.lower().endswith(".txt")]

#cria uma lista para armazenar as saídas
saida = []

#Matriz = np.zeros((Num_arquivos,Num_linhas), dtype=np.float64)
Matriz=[]

NumTabela=3;
MaxPos=100;

tabelaQ = [[0 for col in range(MaxPos)] for row in range(NumTabela)] #Cria a tabela para deposito dos valores lidos

Ntab=0
Npos=0

#percorre os arquivos
for arq in arquivos_txt:
    #abre o arquivo
    with open(arq) as f:
        linhas = f.readlines()
        for linha in linhas:
            valores = linha.split()
            #Matriz.append(valores)
            tabelaQ[Ntab][Npos]=float(valores[1])
            #print Npos
            #print Ntab
            #print valores[1]
            Npos=Npos+1
        Ntab=Ntab+1
        Npos=0

for x in range(MaxPos):
    media = 0
    soma = 0
    for y in range(NumTabela):
        soma = soma + tabelaQ[y][x]
    media = round((soma/Ntab),3) #realiza a soma
    desvio_quad = 0
    for y in range(NumTabela):
        desvio_quad = desvio_quad + ((tabelaQ[y][x] - media)**2)
    desvio_quad = round((math.sqrt(desvio_quad / NumTabela)),3)
    #guarda na lista de saida
    saida.append("{} {}\n".format(media,desvio_quad))


#grava a lista em um novo arquivo
arq_saida = open('saida.txt', 'w')
arq_saida.writelines(saida)
arq_saida.close()
