import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

#Importación de los datos
print("---- Importacion de los datos---------")
df = pd.read_excel (r'C:/Users/Ariel/Desktop/Ejercicio (1).xls')
print("\n")
#Variables disponibles en los datos
print("------ Variables disponibles en los datos---------")
print(list(df))
print("\n")
#Crear la columna de fecha
df["Fecha"] = df.apply(lambda row: datetime(
                              row['Año'], row['Mes'], row['Dia']), axis=1)
#Cantidad de registros y cantidad de variables
print("------- Cantidad de registros y varilables--------")
print(df.shape)
print("\n")

#---------------Desarrollo------------------------
#1. Segmentación de los clientes por Margen Bruto
#Cantidad de clientes unicos
print("----------Cantidad de clientes unicos---------")
print(df["ID Cliente"].nunique())
print("\n")

#Distribucion de las Ventas
#Descripci{on de los datos
print(df["Ventas"].describe())
#Histograma de las Ventas
# df["Ventas"].plot(kind="hist")
#Organizacion de los clientes con mayores Ventas
dfVentas = df[["ID Cliente","Ventas","Fecha","Año","Margen Bruto"]]
#Ventas historicas
ventasHistoricas = dfVentas.pivot_table(index="Fecha",aggfunc=sum)

# ventasHistoricas["Ventas"].plot(kind="barh")
ventasHistoricas["Margen Bruto"].plot(kind="hist")
# plt.ylabel("Ventas (COP($))")
#Clientes con mayores Ventas
clientesOrganizadosVentas = dfVentas.pivot_table(index="ID Cliente", 
	values="Ventas", aggfunc=sum).sort_values(by="Ventas", ascending=False)
#Seleccionar los primeros 10 Cliente con mayores Ventas
print(clientesOrganizadosVentas[:5])
# clientesOrganizadosVentas.head(5).plot(kind="barh")
#Cliente con mayores Ventas por años
clientesVentasAño = dfVentas.pivot_table(index=["Fecha","ID Cliente"],
	values="Ventas",aggfunc=sum).sort_values(by="Ventas", ascending=False)
print("--------Cliente con mayores Ventas por Año----------")
print(clientesVentasAño)

#Distribucion del Margen Bruto
#Descripcion de los datos
print(df["Margen Bruto"].describe())
#Histograma del Margen Bruto
# df["Margen Bruto"].plot(kind="barh", color="green")
plt.show()
dfMargenBruto = df[["ID Cliente", "Margen Bruto"]]
clientesOrganizadosMargenBruto = dfMargenBruto.pivot_table(index="ID Cliente", 
	values="Margen Bruto", aggfunc=sum).sort_values(by="Margen Bruto", ascending=False)
print(clientesOrganizadosMargenBruto[:5])

#Boxplot para Ventas y para Margen Bruto
sns.boxplot( y=df["Margen Bruto"])
sns.stripplot(y=df["Margen Bruto"], color="orange", jitter=0.2, size=2.5)

from sklearn.tree import DecisionTreeClassifier as DTC# Import Decision Tree Classifier
from sklearn.model_selection import train_test_split as TTS# Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

df.head()