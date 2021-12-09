#!/usr/bin/python3

import matplotlib.pyplot as plt
import csv

data = []

with open("BrowserSurvey.csv", mode='r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        d = {}
        d["Browsers"] = row["Browsers"].split(";")
        for b in d["Browsers"]:
            b.strip()
        #d["Why"] = row["Why"].split(";")
        #d["Significance"] = row["Significance"]
        #d["Privacy"] = row["Privacy"]
        data.append(d)

browsers = {}
for d in data:
    for b in d["Browsers"]:
        if b not in browsers.keys():
            browsers[b] = 0
        browsers[b] += 1 

plt.bar(browsers.keys(), browsers.values())
plt.xlabel('Browser Usage')

plt.show()
