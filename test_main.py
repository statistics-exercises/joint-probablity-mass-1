import unittest
from main import *

class UnitTests(unittest.TestCase) :
      def test_xmarginal(self) :
          student = xmarginal(jpmass)
          self.assertTrue( len(student)==len(xvals), "Your function for calculating P(X=x) is not working" )
          for i in range(len(xvals)) :
              self.assertTrue( sum(jpmass[:,i])==student[i], "Your function for calculating P(X=x) is not working" )
              
      def test_ymarginal(self) :
          student = ymarginal(jpmass)
          self.assertTrue( len(student)==len(yvals), "Your function for calculating P(Y=y) is not working" )
          for i in range(len(yvals)) : 
              self.assertTrue( sum(jpmass[i,:])==student[i], "Your function for calculating P(Y=y) is not working" )
      def test_expectationx(self) :
          myex = 0 
          for i in range(len(xvals)) : 
              myex = myex + xvals[i]*sum(jpmass[:,i])
          self.assertTrue( expectation_x( xvals, jpmass )==myex, "Your function for calculating E(X) is not working )
          
      def test_expectationy(self) :
          myey =  0
          for i in range(len(yvals)) : 
              myey = myey + yvals[i]*sum(jpmass[i,:])
          self.assertTrue( expectation_y( yvals, jpmass )==myey, "Your function for calculating E(Y) is not working" )
          
      def test_covxy(self) :
          mycov, myex, myey = 0, 0, 0
          for i in range(len(xvals)) : 
            for j in range(len(yvals)) : 
              myex = myex + xvals[i]*jpmass[j,i]
              myey = myey + yvals[j]*jpmass[j,i]
              mycov = mycov + xvals[i]*yvals[j]*jpmass[j,i] 
          self.assertTrue( np.abs(mycov - myex*myey-cov_xy(xvals, yvals, jpmass) )<1e-7, "The covariance is not computed correctly" )
          
      def test_rhoxy(self) :
          mycov, myex, myey, myvarx, myvary = 0, 0, 0, 0, 0
          for i in range(len(xvals)) : 
              for j in range(len(yvals)) : 
                  myex = myex + xvals[i]*jpmass[j,i]
                  myvarx = myvarx + xvals[i]*xvals[i]*jpmass[j,i]
                  myey = myey + yvals[j]*jpmass[j,i]
                  myvary = myvary + yvals[j]*yvals[j]*jpmass[j,i]
                  mycov = mycov + xvals[i]*yvals[j]*jpmass[j,i]
          mycorr = ( mycov - myex*myey ) / np.sqrt( (myvarx-myex*myex)*(myvary-myey*myey) )
          self.assertTrue( np.abs(mycorr-rho_xy( xvals, yvals, jpmass))<1e-7, "The correlation coefficient is not computed correctly" )
      
