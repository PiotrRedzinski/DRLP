# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:51:52 2023

@author: Piotr Rędziński

python script for generating bar charts for technologies in landscape planning
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='white')
plt.rcParams.update({'legend.labelspacing':0.1,'legend.fontsize':9,
                     'legend.frameon':True, 'patch.linewidth':0,
                     'figure.dpi':300,'ytick.left':True,
                     'legend.fancybox':True, 'legend.framealpha':1})

#df = pd.read_excel('C:/ProjektyPython/textClasification/output/ALL PAPERS MAY10_processed_with_pred_app32092023_2.xlsx')
df = pd.read_excel('C:/ProjektyPython/textClasification/output/ALL PAPERS MAY10_processed_with_pred_app_12112023.xlsx')


chart_data = df[['Year','Data science','Data mining','Big data','Crowdsourcing',
                'Open data', 'OthersData']]
chart_data.columns = ['Year','Data Science','Data Mining','Big Data','Crowdsourcing',
                'Open Data', 'Other Data']

chart_vr = df[['Year',"VR", "AR", "MR"]]
chart_3dModelling = df[['Year',"BIM", "LIM", "PointCloud", "Rendering", "3dScanning", "3dModelling"]]
chart_3dModelling.columns = ['Year',"BIM", "LIM", "Point Cloud", "Rendering", "3D Scanning", "3D Models"]

chart_AIrelated = df[['Year',"Deep Learning", "Artificial Intelligence", "Machine learning", "MAS", 'OthersAI']]
chart_AIrelated.columns = ['Year',"Deep Learning", "Artificial Intelligence", "Machine Learning", "MAS", 'Other AI']

chart_desicionSupport = df[['Year',"MCDA/AHP", "PSS/DSS"]]
chart_otherICT = df[['Year',"GPS", "GNSS", "ICT", "Blockchain", "Cloud", "IoT", "Devices"]]


dfdata = chart_data.groupby('Year').agg('sum')
dfvr = chart_vr.groupby('Year').agg('sum')
df3dModelling = chart_3dModelling.groupby('Year').agg('sum')
dfAIrelated = chart_AIrelated.groupby('Year').agg('sum')
dfdesicionSupport = chart_desicionSupport.groupby('Year').agg('sum')
dfotherICT = chart_otherICT.groupby('Year').agg('sum')


dfdata.plot(kind='bar', stacked=True, ylabel="Count", title="Data", color=["#BF0120", "#ee8988", "#fd5a3d", "#580d0d", "#ddb260", "#9E4A4A"]).grid(axis='y')
dfvr.plot(kind='bar', stacked=True, ylabel="Count", title="VR/AR/MR", color=["#db26ab", "#7d2071", "#f7bcdf"]).grid(axis='y')
df3dModelling.plot(kind='bar', stacked=True, ylabel="Count", title="3D Modelling", color=["#051DFA", "#050240", "#39d0fa", "#2e4b7b", "#c1e4e8", "#95A8C6"]).grid(axis='y')
dfAIrelated.plot(kind='bar', stacked=True, ylabel="Count", title="AI Related", color=["#533A7B", "#E3C2FB", "#991794", "#AD2EFB", "#4B244A","#FF00FF"]).grid(axis='y')
dfdesicionSupport.plot(kind='bar', stacked=True, ylabel="Count", title="Decision Support", color=["#FFEA06", "#Ffa600"]).grid(axis='y')
dfotherICT.plot(kind='bar', stacked=True, ylabel="Count", title="Other ICT", color=["#74b933", "#093c19", "#4cfe60", "#2c6d2c", "#c1f084", "#54591E", "#3F5E5A"]).grid(axis='y')

''' kolor który był dla 5G/Byond "#67c4a2" został przydzielony CAD'''

dfCAD = df[['Year',"CAD"]].groupby('Year').agg('sum')
dfdataSum = df[['Year',"Data"]].groupby('Year').agg('sum')
dfvrSum = df[['Year',"VR/AR/MR"]].groupby('Year').agg('sum')
df3dModellingSum = df[['Year',"all3dmodeling"]].groupby('Year').agg('sum')
dfAIrelatedSum = df[['Year',"AI&related"]].groupby('Year').agg('sum')
dfdesicionSupportSum = df[['Year',"MCDA/PSS"]].groupby('Year').agg('sum')
dfotherICTSum = df[['Year',"allICT"]].groupby('Year').agg('sum')
dfRobotic = df[['Year',"Robotic"]].groupby('Year').agg('sum')
dfGIS = df[['Year',"GIS"]].groupby('Year').agg('sum')
dfRemoteSensing = df[['Year',"Remote sensing"]].groupby('Year').agg('sum')
dfOtherDigitalModelling = df[['Year',"Other Digital Modelling"]].groupby('Year').agg('sum')
dfSocialMedia = df[['Year',"Social Media"]].groupby('Year').agg('sum')



