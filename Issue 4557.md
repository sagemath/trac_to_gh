# Issue 4557: cos._fast_float_ returns math.sin

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-11-19 22:22:36

Assignee: burcin

This is pretty embarrassing.  Apparently a copy-paste error.


---

Comment by jason created at 2008-11-19 22:27:34

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-11-19 22:28:12

Oops. This patch will make it into 3.2.final.

Cheers,

Michael


---

Attachment

added doctests.


---

Comment by mabshoff created at 2008-11-19 22:35:34

Thanks for the doctests. I guess having some coverage tool of the code itself could be useful in the long term.

Cheers,

Michael


---

Comment by was created at 2008-11-20 01:56:18

See #4561 for speed issues.


---

Comment by mabshoff created at 2008-11-20 09:35:35

Resolution: fixed


---

Comment by mabshoff created at 2008-11-20 09:35:35

Merged in Sage 3.2.final
