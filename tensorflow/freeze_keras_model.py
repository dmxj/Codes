# -*- coding: utf-8 -* -
'''
freeze keras模型
'''
import tensorflow as tf

def save(model, filename):
    '''
    freeze Keras 模型
    :param model: Keras模型对象
    :param filename: 保存的文件路径
    :return:
    '''
    # First freeze the graph and remove training nodes.
    output_names = model.output.op.name
    sess = tf.keras.backend.get_session()
    frozen_graph = tf.graph_util.convert_variables_to_constants(sess, sess.graph.as_graph_def(), [output_names])
    frozen_graph = tf.graph_util.remove_training_nodes(frozen_graph)
    # Save the model
    with open(filename, "wb") as ofile:
        ofile.write(frozen_graph.SerializeToString())