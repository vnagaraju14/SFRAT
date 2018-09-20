#Kenan Chen
#09/19/2018
import pandas as pd

df=pd.read_excel("model_data.xlsx")
print(df.head())

#Failure time to interfailure time
def ft_to_if(data):
    testlist=[]
    testlist.append(data.FT[0])
    for x in range(1,len(data.FT)):
        testlist.append(data.FT[x]-data.FT[x-1])
    return testlist

if_list=ft_to_if(df)
print("First 5 values of IF", if_list[0:5])

#Interfailure time to failure time
def if_to_ft(data):
    testlist=[]
    count=0
    for x in range(0,len(data.IF)):
        count=data.IF[x]+count
        testlist.append(count)
    return testlist


ft_list=if_to_ft(df)
print("First 5 values of FT", ft_list[0:5])