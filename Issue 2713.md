# Issue 2713: [with patch, needs review] sage-doctest applies backslash handling to expected outputs

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-03-29 01:02:51

Assignee: failure

sage-doctest applies "backslash handling" to doctests, where a line that ends with a single backslash is merged with the next line (with the backslash removed).  As far as I can tell, this makes it impossible to doctest something with an expected output having a line ending with a backslash.

This patch to the "hg_scripts" repository removes the behavior for expected outputs (but keeps backslash handling for inputs; that is, for lines beginning "sage:").  There was one doctest in Sage that depended on the previous behavior; the second patch modifies that doctest to pass with the new sage-doctest.


---

Attachment


---

Attachment


---

Comment by mhansen created at 2008-04-04 20:25:06

Looks good to me.


---

Comment by mabshoff created at 2008-04-04 21:54:07

Merged in Sage 3.0.alpha1


---

Comment by mabshoff created at 2008-04-04 21:54:07

Resolution: fixed
