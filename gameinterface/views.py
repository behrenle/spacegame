from django.shortcuts import render

resources = [
    {"name": "Iron", "value": 10000},
    {"name": "Nickel", "value": 9000},
    {"name": "Cobalt", "value": 8000},
    {"name": "Magnesium", "value": 7000},
    {"name": "Silicon", "value": 6000},
    {"name": "Silver", "value": 5000},
    {"name": "Gold", "value": 4000},
    {"name": "Platinum", "value": 3000},
    {"name": "Uranium", "value": 2000},
    {"name": "Oxygen", "value": 1000},
    {"name": "Hydrogen", "value": 0},
    {"name": "Energy", "value": 0}
]

menu = [
    {"label":"Summary", "link":"#"},
    {"label":"Production", "link":"#"},
    {"label":"Facilities", "link":"#"},
    {"label":"Research", "link":"#"},
    {"label":"Development", "link":"#"},
    {"label":"Factory", "link":"#"},
    {"label":"Defense", "link":"#"},
    {"label":"Fleet Command", "link":"#"},
    {"label":"Astrometrics", "link":"#"},
    {"label":"Intergalactic market", "link":"#"},
]

pipelines = {
    "constructions": [
        {"label":"Banana farm", "time_left": 1234},
        {"label":"Disney like castle", "time_left": 123},
        {"label":"Icecream machine", "time_left": 12},
        {"label":"Pizza shop", "time_left": 1}
    ],
    "research": [
        {"label":"How to eat icecream?", "time_left": 1234},
        {"label":"How to go to sleep?", "time_left": 123},
        {"label":"How to lick my elbow?", "time_left": 12},
    ]
}

# Create your views here.
def home(request):
    context = {
        "title": "Summary",
        "res": resources,
        "menu": menu,
        "menu_select": "Summary",
        "planet_name": "[planetname]",
        "pipelines": pipelines,
    }
    return render(request, "gameinterface/home.html", context)
