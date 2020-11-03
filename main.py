import numpy as np 

def xmarginal( jpmass ) :
  # Your code to calculate the marginal along x goes here
  return 0
  
def ymarginal( jpmass ) : 
  # Your code to calculate the marginal along y goes here
  return 0
  
def expectation_x( xvals, jpmass ) :
  # Your code to calculate E(X) goes here
  return 0
  
def expectation_y( yvals, jpmass ) :
  # Your code to calculate E(Y) goes here
  return 0
  
def cov_xy( xvals, yvals, jpmass ) :
  # Your code to calculate cov(X,Y) goes here
  return 0
  
def rho_xy( xvals, yvals, jpmass ) : 
  # Your code to calculate rho(X,Y) goes here
  return 0


# This is the probability mass function from the example problem 
# on the problem sheet you have just completed
xvals, yvals = np.array([0,1,2]), np.array([1,2,4])
jpmass = np.array([[0.1,0.1,0],[0.2,0.1,0.1],[0,0.2,0.2]])
print("The marginal for the random variable X is", xmarginal(jpmass) )
print("The marginal for the random variable y is", ymarginal(jpmass) )
print("The expectations of X is", expectation_x(xvals,jpmass) )
print("The expectations of Y is", expectation_y(yvals,jpmass) )
print("The covariance of the distribution is", cov_xy(xvals,yvals,jpmass))
print("The correlation coefficient for the two variables is", rho_xy(xvals,yvals,jpmass))
