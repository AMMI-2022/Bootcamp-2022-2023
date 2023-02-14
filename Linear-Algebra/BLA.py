
### INSTRUCTIONS ###
"""
1. DO NOT IMPORT ADDITIONAL LIBRARIES, ONLY NUMPY IS ENOUGH FOR THIS ASSIGNMENT.
THE MAX AND ABSOLUTE VALUE FUNCTIONS HAVE CODED FROM SCRATCH. DO NOT USE FOR INSTANCE, abs() or np.max() or max(). IF YOU NEED ANY OF THEM, PLEASE WRITE YOUR OWN CODES.
2. DO NOT TOUCH THE main() function

"""

import numpy as np

"""
Helper functions: START

Helper functions are functions that will be used within the required functions. This may not be useful if you decide to write everything within your functions.
--- For this assignment, personally I wrote two helper functions, namely, absolute_value() and max_of_an_array() that helped me to find the absolute value of a 
given value and the maximum value of a given array respectively. However, you may have more than two.
"""
## WRITE YOUR HELPER FUNCTIONS HERE (ONLY IF YOU HAVE)
"""
Helper functions: END
"""
def inner(x,y):

  """
	r = inner(x,y)
  Compute the inner product of two vectors x and y.

  Parameters
  ----------
  x: vector of size n
  y: vector of size n

  Return
  ------
  r: a float
  
  Example
  -------
  >>> x= np.array([-8, 4, 6, 2, 5])
  >>> y= np.array([2, 2, -1, 4, 3])
  >>> r= inner(x,y)
  >>> r
  9.0
  
  """
  ##### WRITE YOUR CODE HERE #####
  pass

def hadamard(x,y):

  """
	r = hadamard(x,y)
  Compute the hadamard (element-wise) product of two vectors x and y.

  Parameters
  ----------
  x: vector of size n
  y: vector of size n

  Return
  ------
  r: an array of length n
  
  Example
  -------
  >>> x= np.array([-8, 4, 6, 2, 5])
  >>> y= np.array([2, 2, -1, 4, 3])
  >>> r= hadamard(x,y)
  >>> r
  array([-16.,   8.,  -6.,   8.,  15.])
  """
  ##### WRITE YOUR CODE HERE #####
  pass
  


def outer(x,y):

  """
	r = outer(x,y)
  Compute the inner product of two vectors x and y.

  Parameters
  ----------
  x: vector of size m
  y: vector of size n

  Return
  ------
  M: an mxn matrix 
  
  Example
  -------
  >>> x= np.array([8, 4, 6, 2, 5])
  >>> y= np.array([2, 2, 1, 4, 3, 9, 10])
  >>> M= outer(x,y)
  >>> M
  array([[16. 16.  8. 32. 24. 72. 80.]
  [ 8.  8.  4. 16. 12. 36. 40.]
  [12. 12.  6. 24. 18. 54. 60.]
  [ 4.  4.  2.  8.  6. 18. 20.]
  [10. 10.  5. 20. 15. 45. 50.]])
  
  """
  ##### WRITE YOUR CODE HERE #####
  pass

def mynorm(x,p):
  """
	r = mynorm(x)
  Compute the 2-norm of a vector x.

  Parameters
  ----------
  x: vector of size n
  p: int for p-norm

  Return
  ------
  r: a float
  
  Example
  -------
  >>> x= np.array([-8,4,6, 2, 5])
  >>> r= mynorm(x,p= 2) # p may be: "inf", 1 or 2 or any integer.
  >>> r
  12.041594578792296
  
  """
  ##### WRITE YOUR CODE HERE #####
  pass
    
def normalize(x):
  
  """
	s = mynormalize(x)
   Return a vector s that is the normalized vector x.
   
  Parameters
  ----------
   x: a vector of size n
   
  Return
  ------
  s: a normalized vector of size n
  
  Example
  -------
  >>> x= np.array([-8,4,6, 2, 5])
  >>> s= normalize(x)
  >>> s
  array([-0.66436384  0.33218192  0.49827288  0.16609096  0.4152274 ])

  """
  ##### WRITE YOUR CODE HERE #####
  pass

def projection(x,y):

  """
	 s = project(x, y)
   Project vector x onto vector y.

   Parameters
   ----------
   x: a vector of size n
   y: a vector of size n

   Return
   ------
   s: an arrray of size n
   
   Example
   -------
   >>> x= np.array([8,4,6, 2, 5])
   >>> y= np.array([2,2,1, 4,3])
   >>> s= projection(x,y)
   >>> s
   array([ 0.52941176  0.52941176 -0.26470588  1.05882353  0.79411765])
   
  """
  ##### WRITE YOUR CODE HERE #####
  pass

