#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:59:01 2018

@author: jeanfernandes
"""

import pandas as pd

base = pd.read_csv('./bigData/census.csv')
previsores = base.iloc[:, 0:14].values
classe = base.iloc[:, 14].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
encoder_previsores = LabelEncoder()
#labels = encoder_previsores.fit_transform(previsores[:, 1])
previsores[:, 1] = encoder_previsores.fit_transform(previsores[:, 1])
previsores[:, 3] = encoder_previsores.fit_transform(previsores[:, 3])
previsores[:, 5] = encoder_previsores.fit_transform(previsores[:, 5])
previsores[:, 6] = encoder_previsores.fit_transform(previsores[:, 6])
previsores[:, 7] = encoder_previsores.fit_transform(previsores[:, 7])
previsores[:, 8] = encoder_previsores.fit_transform(previsores[:, 8])
previsores[:, 9] = encoder_previsores.fit_transform(previsores[:, 9])
previsores[:, 13] = encoder_previsores.fit_transform(previsores[:, 13])

onehotencoder = OneHotEncoder(categorical_features = [1, 3, 5, 6, 7, 8, 9, 13])
previsores = onehotencoder.fit_transform(previsores).toarray()

labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe)