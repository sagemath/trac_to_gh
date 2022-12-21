# Issue 4777: Sage is_prime_power is seriously buggy, because pari's ispower is BROKEN

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-13 02:31:36

Assignee: somebody


```
18:18 < wstein> sage: n = 
3089265681159475043336839581081873360674602365963130114355701114591322241990483812812582393906477998611814245513881
18:18 < wstein> sage: factor(n)
18:18 < wstein> 150607571^14
18:18 < wstein> sage: sage.rings.arith.is_prime_power(n)False
18:18 < wstein> sage: n.is_prime_power()
18:18 < wstein> False
18:18 < wstein> sage: is_prime(150607571)
18:18 < wstein> True
18:19 < wstein> Yep, Sage's is_prime_power function is just plain wrong.
18:19 < wstein> Great.
18:19 < wstein> I wrote that, I think... :-(
18:20 < wstein> sage: k = pari(n); k.ispower()
18:20 < wstein> (2, 1757630701017558763141032341047742794506161527817537960891)
18:20 < wstein> Oh, it's a bug in pari, actually.
18:20 < wstein> Since pari's ispower is guaranteed to give the maximal k such that x=n^k according
18:20 < wstein> to the docs.
18:20 < wstein> But it doesn't.
```


Pari's docs say this:

```
    ispower(x,{k},{&n}): true (1) if x is a k-th power, false (0) if not. If n is 
    given and a k-th root was computed in the process, put that in n. If k is 
    omitted, return the maximal k >= 2 such that x = n^k is a perfect power, or 0 
    if no such k exist.
```


So this is a bug in pari.  The short-term solution is to I think just factor that damned number at the end.  This obviously could be slow in general, but at least it will be right.  Plus add a note to the docs and post a bugreport upstream (but check latest svn pari first, since we use an ancient pari).  I've reported bugs in this ispower function in pari before, by the way, so it's a known offender. 


---

Comment by was created at 2008-12-13 02:34:36

BEFORE patch:

```
teragon-2:~ wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: n = 150607571^14
sage: n.is_prime_power()
False
```

| Sage Version 3.2.1, Release Date: 2008-12-01                       |
| Type notebook() for the GUI, and license() for information.        |
AFTER patch:

```
sage: n = 150607571^14
sage: n.is_prime_power()
True
```


And I'm making this a blocker, since it is a situation where one can silently get very wrong answers.


---

Attachment


---

Comment by jhpalmieri created at 2008-12-13 04:46:22

In the line `See trac #4777`, you should put a backslash before the #.


---

Comment by craigcitro created at 2008-12-13 09:31:18

Patch looks good, except for the missing backslash noted by John Palmieri above. Beyond that, we just need to make sure that someone makes a note to test this in pari 2.4.2, and send a bug report upstream if it's really broken ...


---

Comment by mabshoff created at 2008-12-13 09:38:31

I am taking care of the problem pointed out by John.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-13 10:22:17

Merged in Sage 3.2.2.alpha2


---

Comment by mabshoff created at 2008-12-13 10:22:17

Resolution: fixed
