def load_game_data():
    f = open('data.txt', 'r')
    game_data = f.readlines()

    high_score = int(game_data[0])
    caracter_color = game_data[1]
    league = game_data[2]
    coins = int(game_data[3])
    batch = game_data[4]
    is_active = game_data[5]


    return (high_score,caracter_color,league,coins,batch,is_active)


print(load_game_data())
