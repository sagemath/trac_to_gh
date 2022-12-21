# Issue 3780: [with patch, depends on #3324

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-08-06 16:28:22

Assignee: malb

Keywords: m4ri

add fast col_swap method for dense matrices over GF(2).


---

Attachment


---

Comment by rlm created at 2008-08-31 00:11:02

I haven't tested this, but it looks fine. If it works, apply.


---

Comment by rlm created at 2008-08-31 00:21:10

...other than the missing output from the last doctest! :-[


---

Comment by mabshoff created at 2008-08-31 00:34:32

Note that the doctests only pass with #3376 applied, where the missing output that rlm mentions above is actually added :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-31 00:53:39

Merged in Sage 3.1.2.alpha3


---

Comment by mabshoff created at 2008-08-31 00:53:39

Resolution: fixed


---

Comment by mabshoff created at 2008-08-31 03:55:40

Note that the patch attached to this ticket is a diff. I did commit it in Martin's name.

Cheers,

Michael
