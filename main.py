from connect_four_bot.bot import ConnectFourBotRandom
from connect_four_bot.bot import ConnectFourBotNN
from connect_four_bot.envs import ConnectFourEnv

import tensorflow as tf

w_init = tf.random_normal_initializer()
w = tf.Variable(initial_value=w_init(shape=(42, 7), dtype='float32'), trainable=True)
b_init = tf.zeros_initializer()
b = tf.Variable(initial_value=b_init(shape=(42,), dtype='float32'), trainable=True)

bot1 = ConnectFourBotRandom()
bot2 = ConnectFourBotNN(w, b)

numberiter=150

gameswon = 0
gamesundecided = 0

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

