# Issue 3085: [with patch, needs *really* easy review] identity matrix docs

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-05-02 22:08:38

Assignee: was

The docs for identity matrix contain a "\t", so the string should be a raw string so \t doesn't expand to a tab.


---

Attachment


---

Comment by jason created at 2008-05-02 22:09:49

Credit goes to Geoff Tims for reporting this.


---

Comment by jason created at 2008-05-02 22:13:00

uh, in the interest of full disclosure, I didn't doctest this, but I did sage -br and check the docs to make sure they look better.


---

Comment by mabshoff created at 2008-05-03 04:43:50

After looking at the patch I am convinced it will not harm anybody when we merge this in 3.0.1.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-03 13:34:55

Merged in Sage 3.0.1.final


---

Comment by mabshoff created at 2008-05-03 13:34:55

Resolution: fixed
