# -*- coding: utf-8 -*-
from random import shuffle, sample, randint 
"""
Created on Sun Jan 14 16:25:48 2018

@author: Matthew Ellis
"""

"""
PeeWee Division
a simulation of introducing a "PeeWee" division into the NFL.

See "README" file for information on this project.

"""

# NFL Structure: League made up of two conferences which are each made up of 4
# divisions of 4 teams each.

NUM_DIV_IN_CONF = 4
NUM_TEAMS_IN_DIV = 4

from objects import *


def game(HomeTeam, AwayTeam):
    HFA = 0  # Home Field Advantage: currently set to disregard it.
    HomeTeam.home_games += 1
    HomeTeam.schedule_games.append('H')
    AwayTeam.away_games += 1
    AwayTeam.schedule_games.append('A')
    HomeTeam.schedule_opponents.append(AwayTeam.name)
    AwayTeam.schedule_opponents.append(HomeTeam.name)
    HomeTeam.schedule_divs.append(AwayTeam.divname)
    AwayTeam.schedule_divs.append(HomeTeam.divname)
    HomeWin = True
    if(HomeTeam.IsPeeWee and not AwayTeam.IsPeeWee):
        HomeWin = False
    elif(AwayTeam.IsPeeWee and not HomeTeam.IsPeeWee):
        HomeWin = True
    elif(randint(1, 101) + HFA >= 50):
        HomeWin = True
    else:
        HomeWin = False
    if(HomeWin):
        HomeTeam.add_win()
        AwayTeam.add_loss()
        print(HomeTeam.name, "win,", AwayTeam.name, "lose")
    else:
        HomeTeam.add_loss()
        AwayTeam.add_win()
        print(HomeTeam.name, "lose,", AwayTeam.name, "win")

def rotate_list(l, n):
    return l[n%len(l):] + l[:n%len(l)]

def intra_div_play(division):  # Simulates intra-division play
    for hometeam in division.list_teams():
        for awayteam in division.list_teams():
            if(hometeam != awayteam):
                game(hometeam, awayteam)

def two_div_play(div1, div2):
    div1.schedule_opponents.append(div2.name)
    div2.schedule_opponents.append(div1.name)
    div_a = div1.list_teams()
    div_b = div2.list_teams()
    shuffle(div_a)
    shuffle(div_b)  # randomizing the lists = randomizing the games
    for i in range(NUM_TEAMS_IN_DIV):
        if(i < NUM_TEAMS_IN_DIV / 2):
            for j in range(NUM_TEAMS_IN_DIV):  # A home games }
                game(div_a[j], div_b[j])                    # }}} since these are randomized lists, the home/away teams are randomized
        else:                                               # }}
            for j in range(NUM_TEAMS_IN_DIV):  # B home games }
                game(div_b[j], div_a[j])
        div_b = rotate_list(div_b, 1)
 
def one_game_each(div1, div2):
    div_a = sample(div1.list_teams(), NUM_TEAMS_IN_DIV)
    div_b = sample(div2.list_teams(), NUM_TEAMS_IN_DIV)
    for i in range(NUM_TEAMS_IN_DIV):
        game(div_a[i], div_b[i])

def inter_div_play(conference):  # Simulates intra-conference, inter-div play
    div_list = sample(conference.list_divisions(), NUM_DIV_IN_CONF)  # shuffles divisions = random matchups of divisions
    for i in range(0, NUM_DIV_IN_CONF, 2):  # putting divisions into A+B pairs
        a = div_list[i]
        b = div_list[i+1]
        print(a.name, "vs", b.name)
        two_div_play(a,b)
    rev_div_list = div_list[::-1]  # a reversed copy of the div_list
    one_game_each(div_list[0], div_list[2])  # HARDCODE of four. Need to figure out a way to generalize.
    one_game_each(div_list[3], div_list[0])  # Also w/ this and one_game_each, H/A decided at division-level
    one_game_each(div_list[1], div_list[3])
    one_game_each(div_list[2], div_list[1])

    
def intra_conf_play(conference):
    inter_div_play(conference)
    for div in conference.list_divisions():
        intra_div_play(div)

def inter_conf_play(conf1, conf2):  # pairs divisions randomly, puts through two_div_play
   conf_a = sample(conf1.list_divisions(), NUM_DIV_IN_CONF)
   conf_b = sample(conf2.list_divisions(), NUM_DIV_IN_CONF)
   for i in range(NUM_DIV_IN_CONF):
       two_div_play(conf_a[i], conf_b[i])

def season(conf1, conf2):
    inter_conf_play(conf1, conf2)
    intra_conf_play(conf1)
    intra_conf_play(conf2)

def playoff_bound(conf1, conf2):  # to add later: determine the playoff picture from a season
    pass

AFCN = Division()
AFCS = Division()
AFCE = Division()
AFCW = Division()
AFCN.init_names("AFC North", "Bengals", "Steelers", "Browns", "Ravens")
AFCS.init_names("AFC South","Jaguars","Titans","Colts","Texans")
AFCE.init_names("AFC East","Bills","Dolphins","Jets","Patriots")
AFCW.init_names("AFC West","Chiefs","Chargers","Raiders","Broncos")

AFConf = Conference.init_conference("AFC", AFCN, AFCS, AFCE, AFCW)

NFCN = Division()
NFCS = Division()
NFCE = Division()
NFCW = Division()
NFCN.init_names("NFC North", "Vikings", "Lions", "Packers", "Bears")
NFCS.init_names("NFC South","Saints","Panthers","Falcons","Buccaneers")
NFCE.init_names("NFC East","Eagles","Cowboys","Washington","Giants")
NFCW.init_names("NFC West","Rams","Seahawks","Cardinals","49ers")

NFConf = Conference.init_conference("NFC", NFCN, NFCS, NFCE, NFCW)

season(AFConf, NFConf)

for div in AFConf.list_divisions():
    for team in div.list_teams():
        # team.record()
         team.games()
for div in NFConf.list_divisions():
    for team in div.list_teams():
        # team.record()
         team.games()
       
