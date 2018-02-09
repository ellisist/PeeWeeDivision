# -*- coding: utf-8 -*-
import random
"""
Created on Sun Jan 14 16:25:48 2018

@author: matte
"""

"""
PeeWee Division
a simulation of introducing a "PeeWee" division into the NFL.

See "README" file for information on this project.

"""

# NFL Structure: League made up of two conferences which are each made up of 4
# divisions of 4 teams each.


class Team(object):
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.IsPeeWee = False
        self.name = ""
        self.RelativeStrength = 100  # Currently not used
        self.home_games = 0
        self.away_games = 0

    def games(self):
        return print(self.name, "Home:", str(self.home_games), "Away:", str(self.away_games))

    def set_record(self, wins, losses):
        self.wins = wins
        self.losses = losses

    def add_win(self):
        self.wins += 1

    def add_loss(self):
        self.losses += 1

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


def intra_div_play(division):  # Simulates intra-division play
    for hometeam in division.list_teams():
        for awayteam in division.list_teams():
            if(hometeam != awayteam):
                game(hometeam, awayteam)

def two_div_play(div_a, div_b):  # matches two divisions against each other. only used for intra-divisional play
    for teama in div_a.list_teams():
        for teamb in div_b.list_teams():
            if(teama.home_games >= 2 or teamb.away_games >= 2):
                game(teamb, teama)
            elif(teamb.home_games >= 2 or teama.away_games >= 2):
                game(teama, teamb)
            else:
                if(bool(random.getrandbits(1))):  # rand 0 or 1, meaning False or True, respectively
                    game(teama, teamb)
                else:
                    game(teamb, teama)
    for teama in div_a.list_teams():
        if(teama.home_games > 2 or teama.away_games > 2):
            div_a.clear_games()
            div_b.clear_games()
            two_div_play(div_a, div_b)
            break
 
def inter_div_play(conference):  # Simulates intra-conference, inter-div play
    n = random.randint(1,100)  # rand number 1-99. determines inter-div matches
    div_a = conference.Division1
    if(n < 33):
        div_b = conference.Division2
        div_c = conference.Division3
        div_d = conference.Division4
    elif(n < 66): 
        div_b = conference.Division3
        div_c = conference.Division2
        div_d = conference.Division4
    else:
         div_b = conference.Division4
         div_c = conference.Division2
         div_d = conference.Division3
    print(div_a.name, "vs", div_b.name)
    print(div_c.name, "vs", div_d.name)
    two_div_play(div_a, div_b)
    two_div_play(div_c, div_d)
       
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
        
