# Issue 624: Inplace operators

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-09-07 19:44:53

Assignee: somebody

Despite the potential speed increase (I've implemented some and it  
can be considerable), SAGE has avoided almost all use of inplace  
operators due to the fact that elements are supposed to be immutable,  
despite the fact that one does not really need the "old" result  
anymore. For example, if I type x^5 - 3*x + 1, the subexpressions  
(x^5), (3*x), and (x^5-3*x) are all created and then discarded. This  
also shows up in places like the operation sum() which doesn't return  
any of its intermediate results, or loops that increment variables in  
certain ways. The worry is that perhaps somewhere something else is  
holding onto a given variable, and we don't want to mess it up.

Just the other day, I realized that Python provides the perfect  
solution--by looking at the reference count of an object we can  
detect whether or not its safe to mutate it (i.e. nothing else is  
holding onto it but the current call). If it is safe to mutate, then  
do so, otherwise create and return a new object. I propose adding  
_iadd_c, _imul_c, etc. to the coercion hierarchy such that the  
default __iadd__/__add__ detects whether or not inplace operations  
are safe and calls the respective operation accordingly. One would  
have bold comments on functions that are not safe to call directly.

The only caveat is that it might make it a tiny bit slower for types  
that do not define inplace operations, and it would take a slight  
(SAGE-specific and optional) tweak to Cython (specifically Cython  
local function variables have a refcount one less than expected due  
to their not being in any kind of a python "scope" container, so we  
would need an extra incref/decref them when performing arithmetic on  
them).


---

Comment by robertwb created at 2007-09-07 19:44:58

Changing assignee from somebody to robertwb.


---

Comment by robertwb created at 2007-09-07 19:44:58

Changing status from new to assigned.


---

Comment by robertwb created at 2007-09-12 04:09:17

This has been implemented (along with various other coercion optimizations and cleanup). Patch at http://sage.math.washington.edu/home/robertwb/coerce/ with all doctests passing. The new cython spkg in that folder MUST be installed as well, with a sage -ba. 

Inplace operations only defined for ZZ, QQ, RDF, and a couple of others (a bit in laurent/power series, generic polynomials)

Download and try it out.


---

Comment by robertwb created at 2007-09-13 18:58:02

Without inplace operators:

```
sage: A = [Integer(n) for n in range(10^6)]
sage: %time
sage: time sum(A)
499999500000
CPU time: 0.26 s,  Wall time: 0.26 s

sage: E = EllipticCurve('37a').change_ring(GF(5^6, 'a'))
sage: P = E(0,0)
sage: %time
sage: for i in range(1000):
...       Q = i*P
CPU time: 1.46 s,  Wall time: 1.46 s

sage: %cython
sage: def get_address(o):
...       return <Py_ssize_t>o
sage: a = 20
sage: get_address(a)
278949184
sage: a += 10
sage: get_address(a)
190804384
sage: b = a
sage: a += 10
sage: get_address(a)
278947360
sage: del b
sage: a += 10
sage: get_address(a)
278949184
```



---

Comment by robertwb created at 2007-09-13 19:01:48

With inplace operators: 


```
sage: A = [Integer(n) for n in range(10^6)]
sage: %time
sage: sum(A)    # Note: I did not edit the sum function at all, just __add__
499999500000
CPU time: 0.11 s,  Wall time: 0.12 s

sage: E = EllipticCurve('37a').change_ring(GF(5^6, 'a'))
sage: P = E(0,0)
sage: %time
sage: for i in range(1000):
...       Q = i*P
CPU time: 0.28 s,  Wall time: 0.29 s

sage: %cython
sage: def get_address(o):
...       return <Py_ssize_t>o
sage: a = 20
sage: get_address(a)
343719648
sage: a += 10
sage: get_address(a)  # same as above => mutated
343719648
sage: b = a
sage: a += 10
sage: get_address(a)  # not mutated because we can still access the integer via b
343719584
sage: b = a
sage: del b
sage: a += 10
sage: get_address(a)  # after b is gone, it is safe to mutate
343719584
```



---

Comment by robertwb created at 2007-09-13 19:10:09

Another example without


```
sage: R.<t> = ZZ[]
sage: S.<x> = LaurentSeriesRing(R)
sage: type(x)
<type 'sage.rings.laurent_series_ring_element.LaurentSeries'>
sage: %time
sage: for _ in range(1000):
...       f = x^3 - t*x^2 + x
CPU time: 1.42 s,  Wall time: 1.43 s
```


and with


```
sage: R.<t> = ZZ[]
sage: S.<x> = LaurentSeriesRing(R)
sage: type(x)
<type 'sage.rings.laurent_series_ring_element.LaurentSeries'>
sage: %time
sage: for _ in range(1000):
...       f = x^3 - t*x^2 + x
CPU time: 0.88 s,  Wall time: 0.88 s
```



---

Comment by mabshoff created at 2007-10-19 18:53:16

I believe this ticket can be closed because it seems to be included in the new coerce framework which has been merged.

Cheers,

Michael


---

Comment by was created at 2007-10-21 02:25:46

Resolution: fixed
