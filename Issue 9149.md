# Issue 9149: spelling error (trivial to fix)

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-06-05 12:02:01

Assignee: GeorgSWeber

The following message has a spelling error: `occured` should be
`occurred`:

```
Unhandled SIGFPE: An unhandled floating point exception occured in Sage.
This probably occured because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
```



---

Attachment


---

Comment by zimmerma created at 2010-06-05 12:27:01

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-06-05 12:27:01

The attached patch fixes that spelling error. (Note there are other similar errors in the source
files, but that one is directly visible to the user.)


---

Comment by mvngu created at 2010-06-05 15:21:41

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-06-05 15:21:41

Thanks for this.


---

Comment by mhansen created at 2010-06-06 01:25:00

Resolution: fixed
