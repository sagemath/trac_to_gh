# Issue 5907: [with patch; needs review] incorrect fast_float evaluation of constant polynomials

Issue created by migration from https://trac.sagemath.org/ticket/5907

Original creator: tornaria

Original creation time: 2009-04-27 01:10:19

Assignee: tornaria

Keywords: fast_float

A constant polynomial `a` is incorrectly `_fast_float_`- evaluated as `a*x`:

```
sage: R.<t> = QQ[]
sage: f = t + 2 - t
sage: ff = f._fast_float_()
sage: ff(3)
6.0
sage: list(ff)
['load 0', 'push 2.0', 'mul']
```



---

Comment by tornaria created at 2009-04-27 01:13:11

Fix fast_float evaluation of constant polynomials


---

Attachment


---

Attachment

Positive review for the original patch (code looks good, doctests pass).  Unfortunately _fast_callable_ copied the buggy code; seems like we might as well fix both bugs on the same ticket, so I've added a second patch to fix the _fast_callable_ bug.  (So this second patch needs review.)


---

Comment by mhansen created at 2009-05-19 05:04:15

Positive review for cwitty's change.


---

Comment by mabshoff created at 2009-05-19 19:08:19

Merged both patches in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 19:08:19

Resolution: fixed
