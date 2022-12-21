# Issue 3028: Ideals in multivariate polynomial rings raise exceptions on comparison

Issue created by migration from Trac.

Original creator: broune

Original creation time: 2008-04-26 01:45:51

Assignee: malb

Keywords: multivariate polynomial ring, no variables

This code

ring = PolynomialRing(QQ, names=[])

id = ring.ideal(0)

print id == id


gives the following error message

---------------------------------------------------------------------------
<type 'exceptions.StopIteration'>         Traceback (most recent call last)

/Users/bjarke/sync/<ipython console> in <module>()

/Users/bjarke/sync/element.pyx in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:4558)()

/Users/bjarke/sync/element.pyx in sage.structure.element.Element._richcmp (sage/structure/element.c:4453)()

/Users/bjarke/sage-3.0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in __cmp__(self, other)
    347             True
    348         """
--> 349         l = self.groebner_basis()
    350         r = other.groebner_basis()
    351         return cmp(r,l)

/Users/bjarke/sage-3.0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in groebner_basis(self, algorithm, *args, **kwds)
   1836                 except TypeError: # conversion to Singular not supported
   1837                     # we might want to print a warning here
-> 1838                     gb = toy_buchberger.buchberger_improved(self, *args, **kwds)
   1839         elif algorithm.startswith('singular:'):
   1840             gb = self._groebner_basis_using_singular(algorithm[9:])

/Users/bjarke/sage-3.0/local/lib/python2.5/site-packages/sage/rings/polynomial/toy_buchberger.py in buchberger_improved(F)
    232         print "%d reductions to zero."%(reductions_to_zero)
    233 
--> 234     return Sequence(inter_reduction(G))
    235 
    236 def update(G,B,h):

/Users/bjarke/sage-3.0/local/lib/python2.5/site-packages/sage/rings/polynomial/toy_buchberger.py in inter_reduction(Q)
    324         Q -- a set of polynomials
    325     """
--> 326     base_ring = iter(Q).next().base_ring()
    327     Q = set(Q)
    328     while True:

<type 'exceptions.StopIteration'>: 





---

Attachment


---

Comment by broune created at 2008-05-07 22:16:56

Changing assignee from malb to broune.


---

Comment by broune created at 2008-05-07 22:16:56

Changing status from new to assigned.


---

Comment by cwitty created at 2008-05-10 23:16:55

Code looks good, doctests pass in sage/rings/polynomial.  Positive review.


---

Comment by mabshoff created at 2008-05-11 08:07:54

Merged in Sage 3.0.2.alpha0


---

Comment by mabshoff created at 2008-05-11 08:07:54

Resolution: fixed
