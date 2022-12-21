# Issue 8545: \opi -> \overline\pi in coxter_groups.py

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2010-03-15 21:02:37

Assignee: mvngu

CC:  sage-combinat

The docstring to apply_simple_projection method of CoxeterGroups
contains `\opi` which is not a valid latex symbol.

As a consequence the pdf version of the reference manual does
not build cleanly. Thus 

`sage -docbuild reference pdf`

eventually halts with the line:


```
! Undefined control sequence.
<recently read> \opi 
                     
l.185462 projection $\pi_i$ (resp. $\opi
                                        _i$) on self.
```


Evidently ``\opi`` is supposed to be ``\overline\pi``, as elsewhere in the file around line 379 in coxeter_groups.py.


---

Attachment


---

Comment by jhpalmieri created at 2010-03-15 21:32:26

I think this is fixed in #8492 (which I tried to cc you on).


---

Comment by bump created at 2010-03-15 22:32:25

Resolution: duplicate


---

Comment by bump created at 2010-03-15 22:32:25

For some reason cc: bump does not cause me to be copied.
