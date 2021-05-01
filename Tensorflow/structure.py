import tensorflow as tf
import numpy as np
tf.compat.v1.disable_eager_execution()

# create data
x_data = np.random.rand(100).astype(np.float32)   # 使用亂數製造出100個(x,y)的座標點
y_data = x_data * 0.1 + 0.3   # Weights 會越來越接近0.1 , biases 會越來越接近0.3

### create tensorflow structure start ###  
Weights = tf.Variable(tf.random.uniform([1], -1.0, 1.0))  # 起始值為 -1 ~ 1 之間的亂數
biases = tf.Variable(tf.zeros([1]))  # 偏差值一開始為
y = Weights * x_data + biases      # 預測值

loss = tf.reduce_mean(tf.square(y - y_data))    # 計算損失函數
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.6)  # 優化器  梯度下降法: Gradient Descent
train = optimizer.minimize(loss)   # 訓練自己修正誤差, 誤差會隨著訓練的次數越變越小
### create tensorflow structure end ###


init = tf.compat.v1.global_variables_initializer()   # If you define variable you need initial

with tf.compat.v1.Session() as sess:    # use this method you don't need sess.close()
    sess.run(init)
    for step in range(201):  # 訓練201次
        sess.run(train)
        if step % 20 == 0:
            print(step, sess.run(Weights), sess.run(biases))   # 每20次 印出一次結果