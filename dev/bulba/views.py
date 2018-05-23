'''
Stuff that needs fixed:
Custom bear images to replace temp stock pictures
Uniform button styling
General design improvements: font, color scheme, layout
Final page bordered, responsive, & printable (print button?)
Add credits & contact info
***Site needs to be deployed***
'''
from django.shortcuts import render
import json
import random
from dev import settings

def index(request):
    return render(request, 'index.html')

def gender_question(request):
    return render(request, 'gender_question.html')

def name(request):
    if request.POST.get("boy_name"):
        first_name = random.choice(settings.boy_name)
        last_name = random.choice(settings.surname)
        update_stats("first_name", first_name)
        update_stats("last_name", last_name)
        return render(request, 'name.html', {"first_name": first_name, "last_name": last_name})
    elif request.POST.get("girl_name"):
        first_name = random.choice(settings.girl_name)
        last_name = random.choice(settings.surname)
        update_stats("first_name", first_name)
        update_stats("last_name", last_name)
        return render(request, 'name.html', {"first_name": first_name, "last_name": last_name})
    else:
        first_name = random.choice(settings.asex_name)
        last_name = random.choice(settings.surname)
        update_stats("first_name", first_name)
        update_stats("last_name", last_name)
        return render(request, 'name.html', {"first_name": first_name, "last_name": last_name})
#^If statement determines gender path of names based on "name" of button clicked in gender_question.html
#^ This function actually works - writes over the json!


def stats(request):
    personality_stat = random.choice(settings.personalities)
    bear_types_stat = random.choice(settings.bear_types)
    criminal_roles_stat = random.choice(settings.criminal_roles)
    update_stats("bear_stats", [personality_stat, bear_types_stat, criminal_roles_stat])
    return render(request, 'stats.html', {'personality_stat': personality_stat,
                                          'bear_types_stat': bear_types_stat,
                                          'criminal_roles_stat': criminal_roles_stat,
                                          'postStat': settings.prompts["postStat"]})

def final(request):
    with open("all_bear_info.json", "r") as jsonFile:
        bear_info = json.load(jsonFile)
        return render(request, 'final.html', {
                             'personality_stat': bear_info['bear_stats'][0],
                             'bear_types_stat': bear_info['bear_stats'][1],
                             'criminal_roles_stat': bear_info['bear_stats'][2],
                             'first_name': bear_info['first_name'],
                             'last_name': bear_info['last_name']
                              })

def diy_page(request):
    return render(request, 'diy_page.html')


def diy_final(request):
    full_name = request.GET['full_name']
    update_stats("full_name", full_name)
    with open("all_bear_info.json", "r") as jsonFile:
        bear_info = json.load(jsonFile)
    return render(request, 'diy_final.html', {
                            'personality_stat': bear_info['bear_stats'][0],
                            'bear_types_stat': bear_info['bear_stats'][1],
                            'criminal_roles_stat': bear_info['bear_stats'][2],
                            'full_name': bear_info['full_name']
                            })


############################# UTILITY FUNCTIONS ####################################

def update_stats(stat_key, stat_value):
    with open("all_bear_info.json", "r") as jsonFile:
        bear_info = json.load(jsonFile)
    bear_info[stat_key] = stat_value
    with open("all_bear_info.json", "w") as jsonFile:
        jsonFile.write(json.dumps(bear_info))