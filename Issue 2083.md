# Issue 2083: [with patch, needs review] Make number_field .galois_closure require a name and .galois_conjugates take an explicit field.

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-02-07 08:57:01

Assignee: was

Keywords: number field galois closure names

`.galois_closure` used to guess a variable name, which is not very Sage-like.  This and a related issue with `.galois_conjugates` are fixed.


---

Attachment


---

Comment by mhansen created at 2008-02-07 10:16:18

Looks good to me.


---

Comment by mabshoff created at 2008-02-07 10:33:27

Resolution: fixed


---

Comment by mabshoff created at 2008-02-07 10:33:27

Merged in Sage 2.10.2.alpha0
