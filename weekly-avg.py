import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as seabornInstance
import numpy
os.chdir("C:/Users\pabou\Documents\GitHub\Web-Scraper\data\Cleaned\cleaned2")

for file in os.listdir("C:/Users/pabou/Documents/GitHub/Web-Scraper/data/cleaned/cleaned2"):
    if file.endswith(".csv"):
        print("Processing "+file)
        dataset=pd.read_csv(file)
        filename=file.replace(".csv","")


        keys=dataset["Week"].value_counts().keys().tolist()
        vals=dataset["Week"].value_counts().tolist()
        vals=[x / 2 for x in vals]
        fig, axs = plt.subplots(2)
        fig.suptitle(file)
        axs[0].plot(keys,vals,'o')
        z = numpy.polyfit(keys, vals, 1)
        p = numpy.poly1d(z)
        axs[0].plot(keys,p(keys),"r--")
        axs[0].set(ylabel="Num Transactions")

        d={}
        for i in dataset['Week'].unique():
            d[i] = [dataset['Amount'][j] for j in dataset[dataset['Week']==i].index] # create dictionary where week number acts as key, and amounts of each transaction are stored as list
        week_sum={} #dictionary to keep the sum of all transactions for each week
        num_week_avg=0
        for i in d:
            week_sum[i]=sum(d[i])/2 #average (over 2 years) of the amount of cash withdrawn each week
            num_week_avg+=len(d[i])/2 #average (over 2 years) of the number of transactions each week
        num_week_avg=num_week_avg/len(d)
        weekly_cash_avg=0
        for i in week_sum:
            weekly_cash_avg+=week_sum[i]
        weekly_cash_avg=weekly_cash_avg/len(week_sum)
        f=open("C:/Users\pabou\Documents\GitHub\Web-Scraper\data\Cleaned\cleaned2\overview\overview.csv","a")
        f.write(filename+","+str(num_week_avg)+","+str(weekly_cash_avg)+"\n")

        axs[1].set(xlabel="Weeks",ylabel="Amount of Cash")
        axs[1].plot(list(week_sum.keys()),list(week_sum.values()),'o')
        z = numpy.polyfit(list(week_sum.keys()), list(week_sum.values()), 1)
        p = numpy.poly1d(z)
        axs[1].plot(list(week_sum.keys()),p(list(week_sum.keys())),"r--")
        plt.savefig(filename+"_weekly-avg.png")