colors = {
    'CAD':"#67c4a2",
    'Remote Sensing':"#512E04",
    'GIS':"#FF7800",
    'Other Digital Modelling':"#C1C0CF",
    'AI Related':"#533A7B",
    "Other ICT":"#05F815",
    "3D Modelling":"#051DFA",
    "Data":"#BF0120",
    "Decision Support":"#FFEA06",
    "Robotic":"#27FCE0",
    "VR/AR/MR":"#db26ab",
    "Social Media":"#3E3E42"
    }

dfallframes = {
    'CAD':dfCAD,
    'Remote Sensing':dfRemoteSensing,
    'GIS':dfGIS,
    'Other Digital Modelling':dfOtherDigitalModelling,
    'AI Related':dfAIrelatedSum,
    "Other ICT":dfotherICTSum,
    "3D Modelling":df3dModellingSum,
    "Data":dfdataSum,
    "Decision Support":dfdesicionSupportSum,
    "Robotic":dfRobotic,
    "VR/AR/MR":dfvrSum,
    "Social Media":dfSocialMedia
    }

''' na podstawie dfallsum.sort_values(ascending = False).index.tolist() '''
techorder = ['Remote Sensing',
 'GIS',
 'Other Digital Modelling',
 'AI Related',
 'Other ICT',
 '3D Modelling',
 'Data',
 'Decision Support',
 'Robotic',
 'VR/AR/MR',
 'Social Media',
 'CAD']

colororder = []
for o in techorder:
    colororder.append(colors[o])


dfall = pd.concat([dfRemoteSensing,dfGIS,dfOtherDigitalModelling,
                   dfAIrelatedSum,dfotherICTSum,df3dModellingSum,
                   dfdataSum,dfdesicionSupportSum,dfRobotic,
                   dfvrSum,dfSocialMedia,dfCAD],axis=1)
'''dfallrev = pd.concat([dfSocialMedia,dfvrSum,dfRobotic,dfdesicionSupportSum,
                      dfdataSum,df3dModellingSum,dfotherICTSum,dfAIrelatedSum,
                      dfOtherDigitalModelling,dfGIS,dfRemoteSensing],axis=1)'''
#not needed dfall.columns = techorder
'''dfallrev.columns = techorder[::-1]'''

dfall.plot(kind='bar', stacked=True, ylabel="Count", color=colororder).grid(axis='y')


dfallsum = dfall.sum(axis=0)
dfallsum.sort_values(ascending = False).plot(kind='bar',ylabel="Count", color=colororder).grid(axis='y')
''' uwaga - powyższe nie rysuje się za pierwszym razem '''

dfdata['Sum'] = df[['Year',"Data"]].groupby('Year').agg('sum')
dfvr['Sum'] = df[['Year',"VR/AR/MR"]].groupby('Year').agg('sum')
df3dModelling['Sum'] = df[['Year',"all3dmodeling"]].groupby('Year').agg('sum')
dfAIrelated['Sum'] = df[['Year',"AI&related"]].groupby('Year').agg('sum')
dfdesicionSupport['Sum'] = df[['Year',"MCDA/PSS"]].groupby('Year').agg('sum')
dfotherICT['Sum'] = df[['Year',"allICT"]].groupby('Year').agg('sum')


dfCAD.to_csv('C:/ProjektyPython/textClasification/output/tabelki/CAD.csv', sep='\t')
dfdata.to_csv('C:/ProjektyPython/textClasification/output/tabelki/data.csv', sep='\t')
dfvr.to_csv('C:/ProjektyPython/textClasification/output/tabelki/vr.csv', index = True, sep='\t')
df3dModelling.to_csv('C:/ProjektyPython/textClasification/output/tabelki/3dModelling.csv', index = True, sep='\t')
dfAIrelated.to_csv('C:/ProjektyPython/textClasification/output/tabelki/AIrelated.csv', index = True, sep='\t')
dfdesicionSupport.to_csv('C:/ProjektyPython/textClasification/output/tabelki/desicionSupport.csv', index = True, sep='\t')
dfotherICT.to_csv('C:/ProjektyPython/textClasification/output/tabelki/otherICT.csv', index = True, sep='\t')
dfRobotic.to_csv('C:/ProjektyPython/textClasification/output/tabelki/Robotic.csv', index = True, sep='\t')
dfGIS.to_csv('C:/ProjektyPython/textClasification/output/tabelki/GIS.csv', index = True, sep='\t')
dfRemoteSensing.to_csv('C:/ProjektyPython/textClasification/output/tabelki/RemoteSensing.csv', index = True, sep='\t')
dfOtherDigitalModelling.to_csv('C:/ProjektyPython/textClasification/output/tabelki/OtherDigitalModelling.csv', index = True, sep='\t')
dfSocialMedia.to_csv('C:/ProjektyPython/textClasification/output/tabelki/SocialMedia.csv', index = True, sep='\t')

dfall['Sum'] = dfall.sum(axis=1)
dfall.to_csv('C:/ProjektyPython/textClasification/output/tabelki/dfall.csv', index = True, sep='\t')


''' trzeba powtórzyć dfall.plot bo za pierwszym razem źle sortuje
dfall.drop(columns=['Sum'],axis=1,inplace=True)   
dfall.plot(kind='bar', stacked=True, ylabel="Count", color=colororder).grid(axis='y')
''' 





