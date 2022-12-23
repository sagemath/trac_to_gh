# Issue 4006: [with patch, needs review] Remove unused code in sage/libs/pari/functional.py

Issue created by migration from https://trac.sagemath.org/ticket/4006

Original creator: mhansen

Original creation time: 2008-08-30 19:05:49

Assignee: was




---

Attachment

This code is totally broken due to the imports at the top.  Plus, it's old, untested, and a bit crufty.


---

Comment by mabshoff created at 2008-08-30 22:24:53

Replying to [comment:1 mhansen]:
> This code is totally broken due to the imports at the top.  Plus, it's old, untested, and a bit crufty.

+1. Should anybody want this code he/she has to resubmit it. It has been broken since at least Sage 0.10.12, so good riddance. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-30 22:46:20

Resolution: fixed


---

Comment by mabshoff created at 2008-08-30 22:46:20

Merged in Sage 3.1.2.alpha3
