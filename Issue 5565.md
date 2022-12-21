# Issue 5565: sage crashes because of too small stacksize

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2009-03-19 13:25:00

Assignee: cwitty

it seems a stacksize of 10M is not enough to run Sage, at least under
Fedora 10 (I typed <tab> after Poly):

```
patate% limit stacksize 10m
patate% sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: Poly
| Sage Version 3.4, Release Date: 2009-03-11                         |
| Type notebook() for the GUI, and license() for information.        |
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

/usr/local/sage-3.4-core2/sage/local/bin/sage-sage: line 197:   816 Segmentation fault      sage-ipython "$`@`" -i
```

In addition there is a typo in the above error message, where
"occured" should be "occurred". Should I open a separate ticket
for that?


---

Comment by zimmerma created at 2009-03-19 14:43:59

Some additional comments from Emmanuel Thome:

(1) the problem was on a 64-bit machine, maybe it does not appear on 32-bit machines

(2) maybe this problem is difficult to track down. A sanity check at startup would help,
  and/or a hint about "stacksize" in the error message, to avoid other people spend some time
  on this issue.


---

Comment by mabshoff created at 2009-03-26 00:34:52

Mhh, odd. On a 64 bit Ubuntu machine (sage.math) with Sage 3.4 even a 4MB stack works. What kind of shell is involved here? It seems to be either a csh or a tcsh.

Cheers,

Michael


---

Comment by zimmerma created at 2009-03-26 07:41:11

> It seems to be either a csh or a tcsh. 

No, both Pierrick Gaudry and Emmanuel Thome had the problem with bash (I'm the only dinosaur in the
group still using tcsh).


---

Comment by zimmerma created at 2010-02-05 20:17:11

Resolution: worksforme


---

Comment by zimmerma created at 2010-02-05 20:17:11

It seems that problem has gone away with Sage 4.3.1.


---

Comment by mvngu created at 2010-02-05 21:11:50

Make sure you understand the procedure for closing tickets. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for more information.


---

Comment by zimmerma created at 2010-02-07 21:09:20

sorry again!
