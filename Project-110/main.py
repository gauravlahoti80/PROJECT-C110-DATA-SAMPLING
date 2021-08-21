#importing the modules
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random

#reading csv
df = pd.read_csv("data.csv")

#making an array to store the value of data
claps = []
claps = df["reading_time"].tolist()

#making an array to store all the final values
final_list = []

#getting the mean of claps 
claps_mean = statistics.mean(claps)
print(f"Population Mean:- {claps_mean}") 

#creating a function to get the random positions
def getRandomValues():
    #creating to an array to store values of random position
    sample_data = []
    for i in range(0,100):
        random_position = random.randint(0, len(claps) -1)
        #storing all the values in data variable
        data = claps[random_position]
        #appending values in final list
        sample_data.append(data)
    #getting the mean of the sample data
    sample_data_mean = statistics.mean(sample_data)
    #appending all the values to the final list
    final_list.append(sample_data_mean)

#for loop to get the 1000 values
for i in range(1,1001):
    getRandomValues()

#finding the mean for sample data
sample_data_mean = statistics.mean(final_list)
print(f"Sample Mean:- {sample_data_mean}")

