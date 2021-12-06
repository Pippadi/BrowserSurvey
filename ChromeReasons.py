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
        d["Significance"] = row["Significance"]
        d["Privacy"] = row["Privacy"]
        data.append(d)

chromeReasons = {}
for d in data:
    for b in d["Browsers"]:
        if b == "Chrome" and len(d["Browsers"]) == 1:
            for reason in d["Why"]:
                if reason not in chromeReasons:
                    chromeReasons[reason] = 0
                chromeReasons[reason] += 1

plt.barh(list(chromeReasons.keys()), list(chromeReasons.values()))
plt.xlabel("Number of Chrome users")

plt.show()
