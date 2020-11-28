import csv
import os
import matplotlib.pyplot as plt
os.chdir('C:\\Users\\user\\Dropbox\\EIVP\\Programmation Python\\Projet')




import numpy as np
import matplotlib.pyplot as plt
import datetime
from math import sqrt
from datetime import timedelta




def tab_donnees(capteur, variable, start_date, end_date):                       #les arguments variable, start_date et end_date sont à rentrer sous forme de chaîne de caractères, le capteur en integer
    with open('post-32566-EIVP_KM.csv') as f :
        fichier_csv = csv.reader(f)
        var = 0
        if variable == 'noise' :
            var = 2
        elif variable == 'temp':
            var = 3
        elif variable == 'humidity':
            var = 4
        elif variable == 'lum':
            var = 5
        else :
            var = 6
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

    return (dates_intervalle, var_intervalle)



def courbe(capteur, variable, start_date, end_date):
    temps = tab_donnees(capteur, variable, start_date, end_date)[0]
    valeurs = tab_donnees(capteur, variable, start_date, end_date)[1]
    plt.plot(temps, valeurs, label = variable)
    plt.legend()
    plt.show()




def courbe_stat(capteur, variable, start_date, end_date):
    l = tab_donnees(capteur, variable, start_date, end_date)
    n = len(l[0])
    dates = l[0]
    var = l[1]
    points_moy = []
    abscisse_points = []
    sigma_inf = []
    sigma_sup = []
    min = var[0]
    abscisse_min = 0
    max = var[0]
    abscisse_max = 0

    date_stop = datetime.datetime.strptime(start_date, '%Y-%m-%d') + datetime.timedelta(days = 1)
    k = 0
    while (str((date_stop)- datetime.timedelta(days = 1)) <= end_date):
        moy_day = 0
        ecart_moy_carre = 0
        ecart_type = 0
        s_day = 0
        var_day = []

        while (k < len(dates) and (datetime.datetime.strptime(dates[k], '%Y-%m-%d %H:%M:%S') < date_stop)):
            s_day = s_day + var[k]

            if var[k] < min :
                min = var[k]
                abscisse_min = dates[k]
            elif max < var[k]:
                max = var[k]
                abscisse_max = dates[k]

            var_day.append(var[k])
            k = k+1

        moy_day = s_day/len(var_day)
        points_moy.append(moy_day)

        for elements in var_day:
            ecart_moy_carre = ecart_moy_carre + ((elements - moy_day)**2)
        ecart_type = sqrt(ecart_moy_carre/len(var_day))
        sigma_inf.append(moy_day - ecart_type)
        sigma_sup.append(moy_day + ecart_type)

        abscisse_points.append(dates[(k + (k-len(var_day)))//2])                #on prend la date au milieu de la journée (la date de la mesure médiane sur chaque jour)
        date_stop = date_stop + datetime.timedelta(days = 1)


    plt.plot(dates, var, label = variable)
    plt.plot(abscisse_points, points_moy, label = 'moyenne')
    plt.plot(abscisse_points, sigma_inf, label = 'écart-type inférieur')
    plt.plot(abscisse_points, sigma_sup, label = 'écart-type supérieur')
    plt.scatter(abscisse_min, min, label = 'min')
    plt.scatter(abscisse_max, max, label = 'max')
    plt.legend()
    plt.show()



def humidex(capteur, start_date, end_date) :
    dates = tab_donnees(capteur, 'temp', start_date, end_date)[0]
    temp = tab_donnees(capteur, 'temp', start_date, end_date)[1]
    humidity = tab_donnees(capteur, 'humidity', start_date, end_date)[1]
    H = []
    n = len(temp)
    date_stop = datetime.datetime.strptime(start_date, '%Y-%m-%d') + datetime.timedelta(days = 1)
    jours = [str((date_stop)- datetime.timedelta(days = 1))[:10]]           #on prélève seulement la date et non l'heure
    k = 0
    while (str((date_stop)- datetime.timedelta(days = 1)) <= end_date):
        i = 0
        compteur = 0
        sum_i = 0
        while (k < len(dates) and (datetime.datetime.strptime(dates[k], '%Y-%m-%d %H:%M:%S') < date_stop)):
            sum_i = sum_i + temp[k] + (5/9)*(6.112*10**(7.5*(temp[k]/(237.7+temp[k])))*(humidity[k]/100)-10)
            compteur = compteur+1
            k = k+1
        i = sum_i/compteur
        H.append(round(i, 2))
        jours.append(str((date_stop))[:10])
        date_stop = date_stop + datetime.timedelta(days = 1)

    for j in range(len(jours)):
        print('le ' + jours[j] + ', le coef humidex vaut : ' + str(H[j]))




def coef_correlation(capteur, variable_1, variable_2, start_date, end_date):
    l_1 = tab_donnees(capteur, variable_1, start_date, end_date)
    l_2 = tab_donnees(capteur, variable_2, start_date, end_date)
    dates = l_1[0]
    n = len(dates)
    var_1 = l_1[1]
    var_2 = l_2[1]
    sum_1 = 0
    sum_2 = 0
    ecart_moy_carre_1 = 0
    ecart_moy_carre_2 = 0
    produit = 0

    for i in range(n):
        sum_1 = sum_1 + var_1[i]
        sum_2 = sum_2 + var_2[i]
    moy_1 = sum_1/n
    moy_2 = sum_2/n

    for k in range(n):
        ecart_moy_carre_1 += (var_1[i] - moy_1)**2
        ecart_moy_carre_2 += (var_2[i] - moy_2)**2
        produit += (var_1[i] - moy_1)*(var_2[i] - moy_2)
    sigma_1 = sqrt(ecart_moy_carre_1/n)
    sigma_2 = sqrt(ecart_moy_carre_2/n)
    covariance = produit/n
    r = covariance/(sigma_1*sigma_2)

    plt.plot(dates, var_1, label = variable_1)
    plt.plot(dates, var_2, label = variable_2)
    plt.title('r = ' + str(r))
    plt.legend()
    plt.show()
    return (r, moy_1, moy_2, sigma_1, sigma_2, produit, ecart_moy_carre_1, n)




def similarites(capteur_1, capteur_2, variable, start_date, end_date):
    l_1 = tab_donnees(capteur_1, variable, start_date, end_date)
    l_2 = tab_donnees(capteur_2, variable, start_date, end_date)
























