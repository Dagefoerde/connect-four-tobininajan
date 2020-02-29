from connect_four_bot.bot import ConnectFourBotRandom
from connect_four_bot.bot import ConnectFourBotNN
from connect_four_bot.envs import ConnectFourEnv
import numpy as np

import tensorflow as tf

w_init = tf.random_normal_initializer()
w = tf.Variable(initial_value=w_init(shape=(42, 7), dtype='float32'), trainable=True)
b_init = tf.zeros_initializer()
b = tf.Variable(initial_value=b_init(shape=(7,), dtype='float32'), trainable=True)

bot2 = ConnectFourBotRandom()
bot1 = ConnectFourBotNN(w, b)

numberiter = 100
number_ga_configs = 50
results_log = np.array([])
gameswon = 0
gamesundecided = 0

for x in range (number_ga_configs):
    for x in range(numberiter):
        board = ConnectFourEnv()
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
        print(board.board)
        if board.is_win_state() & current_player*-1 == 1:
            gameswon += 1
        else:
            gamesundecided += 1
    if gamesundecided != numberiter:
        results_log.append(np.array(
            np.array(bot1.NN.w),
            np.array(bot1.NN.b),
            gameswon/(numberiter-gamesundecided)))
maximum = results_log[0]

for item in results_log:
    if item[2] > maximum[2]:
        maximum = item

np.savetxt('result.out', results_log[0], delimiter=',')
np.savetxt('maximum.out', maximum, delimiter=',')
#f = open("example.txt", "w")
#f.write(repr(results_log[0]) + "\n")
#f.close()