import pandas as pd

donnees = pd.read_csv('EIVP_KM.csv', sep = ';', names = ['id', 'noise', 'temp', 'humidity', 'lum', 'co2', 'sent_at'], header = 0)

