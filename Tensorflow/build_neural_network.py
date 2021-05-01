import tensorflow as tf     # input layer:1    hidden layer:10    output layer:1
import numpy as np
import matplotlib.pyplot as plt
tf.compat.v1.disable_eager_execution()

def add_layer(inputs, in_size, out_size, activation_function=None):  # activation_function(激勵函數)
    Weights = tf.Variable(tf.random.normal([in_size, out_size]))  # normal distribution(常態分佈)
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)

    return outputs

# Make up some real data
x_data = np.linspace(-1,1,300)[:, np.newaxis]    # input data
noise = np.random.normal(0, 0.05, x_data.shape)  # standard deviation = 0.05
y_data = np.square(x_data) + noise         # output data


# define placeholder for inputs to network
xs = tf.compat.v1.placeholder(tf.float32, [None, 1])   # x_data.step [dtype=None, shape=1]
ys = tf.compat.v1.placeholder(tf.float32, [None, 1])   # y_data.step [dtype=None, shape=1]

# add hidden layer
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)      # hidden layer: inputs = x_data, input_size = 1, output_size = 10

# add output layer
prediction = add_layer(l1, 10, 1, activation_function=None)    # output layer: inputs = l1, input_size = 10, output_size = 1


loss = tf.reduce_mean(tf.square(ys - prediction))   # the error between prediction and real data
train_step = tf.compat.v1.train.GradientDescentOptimizer(0.2).minimize(loss) # 優化器:訓練自己修正誤差 learning rate = 0.1
init = tf.compat.v1.global_variables_initializer()  # If you define variable you need initialize

# plot the real data
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)   # y = x^2 + noise


with tf.compat.v1.Session() as sess:
    sess.run(init)
    for i in range(1000):   # training
        sess.run(train_step, feed_dict={xs:x_data, ys:y_data})   # use placehold you need give it feed_dict={key:value}
        if i % 50 == 0:
            print(sess.run(loss, feed_dict={xs:x_data, ys:y_data}))  # to see the step improvement
            try:
                ax.lines.remove(lines[0])    # plot線段前,先將上一個線段移除
            except Exception:                # 因為第一次還沒有線段,所以會發生異常
                pass                         # 執行pass
            prediction_value = sess.run(prediction, feed_dict={xs:x_data})   
            lines = ax.plot(x_data, prediction_value, "r-", lw=5)    # to visualize the result and improvement
            plt.pause(0.1)
            

            
plt.show(block=True)   # block=True 為了讓figure plot完不要馬上關閉
# 結論發現在此神經網路activation_function使用 softplus 會比 relu 效果更好