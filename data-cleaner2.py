import pandas as pd
import datetime
import os
import matplotlib as plt

os.chdir("C:/Users/pabou/Documents/Github/Web-Scraper/data/cleaned")
for file in os.listdir("C:/Users/pabou/Documents/GitHub/Web-Scraper/data"):
    if file.endswith(".csv"):

        dataset = pd.read_csv("Cleaned_Depanneur Amigos Gatineau.csv")
        print(dataset.dtypes)
        dataset["Date-Time"]=pd.to_datetime(dataset["Date-Time"])
        print(dataset.dtypes)
        dataset["Week"]=dataset['Date-Time'].apply(lambda x: str(x.isocalendar()[0]) + '-' + str(x.isocalendar()[1]).zfill(2))
        dataset["Weekday"]=dataset['Date-Time'].apply(lambda x: str(x.isocalendar()[0]) + '-' + str(x.isocalendar()[2]).zfill(2))
        dataset["Month"]=pd.DatetimeIndex(dataset['Date-Time']).month
        print(dataset.head())
        dataset.to_csv("Cleaned2_"+file)

# keys=dataset["Week"].value_counts().keys().tolist()
# vals=dataset["Week"].value_counts().tolist()

# plt.plot(keys,vals,'o')