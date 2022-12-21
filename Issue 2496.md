# Issue 2496: bug in introspection (probably easy to fix)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-12 15:48:31

Assignee: tba

See near the bottom below.    In particular the `X.points??` input
should fail gracefully rather than going boom with an eval error.  Closing
this ticket does not necessarily mean fixing anything more than making this
fail gracefully. 


```
> 
>  I had a Sage worksheet that created an Elliptic curve
>  (E=EllipticCurve([0,17]))
>  and then invoked E.rational_points(10).
>  The code has obviously changed as it now expects
>  different parameters and needs to be E.rational_points(bound=10).
>  The real problems is I no longer get all the rational points. Maybe
>  the
>  definition of bound has changed? I had assumed it was a logarithmic
>  bound on the points, but I get only the first few points (max X=4).
>  
>  I then tried to follow through the code and it's changed a lot since I
>  first looked
>  at it. rational_points() is now defined in .../schemes/generic/
>  algebraic_schemes
>  and I'm unable to figure out where to go from there. The code reads:
>  
>  ...
>   if F == None:
>             F = self.base_ring()
>         X = self(F)
>  ...
>   return X.points(bound)
>  
>  Substituting the first part into my worksheet, with substituting E for
>  self, I get
>  X is Abelian group of points on Elliptic Curve defined by y^2  = x^3 +
>  17
>  over Rational Field.
>  
>  Next I try:
>   X.points??
>  
>  and get
>  ---------------------
>  Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
>   File "/home/bill/.sage/sage_notebook/worksheets/bill/5/code/16.py",
>  line 6, in <module>
>     print _support_.source_code("", globals())
>   File "/sage/current/local/lib/python2.5/site-packages/sage/server/
>  support.py", line 154, in source_code
>     obj = eval(s, globs)
>   File "<string>", line 0
>  
>     ^
>  SyntaxError: unexpected EOF while parsing
>  ----------------------
>  Not much help there...
>  Is this a  bug, two bugs, or am I just being my usual stupid self?
>  

You score +1 for at least one bug (the second one).  The first
regarding the bound is *probably* related to changes John Cremona
made to elliptic curves, and I hope he will comment on them soon.
I've made your second bug above trac # 
```



---

Comment by was created at 2008-05-11 06:12:05

Resolution: fixed


---

Comment by was created at 2008-05-11 06:12:05

This is already fixed.  First, I can't figure out how to replicate any sort of X.points?? problem.  For me that works just fine.  Also, the questionable eval above in the traceback is as of sage-3.0.1 already wrapped in a try/except block.
