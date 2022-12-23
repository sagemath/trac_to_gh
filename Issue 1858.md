# Issue 1858: plot.py coverage is crap -- get it to 100%

Issue created by migration from https://trac.sagemath.org/ticket/1858

Original creator: was

Original creation time: 2008-01-20 00:33:52

Assignee: was

Right now:

```
$ sage -coverage plot.py
----------------------------------------------------------------------
plot.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE plot.py: 13% (25 of 185)
```




---

Comment by was created at 2008-01-20 01:29:45

Changing status from new to assigned.


---

Comment by was created at 2008-01-20 04:48:43

after:

```
teragon:plot was$ sage -coverage plot.py|more
----------------------------------------------------------------------
plot.py
SCORE plot.py: 35% (64 of 180)
```


It's a start at least.


---

Attachment


---

Comment by ncalexan created at 2008-01-20 21:41:30

The following docstring is probably wrong -- each entry is probably a float between 0 and 1, inclusive.


```
467	        INPUT: 
468	            c -- an rgb color 3-tuple, where each tuple entry is an 
469	                 integer between 0 and 1 
```


But I think this should be applied.


---

Comment by was created at 2008-01-20 21:44:22

fixes the typo nick pointed out


---

Attachment

Ok, since was fixed the issue this looks good to merge now.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-21 02:16:10

These two patches seem to depend on at least 1508 to be applied - maybe more.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-21 03:52:33

This patch also clashes with #1859, so I applied two hunks manually.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-21 03:52:51

Resolution: fixed


---

Comment by mabshoff created at 2008-01-21 03:52:51

Merged in Sage 2.10.1.alpha1
