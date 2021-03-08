import pandas as pd
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv("C-110_project.csv")
data = df['claps'].tolist()
print(statistics.mean(data))
def sampler(counter):
    # count the mean of random numbers
    array = []
    for i in range(0,counter):
        index = random.randint(0,len(data)-1)
        value = data[index]
        array.append(value)
    mean = statistics.mean(array)
    return mean

def setup():
    # get the fnal mean array
    array=[]
    for i in range(0,100):
        mean = sampler(30)
        array.append(mean)
    return array

if __name__ == "__main__":
    dataset = setup()
    fig = ff.create_distplot([dataset],["Claps"], show_hist=False)
    fig.show()
