# PeeWeeDivision
A simulator of a PeeWee division being in a professional football league

Basically, the idea is to make a simple simulator of a season of professional football, to play with the parameters and structure 
of the NFL (or a similarly-set league).

More specifically, the idea behind this is to find the edge cases of could possibly happen in the NFL-- 
how many losses could a team get and still make the playoffs, what would it look like if one division was absolutely below
the rest of the league in terms of skill, or absolutely above. The second case there is what I call the "PeeWee Division" model, 
which was the inspiration for this project.

This isn't going to be a phenomenally complex project, but I'll do my best to make it interesting. I am working on it on my own,
in my spare time, so don't have too high of expectations. It also perhaps needs saying that I am in no way affiliated with the NFL
or any team in the NFL, and all names mentioned in this program, as well as the rules governing the structure of a season are owned
by the NFL and are only being used by me under the fair use doctrine of the US, as this project will not make me any money and could
in no way take away money/audience/etc. from the NFL.

## How a season works

In the entire system (can be referred to as the "League"), there are two Conferences, which are each made up of four Divisions, 
each of which are made up of four teams. This gives us 32 total teams who each play 16 games in a season, which means there are 256
matchups simulated in a season.

According to <a href=https://operations.nfl.com/the-game/creating-the-nfl-schedule/>NFL guidelines</a>, every team's 16 games have to 
follow certain rules. 6 games against the three teams in their own division, 4 games against the 4 teams in another division within their
conference, 4 games against the 4 teams in one division in the other conference, and two games against two teams, one each pulled from the
divisions within their conference not yet faced. Each of these "sections" need to be broken evenly into Home/Away games, meaning a total of
8 home games and 8 away games in a season. 

There are additional rules and considerations that the NFL takes into account when making a season, such as not going a certain number of 
seasons without facing a certain team, or considerations of the specific order/timing/etc. of games, which we won't take into consideration
for this simulation.

## What does "PeeWee" mean in this context?

For the purposes of this simulation, teams can be marked as "PeeWee" to indicate they are entirely below the level of skill of <b>all</b> 
teams not marked "PeeWee". This means a game between any two PeeWee teams, or any two non-PeeWee teams, will be effectively decided by a 
coinflip (for now..?), while any game featuring exactly one PeeWee team will be lost by the PW automatically. 

Of course, if there were an entire division of PW (NFCPW, say), there would have to be a PW team sent to the playoffs, and this team
would be in the bottom 12 of the next NFL draft. This currently (as of 2/13/2018) isn't part of this simulation, though could be
incorporated.

### Questions?
