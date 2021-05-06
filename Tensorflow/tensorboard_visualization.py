import tensorflow as tf     # input layer:1    hidden layer:10    output layer:1
import numpy as np
tf.compat.v1.disable_eager_execution()

def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    # add one more layer and return the output of this layer
    layer_name = "layer%s" % n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope("weights"):
            Weights = tf.Variable(tf.random.normal([in_size, out_size]), name="W")
            tf.compat.v1.summary.histogram(layer_name + "/weights", Weights)
        with tf.name_scope("biases"):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name="b")
            tf.compat.v1.summary.histogram(layer_name + "/biases", biases)
        with tf.name_scope("Wx_plus_b"):
            Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tf.compat.v1.summary.histogram(layer_name + "/outputs", outputs)
    return outputs

# Make up some real data
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise


# define placeholder for inputs to network
with tf.name_scope("inputs"):
    xs = tf.compat.v1.placeholder(tf.float32, [None, 1], name="x_input")
    ys = tf.compat.v1.placeholder(tf.float32, [None, 1], name="y_input")

# add hidden layer
with tf.name_scope("hidden_layer"):
    l1 = add_layer(xs, 1, 10, n_layer=1, activation_function=tf.nn.relu)

# add output layer
with tf.name_scope("output_layer"):
    prediction = add_layer(l1, 10, 1, n_layer=2, activation_function=None)


with tf.name_scope("loss"):
    loss = tf.reduce_mean(tf.square(ys - prediction))   # the error between prediction and real data
    tf.compat.v1.summary.scalar("loss", loss)

with tf.name_scope("train"):
    train_step = tf.compat.v1.train.GradientDescentOptimizer(0.2).minimize(loss) # 優化器:訓練自己修正誤差 learning rate = 0.2


with tf.compat.v1.Session() as sess:
    merged_summary = tf.compat.v1.summary.merge_all()
    writer = tf.compat.v1.summary.FileWriter("logs/", sess.graph)
    init = tf.compat.v1.global_variables_initializer()  # If you define variable you need initialize
    sess.run(init)
    for i in range(1000):
        sess.run(train_step, feed_dict={xs:x_data, ys:y_data})
        if i % 50 == 0:
            result = sess.run(merged_summary, feed_dict={xs:x_data, ys:y_data})
            writer.add_summary(result, i)