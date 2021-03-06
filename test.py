#!/usr/bin/env python
# encoding: utf-8
# Created Time: 日 12/24 18:31:07 2017

import numpy as np
import pandas as pd
import tensorflow as tf


def main():
    x = tf.placeholder(tf.float32, shape=[None])
    sess = tf.Session()
    x_np = sess.run(x, feed_dict={x: np.random.randn(10)})
    print(x_np)

    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    print(df)


if __name__ == '__main__':
    main()
