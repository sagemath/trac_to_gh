# Issue 7579: notebook -- autosave needs to save a snapshot

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-02 04:35:40

Assignee: was

CC:  chapoton


```
> On both sagenb.org and my personal notebook the revision history for
> any worksheet is blank. Is revision history no longer supported?

There is a bug. Thanks for the report!  A workaround is to *explicitly* click on the Save button -- that will  create a revision.  I should fix this.    However does this (likely me, as soon as Sage Days 18 is over I'll be done with everything and can focus totally on the notebook for the rest of the year), should also implement rolling backups (i.e., daily, weekly monthly only, i.e., smart deleting of old snapshots).  
```



---

Comment by kcrisman created at 2014-09-18 16:35:42

A related enough issue is upstream at https://github.com/sagemath/sagenb/issues/233


---

Comment by kcrisman created at 2014-09-18 16:35:57

See also #5459.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by dimpase created at 2020-08-25 09:31:06

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-08-29 10:10:21

Resolution: invalid
