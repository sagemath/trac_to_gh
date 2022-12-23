# Issue 6487: Plethysm with the zero symmetric function causes a segfault

Issue created by migration from https://trac.sagemath.org/ticket/6487

Original creator: saliola

Original creation time: 2009-07-08 19:17:28

Assignee: mhansen

CC:  mhansen


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage:
sage: sage: s = SFASchur(QQ)
sage: sage: s([2]).plethysm(s.zero_element())
sage.bin:
| Sage Version 4.1.rc1, Release Date: 2009-07-07                     |
| Type notebook() for the GUI, and license() for information.        |
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

This problem also exists with sage-4.0.2.


---

Comment by jbandlow created at 2010-05-06 15:43:33

This appears to be fixed in sage-4.4.

```
sage: sage: sage: s = SFASchur(QQ)
sage: sage: sage: s([2]).plethysm(s.zero_element())
0
```



---

Comment by mhansen created at 2010-05-06 16:02:48

I'll mark this as invalid then.


---

Comment by mhansen created at 2010-05-06 16:02:48

Resolution: invalid
