
class Team(object):
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.IsPeeWee = False
        self.name = ""
        self.divname = ""
        self.RelativeStrength = 100  # Currently not used
        self.home_games = 0
        self.away_games = 0
        self.schedule_opponents = []  # list of names of opponents, generated over the season
        self.schedule_record = []  # list of 'W's and 'L's
        self.schedule_games = []  # list of H(ome)/A(way)
        self.schedule_divs = []  # list of divs of opponents
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
        self.schedule_opponents = []  # list of paired divs. Should only have len() = 2 for a season

    def init_names(self, divname, name1, name2, name3, name4):
        self.name = divname
        self.Team1.name = name1
        self.Team2.name = name2
        self.Team3.name = name3
        self.Team4.name = name4
        self.Team1.divname = divname
        self.Team2.divname = divname
        self.Team3.divname = divname
        self.Team4.divname = divname


    def make_peewee(self):
        self.Team1.IsPeeWee = self.Team2.IsPeeWee = True
        self.Team3.IsPeeWee = self.Team4.IsPeeWee = True

    def list_teams(self):
        return [self.Team1, self.Team2, self.Team3, self.Team4]

    def list_team_names(self):
        return[self.Team1.name, self.Team2.name, self.Team3.name, self.Team4.name]
    
    def rank_teams(self):  # to add later: ability to rank teams based on record from season
        pass

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
    @staticmethod
    def init_conference(name, div1, div2, div3, div4):
        conf = Conference()
        conf.set_divisions(div1, div2, div3, div4)
        conf.name = name
        return conf

