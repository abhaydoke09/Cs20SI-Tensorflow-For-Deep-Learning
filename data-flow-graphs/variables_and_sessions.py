import tensorflow as tf 

W = tf.Variable(20)

sess1 = tf.Session()
sess2 = tf.Session()

sess1.run(W.initializer)
sess2.run(W.initializer)

print sess1.run(W.assign_add(10)) # >> 30
print sess2.run(W.assign_sub(30)) # >> -10

sess1.close()
sess2.close()