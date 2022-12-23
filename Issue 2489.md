# Issue 2489: symmetric crashes when giving a skew partition to kostka_tab

Issue created by migration from https://trac.sagemath.org/ticket/2489

Original creator: mhansen

Original creation time: 2008-03-12 11:01:42

Assignee: mhansen

CC:  sage-combinat


```

symmetrica.kostka_tab([[2,2],[1]],[2,1])

evaluating this expression leads to the error message:

Exception exceptions.TypeError: 'an integer is required' in
'sage.libs.symmetrica.symmetrica._op_integer' ignored
Exception exceptions.TypeError: 'an integer is required' in
'sage.libs.symmetrica.symmetrica._op_integer' ignored
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

Comment by mhansen created at 2008-03-12 11:20:21

Changing status from new to assigned.


---

Attachment


---

Comment by saliola created at 2008-03-14 19:32:05

Successfully installs, no more error, code looks good.


---

Attachment


---

Comment by mabshoff created at 2008-03-14 20:34:30

Resolution: fixed


---

Comment by mabshoff created at 2008-03-14 20:34:30

Merged in Sage 2.10.4.alpha0
