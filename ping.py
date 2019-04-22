import os
import subprocess as sb
import pandas as pd
import matplotlib.pyplot as plt

os.chdir("/home/ec2-user/environment/Project/411-MTP")
"""
# Create a list of processes to run
processes = []
for i in range(1, 6):
    bsh = "./ping" + str(i) + ".sh"
    processes.append(sb.Popen(bsh, shell = True))

# Execute all the processes simultaneously by waiting for each of them    
for p in processes:
    p.wait()
"""
# To associate a country to each data
names = ["es", "fi", "fr", "lv", "pl"]  
data = []

# For each country in the list
for name in names:
    bsh = "data/" + name + ".txt"
    vals = []
    # Open the text file in result of the bash file
    with open(bsh) as file:
        line = file.readlines()
        for val in line:
            # Add every data in the text file as float values
            vals.append(float(val))
    # Append the country's values to the overall ping values
    data.append(vals)

# Transpose the data matrix
panda = pd.DataFrame(data = data).T

# Create the data text file in a write mode
f = open("data.txt","w+")

# Compute the average, standard deviation and variation of each country
for i in range(0, 5):
    compute = names[i] + ": " + str(panda[i].mean()) + ", " + str(panda[i].std()) + ", " + str(panda[i].var()) + ".\n"
    f.write(compute)
f.close()

# Create the histogramm and save it as an image
fig, ax = plt.subplots()
panda.hist(ax=ax)
fig.savefig("images/hist.png")

# Create the boxplot and save it as an image
fig, ax = plt.subplots()
panda.boxplot(ax=ax)
fig.savefig("images/boxplot.png")