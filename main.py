from connect_four_bot.bot import ConnectFourBot
from connect_four_bot.envs import ConnectFourEnv

bot1 = ConnectFourBot()
bot2 = ConnectFourBot()

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

