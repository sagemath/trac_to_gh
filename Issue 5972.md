# Issue 5972: [with patch; needs review] segfault in degenerate matrix multiply

Issue created by migration from https://trac.sagemath.org/ticket/5972

Original creator: was

Original creation time: 2009-05-04 03:45:14

Assignee: was

OUCH:


```
wstein@sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
matrix(QQ,2,0)sage: matrix(QQ,2,0)*matrix(QQ,0,2)
| Sage Version 3.4.1, Release Date: 2009-04-21                       |
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



---

Attachment

William's patch rebased


---

Comment by mabshoff created at 2009-05-04 04:05:26

Nice catch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-04 04:19:00

Resolution: fixed


---

Comment by mabshoff created at 2009-05-04 04:19:00

Merged in Sage 3.4.2.final.

Cheers,

Michael


---

Comment by was created at 2009-05-04 13:45:57

the rebased patch michael posted doesn't work for me on 3.4.2.rc0, but this patch does, so I'm posting it.
