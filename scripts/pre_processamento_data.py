#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 21:37:25 2018

@author: jeanfernandes
"""

import pandas as pd

base = pd.read_csv('./bigData/credit-data.csv')
base.describe()
base.loc[base['idade'] < 0]

#apagar a coluna
base.drop('idade', 1, inplace = True)

#apagar somento os reg com problema
base.drop(base[base.idade < 0].index, inplace = True)

#preenche os valores manualmente
base.mean()
base['idade'].mean()
base['idade'][base.idade > 0].mean()
base.loc[base.idade < 0, 'idade'] = 40.92

pd.isnull(base['idade'])
base.loc[pd.isnull(base['idade'])]

previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(previsores[:, 0:3])
previsores[:, 0:3] = imputer.transform(previsores[:, 0:3])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)