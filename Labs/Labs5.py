import game

player_one = game.name(1)
player_two = game.name(2)

player_points = game.game_process(player_one, player_two)

game.who_win(player_points, name1=player_one, name2=player_two)
