# -*- coding: utf-8 -*-
import random
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

class Team(object):
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.IsPeeWee = False
        self.name = ""
        self.RelativeStrength = 100  # Currently not used
        self.home_games = 0
        self.away_games = 0
        self.schedule_opponents = []  # list of names of opponents, generated over the season
        self.schedule_record = []  # list of 'W's and 'L's

    def games(self):
        return print(self.name, "Home:", str(self.home_games), "Away:", str(self.away_games))

    def set_record(self, wins, losses):
        self.wins = wins
        self.losses = losses

    def add_win(self):
        self.wins += 1
        self.schedule_record.append('W')

    def add_loss(self):
        self.losses += 1
        self.schedule_record.append('L')

    def record(self):
        print(self.name, "Wins:", self.wins, "Losses:", self.losses)

    def clear_games(self):
        self.home_games = 0
        self.away_games = 0
        self.wins = 0
        self.losses = 0

class Division(object):
    def __init__(self):
        self.name = ""
        self.Team1 = Team()
        self.Team2 = Team()
        self.Team3 = Team()
        self.Team4 = Team()

    def init_names(self, divname, name1, name2, name3, name4):
        self.name = divname
        self.Team1.name = name1
        self.Team2.name = name2
        self.Team3.name = name3
        self.Team4.name = name4

    def make_peewee(self):
        self.Team1.IsPeeWee = self.Team2.IsPeeWee = True
        self.Team3.IsPeeWee = self.Team4.IsPeeWee = True

    def list_teams(self):
        return [self.Team1, self.Team2, self.Team3, self.Team4]

    def list_team_names(self):
        return[self.Team1.name, self.Team2.name, self.Team3.name, self.Team4.name]

    def clear_games(self):
        self.Team1.clear_games()
        self.Team2.clear_games()
        self.Team3.clear_games()
        self.Team4.clear_games()


class Conference(object):
    def __init__(self):
        self.name = ""
        self.Division1 = Division()
        self.Division2 = Division()
        self.Division3 = Division()
        self.Division4 = Division()



    def list_divisions(self):
        return [self.Division1, self.Division2, self.Division3, self.Division4]

    def set_divisions(self, div1, div2, div3, div4):
        self.Division1 = div1
        self.Division2 = div2
        self.Division3 = div3
        self.Division4 = div4

    def print_conf(self):
        print(self.name, ":")
        for div in self.list_divisions():
            print("  ", div.name, ":")
            for team in div.list_teams():
                print("    ", team.name)

def init_conference(name, div1, div2, div3, div4):
    conf = Conference()
    conf.set_divisions(div1, div2, div3, div4)
    conf.name = name
    return conf


def game(HomeTeam, AwayTeam):
    HFA = 0  # Home Field Advantage: currently set to disregard it.
#    print(AwayTeam.name, "at", HomeTeam.name)
    HomeTeam.home_games += 1
    AwayTeam.away_games += 1
    HomeTeam.schedule_opponents.append(AwayTeam.name)
    AwayTeam.schedule_opponents.append(HomeTeam.name)
    HomeWin = True
    if(HomeTeam.IsPeeWee and not AwayTeam.IsPeeWee):
        HomeWin = False
    elif(AwayTeam.IsPeeWee and not HomeTeam.IsPeeWee):
        HomeWin = True
    elif(random.randint(1, 101) + HFA >= 50):
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
    return l[n:] + l[:n]

def intra_div_play(division):  # Simulates intra-division play
    for hometeam in division.list_teams():
        for awayteam in division.list_teams():
            if(hometeam != awayteam):
                game(hometeam, awayteam)

def two_div_play(div1, div2):
    div_a = div1.list_teams()
    div_b = div2.list_teams()
    random.shuffle(div_a)
    random.shuffle(div_b)  # randomizing the lists = randomizing the games
    for i in range(NUM_TEAMS_IN_DIV):
        if(i < NUM_TEAMS_IN_DIV / 2):
            for j in range(NUM_TEAMS_IN_DIV):  # A home games
                game(div_a[j], div_b[j])
        else:
            for j in range(NUM_TEAMS_IN_DIV):  # B home games
                game(div_b[j], div_a[j])
 
def inter_div_play(conference):  # Simulates intra-conference, inter-div play
    div_list = random.sample(conference.list_divisions(), NUM_DIV_IN_CONF)  # shuffles divisions = random matchups of divisions
    for i in range(0, NUM_DIV_IN_CONF, 2):  # putting divisions into A+B pairs
        a = div_list[i]
        b = div_list[i+1]
        print(a.name, "vs", b.name)
        two_div_play(a,b)

    
def intra_conf_play(conference):
    inter_div_play(conference)
    for div in conference.list_divisions():
        intra_div_play(div)

AFCN = Division()
AFCS = Division()
AFCE = Division()
AFCW = Division()
AFCN.init_names("AFC North", "Bengals", "Steelers", "Browns", "Ravens")
AFCS.init_names("AFC South","Jaguars","Titans","Colts","Texans")
AFCE.init_names("AFC East","Bills","Dolphins","Jets","Patriots")
AFCW.init_names("AFC West","Chiefs","Chargers","Raiders","Broncos")

AFConf = init_conference("AFC", AFCN, AFCS, AFCE, AFCW)


intra_conf_play(AFConf)

for div in AFConf.list_divisions():
    for team in div.list_teams():
        # team.record()
         team.games()
        
