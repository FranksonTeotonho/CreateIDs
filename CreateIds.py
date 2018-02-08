import numpy as np
import pandas as pd

def createIds():

    N_protein_a = pd.read_csv('OriginalFiles/N_protein_a_Yeast.csv', header = None)
    a = N_protein_a.iloc[:, :].values
    N_protein_b = pd.read_csv('OriginalFiles/N_protein_b_Yeast.csv', header = None)
    b = N_protein_b.iloc[:, :].values
    P_protein_a = pd.read_csv('OriginalFiles/P_protein_a_Yeast.csv', header = None)
    c = P_protein_a.iloc[:, :].values
    P_protein_b = pd.read_csv('OriginalFiles/P_protein_b_Yeast.csv', header = None)
    d = P_protein_b.iloc[:, :].values

    visitados = []

    NPa = open('N_protein_a_Yeast_IDs.csv','w')
    NPb = open('N_protein_b_Yeast_IDs.csv','w')
    PPa = open('P_protein_a_Yeast_IDs.csv','w')
    PPb = open('P_protein_b_Yeast_IDs.csv','w')

    NPa.close()
    NPb.close()
    PPa.close()
    PPb.close()

    print("============= N_protein_a ===============")

    for i in a:
        print(i)

        if((existeNaLista(i,visitados)) == False):
            visitados.append(i)

        NPa = open('N_protein_a_Yeast_IDs.csv', 'r')  # Abra o arquivo (leitura)
        conteudo = NPa.readlines()
        conteudo.append(str(visitados.index(i)) + '\n')  # insira seu conteúdo

        NPa = open('N_protein_a_Yeast_IDs.csv', 'w')  # Abre novamente o arquivo (escrita)
        NPa.writelines(conteudo)  # escreva o conteúdo criado anteriormente nele.

        NPa.close()

    print("============= N_protein_b ===============")

    for i in b:
        print(i)

        if ((existeNaLista(i, visitados)) == False):
            visitados.append(i)

        NPb = open('N_protein_b_Yeast_IDs.csv', 'r')  # Abra o arquivo (leitura)
        conteudo = NPb.readlines()
        conteudo.append(str(visitados.index(i)) + '\n')  # insira seu conteúdo

        NPb = open('N_protein_b_Yeast_IDs.csv', 'w')  # Abre novamente o arquivo (escrita)
        NPb.writelines(conteudo)  # escreva o conteúdo criado anteriormente nele.

        NPb.close()

    print("============= P_protein_a ===============")

    for i in c:
        print(i)

        if ((existeNaLista(i, visitados)) == False):
            visitados.append(i)

        PPa = open('P_protein_a_Yeast_IDs.csv', 'r')  # Abra o arquivo (leitura)
        conteudo = PPa.readlines()
        conteudo.append(str(visitados.index(i)) + '\n')  # insira seu conteúdo

        PPa = open('P_protein_a_Yeast_IDs.csv', 'w')  # Abre novamente o arquivo (escrita)
        PPa.writelines(conteudo)  # escreva o conteúdo criado anteriormente nele.

        PPa.close()

    print("============= P_protein_b ===============")

    for i in d:
        print(i)

        if ((existeNaLista(i, visitados)) == False):
            visitados.append(i)

        PPb = open('P_protein_b_Yeast_IDs.csv', 'r')  # Abra o arquivo (leitura)
        conteudo = PPb.readlines()
        conteudo.append(str(visitados.index(i)) + '\n')  # insira seu conteúdo

        PPb = open('P_protein_b_Yeast_IDs.csv', 'w')  # Abre novamente o arquivo (escrita)
        PPb.writelines(conteudo)  # escreva o conteúdo criado anteriormente nele.

        PPb.close()

def existeNaLista(Elem, lista):

    for i in lista:
        if i == Elem:
            return True

    return False
