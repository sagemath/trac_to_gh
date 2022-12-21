# Issue 7735: [with patch] incorrect sage exponentiation in interreduced_basis '^' vs '**'

Issue created by migration from Trac.

Original creator: lftabera

Original creation time: 2009-12-18 13:42:36

Assignee: AlexGhitza

Keywords: interreduced_basis, python

There is a bug in the code of interreduced_basis in

sage/rings/polynomial/multi_polynomial_ideal.py


```
sage: R=QQ['t'].fraction_field()['x,y']                                                                              
sage: R.inject_variables()                                                                                       
Defining x, y                                                                                                    
sage: I=x*R                                                                                                      
sage: I.interreduced_basis()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/luisfe/<ipython console> in <module>()

/opt/SAGE/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.pyc in wrapper(*args, **kwds)
    362         """
    363         with RedSBContext():
--> 364             return func(*args, **kwds)
    365
    366     from sage.misc.sageinspect import sage_getsource

/opt/SAGE/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.pyc in interreduced_basis(self)
   1542                 for f in self._singular_().interred():
   1543                     f = R(f)
-> 1544                     ret.append(f.lc()^(-1)*f) # lead coeffs are not reduced by interred
   1545                 s.option("set",o)
   1546             except TypeError:

/opt/SAGE/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__xor__ (sage/structure/element.c:4469)()

RuntimeError: Use ** for exponentiation, not '^', which means xor
in Python, and has the wrong precedence.

```



---

Comment by lftabera created at 2009-12-18 13:43:02

Patch to correct the problem and a test case


---

Attachment


---

Comment by lftabera created at 2009-12-18 13:44:09

Changing status from new to needs_review.


---

Comment by cremona created at 2009-12-18 16:47:01

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2009-12-18 16:47:01

Changing keywords from "interreduced_basis, python" to "interreduced_basis".


---

Comment by cremona created at 2009-12-18 16:47:01

Looks good, applies to 4.3.rc0, tests pass and it has a relevant doctest.


---

Comment by mhansen created at 2009-12-19 20:27:54

Resolution: fixed
