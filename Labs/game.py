def name (num) :
    nam = input('Введите имя {0}-го играющего: '.format(num))
    return nam

def game_process(name1, name2) :
    from random import randint
    import time

    print("\nНачало партии")
    player_points = {"player_one":0, "player_two":0}
    for throw in range(5) : 
        print('Кубик бросает', name1)
        time.sleep(2)
        n1 = randint(1, 6)
        print('Выпало:', n1)
        player_points["player_one"] += n1

        print('Кубик бросает', name2)
        time.sleep(2)
        n2 = randint(1, 6)
        print('Выпало:', n2)
        player_points["player_two"] += n2

    return player_points

def who_win (player_points, name1, name2) : 
    if player_points["player_one"] > player_points["player_two"] :
        print('\nВыиграл(а)', name1)
    elif player_points["player_one"] < player_points["player_two"] :
        print('\nВыиграл(а)', name2)
    else:
        print('\nНичья')
