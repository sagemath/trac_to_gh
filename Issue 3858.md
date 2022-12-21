# Issue 3858: [with patch, needs review] 3.1alpha: fix issues with the reference manual

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2008-08-14 22:05:46

Assignee: tba

Keywords: documentation, reference

This may be premature (and if it is, feel free to ignore/dispose of this ticket), but when I tried to build the reference manual in 3.1alpha, there were a bunch of small errors -- things like `"""` instead of `r"""`, immediately followed by a docstring using backslashes.  This patch fixes these.




---

Attachment

Hi John,

thanks a lot for doing this. Usually we end up doing this at the last minute, so thanks again :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-15 09:45:40

Patch looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-15 09:45:53

Merged in Sage 3.1.rc0


---

Comment by mabshoff created at 2008-08-15 09:45:53

Resolution: fixed
