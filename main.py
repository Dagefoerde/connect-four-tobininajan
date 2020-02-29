from connect_four_bot.bot import ConnectFourBotRandom
from connect_four_bot.bot import ConnectFourBotNN
from connect_four_bot.envs import ConnectFourEnv
import numpy as np

bot2 = ConnectFourBotRandom()

usemax = False
if usemax:
    maximumconf = np.loadtxt('maximum.out')
    #w2 = tf.Variable(initial_value=maximumconf[0], trainable=True)
    #b2 = tf.Variable(initial_value=maximumconf[1], trainable=True)
    #bot2 = ConnectFourBotNN(w2, b2)

w = np.random.rand(42,7)
b = np.random.rand(7)

bot2 = ConnectFourBotNN(w, b)

numberiter = 50
number_ga_configs = 20
results_log = np.array([])

maximum = np.array([]);
for x in range(number_ga_configs):
    print('Config')
    print(x)
    gameswon = 0
    gamesundecided = 0
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
            current_player *= -1
            if board.is_valid_action(move):
               board.step(move)
               bot1.inform(move)
               bot2.inform(move)
            if len(board.available_moves()) == 0:
                break
        if board.is_win_state() and (current_player*-1 == 1):
            gameswon += 1
            print(current_player)
        else:
            gamesundecided += 1
    if gamesundecided != numberiter:
        newresult = np.array([bot1.NN.w, bot1.NN.b, gameswon/(numberiter-gamesundecided)])
        if len(maximum) == 0:
            maximum = newresult
            print(maximum[2])
            print('won:',gameswon)
        else:
            if maximum[2] < gameswon/(numberiter-gamesundecided):
                maximum = newresult
                print(maximum[2])
                print('won:',gameswon)
print(maximum[2])
#np.savetxt('maximum.out', maximum, delimiter=',')
#f = open("example.txt", "w")
#f.write(repr(results_log[0]) + "\n")
#f.close()