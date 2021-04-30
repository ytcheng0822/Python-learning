import tensorflow as tf
tf.compat.v1.disable_eager_execution()


matrix1 = tf.constant([[3,3]])     # 1x2 的二維陣列
matrix2 = tf.constant([[2],[2]])   # 2x1 的二維陣列

product = tf.matmul(matrix1, matrix2)  # matrix multiply

# method 1
# init = tf.compat.v1.global_variables_initializer()
# sess = tf.compat.v1.Session()      # create session
# result = sess.run(product)         # 3x2 + 3x2 = 12
# print(result)
# sess.close()

# method 2  (method2 better than method1)
with tf.compat.v1.Session() as sess:
    result2 = sess.run(product)
    print(result2)