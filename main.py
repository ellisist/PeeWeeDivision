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
    wins = 0
    losses = 0
    IsPeeWee = False
    name = ""
    RelativeStrength = 100  # Currently not used

    def set_record(self, wins, losses):
        self.wins = wins
        self.losses = losses

    def add_win(self):
        self.wins += 1

    def add_loss(self):
        self.losses += 1

    def record(self):
        print(self.name, "Wins:", self.wins, "Losses:", self.losses)


class Division(object):
    name = ""
    Team1 = Team()
    Team2 = Team()
    Team3 = Team()
    Team4 = Team()

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


def game(HomeTeam, AwayTeam):
    HFA = 0  # Home Field Advantage: currently set to disregard it.
    print(AwayTeam.name, "at", HomeTeam.name)
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


def season(division):  # Currently just simulates intra-division play
    for hometeam in division.list_teams():
        for awayteam in division.list_teams():
            if(hometeam != awayteam):
                game(hometeam, awayteam)

AFCN = Division()
AFCN.init_names("AFC North", "Bengals", "Steelers", "Browns", "Ravens")
season(AFCN)

for team in AFCN.list_teams():
    team.record()
