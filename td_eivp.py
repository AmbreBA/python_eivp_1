import csv
import os
import matplotlib.pyplot as plt
os.chdir('C:\\Users\\user\\Dropbox\\EIVP\\Programmation Python\\Projet')

f = open('post-32566-EIVP_KM.csv')

fichier_csv = csv.reader(f)


import numpy as np
import matplotlib.pyplot as plt



def tableau_donnees():                                                          #fichier d'essai, peut être supprimé
    tab = []
    for line in fichier_csv :
        tab.append(line)
    return tab


def tab1_donnees():
    tab = []
    for line in fichier_csv :
        for i in range(len(line)):
            tab.append(line[i].split(sep = ";", maxsplit = -1))
    n = len(tab)
    tab_donnees = []
    tab_dates = []
    for k in range(1, n):
        line = []
        for i in range(1, 7):
            line.append(float(tab[k][i]))
        line.append(tab[k][7])
        tab_donnees.append(line)
    return tab_donnees                                                          #fonctionne mais on ne peut pas en faire un tab numpy car le dtype de la colonne 7 est un string, et un tab numpy ne prend qu'un seul dtype





def tab_donnees():                                                              #fonctionne. Il faut maintenant faire pareil pour chaque capteur, donc 6 tableaux de données et 6 tableaux de dates
    list = []
    for line in fichier_csv :
        for i in range(len(line)):
            list.append(line[i].split(sep = ";", maxsplit = -1))
    n = len(list)
    list_donnees_1 = []
    list_donnees_2 = []
    list_donnees_3 = []
    list_donnees_4 = []
    list_donnees_5 = []
    list_donnees_6 = []
    list_dates_1 = []
    list_dates_2 = []
    list_dates_3 = []
    list_dates_4 = []
    list_dates_5 = []
    list_dates_6 = []
    for k in range(1, n):
        if list[k][1] == '1':
            line = []
            for i in range(2, 7):
                line.append(float(list[k][i]))
            date = list[k][7][0:19]
            list_donnees_1.append(line)
            list_dates_1.append(date)
        elif list[k][1] == '2':
            line = []
            for i in range(2, 7):
                line.append(float(list[k][i]))
            date = list[k][7][0:19]
            list_donnees_2.append(line)
            list_dates_2.append(date)
        elif list[k][1] == '3':
            line = []
            for i in range(2, 7):
                line.append(float(list[k][i]))
            date = list[k][7][0:19]
            list_donnees_3.append(line)
            list_dates_3.append(date)
        elif list[k][1] == '4':
            line = []
            for i in range(2, 7):
                line.append(float(list[k][i]))
            date = list[k][7][0:19]
            list_donnees_4.append(line)
            list_dates_4.append(date)
        elif list[k][1] == '5':
            line = []
            for i in range(2, 7):
                line.append(float(list[k][i]))
            date = list[k][7][0:19]
            list_donnees_5.append(line)
            list_dates_5.append(date)
        else :
            line = []
            for i in range(2, 7):
                line.append(float(list[k][i]))
            date = list[k][7][0:19]
            list_donnees_6.append(line)
            list_dates_6.append(date)

    tab_donnees_1 = np.array(list_donnees_1)
    tab_donnees_6 = np.array(list_donnees_6)

    temp_11 = []
    dates_1 = []
    for i in range(len(list_dates_1)):
        if ('2019-08-14' < list_dates_1[i] < '2019-08-23'):
            dates_1.append(list_dates_1[i])
            temp_11.append(tab_donnees_1[i,0])

    temp_1 = tab_donnees_1[:,0]
    temp_6 = tab_donnees_6[:,0]
    tab_donnees_2 = np.array(list_donnees_2)
    tab_donnees_3 = np.array(list_donnees_3)
    tab_donnees_4 = np.array(list_donnees_4)
    tab_donnees_5 = np.array(list_donnees_5)
    tab_donnees_6 = np.array(list_donnees_6)
    tab_dates_1 = np.array(list_dates_1)
    tab_dates_2 = np.array(list_dates_2)
    tab_dates_3 = np.array(list_dates_3)
    tab_dates_4 = np.array(list_dates_4)
    tab_dates_5 = np.array(list_dates_5)
    tab_dates_6 = np.array(list_dates_6)

    m = moy


    plt.plot(dates_1, temp_11)
    plt.plot(list_dates_6, temp_6)                                                #marche, mais une fois sur 2 : affiche le message
    plt.show()                                                                  #d'erreur too many indices for array
    return temp_6





