import csv
import os
os.chdir('C:\\Users\\user\\Dropbox\\EIVP\\Programmation Python\\Projet')

f = open('EIVP_KM.csv')

fichier_csv = csv.reader(f)


import numpy as np
import matplotlib.pyplot as plt



def tableau_donnees():                                                          #fichier d'essai, peut être supprimé
    tab = []
    for line in fichier_csv :
        tab.append(line)
    return tab


def tab_donnees():
    tab = []
    for line in fichier_csv :
        for i in range(len(line)):
            tab.append(line[i].split(sep = ";", maxsplit = -1))
    n = len(tab)
    tab_donnees = []
    for k in range(1, n):
        line = []
        for i in range(6):
            line.append(float(tab[k][i]))
        line.append(tab[k][6])
        tab_donnees.append(line)
    return tab_donnees                                                          #fonctionne








