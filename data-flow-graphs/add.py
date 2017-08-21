import tensorflow as tf

a = tf.add(3,5)
print a

b = tf.add(4.8,9.2)
print b

c = tf.add(123, 456)
print c

sess = tf.Session()

print sess.run(a)
print sess.run(b)
print sess.run(c)

sess.close()
