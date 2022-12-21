# Issue 7285: remove hgmerge from list of installed scripts

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-25 03:47:15

Assignee: tbd

Mercurial no longer has an hgmerge script.  This if one does 

```
sage: install_scripts('/usr/local/bin/')
```

with sage right now then very bad things happen.  For starters, you get an hgmerge script that hangs, which means any time any file ever gets merged with mercurial, instead of getting a merge option, you get a hang.  Pretty confusing. 


---

Attachment


---

Comment by was created at 2009-10-25 03:52:13

Changing status from new to needs_review.


---

Comment by was created at 2009-10-25 03:52:13

Changing component from algebra to misc.


---

Comment by mhansen created at 2009-11-04 14:50:02

Looks good to me.


---

Comment by mhansen created at 2009-11-04 14:50:02

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-06 04:11:07

Resolution: fixed
