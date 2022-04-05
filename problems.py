# Convert a List into a string and print it
#
# Write a program that takes a list and turns it into a string.
#
# Example:
#
# >>> a = [1, 2, 3]
# >>> a
# [1, 2, 3]
# >>> a = str(a)
# >>> a
# '[1, 2, 3]'
#
# Hint: Use the join method.
#
# Write a program that takes a list and turns it into a string.
#
# Example:
#
# >>> a = [1, 2, 3]
# >>> a
# [1, 2, 3]
# >>> a = str(a)
# >>> a
# '[1, 2, 3]'



#  Convert a list into a tuple and print it
#
# Write a program that takes a list and turns it into a tuple.
#
# Example:
#
# >>> a = [1, 2, 3]
# >>> a
# [1, 2, 3]
# >>> a = tuple(a)



# HOW TO COUNT THE OCCURENCES OF A PARTICULAR WORD IN A LIST
#
# Write a program that takes a list of strings and a string containing a single word, and prints the number of times the word appears in the list.
#
# Example:
#
# >>> a = ['cat', 'dog', 'rabbit', 'cat', 'mouse']
# >>> a
# ['cat', 'dog', 'rabbit', 'cat', 'mouse']
# >>> word = 'cat'
# >>> word
# 'cat'
# print(a.count(word))


#  What is Numpy array?
#
# Numpy is a library that provides a high-performance multidimensional array object.
#
# Numpy arrays are similar to lists, but they are much more efficient.
#
# Numpy arrays are used to store large amounts of data.
#


# Create a empty numpy array in Python
#
# Create a numpy array with zeros.
#
# Example:
#
# >>> import numpy as np
# >>> a = np.zeros(5)
# >>> a
# array([0., 0., 0., 0., 0.])
#
# Create a numpy array with ones.
#
# Example:
#
# >>> import numpy as np
# >>> a = np.ones(5)
# >>> a
# array([1., 1., 1., 1., 1.])
#
# Create a numpy array with random numbers.
#
# Example:
#
# >>> import numpy as np
# >>> a = np.random.random(5)
# >>> a
# array([0.82748892, 0.82748892, 0.82748892, 0.82748892, 0.82748892])
#
# Create a numpy array with random numbers between 0 and 1.
#
# Example:
#
# >>> import numpy as np
# >>> a = np.random.rand(5)
# >>> a
# array([0.82748892, 0.82748892, 0.82748892, 0.82748892, 0.82748892])
#
# Create a numpy array with random numbers between 5 and 10.
#
# Example:
#
# >>> import numpy as np
# >>> a = np.random.randint(5, 10, 5)
# >>> a
# array([7, 8, 9, 7, 8])
#


#  negative index in python
#
# Python supports negative indexing.
#
# Example:
#
# >>> a = [1, 2, 3, 4, 5]
# >>> a[-1]
# 5
# >>> a[-2]
# 4
# >>> a[-3]
# 3
# >>> a[-4]
# 2
# >>> a[-5]
# 1
#


# concatenate strings in python
#
# Example:
#
# >>> a = 'Hello'
# >>> b = 'World'
# >>> a + b
# 'HelloWorld'
# >>> a = 'Hello'
# >>> b = 'World'
# >>> a + ' ' + b
# 'Hello World'
#


#  What is yield in Python?
#
# The yield statement is a keyword in Python, and the yield statement is used to create generators.
#
# Example:
#
# >>> def gen():
# ...     yield 1
# ...     yield 2
# ...     yield 3
# ...
# >>> g = gen()
# >>> next(g)
# 1
# >>> next(g)
# 2
# >>> next(g)


from xml.dom.minidom import Notation


def gen():
    yield 1
    yield 2
    yield 3

gen()



# Big o Notation in Python 
#
# Big O notation is a mathematical notation for describing the growth of a function.
#
# Example:
#
# >>> def f(n):
# ...     return n * n
# ...
# >>> f(2)
# 4
# >>> f(3)
# 9
# >>> f(4)
# 16
# >>> f(5)
# 25


