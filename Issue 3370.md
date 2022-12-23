# Issue 3370: [with patch, needs review] converting strings to ZZ[x,y] fails

Issue created by migration from https://trac.sagemath.org/ticket/3370

Original creator: burcin

Original creation time: 2008-06-05 01:57:38

Assignee: malb

With 3.0.2:


```
sage: P.<x,y> = ZZ[]
sage: P('x+y')
TypeError                                 Traceback (most recent call last)

/home/burcin/work/sage/sage-3.0.2/<ipython console> in <module>()

/home/burcin/work/sage/sage-3.0.2/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ring.py in __call__(self, x, check)
    386 
    387         elif isinstance(x , str) and self._has_singular:
--> 388             self._singular_().set_ring()
    389             try:
    390                 return self._singular_().parent(x).sage_poly(self)

/home/burcin/work/sage/sage-3.0.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in _singular_(self, singular, force)
    172             return R
    173         except (AttributeError, ValueError):
--> 174             return self._singular_init_(singular, force)
    175 
    176     def _singular_init_(self, singular=singular_default, force=False):

/home/burcin/work/sage/sage-3.0.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in _singular_init_(self, singular, force)
    243 
    244         else:
--> 245             raise TypeError, "no conversion to a Singular ring defined"
    246 
    247         return self.__singular

TypeError: no conversion to a Singular ring defined

```


Attached patch fixes this problem.


---

Comment by burcin created at 2008-06-05 02:00:02

convert strings to mpolynomials using sage_eval


---

Attachment

patch looks good.


---

Comment by mabshoff created at 2008-06-15 19:00:34

Resolution: fixed


---

Comment by mabshoff created at 2008-06-15 19:00:34

Merged in Sage 3.0.3.rc0
