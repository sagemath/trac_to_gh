# Issue 3841: [with patch, not ready for review] Use singular for calculus by default.

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-08-13 18:31:46

Assignee: gfurnish

This patch makes symbolic polynomials use libsingular via the ring interface by default.
It also contains a large number of doctest changes because polynomials in Sage have a better ordering.


```
%cython
from sage.calculus.calculus import var
from sage.rings.integer cimport Integer
from random import random
def blah(rng):
    global five
    x,y = var('x,y')
    foo = x
    cdef i
    for i from 0<=i<rng:
        foo+= x**int(random()*1000)+y**int(random()*10000)+x+1
    return foo

The python code used to test maxima was:
sage: def blah(rng):
   foo = x
   for i in xrange(0, rng):
       foo+=x^int(random()*10000)+y^int(random()*10000)+x+1; foo = simplify(foo)             
   return foo

I'm well aware that I'm comparing cython timings to python timings.. but the cython overhead isn't the dominating factor here.
The simplify exists to force it to go to maxima to evaluate the expression between additions (as singular does).  Otherwise this is not a very fair/real world comparison if Maxima gets to build the entire addition and send it to Maxima as one batch (and only do the addition once as opposed to rng times).  

%timeit blah(10)

125 loops, best of 3: 1.98 ms per loop

Maxima: 
CPU times: user 0.14 s, sys: 0.05 s, total: 0.18 s
Wall time: 1.97 s

%timeit blah(100)
 	
25 loops, best of 3: 20.8 ms per loop

Maxima:
CPU times: user 3.30 s, sys: 1.16 s, total: 4.47 s
Wall time: 28.89 s


%timeit blah(1000)
	
5 loops, best of 3: 214 ms per loop

Maxima: Raises exception

%timeit blah(10000)

5 loops, best of 3: 2.09 s per loop


```



---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment

Replaces the other patches.


---

Comment by rlm created at 2008-08-14 23:19:28

Pre-review comments.


---

Attachment

I didn't make it through the whole patch, but these are my initial impressions. I'll have much more time to give this my full attention tomorrow.


---

Comment by gfurnish created at 2008-08-14 23:37:23

1) Fixed 
2) I disagree, but will comply.  Symbolic polynomials be default still printed in this ordering.  However, before most polynomials were not actually constructed as polynomials.  This is what the ordering should have been.
3) The doctests were moved to 4485
4) Functionality was subsumed by other substitutes (For instance variable now uses polynomial's substitute)
5) It corrects for an issue where the equation is lexically reversed (so that x<=y becomes y>=x in some cases) because of changes to polynomial ordering. 
6) I'll move existing doctests that cover the functions to the functions in question.


---

Comment by rlm created at 2008-08-14 23:40:05

Replying to [comment:2 gfurnish]:
> 2) I disagree, but will comply.  Symbolic polynomials be default still printed in this ordering.  However, before most polynomials were not actually constructed as polynomials.  This is what the ordering should have been.

You disagree with the need to discuss one of your proposed changes? Perhaps you should then be developing your own project, to avoid the inconvenience of other's opinions.


---

Comment by gfurnish created at 2008-08-14 23:47:50

I don't see why fixing a bug (and yes, it is a bug.  Symbolic Polynomials have always used the same representation as the underlying object) has suddenly become a new feature.  I said I would ask because people may be interested, but the ordering was entirely determined by existing code in SymbolicPolynomial.


---

Comment by rlm created at 2008-08-15 14:01:08

> I don't see why fixing a bug (and yes, it is a bug.  ...) has suddenly become a new feature.

This isn't a bug or a new feature: it is a convention. Based on William's comments in the lab today, I don't think there will be a huge amount of support for printing polynomials the way they are here. The point is that it is just a convention, and in changing such, you are not doing things the way people expect them to be done. If you make a change in conventions, there had better be a very good reason for it, and the Sage community must support it. Probably "Symbolic Polynomials alway use the same representation as the underlying object" should change if this is going to fly (also, this is hardly a justification of anything...).

Applied to sage-3.1.alpha2, the following test fails, aside from the two (now) resolved issues for coercion:

```
sage -t  devel/sage/sage/structure/coerce_maps.pyx
**********************************************************************
File "/home/rlmill/sage-3.1.alpha2-sage.math-only-x86_64-Linux/tmp/coerce_maps.py", line 113:
    sage: mor(x^2/4+1)
Exception raised:
    Traceback (most recent call last):
      File "/home/rlmill/sage-3.1.alpha2-sage.math-only-x86_64-Linux/local/lib/python/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[5]>", line 1, in <module>
        mor(x**Integer(2)/Integer(4)+Integer(1))###line 113:    sage: mor(x^2/4+1)
      File "map.pyx", line 128, in sage.categories.map.Map.__call__ (sage/categories/map.c:2676)
      File "coerce_maps.pyx", line 146, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:3333)
(*)   File "/home/rlmill/sage-3.1.alpha2-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1833, in _polynomial_
        return self.substitute_over_ring(dict(sub), ring=R)
(*)   File "/home/rlmill/sage-3.1.alpha2-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 3682, in substitute_over_ring
        return self._recursive_sub_over_ring(kwds, ring)
(*)   File "/home/rlmill/sage-3.1.alpha2-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 4591, in _recursive_sub_over_ring
        return ring(f(kwds[v]))
      File "polynomial_element.pyx", line 489, in sage.rings.polynomial.polynomial_element.Polynomial.__call__ (sage/rings/polynomial/polynomial_element.c:4775)
      File "element.pyx", line 1382, in sage.structure.element.RingElement.__mul__(sage/structure/element.c:9190)
      File "coerce.pyx", line 662, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6288)
    TypeError: unsupported operand parent(s) for '*': 'Rational Field' and 'Power Series Ring in t over Finite Field of size 7'
```


Here is the original docstring:

```
"""
EXAMPLES: 
    sage: from sage.structure.coerce_maps import NamedConvertMap
    sage: mor = NamedConvertMap(SR, QQ['t'], '_polynomial_')
    sage: mor(x^2/4+1)
    1/4*t^2 + 1
    sage: mor = NamedConvertMap(SR, GF(7)[This is the Trac macro *'t'* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#'t'-macro), '_polynomial_')
    sage: mor(x^2/4+1)
    1 + 2*t^2
"""
```



---

Comment by gfurnish created at 2008-08-15 19:35:08

Probably "Symbolic Polynomials alway use the same representation as the underlying object" should change if this is going to fly (also, this is hardly a justification of anything...).  << Symbolic polynomials now use the representation as determined by the coefficient and exponent functions.  Therefore while we can easily reverse it, it is pretty much determined by the underlying object.  If this is not to be the case, I strongly recommend putting it off past here as this is an unrelated issue (although the polynomial repr should go to devel as it relevant to both GiNaC and this patch).  

The doctest failure is known to be related to bug 3856 (if it is a bug or not depends on how exactly _polynomial_ should behave (So pending on figuring out how coercion specs this)).


---

Comment by rlm created at 2008-08-15 20:36:27

Resolution: invalid


---

Comment by rlm created at 2008-08-15 20:36:27

After some discussion with gfurnish, it is clear that there is no point in trying to merge this patch. Although there are some merits to this patch, the current situation with GiNaC would render it obsolete in short time, and thus it is not worth the effort. 

I should also (on record) apologize for my flame on this ticket. I was under time pressure and very impatient and I didn't mean it the way it came across.

For what it's worth, Maxima still sucks. :-)
