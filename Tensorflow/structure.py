import tensorflow as tf
import numpy as np
tf.compat.v1.disable_eager_execution()

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3   # Weights 會越來越接近0.1 , biases 會越來越接近0.3

### create tensorflow structure start ###
Weights = tf.Variable(tf.random.uniform([1], -1.0, 1.0))  # 起始值為 -1 ~ 1 之間的亂數
biases = tf.Variable(tf.zeros([1]))  # 偏差值一開始為0

y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))    # 誤差值
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.5)  # 優化器
train = optimizer.minimize(loss)   # 訓練自己修正誤差, 誤差會隨著訓練的次數越變越小
### create tensorflow structure end ###

s = tf.compat.v1.Session()

init = tf.compat.v1.global_variables_initializer()
s.run(init)      #  activate init

for step in range(201):  # 訓練201次
    s.run(train)
    if step % 20 == 0:
        print(step, s.run(Weights), s.run(biases))   # 每20次 印出一次結果