# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import scipy as sp
import statsmodels.api as sm
import os
import matplotlib.pyplot as plt
import sys

folder='/Users/maxstev/Documents/Grad_School/Avalanche/PDO_ElNino/'

pdo1=pd.read_csv(folder+'PDO19002016.txt',header=0,names=range(1,13))
oni1=pd.read_csv(folder+'ONI19502016.txt',header=0,names=range(1,13))
psnow=pd.read_csv(folder+'ParadiseSnow2016.csv',header=0)

psnow1=psnow
psnow2=pd.Series(data=psnow.values[:,1],index=pd.PeriodIndex(year=psnow.values[:,0],month=5,freq='M'))
psnow3=pd.Series(data=psnow.values[:,1],index=pd.PeriodIndex(year=psnow.values[:,0],month=5,freq='M'))

pdo=pdo1.stack()
oni=oni1.stack()

pyr=pdo.index.get_level_values(0).values
pmo=pdo.index.get_level_values(1).values

oyr=oni.index.get_level_values(0).values
omo=oni.index.get_level_values(1).values

pdo.index=pd.PeriodIndex(year=pyr,month=pmo,freq='M')
oni.index=pd.PeriodIndex(year=oyr,month=omo,freq='M')

pdo.index.name='date'
oni.index.name='date'
psnow2.index.name='date'

all3=pd.DataFrame({'pdo' : pdo, 'oni':oni, 'snow':psnow2})

# psnow2.index=pd.PeriodIndex(year=psnow.values[:,0],month=5,freq='M')

