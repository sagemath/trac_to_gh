# Issue 91: gcd for polynomials over ZZ

Issue created by migration from Trac.

Original creator: jdc

Original creation time: 2006-09-27 19:26:49

Assignee: somebody

CC:  jdc@uwo.ca

If I start with this example from a sage docstring:                                                              
                                                                                                                 
  sage: x, y = PolynomialRing(RationalField(), 2, ['x','y']).gens()                                              
  sage: f = (x^3 + 2*y<sup>2*x)</sup>2                                                                                    
  sage: g = x<sup>2*y</sup>2                                                                                              
  sage: f.gcd(g)                                                                                                 
  x^2                                                                                                            
                                                                                                                 
but change RationalField to IntegerRing, I get an error when executing                                           
the last line:                                                                                                   
                                                                                                                 
  TypeError: no conversion of this ring to a Singular ring defined                                               

I could of course work over Q, but I was wondering if it would
be easy to make sage handle this.

Dan


---

Comment by ncalexan created at 2007-02-19 04:51:19

Resolution: fixed


---

Comment by ncalexan created at 2007-02-19 04:51:19

Fixed and doctested as of 2.1.5.
