# Issue 4015: [with patch, needs review] add docs to tests/benchmark.py

Issue created by migration from https://trac.sagemath.org/ticket/4015

Original creator: rlm

Original creation time: 2008-08-31 06:49:01

Assignee: mabshoff




---

Attachment

Nice work. Positive review. I guess eventually the code should be extended, but as is at least the code is being doctested :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-31 07:34:27

Resolution: fixed


---

Comment by mabshoff created at 2008-08-31 07:34:27

Merged in Sage 3.1.2.alpha3


---

Attachment

Note that in the second patch, calling the string representation of these functions also actually runs the test code.


---

Comment by mabshoff created at 2008-08-31 07:51:53

The second patch looks good to me. Positive review. It seems that some of the optional MMA doctests are broken, but we will deal with that on a follow up ticket.

Cheers,

Michael
