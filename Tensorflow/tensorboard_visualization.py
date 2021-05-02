import tensorflow as tf     # input layer:1    hidden layer:10    output layer:1
tf.compat.v1.disable_eager_execution()

def add_layer(inputs, in_size, out_size, activation_function=None):
    # add one more layer and return the output of this layer
    with tf.name_scope("layer"):
        with tf.name_scope("weights"):
            Weights = tf.Variable(tf.random.normal([in_size, out_size]), name='W')
        with tf.name_scope("biases"):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name="b")
        with tf.name_scope("Wx_plus_b"):
            Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs


# define placeholder for inputs to network
with tf.name_scope("inputs"):
    xs = tf.compat.v1.placeholder(tf.float32, [None, 1], name="x_input")
    ys = tf.compat.v1.placeholder(tf.float32, [None, 1], name="y_input")

# add hidden layer
with tf.name_scope("hidden_layer"):
    l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)

# add output layer
with tf.name_scope("output_layer"):
    prediction = add_layer(l1, 10, 1, activation_function=None)


with tf.name_scope("loss"):
    loss = tf.reduce_mean(tf.square(ys - prediction))   # the error between prediction and real data

with tf.name_scope("train"):
    train_step = tf.compat.v1.train.GradientDescentOptimizer(0.2).minimize(loss) # 優化器:訓練自己修正誤差 learning rate = 0.2

init = tf.compat.v1.global_variables_initializer()  # If you define variable you need initialize

with tf.compat.v1.Session() as sess:
    writer = tf.compat.v1.summary.FileWriter("logs/", sess.graph)
    sess.run(init)