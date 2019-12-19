import pandas as pd
import numpy as np
import os
import datetime

def simplify(item):
    result=""
    for char in item:
        if(char=="."):
            result+="."
            continue
        try:
            int(char)
            result+=char
        except (ValueError):
            continue
    return float(result)
os.chdir("C:/Users/pabou/Documents/GitHub/Web-Scraper/data")
for file in os.listdir("C:/Users/pabou/Documents/GitHub/Web-Scraper/data"):
    if file.endswith(".csv"):
        print("Processing: "+file)
        header = {"Date":str,"Time":str,"Type":str,"Fee":str,"Amount":float,"Status":str}
        data = pd.read_csv(file, sep='delimiter',delimiter=",",header=None,engine='python',error_bad_lines=False)
        data.dropna(how="all",inplace=True)
        data.drop([2,3,5,6,9], axis=1, inplace=True)
        data.dropna(how="any",inplace=True)
        data.columns=header
        print("Formatting date-time")
        
        data['Fee'].apply(simplify)
        data['Amount'].apply(simplify)
        data.columns=header
        datetime=data["Date"].map(str)+" "+data["Time"]
        data.insert(3,column="Date-Time",value=datetime)
        
        data["Time"]=pd.to_datetime(["Time"])
        data['Time'] = data['Time'].dt.time
        data["Date"]=pd.to_datetime(data["Date"])

        data["Date-Time"]=pd.to_datetime(data["Date-Time"])
        # data['Week'] = data['Date-Time'].dt.strftime('%Y-%V')
        data.to_csv("Cleaned_"+file)


