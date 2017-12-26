"""This module does blah blah."""

import wikipedia
import json
from functions import parse_content

YEAR_LIST = []

for i in range(1200, 2017):
    YEAR_LIST.append(str(i))

event_list = {}

for year in YEAR_LIST:
    print(year)
    content = wikipedia.page(year).content
    event_list[year] = parse_content(content)


with open('result.json', 'w') as fp:
    json.dump(event_list, fp)
