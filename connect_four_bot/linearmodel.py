from tensorflow.keras import layers
import tensorflow as tf

from connect_four_bot.envs import ConnectFourEnv


class Linear(layers.Layer):

    def __init__(self, w, b):
        super(Linear, self).__init__()
        self.w = w
        self.b = b

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b
