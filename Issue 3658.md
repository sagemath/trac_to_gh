# Issue 3658: A PARI bug results in an unreliable prime_pi

Issue created by migration from Trac.

Original creator: fwclarke

Original creation time: 2008-07-15 20:50:50

Assignee: was


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.5, Release Date: 2008-07-11                       |
| Type notebook() for the GUI, and license() for information.        |
sage: [prime_pi(n) for n in [500508..500510]]
[41580, 45056, 41581]
sage: [prime_pi(n) for n in [500508..500510]]
[41580, 41581, 41581]
```


The problem lies with pari/gp:

```
sage: %gp

  --> Switching to GP/PARI interpreter <-- 

''
gp: for(n=500508, 500510, print(primepi(n)))

41580
45056
  *** primepi: not enough precomputed primes, need primelimit ~ 500510.
```



---

Comment by craigcitro created at 2009-01-23 14:21:18

Changing assignee from was to craigcitro.


---

Comment by craigcitro created at 2009-01-23 14:21:18

The attached patch fixes the issue. This was a strange case -- in some cases, Pari is more than happy to return an (incorrect!) answer when you call `primepi` with a number larger than the prime limit. This patch fixes this in a uniform way.


---

Comment by craigcitro created at 2009-01-23 14:21:18

Changing status from new to assigned.


---

Comment by boothby created at 2009-01-24 10:39:44

works for me


---

Comment by mabshoff created at 2009-01-24 16:24:35

On sage.math: oops:

```
sage -t -long "devel/sage/sage/libs/pari/gen.pyx"           
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/libs/pari/gen.pyx", line 7400:
    sage: pari._primelimit()
Expected:
    500000
Got:
    500519
**********************************************************************
```


Cheers,

Michael


---

Attachment


---

Comment by boothby created at 2009-01-24 20:00:15

+1


---

Comment by mabshoff created at 2009-01-24 23:00:49

Merged in Sage 3.3.alpha2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 23:00:49

Resolution: fixed
