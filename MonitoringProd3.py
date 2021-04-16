# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:37:13 2021

@author: A489100
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:58:03 2021

@author: A489100
"""

import pandas as pd
import plotly_express as px
import numpy as np
import streamlit as st
#path = r"C:\Users\A489100"
#file = r"\DataTest.csv"
#data=pd.read_csv(path+file,encoding='latin1',sep=";") 

				

def demande_en_nombre(df):
   
    d_f=pd.pivot_table(df,index=["TYP_CLIENT2"],columns=["TIMEUNIT_APPLICATION_MONTH"],values=["Count"],aggfunc="sum",fill_value=0,margins=True,dropna=True)
    return d_f

def distribution(df):
    df1=df.groupby('TIMEUNIT_APPLICATION_MONTH').sum().reset_index()
    merged=pd.merge(left = df, right = df1, how="outer",on=["TIMEUNIT_APPLICATION_MONTH"])
    df_Distribution=pd.DataFrame(columns=['TIMEUNIT_APPLICATION_MONTH','TYP_CLIENT2','Distribution'])
    for i in merged.index : 
        distribution=(merged["Count_x"][i])/(merged["Count_y"][i])
        A=(merged["TIMEUNIT_APPLICATION_MONTH"][i])
        B=(merged["TYP_CLIENT2"][i])
        df2=pd.DataFrame({'TIMEUNIT_APPLICATION_MONTH': [A], 'TYP_CLIENT2': [B], 'Distribution': [str(round(distribution*100))+'%']})
        df_Distribution=pd.concat([df_Distribution,df2],ignore_index = True)
    res=pd.pivot_table(df_Distribution,index="TYP_CLIENT2",columns=["TIMEUNIT_APPLICATION_MONTH"],values=["Distribution"],aggfunc="sum",fill_value=0)#,margins=True,dropna=True)
    return res
def evolution(df):
    df_evolution=pd.pivot_table(df,index=["TYP_CLIENT2"],columns=["TIMEUNIT_APPLICATION_MONTH"],values=["Count"],aggfunc="sum",fill_value=0,margins=True,dropna=True)
    res=df_evolution.pct_change(axis='columns')
    res=res.fillna(0)
    return res
def graphe_demande_en_nombre(df):
    fig1 = px.bar(df, x='TIMEUNIT_APPLICATION_MONTH', y='Count', color='TYP_CLIENT2', height=400)
    return fig1


###########################################demande_financée_en_nombre



def demande_fin_en_nombre(dfin):
    res=pd.pivot_table(dfin,index=["TYP_CLIENT2"],columns=["TIMEUNIT_APPLICATION_MONTH"],values=["Count"],aggfunc="sum",fill_value=0,margins=True,dropna=True)
    return res

def distributionfin(dfin):
    dfin1=dfin.groupby('TIMEUNIT_APPLICATION_MONTH').sum().reset_index()
    #df1=df.groupby('TIMEUNIT_APPLICATION_MONTH').sum().reset_index()
    merged=pd.merge(left = dfin, right = dfin1, how="outer",on=["TIMEUNIT_APPLICATION_MONTH"])
    df_Distribution=pd.DataFrame(columns=['TIMEUNIT_APPLICATION_MONTH','TYP_CLIENT2','Distribution'])
    for i in merged.index : 
        distribution=(merged["Count_x"][i])/(merged["Count_y"][i])
        A=(merged["TIMEUNIT_APPLICATION_MONTH"][i])
        B=(merged["TYP_CLIENT2"][i])
        df2=pd.DataFrame({'TIMEUNIT_APPLICATION_MONTH': [A], 'TYP_CLIENT2': [B], 'Distribution': [str(round(distribution*100))+'%']}
                      )
        #pd.DataFrame([[A,B,distribution]])
        #print(df2)
        df_Distribution=pd.concat([df_Distribution,df2],ignore_index = True)
    res=pd.pivot_table(df_Distribution,index="TYP_CLIENT2",columns=["TIMEUNIT_APPLICATION_MONTH"],values=["Distribution"],aggfunc="sum",fill_value=0)#,margins=True,dropna=True)
    return res
def evolutionfin(dfin):
    df_evolution=pd.pivot_table(dfin,index=["TYP_CLIENT2"],columns=["TIMEUNIT_APPLICATION_MONTH"],values=["Count"],aggfunc="sum",fill_value=0,margins=True,dropna=True)
    res=df_evolution.pct_change(axis='columns')
    res=res.fillna(0)
    return res
def graphe_demande_fin_en_nombre(dfin):
    fig1 = px.bar(dfin, x='TIMEUNIT_APPLICATION_MONTH', y='Count', color='TYP_CLIENT2', height=400)
    return fig1


###########################################demande_en_montant
def demande_en_montant(dfm):
    d_f=pd.pivot_table(dfm,index=["TYP_CLIENT2"],columns=["TIMEUNIT_APPLICATION_MONTH"],values=["Montant"],aggfunc="sum",fill_value=0,margins=True,dropna=True)
    return d_f

def distributionmont(dfm):
    df1m=dfm.groupby('TIMEUNIT_APPLICATION_MONTH').sum().reset_index()
    merged=pd.merge(left = dfm, right = df1m, how="outer",on=["TIMEUNIT_APPLICATION_MONTH"])
    df_Distribution=pd.DataFrame(columns=['TIMEUNIT_APPLICATION_MONTH','TYP_CLIENT2','Distribution'])
    for i in merged.index : 
        distribution=(merged["Montant_x"][i])/(merged["Montant_y"][i])
        A=(merged["TIMEUNIT_APPLICATION_MONTH"][i])
        B=(merged["TYP_CLIENT2"][i])
        df2=pd.DataFrame({'TIMEUNIT_APPLICATION_MONTH': [A], 'TYP_CLIENT2': [B], 'Distribution': [str(round(distribution*100))+'%']}
                      )
        #pd.DataFrame([[A,B,distribution]])
        #print(df2)
        df_Distribution=pd.concat([df_Distribution,df2],ignore_index = True)
    res=pd.pivot_table(df_Distribution,index="TYP_CLIENT2",columns=["TIMEUNIT_APPLICATION_MONTH"],values=["Distribution"],aggfunc="sum",fill_value=0)#,margins=True,dropna=True)
    return res
def evolutionMONT(dfm):
    df_evolution=pd.pivot_table(dfm,index=["TYP_CLIENT2"],columns=["TIMEUNIT_APPLICATION_MONTH"],values=["Montant"],aggfunc="sum",fill_value=0,margins=True,dropna=True)
    res=df_evolution.pct_change(axis='columns')
    res=res.fillna(0)
    return res
def graphe_demande_en_montant(dfm):
    fig1 = px.bar(dfm, x='TIMEUNIT_APPLICATION_MONTH', y='Montant', color='TYP_CLIENT2', height=400)
    return fig1

###########################################demande_financée_en_montant
def demande_fin_en_montant(dfinm):
    d_f=pd.pivot_table(dfinm,index=["TYP_CLIENT2"],columns=["TIMEUNIT_APPLICATION_MONTH"],values=["Montant"],aggfunc="sum",fill_value=0,margins=True,dropna=True)
    return d_f

def distributionfinmont(dfinm):
    dfin1m=dfinm.groupby('TIMEUNIT_APPLICATION_MONTH').sum().reset_index()
    merged=pd.merge(left = dfinm, right = dfin1m, how="outer",on=["TIMEUNIT_APPLICATION_MONTH"])
    df_Distribution=pd.DataFrame(columns=['TIMEUNIT_APPLICATION_MONTH','TYP_CLIENT2','Distribution'])
    for i in merged.index : 
        distribution=(merged["Montant_x"][i])/(merged["Montant_y"][i])
        A=(merged["TIMEUNIT_APPLICATION_MONTH"][i])
        B=(merged["TYP_CLIENT2"][i])
        df2=pd.DataFrame({'TIMEUNIT_APPLICATION_MONTH': [A], 'TYP_CLIENT2': [B], 'Distribution': [str(round(distribution*100))+'%']}
                      )
        #pd.DataFrame([[A,B,distribution]])
        #print(df2)
        df_Distribution=pd.concat([df_Distribution,df2],ignore_index = True)
    res=pd.pivot_table(df_Distribution,index="TYP_CLIENT2",columns=["TIMEUNIT_APPLICATION_MONTH"],values=["Distribution"],aggfunc="sum",fill_value=0)#,margins=True,dropna=True)
    return res
def evolutionfinMONT(dfinm):
    df_evolution=pd.pivot_table(dfinm,index=["TYP_CLIENT2"],columns=["TIMEUNIT_APPLICATION_MONTH"],values=["Montant"],aggfunc="sum",fill_value=0,margins=True,dropna=True)
    res=df_evolution.pct_change(axis='columns')
    res=res.fillna(0)
    return res

def graphe_demande_fin_en_montant(dfinm):
    fig1 = px.bar(dfinm, x='TIMEUNIT_APPLICATION_MONTH', y='Montant', color='TYP_CLIENT2', height=400)
    return fig1