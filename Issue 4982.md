# Issue 4982: consolidate shifts in polynomial_template

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-01-15 19:57:37

Assignee: tbd

CC:  malb burcin

See discussion at end of #4965. 


---

Comment by AlexGhitza created at 2009-01-22 18:29:08

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2009-02-06 22:59:31

3.4 is for ReST tickets only.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-11-16 05:34:42

The point was to consolidate the three shift methods `shift`, `__lshift__`, and `__rshift__` by having `shift` do all the work and the other two call it.  (Right now there's significant code triplication going on.)

The attached patch does this.


---

Comment by AlexGhitza created at 2009-11-16 05:34:42

Changing status from new to needs_review.


---

Attachment

I'm ccing the participants in the discussion at #4965 in case they had something else in mind.


---

Comment by malb created at 2009-11-16 12:03:12

The only issue I can see is the potential performance overhead.

Vanilla 4.2.1:


```
sage: P.<x> = GF(2)[]
sage: f = P.random_element(50)
sage: %timeit f<<50
1000000 loops, best of 3: 792 ns per loop
```


This patch:


```
sage: P.<x> = GF(2)[]
sage: f = P.random_element(50)
sage: %timeit f<<50
1000000 loops, best of 3: 952 ns per loop
```


Maybe a cdef method could be added which everyone (`shift`, `__lshift__`, `__rshift__`) calls?


---

Comment by malb created at 2009-11-16 13:31:33

Doctests pass btw., applies cleanly etc.


---

Attachment

Alex and I were discussing this off-list. The speedup patch does the following:

 * added a new C function which all methods call now 
 * I inlined it
 * and I changed the code to avoid some initialisation

Here is what I got:

*Vanilla:*

```
sage: P.<x> = GF(2)[]
sage: f = P.random_element(50)
sage: %timeit f<<50
1000000 loops, best of 3: 730 ns per loop
```


*Patch:*

```
sage: P.<x> = GF(2)[]
sage: f = P.random_element(50)
sage: %timeit f<<50
1000000 loops, best of 3: 1.06 µs per loop
```


*Patch + Speed-up:*

```
sage: P.<x> = GF(2)[]
sage: %timeit f<<50
1000000 loops, best of 3: 761 ns per loop
```


So there is still some overhead, but I think its acceptable.


---

Comment by AlexGhitza created at 2009-11-22 22:50:14

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2009-11-22 22:50:14

So I believe that Martin gave a positive review to my patch, except for the performance issue.

I have read and tested his patch, and I'm happy with it.


---

Comment by mhansen created at 2009-11-29 04:44:16

Resolution: fixed
