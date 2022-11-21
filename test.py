from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
import numpy as np
from collections import OrderedDict
import csv
import json
import pprint

metadata = pd.read_csv("Metadata.csv")
club = pd.read_csv("Clubs_data.csv")
organisers = pd.read_csv("Organisers_In_Fests.csv")
participants = pd.read_csv("Participants_In_Fests.csv")

df1_names = list(metadata.Name.unique())
df2_names = list(club.Name.unique())
df3_names = list(organisers.Name.unique())
df4_names = list(participants.Name.unique())


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
# club.to_csv('club.csv')

#dict1 = OrderedDict(reversed(list(name_dict.items())))
#club.Name = club.Name.replace(dict1)
# club['Name'].map(dict1)
#club.replace({"Name": dict1})
# club['Name'].update(pd.Series(dict1))
#club['Name'].replace(dict=name_dict, inplace=True)

# print(club)
combined_dataframe = pd.merge(metadata, club, how='left', on='Name')
combined_dataframe.fillna('False', inplace=True)

# print(combined_dataframe)

combined_dataframe.to_csv('club.csv')


# print(combined_dataframe)

####################################
names = []
for x in df3_names:
    match = match_names(x, df1_names, 0)
    if match[1] >= 0:
        name = ('(' + str(x), str(match[0]) + ')')
        names.append(name)
name_dict = dict(names)

# print(name_dict)

for key in name_dict.keys():
    # print(key)
    organisers.loc[organisers['Name'] == key[1:], 'NAME'] = name_dict[key][:-1]
organisers['Name'] = organisers['NAME']
del organisers['NAME']


combined_dataframe_org = pd.merge(metadata, organisers, how='left', on='Name')

combined_dataframe_org.fillna('False', inplace=True)


combined_dataframe_org.to_csv('metorg.csv')
# print(combined_dataframe_org)

#################################################
names = []
for x in df4_names:
    match = match_names(x, df1_names, 0)
    if match[1] >= 0:
        name = ('(' + str(x), str(match[0]) + ')')
        names.append(name)
name_dict = dict(names)

# print(name_dict)

for key in name_dict.keys():
    # print(key)
    participants.loc[participants['Name'] ==
                     key[1:], 'NAME'] = name_dict[key][:-1]
participants['Name'] = participants['NAME']
del participants['NAME']


combined_dataframe_part = pd.merge(
    metadata, participants, how='left', on='Name')
combined_dataframe.fillna('False', inplace=True)

combined_dataframe_part.to_csv('metfestpart.csv')
# print(combined_dataframe_part)

##########################################################
combined1 = pd.merge(combined_dataframe,
                     combined_dataframe_org, how='left', on='Name')
combined2 = pd.merge(combined1, combined_dataframe_part, how='left', on='Name')

combined2.to_csv('combined.csv')


#############################################################

########################################################################
