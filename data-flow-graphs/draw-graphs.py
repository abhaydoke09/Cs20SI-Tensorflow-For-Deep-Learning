import tensorflow as tf

x = 3.5
y = 420.0

op1 = tf.add(x,y)
op2 = tf.multiply(x,y)
useless = tf.multiply(x,op1)
op3 = tf.pow(op1,op2)

with tf.Session() as sess:
  writer = tf.summary.FileWriter('log',sess.graph)
  print sess.run(op3)
  writer.close()
