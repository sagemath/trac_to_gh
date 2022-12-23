# Issue 9357: Unhandled SIGFPE: in number_field_element_quadratic

Issue created by migration from https://trac.sagemath.org/ticket/9357

Original creator: lftabera

Original creation time: 2010-06-28 16:18:05

Assignee: AlexGhitza

Keywords: SIGFPE, ZeroDivisionError


```
sage: d=QQ[i](0)
sage: ~d


------------------------------------------------------------
Unhandled SIGFPE: An unhandled floating point exception occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------

```


The code dos not check if the element to be inverted is zero or not and does not handle the exception that ocurred in the c extension.

There is a trivial patch that checks if the input is zero or not. I am not sure if the sourronding code should have some _sig_on _sig_off to made it more robust. _sig_on _sig_off would avoid the sage crash but would raise a RunTime exception.


---

Attachment


---

Comment by robertwb created at 2010-06-30 07:28:16

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-06-30 07:28:23

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 09:31:02

Resolution: fixed
