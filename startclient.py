#!/usr/env/python

import logging

import numpy as np

from connect_four_bot.bot import ConnectFourBotNN
from example.TobiNinaJanPlayer import TobiNinaJanPlayer
from py_client.udp_client import UdpClient

logging.basicConfig(level=logging.DEBUG)

USERNAME = "NumpyNN0.1"
UDP_IP = "192.168.1.136"
UDP_PORT = 4446

w = np.random.rand(42,7)
b = np.random.rand(7)

bot2 = ConnectFourBotNN(w, b)
bot = ConnectFourBotNN(w, b)

player = TobiNinaJanPlayer(bot)

c = UdpClient(username=USERNAME, ip=UDP_IP, port=UDP_PORT, player=player)
c.send_register()
