import json
import random

with open('result.json') as fp:
    data = json.load(fp)

years = list(data.keys())

while(True):
    year = random.choice(years)
    events = data[year]
    event = random.choice(events)
    events.remove(event)
    data[year] = events
    event.replace(year, "[censor]")
    print()
    print(event)
    print()
    print("click enter to get the year")
    input()
    print(year)
    print("Did you get it? (y/n)")
    inpt = input()
    if 'y' in inpt:
        del data[year]
