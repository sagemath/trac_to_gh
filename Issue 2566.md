# Issue 2566: [with patch, needs review] fix type of "size" in graph_isom and binary_code

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-03-17 06:39:38

Assignee: rlm

Because, after all, 14! > 2<sup>32</sup> and 21! > 2<sup>64</sup>.

This also makes the codewords in `binary_code.pyx` unsigned, because of those pesky signed integer shifting issues...


---

Attachment


---

Comment by mhansen created at 2008-03-19 23:56:13

Applies and passes tests.  Looks good to me.


---

Comment by mabshoff created at 2008-03-20 00:58:07

Resolution: fixed


---

Comment by mabshoff created at 2008-03-20 00:58:07

Merged in Sage 2.11.alpha0
