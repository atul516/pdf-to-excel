import pandas
import datetime as dt

cs = pandas.read_csv('combined_final_no_header.csv')
print(len(cs.columns))
date = cs['Time/Date'].str.split(" ", expand=True)[0]
time = cs['Time/Date'].str.split(" ", expand=True)[1]
cs.insert(loc=0, column='Time', value=time)
cs.insert(loc=0, column='Date', value=date)

print(date)