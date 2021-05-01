import tensorflow as tf
tf.compat.v1.disable_eager_execution()

state = tf.Variable(0, name="counter")   # This is a variable
# print(state.name)

one = tf.constant(1)

new_value = tf.add(state, one)  # state + one

update = tf.compat.v1.assign(state, new_value)  # tf.compat.v1.assign (TensorFlow Core v2.4.1)

init = tf.compat.v1.global_variables_initializer()   # must have if define variable

with tf.compat.v1.Session() as sess:   # use this method you don't need sess.close()
    sess.run(init)
    for i in range(6):
        sess.run(update)
        print(sess.run(state))  # sess.run()  like a pointer