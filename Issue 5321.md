# Issue 5321: [with patch, needs review] follow up to #5287

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-02-20 11:51:37

Assignee: malb

CC:  was

The attached patch addresses some outstanding referee remarks from #5287.


---

Comment by mabshoff created at 2009-03-20 20:56:01

This seems to conflict with either #5493 or #5527. Please rebase post 3.4.1.alpha0.

Cheers,

Michael


---

Comment by malb created at 2009-05-12 02:00:22

Rebased to 3.4.2 + #5586


---

Comment by burcin created at 2009-06-04 19:49:07

AFAICS, this already had a positive review from was and only needed to be rebased. In any case, the patch looks good to me and it applies cleanly to 4.0. Positive review once again.


---

Attachment

The updated patch _only_ changes ` \var{foo} ` to ` ``foo`` `.


---

Comment by ncalexan created at 2009-06-13 19:35:55

Resolution: fixed
