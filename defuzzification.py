from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
import numpy as np
from collections import OrderedDict
import json
from collections import ChainMap

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


def stringmatch_retDICT(df2_names):
    names = []
    for x in df2_names:
        match = match_names(x, df1_names, 65)
        if match[1] >= 65:
            name = ('(' + str(x), str(match[0]) + ')')
            names.append(name)
    name_dict = dict(names)
    return(name_dict)


def keymatchingInDataframe(df, name_dict):
    for key in name_dict.keys():
        # print(key)
        df.loc[df['Name'] == key[1:], 'NAME'] = name_dict[key][:-1]
    df['Name'] = df['NAME']
    del df['NAME']
    return(df)


def CombiningDataFrames(df, metadata):
    combined_dataframe = pd.merge(metadata, df, how='left', on='Name')
    combined_dataframe.fillna('False', inplace=True)

    return(combined_dataframe)


##################################################################################################################
# IMPLEMENTING THE FUNCTIONS:
club_name_dict = stringmatch_retDICT(df2_names)
Club_df = keymatchingInDataframe(club, club_name_dict)
Club_Meta_Comb_DF = CombiningDataFrames(Club_df, metadata)
Club_Meta_Comb_DF['Club'] = Club_Meta_Comb_DF[[
    'Club_Name', 'Event', 'Role']].to_dict('records')
Club_Meta_Comb_DF = Club_Meta_Comb_DF[['Name', 'ID', 'Club']]


organisers_name_dict = stringmatch_retDICT(df3_names)
Organisers_df = keymatchingInDataframe(organisers, organisers_name_dict)
Org_Meta_Comb_DF = CombiningDataFrames(Organisers_df, metadata)
Org_Meta_Comb_DF['Organiser'] = Org_Meta_Comb_DF[[
    'Fest_Name', 'Role']].to_dict('records')


participants_name_dict = stringmatch_retDICT(df4_names)
Participants_df = keymatchingInDataframe(participants, participants_name_dict)
Part_Meta_Comb_DF = CombiningDataFrames(Participants_df, metadata)
Part_Meta_Comb_DF['Participant'] = Part_Meta_Comb_DF[[
    'Fest_Name', 'Event', ]].to_dict('records')

org_part_met_combdf = CombiningDataFrames(Part_Meta_Comb_DF, Org_Meta_Comb_DF)
org_part_met_combdf['Fest'] = org_part_met_combdf[[
    'Organiser', 'Participant']].to_dict('records')

finaldf = CombiningDataFrames(org_part_met_combdf, Club_Meta_Comb_DF)
finaldf['student profile'] = finaldf[['Club', 'Fest']].to_dict('records')

out = finaldf[['Name', 'ID', 'student profile']
              ].to_json('final.json', orient='records', indent=4)


####################################################################################################################
