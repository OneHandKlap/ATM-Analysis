import pandas as pd
import datetime
import os
import matplotlib as plt

#Customer requested other functionality, so a second pass was required for date formatting

os.chdir("C:/Users/pabou/Documents/Github/Web-Scraper/data/cleaned")
for file in os.listdir("C:/Users/pabou/Documents/GitHub/Web-Scraper/data/cleaned"):
    if file.endswith(".csv"):

        dataset = pd.read_csv(file)
        print(dataset.dtypes)
        dataset["Date-Time"]=pd.to_datetime(dataset["Date-Time"])
        print(dataset.dtypes)
        dataset["Week"]=dataset['Date-Time'].apply(lambda x: str(x.isocalendar()[1]).zfill(2))
        dataset["Weekday"]=dataset['Date-Time'].apply(lambda x: str(x.isocalendar()[2]).zfill(2))
        dataset["Month"]=pd.DatetimeIndex(dataset['Date-Time']).month
        print(dataset.head())
        dataset.to_csv("Cleaned2_"+file)
