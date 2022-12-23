# Issue 205: prime_range cast problem

Issue created by migration from https://trac.sagemath.org/ticket/205

Original creator: was

Original creation time: 2007-01-22 20:12:39

Assignee: was


```
sage: [ p.is_prime() for p in prime_range(2**160, 2**160+2**12) ]
---------------------------------------------------------------------------
<type 'exceptions.OverflowError'>         Traceback (most recent call last)
 
/Users/nalexand/Devel/sage-alpha8/devel/sage-main/<ipython console> in <module>()
 
/Users/nalexand/Devel/sage/local/lib/python2.5/site-packages/sage/rings/arith.py in prime_range(start, stop, leave_pari)
    477     if stop is None:
    478         start, stop = 2, start
--> 479     v = pari.primes_up_to_n(stop-1)
    480     Z = sage.rings.integer.Integer
    481     if leave_pari:
 }}}


---

Comment by was created at 2007-01-23 23:38:11

fix (somewhat lame) for sage > 1.8


---

Comment by was created at 2007-01-23 23:38:11

Resolution: fixed
