# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:37:17 2020

@author: Ellaine
"""

import pandas as pd

df = pd.read_csv('DataSeerGrabPrizeDataSample.csv')

df.describe()

df.dropna()

df.describe()

df.to_csv('grab_on_spyder.csv', index=False)