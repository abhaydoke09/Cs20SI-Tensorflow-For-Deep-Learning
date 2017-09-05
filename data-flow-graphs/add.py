import tensorflow as tf 

int_add = tf.add(3,4)
float_add = tf.add(5,6)

sess = tf.Session()

print sess.run(int_add)
print sess.run(float_add)

sess.close()


'''
to avoid using sess.close() we can use the with statement
'''

with tf.Session() as sess:
	print sess.run(float_add)
	print sess.run(int_add)

