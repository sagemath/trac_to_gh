# Issue 59: optimize elliptic curve arithmetic

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-14 12:37:01

Assignee: somebody

William, my student noticed some slow performance with elliptic curves 
group law.  I think there was a huge overhead in duplication:
 
sage: E = EllipticCurve([GF(101)(1),3])
sage: P = E([-1,1,1])
sage: timeit 2*P
100 loops, best of 3: 3.81 ms per loop
sage: timeit P+P
1000 loops, best of 3: 1.81 ms per loop
 
Basically n*P was passing through all sorts of high-level layers for 
group schemes, abelian groups, and the like.
 
I've started teaching two courses here, and at the latest, will have to 
adapt to becoming a Dad next Tuesday (my wife Martine is overdue). But I 
may be able to add some code in the next three weeks.
 


---

Comment by was created at 2006-09-14 12:37:56

This was from David Kohel.  Here's a better formated version:

William, my student noticed some slow performance with elliptic curves 
group law.  I think there was a huge overhead in duplication:

``` 
sage: E = EllipticCurve([GF(101)(1),3])
sage: P = E([-1,1,1])
sage: timeit 2*P
100 loops, best of 3: 3.81 ms per loop
sage: timeit P+P
1000 loops, best of 3: 1.81 ms per loop
 }}}
Basically n*P was passing through all sorts of high-level layers for 
group schemes, abelian groups, and the like.


---

Comment by mabshoff created at 2007-08-22 19:46:52

I guess this has been fixed. With Sage 2.8.2 I get:

```
sage: E = EllipticCurve([GF(101)(1),3])
sage: P = E([-1,1,1])
sage: timeit 2*P
1000 loops, best of 3: 317 µs per loop
sage: timeit P+P
10000 loops, best of 3: 92.7 µs per loop
```

Cheers,

Michael


---

Comment by was created at 2007-08-23 05:44:55

Resolution: fixed


---

Comment by was created at 2007-08-23 05:44:55

Fixed by Robert bradshaw.


---

Comment by mabshoff created at 2007-08-24 06:55:39

Resolution changed from fixed to 


---

Comment by mabshoff created at 2007-08-24 06:55:39

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-08-24 06:55:39

Ok, reopened.

For details see http://groups.google.com/group/sage-devel/t/e884bb605728649a

To quote David Kohel:

```
I think the problem needs to be profiled.  The problem is likely NOT
in elliptic curves, but some
horrendous chain of calls to module operations before getting to the
(same) actual algorithms.
Note that P*2 is slightly faster since it calls directly the member
function of P rather than a
function on integers.

sage: E = EllipticCurve([GF(101)(1),3])
sage: P = E([-1,1,1])
sage: timeit 2*P
1000 loops, best of 3: 309 µs per loop
sage: timeit P+P
10000 loops, best of 3: 89.8 µs per loop
sage: timeit P*2
1000 loops, best of 3: 204 µs per loop

Yes, reopen it: these sorts of problems need to be looked at and
optimized.  The same problem
applies to points on Jacobians (compare 2*P, P*2, and P+P).

--David 
```



---

Comment by was created at 2007-08-29 02:05:01

Resolution: fixed


---

Comment by was created at 2007-08-29 02:05:01

As of SAGE-2.8.3 (probably due to Tom Boothby's work), this is now resolved:

```
sage: E = EllipticCurve([GF(101)(1),3])
sage: P = E([-1,1,1])
sage: import timeit
sage: t = timeit.Timer('2*P', 'from sage.all import EllipticCurve, GF; E = EllipticCurve([GF(101)(1),3]); P = E([-1,1,1])')
sage: t.timeit(10000)
1.0524919033050537
sage: s = timeit.Timer('P+P', 'from sage.all import EllipticCurve, GF; E = EllipticCurve([GF(101)(1),3]); P = E([-1,1,1])')
sage: s.timeit(10000)
1.067209005355835
```

