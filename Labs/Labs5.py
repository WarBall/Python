def name (num) :
    nam = input('Введите имя {0}-го играющего: '.format(num))
    return nam

def gameProcess(name1,name2) :
    print("\nНачало партии")
    playerPoints = {"playerOne":0,"playerTwo":0}
    for throw in range(5) : 
        print('Кубик бросает', naem1)
        time.sleep(2)
        n1 = randint(1, 6)
        print('Выпало:', n1)
        playerPoints["playerOne"] += n1

        print('Кубик бросает', name2)
        time.sleep(2)
        n2 = randint(1, 6)
        print('Выпало:', n2)
        playerPoints["playerTwo"] += n2

    return playerPoints

def whoWin (playerPoints, name1, name2) : 
    if playerPoints["playerOne"] > playerPoints["playerTwo"] :
        print('Выиграл(а)', name1)
    elif playerPoints["playerOne"] < playerPoints["playerTwo"] :
        print('Выиграл(а)', name2)
    else:
        print('Ничья')
