# coding: utf-8
# test_food_db.py

import json
from pandas import DataFrame
import pandas as pd

db = json.load(open('pydata-book/ch07/foods-2011-10-03.json'))

nutrients = DataFrame(db[0]['nutrients'])
info_keys = ['description', 'group', 'id', 'manufacturer']

info = DataFrame(db, columns=info_keys)

#print(pd.value_counts(info.group)[:10])

nutrients = []

for rec in db:
	fnuts = DataFrame(rec['nutrients'])
	fnuts['id'] = rec['id']
	nutrients.append(fnuts)

nutrients = pd.concat(nutrients, ignore_index=True)

nutrients = nutrients.drop_duplicates()

col_mapping = {'description': 'food', 'group': 'fgroup'}
info = info.rename(columns=col_mapping, copy=False)

col_mapping = {'description': 'nutrient', 'group': 'nutgroup'}

nutrients = nutrients.rename(columns=col_mapping, copy=False)

ndata = pd.merge(nutrients, info, on='id', how='outer')



result = ndata.groupby(['nutrient', 'fgroup'])['value'].quantile(0.5)


result['Zinc, Zn'].order().plot(kind='barh')



by_nutrient = ndata.groupby(['nutgroup', 'nutrient'])

get_maximum = lambda x: x.xs(x.value.idxmax())
get_minimum = lambda x: x.xs(x.value.idxmin())

max_foods = by_nutrient.apply(get_maximum)[['value', 'food']]


# make the food a little smaller
max_foods.food = max_foods.food.str[:50]
