# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 10:20:49 2021

@author: A489100
"""

import streamlit as st
import pandas as pd
import plotly_express as px
import MonitoringProd3 as mp
st.set_page_config(layout="wide")

data_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])


if data_file is not None:
				

				data = pd.read_csv(data_file,encoding='latin1',sep=";")
df = data.groupby(['TIMEUNIT_APPLICATION_MONTH','TYP_CLIENT2'])["NUMDOS"].nunique().reset_index(name="Count")
dfm = data.groupby(['TIMEUNIT_APPLICATION_MONTH','TYP_CLIENT2'])["DEC_MONTANT"].sum().reset_index(name="Montant")
demande_financée=data.loc[data['TP_FINANCED']==1]
dfin = demande_financée.groupby(['TIMEUNIT_APPLICATION_MONTH','TYP_CLIENT2'])["NUMDOS"].nunique().reset_index(name="Count")
dfinm=demande_financée.groupby(['TIMEUNIT_APPLICATION_MONTH','TYP_CLIENT2'])["DEC_MONTANT"].sum().reset_index(name="Montant")
option = st.sidebar.selectbox(
    'Navigation',
     ('Home','Type_Pret', 'Type_Client','Type_Client_Socfin','Décision','Regles'))

if option=='Home':
    st.write('BDP MONITORING DE L_ACCEPTATION')
    
elif option =='Type_Pret':
      option2 = st.selectbox(
    'Navigation',
     ('Demande en nombre','Demande financée en nombre', 'Demande en montant','Demande financée en montant'))
      if option2 =='Demande en nombre':
          st.title('Suivi de la production')
          u=mp.demande_en_nombre(df)
          st.subheader('Demande en nombre')
          st.write(u)
          u1=mp.distribution(df)
          st.subheader('Distribution')
          st.write(u1)
          
          with st.beta_expander("See evolution"):
              st.subheader('Evolution \ période précédente')
              u2=mp.evolution(df)
              st.write(u2)
          fig1 = mp.graphe_demande_en_nombre(df)
          barplot_chart = st.write(fig1)