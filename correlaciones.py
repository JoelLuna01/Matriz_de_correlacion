import numpy as np
import pandas as pd 
import datetime as dt 
import os 
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, DayLocator

archivos= "2021_10_EstMeteorologica.csv"
datos = pd.read_csv(archivos, sep = ";", decimal = ",")
print(datos)
sensores = ["TEMP", "Humudity", "Solar_rad", "Bar_press."]
unidades = ["(ºC)", "(%)", "kW", "hPa"]
tamano = len(datos)

mediciones=datos[sensores].copy()
matriz_correlacion = mediciones,corr()

print("Matriz de Correlación:")
print(matriz_correlacion)