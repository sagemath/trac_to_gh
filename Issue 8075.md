# Issue 8075: Enhance sage/eclib interface

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2010-01-26 09:26:57

Assignee: was

CC:  cremona

The sage/eclib interface is rather old and could be simplified and made more efficient, probably after a major change to eclib to remove the NTL/LiDIA duality which has never been used by Sage and is essentially dead.


---

Comment by chapoton created at 2013-10-24 08:05:44

Changing keywords from "" to "eclib".


---

Comment by chapoton created at 2015-03-16 20:31:14

Is this still of any actual pertinence ?


---

Comment by cremona created at 2015-03-16 21:56:04

Yes.  It would be nice to expose more of the modular symbol functionality of eclib to Sage, more than the minimal `CremonaModularSymbols()` which was done a long time ago:

```
sage: %time M = ModularSymbols(10001)
CPU times: user 6.42 s, sys: 196 ms, total: 6.62 s
Wall time: 6.61 s
sage: %time M = CremonaModularSymbols(10001)
CPU times: user 139 ms, sys: 3.87 ms, total: 143 ms
Wall time: 142 ms
```

There is no reason in principle for Sage not to be able to access all the functionality which is used to produce all the modular elliptic curves of conductor `N` for reasonable `N`.


---

Comment by cremona created at 2021-02-02 15:17:26

I am going to close this since the specific things mentioned were done long ago, though certainly there is more eclib functionality which could be exposed to Sage but is not.


---

Comment by cremona created at 2021-02-02 15:18:05

Changing status from new to needs_review.


---

Comment by cremona created at 2021-02-05 14:24:23

Changing priority from major to trivial.


---

Comment by chapoton created at 2021-02-05 14:58:15

Resolution: invalid


---

Comment by chapoton created at 2021-02-05 14:58:15

ok, John, as you wish
