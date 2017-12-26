import json
import random

with open('result.json') as fp:
    data = json.load(fp)

years = list(data.keys())

stats = []

for year in years:
    stats.append((int(year), len(data[year])))


stats = sorted(stats, key=lambda x: x[0])

for stat in stats:
    print(stat)
