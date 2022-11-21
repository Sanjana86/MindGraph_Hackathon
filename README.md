# MindGraph_Hackathon

# MU Hiring 2022 Dataset
Hi All,
Welcome to the MU Hiring Hackathon 2022 conducted by MindGraph. 

1. You are made available a dataset with student activities across different events by clubs and fests. However, the student names in these datasets are fuzzified(as seen in real life)

2. You are tasked with deduplicating the names(in a table and across tables) and then joining all these tables together with the Metadata table(non fuzzified ground truth), convert the output into a specific JSON format(sample can be found below) necessary for  validation.

3. Once you have the final joined dataset(referred to as profiles from here on), you can perform analysis to identify and understand any number of business problems of your choice. 

4. When you decide on a problem statement and come up with a solution. Start building a dashboard(Streamlit) following the principles of [data storytelling](image.png) to backup your hypothesis with KPI metrics, graphs and any other viz of your choice.

> All your code related to data engineering, ML and dashboards along with the profile data json file for validation should be checked into your private github repo. Please ensure that you submit the url to your github privite repository in the forms circulated by the placement office.

## Deadlines:

* 21-11-2022 12PM - Make public your privite github repo
* 21-11-2022 2PM - Please be available with working versions of code along with all the team members for presentations to our panel

>Note: Team that commits last to the repo will be called to make the first presentation

**TL;DR**
1. Prepare unified student profiles from the activity data provided
    <br>a. Will be validated aganist masked source data
2. Pitch a business solution using analysis of the profiles built
    <br>a. Judged by a panel
## General information
- Number of clubs: 3
- Number of fests: 2
## Dataset description
- College provided source truth: [Metadata](Metadata.csv)
- All club events data: [Clubs_data](Clubs_data.csv)
- All Organizers for fests: [Organisers_In_Fests](Organisers_In_Fests.csv)
- Participation list from all fest related events: [Participants_In_Fests](Participants_In_Fests.csv)

## Mandatory tech features
1. Streamlit
2. Profile JSON should be submitted before presentation
3. Pluggable format



## Sample Profile json format
```
[
    {
        'name': 'Dummy',
        'id': 'id000',
        'clubs': {
            'club_i': {
                'isOrganiser': 'Organiser',
                'club_i_event_j': {
                    'participated': False
                    },
            },
        },
        'fests': {
            'fest_i': {
                'isOrganiser': '',
                'fest_i_event_j': {
                    'participated': True
                    },
            },
        }
    }
]


```

##
Requirements

-Fuzzy wuzzy:0.18.0
-Pandas:1.5. 0
