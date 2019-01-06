import tensorflow as tf

a = tf.constant([5])
b = tf.constant([5])

c = tf.add(a, b)

with tf.Session() as session:
    result = session.run(c)
    print(result)
    