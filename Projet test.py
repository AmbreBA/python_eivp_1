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





def tab_donnees(capteur):                                                       #fonctionne. Il faut maintenant faire pareil pour chaque capteur, donc 6 tableaux de données et 6 tableaux de dates
    list = []
    for line in fichier_csv :
        for i in range(len(line)):
            list.append(line[i].split(sep = ";", maxsplit = -1))
    n = len(list)
    list_donnees = []
    list_dates = []
    for k in range(1, n):
        if (float(list[k][1])) == capteur :
            line = []
            for i in range(2, 7):
                line.append(float(list[k][i]))
            date = list[k][7][0:19]
            list_donnees.append(line)
            list_dates.append(date)
    tab_donnees = np.array(list_donnees)
    tab_donnees = np.array(list_donnees)

    temp_11 = []
    dates_1 = []
    for i in range(len(list_dates)):
        if ('2019-08-14' < list_dates[i] < '2019-08-23'):
            dates_1.append(list_dates[i])
            temp_11.append(tab_donnees[i,0])


    plt.plot(dates_1, temp_11)
    plt.show()