def cosine_similarity(x,y):
  
  """
	 s = cosine_similarity(x, y)
   cosine similarity between vector x and vector y.

   Parameters
   ----------
   x: a list of size n
   y: a list of size n

   Return
   ------
   s: a float
   
   Example
   -------
   >>> x= np.array([8,4,6, 2, 5])
   >>> y= np.array([2,2,1, 4,3])
   >>> r= cosine_similarity(x,y)
   >>> r
   0.12817964067657414
   
  """
  ##### WRITE YOUR CODE HERE #####
  pass


def matrix_norm(A, p):
    """
      p_norm_A = matrix_norm(A, p)
      p-norm of a matrix A.

      Parameters
      ----------
      A: a nxn matrix.
      p: int or string. This parameter determine the norm type.
      
      Return
      ------
      p_norm_A: a float
      
      Example
      -------
      >>> A= np.array([[5,-4,2], [-1,2,3],[-2,1,0]])
      >>> p_norm_A= matrix_norm(A,p= 1) # p may be: "inf", 1 or F
      >>> p_norm_A
      10.0 
      
    """
    ##### WRITE YOUR CODE HERE #####
    pass
    
    
def main():
    ## Test
    """
    DO NOT MODIFY THIS FUNCTION
    """
    print("-----TEST------")
    print("-- Display x --")
    x= np.array([-8,4,6, 2, 5])
    y= np.array([2,2,-1, 4,3])
    print(x)
    print("-- Display y --")
    print(y)
    TOL= 1e-20
    assert ((np.dot(x,y)-inner(x,y))<TOL), "inner function not working fine"
    print("✅✅✅ inner function works fine.")
    print("The solution is: ", inner(x,y))
    assert (mynorm(x*y-hadamard(x,y),2)<TOL), "hadamard function not working fine"
    print("✅✅✅ hadamard function works fine.")
    print("The solution is: ", hadamard(x,y))
    a= np.array([8,4,6, 2, 5])
    print("-- Display a --")
    print(a)
    b= np.array([2,2,1, 4,3,9,10])
    print("-- Display b --")
    print(b)
    print("The solution is: ", outer(a,b))
    assert (np.outer(a,b).all()==outer(a,b).all()), "outer function not working fine"
    """Norm functions checking"""
    assert ((np.linalg.norm(x,1)-mynorm(x,1))<TOL), "1-mynorm function not working fine"
    assert ((np.linalg.norm(x,2)-mynorm(x,2))<TOL), "2-mynorm function not working fine"
    assert ((np.linalg.norm(x,np.inf)-mynorm(x,"inf"))<TOL), "inf-mynorm function not working fine"
    print("✅✅✅ p-mynorm function works fine.")
    print("The solution is: ", mynorm(x,2))

    assert ((mynorm(x/np.linalg.norm(x)-np.array(normalize(x)),2))<TOL), "normalize function not working fine"
    print("✅✅✅ normalize function works fine.")
    print("The solution is: ", normalize(x))
    
    ""
    a= np.array([8,4,6, 2, 5])
    print("-- Display a --")
    print(a)
    print("-- Display b --")
    b= np.array([2,2,1, 4,3])
    print(b)

    assert ((mynorm(np.array([3.1176470588235294, 3.1176470588235294, 1.5588235294117647, 6.235294117647059, 4.676470588235294])-np.array(projection(a,b)),2))<TOL), "projection function not working fine"
    print("✅✅✅ projection function works fine.")
    print("The solution is: ", projection(x,y))

    assert ((np.dot(x,y)/(np.linalg.norm(x,2)*np.linalg.norm(y,2))-cosine_similarity(x,y))<TOL), "cosine_similarity function not working fine"
    print("✅✅✅ cosine_similarity function works fine.")
    print("The solution is: ", cosine_similarity(x,y))
    
    ## Test Matrix norm
    TOL1= 0.08
    np.random.seed(4)
    A= np.random.rand(10,10)
    assert (absolute_value(matrix_norm(A, p=1)-np.linalg.norm(A, 1))<TOL1), "Your matrix 1-norm does not work"
    print("✅✅✅ Your matrix 1-norm works fine.")
    print("The solution is: ", matrix_norm(A, p=1))
    
    assert (absolute_value(matrix_norm(A, p="inf")-np.linalg.norm(A, np.inf))<TOL1), "Your matrix inf-norm does not work"
    print("✅✅✅ Your matrix inf-norm works fine.")
    print("The solution is: ", matrix_norm(A, p='inf'))
    
    assert (absolute_value(matrix_norm(A, p="F")-np.linalg.norm(A, 'fro'))<TOL1), "Your matrix F-norm does not work"
    print("✅✅✅ Your matrix F-norm works fine.")
    print("The solution is: ", matrix_norm(A, p='F'))


if __name__== "__main__":
    main()