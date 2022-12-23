# Issue 4444: Remove duplicate source names in setup.py

Issue created by migration from https://trac.sagemath.org/ticket/4444

Original creator: craigcitro

Original creation time: 2008-11-05 10:21:20

Assignee: craigcitro

In `setup.py`, there are several source files which appear in the `sources` list more than once. For instance, the entry for `sage.rings.rational` looks like:


```
Extension('sage.rings.rational',
           sources = ['sage/rings/rational.pyx',
                      'sage/ext/arith.pyx', \
                      'sage/rings/integer.pyx'],
           libraries=['ntl', 'gmp'])
```


The other two `.pyx` files that appear there were added in the old days, when Pyrex needed us to do this in order to compile `rational.pyx` correctly. Note that because of this, several files in the Sage library get compiled multiple times. (For instance, try changing `sage/ext/arith.pyx` and doing a `sage -br`.) We should fix this.

I've already made the changes to `setup.py`, but I really need to do a `sage -ba` to feel like I've appropriately tested this. I'll do that tomorrow. I'm going to make this ticket dependent on #4443, since I already fixed the situation for `sage/ext/arith.pyx` while working on that ticket.


---

Comment by mabshoff created at 2008-11-05 13:02:39

trac-4443.patch already contains some fixes to setup.py - are the more coming?

Cheers,

Michael


---

Comment by craigcitro created at 2008-11-05 16:36:06

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-11-05 16:36:06

Yep, more coming.


---

Comment by mabshoff created at 2008-11-10 08:56:37

This has been taken care off via #4480. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-10 08:56:37

Resolution: fixed
