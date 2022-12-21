# Issue 6166: [with patch, needs review] strip 'nodetex' from the reference manual

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-05-31 04:58:37

Assignee: jhpalmieri

CC:  rbeezer mhansen

The patch is supposed to remove 'nodetex' (and any other directives in the same line) from  the reference manual; these are already stripped from interactive docstrings by #6122.



---

Attachment


---

Comment by mhansen created at 2009-06-01 05:10:55

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-01 05:10:55

Changing assignee from jhpalmieri to mhansen.


---

Attachment

The original patch looks good except it doesn't handle the case when there is an empty docstring.  I've added a patch on top which fixes this.  John, can you review my small patch?


---

Comment by jhpalmieri created at 2009-06-01 05:16:59

Looks good to me.  (Although we just shouldn't allow empty docstrings in the first place :)


---

Comment by mhansen created at 2009-06-01 05:28:35

Resolution: fixed


---

Comment by mhansen created at 2009-06-01 05:28:35

I think docstringlines is an empty list if there is no docstring as well.

Merged in 4.0.1.alpha0.
