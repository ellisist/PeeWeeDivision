import pytest
import main

@pytest.fixture
def team():
    test = main.Team()
    test.name = "Test"
    return test

@pytest.fixture
def team2():
    test = main.Team()
    test.name = "Test2"
    return test

@pytest.fixture
def div():
    div = main.Division()
    div.init_names('Test', '1', '2', '3', '4')
    return div

@pytest.fixture
def div2():
    div = main.Division()
    div.init_names('Test2', 'a', 'b', 'c', 'd')
    return div

def test_game(team, team2):
    main.game(team, team2)
    assert team.home_games == 1
    assert team2.away_games == 1
    assert team.away_games == 0
    assert team2.home_games == 0
    assert team.schedule_opponents == ['Test2']
    assert team2.schedule_opponents == ['Test']
    assert team.wins + team2.wins == 1
    assert team.losses + team2.losses == 1
    main.game(team2, team)
    assert team.home_games == 1
    assert team2.home_games == 1
    assert team.away_games == 1
    assert team2.away_games == 1
    assert team.schedule_opponents == ['Test2', 'Test2']
    assert team2.schedule_opponents == ['Test', 'Test']
    assert team.wins + team2.wins == 2
    assert team.losses + team2.losses == 2
    
@pytest.mark.parametrize("l, n, expected_list", [
    ([1,2,3,4], 3, [4,1,2,3]),
    ([1,2,3,4], 4, [1,2,3,4]),
    ([1,2], 15, [2,1])
    ])
def test_rotate_list(l, n, expected_list):
    assert main.rotate_list(l, n) == expected_list

def test_intra_div_play(div):
    main.intra_div_play(div)
    wincount = 0
    losscount = 0
    for team in div.list_teams():
        assert team.home_games == 3
        assert team.away_games == 3
        wincount += team.wins
        losscount += team.losses
    assert wincount == 12
    assert losscount == 12

def test_two_div_play(div, div2):
    main.two_div_play(div, div2)
    assert div.schedule_opponents == ['Test2']
    assert div2.schedule_opponents == ['Test']
    wincount = 0
    losscount = 0
    for team in div.list_teams():
        assert team.home_games == 2
        assert team.away_games == 2
        wincount += team.wins
        losscount += team.losses
    for team in div2.list_teams():
        assert team.home_games == 2
        assert team.away_games == 2
        wincount += team.wins
        losscount += team.losses
    assert wincount == 16
    assert losscount == 16


    
