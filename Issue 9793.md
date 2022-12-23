# Issue 9793: Make easy wrapper for symbolic lagrange interpolation

Issue created by migration from https://trac.sagemath.org/ticket/9794

Original creator: kcrisman

Original creation time: 2010-08-24 15:18:15

Assignee: burcin

CC:  jason

Currently, one has to do something like one of these.

```
 > 1. There is no way to get a symbolic interpolated polynomial de novo 
 > without going through polynomial rings, e.g. all these steps: 
 > 
 > pts = [(1,2),(2,3),(3,2),(4,3),(5,2),(6,3)] 
 > R.<x>=QQ[] 
 > f = R.lagrange_polynomial(pts) 
 > SR(f) 
 > 
Yes.  You could define your own function :) (see 
http://sage.cs.drake.edu/home/pub/2/, for example).  Also, mpmath and 
numpy/scipy can get numerical values for the coefficients, I believe. 
Maxima also can construct a lagrange polynomial (load the 'interpol' 
package) 
sage: maxima.load('interpol') 
"/home/jason/sage-4.4.2/local/share/maxima/5.20.1/share/numeric/interpol.ma c" 
sage: maxima.lagrange([[1,2],[3,4]]) 
-x+2*(x-1)+3 
```

That's too bad; we need to wrap this to make it very easy to get the interpolation from a list of points with one command from SR.

One thing to discuss would be whether one would want an approximate one if the coefficients were floats/RR, or always to try for an exact one.
