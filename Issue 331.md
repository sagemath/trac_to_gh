# Issue 331: compiled implementation of dense univariate polynomial arithmetic

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-03-22 14:55:28

Assignee: somebody

CC:  dmharvey@math.harvard.edu

SAGE needs a compiled, well-optimised implementation of dense univariate polynomial arithmetic over a *generic* commutative base ring.

The current implementation is the python class `Polynomial_generic_dense` in `sage/rings/polynomial_element.py`.

The new implementation would probably use a python list to store the coefficients (maybe a C array? I'm not sure...), and would have optimised code for at least the following:

 * addition, subtraction
 * multiplication: classical algorithm, also karatsuba (but this should be optional, since it doesn't work well over certain base rings, especially where numerical stability is an issue)
 * division, at least when the base ring is a field (or for monic divisors), using classical, divide-and-conquer, possibly newton's method
 * polynomial evaluation
 * retrieval of coefficients and conversion to/from python lists
 * comparison, hashing



---

Comment by dmharvey created at 2007-08-28 19:02:44

Some progress has been made on this: Robert Bradshaw moved the implementation of `Polynomial_generic_dense` into Cython (in `sage/rings/polynomial/polynomial_element.pyx`).

Related: I am planning to start work on an implementation of polynomials over Z that interfaces directly with NTL instead of going via the `ntl.pyx` objects, as soon as #411 is resolved.


---

Comment by dmharvey created at 2007-09-11 00:28:58

related: #528


---

Comment by mabshoff created at 2007-11-03 01:35:43

Can this be closed with the NTL wrapper rewrite? If not what need to be done?

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-12 17:59:40

What is the status of this?

Cheers,

Michael


---

Comment by robertwb created at 2008-09-23 19:36:06

I believe this is implemented in lines 4000+ of http://hg.sagemath.org/sage-main/file/a175cdbeb408/sage/rings/polynomial/polynomial_element.pyx


---

Comment by dmharvey created at 2008-09-23 20:18:33

Perhaps the title should be changed to "compiled implementation of asymptotically fast dense univariate polynomial arithmetic" :-)


---

Comment by robertwb created at 2008-09-23 20:25:22

We already have karatsuba, which leads to really bad bugs like


```
sage: R.<x> = RR[]
sage: (x+1e20)^2
1.00000000000000*x^2 + 1.00000000000000e40
```


for inexact rings. I don't think there's anything for division yet though.


---

Comment by dmharvey created at 2008-09-23 20:31:31

For multiplication, Karatubsa has complexity n<sup>1.58</sup> in the degree; there exist algorithms with complexity n log(n) log(log(n)) over arbitrary (associative unital) rings. I think it's worth implementing this at some point.

Yes, we need division too. And we need a framework to deal with the very nasty bug you mentioned above. Basically Karatsuba should be disallowed by default for such rings, I don't see any other way around it. Perhaps the user should be able to call some interface for multiplication which uses karatsuba/etc on polynomials when the user knows in advance that the data is "uniform" enough to make the asymptotically fast algorithm accurate enough.

I totally can't work on this right now.


---

Comment by mabshoff created at 2008-09-23 20:45:32

Well, since this ticket is somewhat vague and there exists some code which at least implements parts of what is wanted I am closing this as fixed. Please open other, more specific tickets for things you want to do in this area.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-23 20:45:32

Resolution: fixed
