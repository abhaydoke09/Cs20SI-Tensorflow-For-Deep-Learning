import tensorflow as tf 

a = tf.Variable(34, name="scalar")
b = tf.Variable([3,2], name="vector")
c = tf.Variable([[2,3],[4,5]], name="matrix")
d = tf.Variable(tf.zeros([784,10]))

init = tf.global_variables_initializer()		# initialize all variables 
#init = tf.variables_initializer([a,b])		# initialze only a subset of variables
with tf.Session() as sess:
	sess.run(init)
	print sess.run(a)
	print sess.run(b)
	print sess.run(c)
	print sess.run(d)[2:5]
	print d.eval().shape


w = tf.Variable(tf.zeros([10,10]))
w_assign = w[2:8,:].assign(tf.ones([6,10]))
init = tf.global_variables_initializer()
with tf.Session() as sess:
	sess.run(init)
	sess.run(w)
	sess.run(w_assign)
	print w_assign.eval()