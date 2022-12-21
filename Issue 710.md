# Issue 710: bad segfault when hitting control-c

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-20 18:13:04

Assignee: somebody

Try this:


```
sage: n=factor(2^997-1)
[hit control c]
---------------------------------------------------------------------------
<type 'exceptions.KeyboardInterrupt'>     Traceback (most recent call last)

sage: gp.eval('factor(2^997-1)')
[hit control c]
Segmentation fault (core dumped)
```



---

Comment by was created at 2007-09-21 05:46:08

This is now fixed for the next SAGE release by Stein and Tornaria.  The fixes involved fixing some
mistakes in gen.pyx a rewriting interrupt.c/h somewhat.


---

Comment by was created at 2007-09-21 05:46:08

Resolution: fixed
