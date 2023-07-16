import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


st.title('Analyse des données')

st.header('Analyse de la consommation et de la production')
st.subheader('La Consommation par Année de 2013 à 2021')


df=pd.read_csv("./df/df_year.csv",index_col=0)
#df=df[df['year']<2022]

st.write(df.shape)
st.write(df.head())
st.write(df.columns)

st.subheader("La consommation en MW d'électricité par année")

# La consommation d'électricité par année


consommation_par_annee = df.groupby("year")["Consommation (MW)"].sum()
st.bar_chart(consommation_par_annee)


# Évolution de la production d'électricité par source au fil du temps
productions = ['Thermique (MW)', 'Nucléaire (MW)', 'Eolien (MW)', 'Solaire (MW)', 'Hydraulique (MW)', 'Pompage (MW)', 'Bioénergies (MW)']
df_day=pd.read_csv("./df/df_day.csv",index_col=0)


#switcher

st.sidebar.header('Filtre')
region=st.sidebar.multiselect( 'Selection régions',
                      options=df['Région'].unique(),
                      default=df['Région'].unique(),
 )
annee=st.sidebar.multiselect('Selection période',      
                      options=df['year'].unique(),
                      default=df['year'].unique(),
                      )
# Évolution de la production d'électricité par source au fil du temps


def load_data():
    data=pd.read_csv('./df/df_day.csv',dtype=('str'))
    return data
#affichage de la table de donnée
df=load_data()

productions = ['Thermique (MW)', 'Nucléaire (MW)', 'Eolien (MW)', 'Solaire (MW)', 'Hydraulique (MW)', 'Pompage (MW)', 'Bioénergies (MW)']

def lineplot():
    fig=plt.figure(figsize=(12, 6))
    for source in productions:
            sns.lineplot(data=df, x='Date', y=source, label=source)
      
    plt.title("Évolution de la production d'électricité par source au fil du temps")
    plt.xlabel('Date')
    plt.ylabel('Production (MW)')
    plt.legend()
    st.line_chart(fig)

lineplot()

#La comparaison de la consommation par région au fil du temps
def lineplot_region():
    fig=plt.figure(figsize=(20,10))
    sns.lineplot(df_day, x="Date", y=productions, hue="Région")
    plt.show()

    st.line_chart(fig)

lineplot_region()
#GRAPH 2
## Évolution de la production d'électricité par source au fil du temps


# La distribution de la consommation d'électricité en fonction des régions

 #pie chart 


# L'évolution de la consommation d'électricité par région au fil du temps



#AxS map libreairy folium

