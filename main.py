from connect_four_bot.bot import ConnectFourBotRandom
from connect_four_bot.bot import ConnectFourBotNN
from connect_four_bot.envs import ConnectFourEnv
import numpy as np

bot2 = ConnectFourBotRandom()

usemax = True
if usemax:
    maximumconf1 = np.loadtxt('maximum1.out', delimiter=',')
    maximumconf2 = np.loadtxt('maximum2.out', delimiter=',')
    w2 = maximumconf1
    b2 = maximumconf2
    bot2 = ConnectFourBotNN(w2, b2)

w2 = np.random.rand(42,7)
b2 = np.random.rand(7)

bot2 = ConnectFourBotNN(w2, b2)

numberiter = 20
number_ga_configs = 30
results_log = np.array([])

maximum = np.array([]);
for x in range(number_ga_configs):
    print('Config')
    print(x)
    gameswon = 0
    gameslost = 0
    w = np.random.rand(42,7)
    b = np.random.rand(7)
    bot1 = ConnectFourBotNN(w, b)
    for x in range(numberiter):
        board = ConnectFourEnv()
        bot1.reset()
        bot2.reset()
        current_player = 1
        while not(board.is_win_state()):
            if current_player == 1:
                move = bot1.nextMove()
            else:
                move = bot2.nextMove()
            current_player = current_player * -1
            if board.is_valid_action(move):
               board.step(move)
               bot1.inform(move)
               bot2.inform(move)
            if len(board.available_moves()) == 0:
                break
        if board.is_win_state():
            if (current_player == 1):
                gameswon += 1
            if (current_player == -1):
                gameslost += 1
    newresult = np.array([bot1.NN.w, bot1.NN.b, gameswon/(gameswon+gameslost)])
    if len(maximum) == 0:
        maximum = newresult
        print(maximum[2])
        print('won:',gameswon)
    else:
        if maximum[2] < gameswon/(gameswon+gameslost):
            maximum = newresult
            print(maximum[2])
            print('won:',gameswon)
print(maximum[2])
np.savetxt('maximum1.out', np.array(maximum[0]), delimiter=',', fmt='%s')
np.savetxt('maximum2.out', np.array(maximum[1]), delimiter=',', fmt='%s')
#f = open("example.txt", "w")
#f.write(repr(results_log[0]) + "\n")
#f.close()