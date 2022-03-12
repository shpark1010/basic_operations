import tensorflow as tf

with tf.compat.v1.Session() as sess:
  h = tf.constant("Hello")
  w = tf.constant("World!")
  hw = h + w
  ans = sess.run(hw)
  print(ans)

g = tf.Graph() 
with g.as_default():   
	a = tf.constant(3, name="a")
	b = tf.constant(2, name="b")
	c = tf.constant(1, name="c")

	d = a * b
	e = d + c

sess = tf.compat.v1.Session(graph=g)
print(sess.run(e))