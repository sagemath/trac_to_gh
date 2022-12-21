# Issue 8337: factorization of multivariate polynomials is terribly slow

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-02-23 18:18:55

Assignee: malb

From http://groups.google.com/group/sage-support/browse_thread/thread/72fbc6d6f5a7d746#, with sage 4.3.3:

```
sage: var('E1, E2, E4, E5, E10, E20'); 
sage: var( 'q' ); 
sage: t=(E20^16*E5^8*q^4*E2^24 + (-E20^16*E5^8*q^4*E4^8*E1^16 + (-E10^24 + E20^8*E5^16)*E4^16*E1^8)) 
sage: factor(t)
```

does not answer in reasonable time (a few seconds).

Maple 13 answers in less than a second (and says the polynomial
is irreducible).


---

Comment by zimmerma created at 2013-08-23 15:02:06

Changing status from new to needs_info.


---

Comment by zimmerma created at 2013-08-23 15:02:06

seems to be fixed in Sage 5.11:

```
sage: %time factor(t)
CPU times: user 0.05 s, sys: 0.00 s, total: 0.05 s
Wall time: 0.09 s
E2^24*E20^16*E5^8*q^4 - E1^16*E20^16*E4^8*E5^8*q^4 - E1^8*E10^24*E4^16 + E1^8*E20^8*E4^16*E5^16
```

Should I add a doctest for that? If yes, how to check the computation is fast enough?

Paul


---

Comment by jdemeyer created at 2013-08-24 08:01:49

Changing component from commutative algebra to performance.


---

Comment by jdemeyer created at 2013-08-24 08:01:49

There currently isn't really a way in Sage to test timings. There has been a lot of thought about this, but it's hard to do right.

So the most reasonable thing to do is to close this ticket.


---

Comment by jdemeyer created at 2013-08-24 08:01:49

Changing status from needs_info to positive_review.


---

Comment by zimmerma created at 2013-08-24 08:09:21

> So the most reasonable thing to do is to close this ticket. 

ok, fine to me.

Paul


---

Comment by jdemeyer created at 2013-08-30 08:43:54

Resolution: worksforme
