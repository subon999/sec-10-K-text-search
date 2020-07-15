#!/usr/bin/env python # coding: utf-8 # In[2]: 
from edgar import Company, TXTML path="/home/subon999/Downloads/cik_ticker.csv" 
import pandas as pd df=pd.read_csv(path, sep='|', delimiter=None, header='infer', names=None, index_col=None) 
# company = Company("Amarantus Bioscience Holdings Inc","1424812") 
# doc = company.get_10K() # text = TXTML.parse_full_10K(doc) 
# In[14]: f
rom edgar import Company, TXTML 
import re 
def findWord(comp,cik): 
    try: 
        company = Company(comp,cik) 
        doc = company.get_10K() 
        text = TXTML.parse_full_10K(doc) 
        #print(text) 
        if (re.search('blockchain', text , re.IGNORECASE)): 
            return("exists") 
        else : 
            return("dosenot") 
    except: 
        return("No 10-k") 
        # In[ ]: 

l=[] 
for index, row in df.iterrows(): 
    d={} 
    print(row['CIK'], row['Name']) 
    d["CIK"]=row['CIK'] 
    d["Name"]=row['Name'] 
    d["Ex"]=findWord(row['Name'],row['CIK']) 
    l.append(d) 
    # In[15]: 
findWord("INTERNATIONAL BUSINESS MACHINES CORP","0000051143") 
