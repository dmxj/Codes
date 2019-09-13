# -*- coding: utf-8 -* -
'''
使用tf.app.flags接收用户的请求参数
'''
import tensorflow as tf

'''
usage:
python flag_usage.py --batch_size=64 --epochs=100 --data_dir=/workspace/dataset --model_dir=/workspace/models
'''

flags = tf.app.flags

flags.DEFINE_integer("batch_size", 100, "Batch size")
flags.DEFINE_integer("epochs", 1, "Number of epochs.")
flags.DEFINE_string("data_dir", "/tmp/data/mnist", "Path from where to load input data")
flags.DEFINE_string("model_dir", "/tmp/ws/mnist", "Path where model params and summaries are saved")

FLAGS = flags.FLAGS

if __name__ == "__main__":
    print("batch size:",FLAGS.batch_size)
    print("epochs:",FLAGS.epochs)
    print("data dir:",FLAGS.data_dir)
    print("model dir:",FLAGS.model_dir)


