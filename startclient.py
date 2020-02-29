#!/usr/env/python

import logging

import tensorflow as tf

from connect_four_bot.bot import ConnectFourBotNN
from example.TobiNinaJanPlayer import TobiNinaJanPlayer
from py_client.udp_client import UdpClient

logging.basicConfig(level=logging.DEBUG)

USERNAME = "NN-Master1.0"
UDP_IP = "192.168.1.136"
UDP_PORT = 4446

w_init = tf.random_normal_initializer()
w = tf.Variable(initial_value=w_init(shape=(42, 7), dtype='float32'), trainable=True)
b_init = tf.random_normal_initializer()
b = tf.Variable(initial_value=b_init(shape=(7,), dtype='float32'), trainable=True)

bot = ConnectFourBotNN(w, b)

player = TobiNinaJanPlayer(bot)

c = UdpClient(username=USERNAME, ip=UDP_IP, port=UDP_PORT, player=player)
c.send_register()
