import streamlit as st
import pandas as pd
import numpy as np
from sklearn.svm import SVC
import matplotlib.pylab as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

#from google.colab import drive
#drive.mount('/content/drive')


st.subheader('Performance du modèle xxxx')

st.subheader('Performance du modèle Xbost')



st.subheader('Comparaison avec le meilleure modele de prediction ')

df_day=pd.read_csv("./df/df_day.csv")

df_day = df_day[["Date", "year", "Région","Consommation (MW)", "Total population", "Température (°C)", "Tarif"]]

df_day=df_day.set_index('Date')
df_day.index=pd.to_datetime(df_day.index)

color_pal=sns.color_palette()
p4=df_day['Consommation (MW)'].plot(style='.',figsize=(15,5),color=color_pal[0],title='Comsomammation en MW 2013 -2022')

st.line_chart(p4, use_container_width=True)



