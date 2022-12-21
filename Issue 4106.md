# Issue 4106: error coercing symbolic variable into polynomial ring modulo 4 (but not mod 3)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-09-12 15:52:42

Assignee: tbd

Paul Zimmerman reports that one coercion works, and another natural similar coercion doesn't, as illustrated below:



```
x = var('x')
R = IntegerModRing(3)
S = PolynomialRing(R, x)
S(x)
///

x
```



```
x = var('x')
R = IntegerModRing(4)
S = PolynomialRing(R, x)
S(x)
///

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/wstein/.sage/sage_notebook/worksheets/admin/1/code/22.py", line 9, in <module>
    exec compile(ur'S(x)' + '\n', '', 'single')
  File "/home/wstein/sage/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/home/wstein/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 1097, in __call__
    return polynomial_modn_dense_ntl.Polynomial_dense_modn_ntl_zz(self, x, check, is_gen, construct=construct)
  File "polynomial_modn_dense_ntl.pyx", line 574, in sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modn_ntl_zz.__init__ (sage/rings/polynomial/polynomial_modn_dense_ntl.cpp:7017)
  File "polynomial_modn_dense_ntl.pyx", line 130, in sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_n.__init__ (sage/rings/polynomial/polynomial_modn_dense_ntl.cpp:3188)
  File "/home/wstein/sage/local/lib/python2.5/site-packages/sage/rings/integer_mod_ring.py", line 617, in __call__
    return integer_mod.IntegerMod(self, x)
  File "integer_mod.pyx", line 132, in sage.rings.integer_mod.IntegerMod (sage/rings/integer_mod.c:2187)
  File "integer_mod.pyx", line 1430, in sage.rings.integer_mod.IntegerMod_int.__init__ (sage/rings/integer_mod.c:10773)
  File "integer_ring.pyx", line 282, in sage.rings.integer_ring.IntegerRing_class.__call__ (sage/rings/integer_ring.c:4998)
TypeError: unable to convert x (=x) to an integer
```



---

Attachment

See the fairly trivial patch attached.


---

Comment by was created at 2008-10-05 16:05:50

Positive review.

I did notice this unfortunate property of the _polynomial_ function that is used
to implement this patch, namely it does something dumb when given x+y as input:


```
sage: var('x')
x
sage: var('y')
y
sage: S = PolynomialRing(Integers(4),1,'x')
sage: S(x+y)
2*x
sage: (x+y)._polynomial_(S)
2*x
```


I think in this case it should raise a TypeError. 

This is my fault, since I implemented _polynomial_... of course.


---

Comment by AlexGhitza created at 2008-10-05 21:50:38

I've opened a new ticket #4246 addressing the issue reported by William (and put a patch there -- it is independent of this ticket).


---

Comment by mabshoff created at 2008-10-07 22:12:57

Resolution: fixed


---

Comment by mabshoff created at 2008-10-07 22:12:57

Merged in Sage 3.1.3.alpha3
