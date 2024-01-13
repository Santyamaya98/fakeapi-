# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:29:32 2023

@author: Santiago
"""

from reader import read_csv
from charter import generate_pie_chart

data = read_csv('data.csv')

print(data)
def get_pop_porcent(data):
    pop_porcent_dict =  {i['Country/Territory']:i['World Population Percentage'] for i in data}
    keys = pop_porcent_dict.keys()
    values = pop_porcent_dict.values()
    return keys, values

keys, values = get_pop_porcent(data)

generate_pie_chart(keys, values)