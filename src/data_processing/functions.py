import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json
import requests
from pandas.io.json import json_normalize
from sklearn.cluster import KMeans
import folium
import regex as re
import pgeocode

def extract_neighborhood_name(df):
    """ Go through each row, extract neighborhood names and postal codes into a dataframe """
    neighbourhoods=[]
    for index,row in df.iterrows():
        for col in df.columns:
            neighbourhoods.append([
                                     row[col][:3],
                                     row[col][row[col].find("(")+1:row[col].find(")")]
                                    ])
    df_hoods = pd.DataFrame(neighbourhoods, columns=['Postal Code','neighbourhood'])
    return df_hoods