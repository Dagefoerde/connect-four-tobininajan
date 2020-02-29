from tensorflow.keras import layers
import tensorflow as tf

from connect_four_bot.envs import ConnectFourEnv


class Linear(layers.Layer):

    def __init__(self, units=32, input_dim=32):
        super(Linear, self).__init__()
        w_init = tf.random_normal_initializer()
        self.w = tf.Variable(initial_value=w_init(shape=(input_dim, units), dtype='float32'), trainable=True)
        b_init = tf.zeros_initializer()
        self.b = tf.Variable(initial_value=b_init(shape=(units,), dtype='float32'), trainable=True)

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b
