import csv
import os
import matplotlib.pyplot as plt
os.chdir('C:\\Users\\user\\Dropbox\\EIVP\\Programmation Python\\Projet')




import numpy as np
import matplotlib.pyplot as plt



def tab_donnees(capteur, variable, start_date, end_date):
    with open('post-32566-EIVP_KM.csv') as f :
        fichier_csv = csv.reader(f)
        var = 0
        if variable == 'noise' :
            var = 1
        elif variable == 'temp':
            var = 2
        elif variable == 'humidity':
            var = 3
        elif variable == 'lum':
            var = 4
        else :
            var = 5
        list = []
        for line in fichier_csv :
            for i in range(len(line)):
                list.append(line[i].split(sep = ";", maxsplit = -1))
        n = len(list)
        list_var_capteur = []
        list_dates_capteur = []
        for k in range(1, n):
            date = []
            if ((float(list[k][1])) == capteur) :
                list_var_capteur.append(float(list[k][var]))
                date = list[k][7][0:19]
                list_dates_capteur.append(date)
        dates_intervalle = []
        var_intervalle = []
        for i in range(len(list_dates_capteur)):
            if (start_date < list_dates_capteur[i] < end_date):
                dates_intervalle.append(list_dates_capteur[i])
                var_intervalle.append(list_var_capteur[i])

    plt.plot(dates_intervalle, var_intervalle)
    plt.show()
    return (dates_intervalle, var_intervalle)



def courbe_stat(capteur, variable, start_date, end_date):
    l = tab_donnees(capteur, variable, start_date, end_date)
    n = len(l)
    dates = l[0]
    var = l[1]
    s = 0
    moy = 0
    sigma = 0
    min = var[0]
    max = var[0]

    for k in range(n):
        s = s+var[k]
        if (var[k] <  min):
            min = var[k]
        else :
            max = var[k]
    moy = s/n
    for i in range(n):
        ecart_moy = ecart_moy + (var[i]-moy)*(var[i]-moy)
    sigma = ecart_moy/n

    plt.plot(dates, var)
    plt.show()



