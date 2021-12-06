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
        d["Why"] = row["Why"].split(";")
        data.append(d)

browsers = []
for d in data:
    for b in d["Browsers"]:
        if b not in browsers:
            browsers.append(b)

for i in range(len(browsers)):
    plt.figure(i+1)
    reasons = {}
    for d in data:
        for b in d["Browsers"]:
            if b == browsers[i]:
                for reason in d["Why"]:
                    if reason not in reasons:
                        reasons[reason] = 0
                    reasons[reason] += 1

    plt.barh(list(reasons.keys()), list(reasons.values()))
    plt.xlabel("Number of {} users".format(browsers[i]))

plt.show()
