import pandas as pd
import numpy as np
from tqdm import tqdm
from itertools import combinations
import math
import sys
 
#Define Dataset
subset = pd.read_csv()
columnas = subset.columns
columnas = [s.replace(" ", "_") for s in columnas]
subset.columns = columnas #Eliminate spaces in name columns
subset = subset.loc[subset["Diagnosis_simplified"].isin(["HB", "HCC", "NOS"])]

#Take features from text file
liste = []
with open(sys.argv[1]) as fa:
    sys.stdout.write(sys.argv[1])
    lines = fa.readlines()
    for line in lines:
        words = line.split()
        words = [s.replace("'", "") for s in words]
        words = [s.replace("[", "") for s in words]
        words = [s.replace("]", "") for s in words]


        for word in words:
            liste.append(word)

variables = liste
megalist =  []
#Create pairs of patients and calculate logFold per gene
for var in tqdm(variables):
    lst = subset["BSC_ID"].to_list()
    combs = combinations(lst, 2)
    d = {}
    dicts = []
    for i in combs:
        A = subset.loc[subset["BSC_ID"] ==i[0]]
        B = subset.loc[subset["BSC_ID"] ==i[1]]
        x = A[var].values
        y = B[var].values
        #fc = (y - x)/x
        try:
            log2fc = math.log(y,2) - math.log(x,2)
            
        except ValueError:
            break
        p1 = subset[subset['BSC_ID'] == i[0]]['Diagnosis_simplified'].ravel()[0]
        p2 = subset[subset['BSC_ID'] == i[1]]['Diagnosis_simplified'].ravel()[0]
        lab = str(i[0]) + "_" + str(p1) + '::' + str(i[1]) + "_" + str(p2)
        d[lab] = log2fc
    dicts.append(d)
    megalist.append(dicts)
    

df = pd.DataFrame.from_dict(megalist).stack().apply(pd.Series) 
df.index = variables
df = df.T.dropna().T
df.to_csv("Log2fc_table"+str(sys.argv[2])+".csv")
