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

maximumconf1 = np.loadtxt('maximum1.out', delimiter=',')
maximumconf2 = np.loadtxt('maximum2.out', delimiter=',')
w2 = maximumconf1
b2 = maximumconf2
bot = ConnectFourBotNN(w2, b2)

player = TobiNinaJanPlayer(bot)

c = UdpClient(username=USERNAME, ip=UDP_IP, port=UDP_PORT, player=player)
c.send_register()
