import tensorflow as tf 

a = tf.constant([2,2], shape=[2,2], name="a")
b = tf.constant([[0,1],[2,3]], name="b")

x = tf.add(a,b, name="addition")
y = tf.multiply(a,b, name="elementwise_multiplication")


with tf.Session() as sess:
	print sess.run(y)


