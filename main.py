# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:25:48 2018

@author: matte
"""

"""
PeeWee Division
a simulation of introducing a "PeeWee" division into the NFL.

Basically, the idea is to replace the NFC South with a division made up of peewee football teams.
That is, all of the NFL is roughly competitive with itself, and NFC PW is competitive within itself,
but any game between NFC PW and the rest of the NFL is completely one-sided and 
NFC PW loses every game.

Should show each team + season w-l record, if it made it to post-season, and post-season record.
Should allow expandability to having a possibility of ties.
Any 'tie' beyond record + head-to-head should be decided by a coin flip
Allow for adjusting the game-determining algorithm, potentially by allowing
for home-field advantage, taking into account Elo, rest/bye weeks/time between games, etc.

Want to also have some method of showing the NFL draft and its theoretical impact on the league
(like having points awarded based on position in the draft, adjusting something like .05% game-winning chance times point differential)
(Look into actual real-life impact of draft on winning games)


Obviously, 'NFL', 'NFC', and team names from the NFL are NFL copyright, yada yada yada. I am not the NFL,
I do not work for the NFL, but I do believe that whatever I write here referencing NFL teams and
league procedure falls under the terms of fair use. I am not making money off of this project, and 
I am committing this project to the public domain, but I do ask that if anyone uses substantial portions
of this project for any purpose, they cite it properly. And let me know--not to get
permission, but to let me see anything that others make of my work.

"""