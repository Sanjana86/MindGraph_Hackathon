from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
import numpy as np
from collections import OrderedDict

metadata = pd.read_csv("Metadata.csv")
club = pd.read_csv("Clubs_data.csv")

df1_names = list(metadata.Name.unique())
df2_names = list(club.Name.unique())


def match_names(name, list_names, min_score=0):
    max_score = -1
    max_name = ''
    for x in list_names:
        score = fuzz.ratio(name, x)
        if (score > min_score) & (score > max_score):
            max_name = x
            max_score = score
    return (max_name, max_score)


names = []
for x in df2_names:
    match = match_names(x, df1_names, 0)
    if match[1] >= 0:
        name = ('(' + str(x), str(match[0]) + ')')
        names.append(name)
name_dict = dict(names)

for key in name_dict.keys():
    # print(key)
    club.loc[club['Name'] == key[1:], 'NAME'] = name_dict[key][:-1]
club['Name'] = club['NAME']
del club['NAME']
club.to_csv('club')

#dict1 = OrderedDict(reversed(list(name_dict.items())))
#club.Name = club.Name.replace(dict1)
# club['Name'].map(dict1)
#club.replace({"Name": dict1})
# club['Name'].update(pd.Series(dict1))
#club['Name'].replace(dict=name_dict, inplace=True)

print(club)
combined_dataframe = pd.merge(metadata, club, how='left', on='Name')
combined_dataframe['Club_Name'] = combined_dataframe['Club_Name'].fillna('-')
combined_dataframe['Event'] = combined_dataframe['Event'].fillna('-')
combined_dataframe['Role'] = combined_dataframe['Role'].fillna('-')

print(combined_dataframe)

combined_dataframe = combined_dataframe.groupby('Name').agg({'ID': 'first',
                                                             'Club_Name': ', '.join,
                                                             'Event': ', '.join,
                                                             'Role': ', '.join}).reset_index()

combined_dataframe.to_csv('metclub.csv')
print(combined_dataframe)
