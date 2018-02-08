import numpy as np
import pandas as pd

def createTableIds():


    data = pd.read_csv('Matine/NP_protein_a_b_Matine_IDs.csv', header = None)
    d = data.iloc[:, :].values

    print(d)
    table = open("MatineTable.csv",'w')

    for i in d:

        #print(i)

        nID = i[0]

        meuVetor = [0]*1426

        meuVetor[nID] = 1

        searchInteractions(nID, meuVetor, d)

        ta = open('MatineTable.csv', 'r')  # Abra o arquivo (leitura)
        conteudo = ta.readlines()
        conteudo.append(str(nID) + ',' + ",".join(map(str, meuVetor)) + '\n')  # insira seu conteúdo

        print(str(nID) + ',' + ",".join(map(str, meuVetor)))

        ta = open('MatineTable.csv', 'w')  # Abre novamente o arquivo (escrita)
        ta.writelines(conteudo)  # escreva o conteúdo criado anteriormente nele.

        ta.close()

def searchInteractions(id, meuVetor, data):

    for i in data:
        if (i[0] == id):
            meuVetor[i[1]] = 1
