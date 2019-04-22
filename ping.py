import os
import subprocess as sb
import pandas as pd
import matplotlib.pyplot as plt

os.chdir("/home/ec2-user/environment/Project/411-MTP")
"""
processes = []

for i in range(1, 6):
    bsh = "./ping" + str(i) + ".sh"
    processes.append(sb.Popen(bsh, shell = True))
    
for p in processes:
    p.wait()
"""
names = ["es", "fi", "fr", "lv", "pl"]  
data = []
for name in names:
    bsh = name + ".txt"
    vals = []
    with open(bsh) as file:
        line = file.readlines()
        for val in line:
            vals.append(float(val))
    data.append(vals)

panda = pd.DataFrame(data = data).T

f = open("data.txt","w+")
for i in range(0, 5):
    compute = names[i] + ": " + str(panda[i].mean()) + ", " + str(panda[i].std()) + ", " + str(panda[i].var()) + ".\n"
    f.write(compute)
f.close()

fig, ax = plt.subplots()
panda.hist(ax=ax)
fig.savefig("hist.png")

fig, ax = plt.subplots()
panda.boxplot(ax=ax)
fig.savefig("boxplot.png")