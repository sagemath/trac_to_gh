# Issue 310: Debian testing version of mercurial refers to plugin not included in SAGE mercurial

Issue created by migration from https://trac.sagemath.org/ticket/310

Original creator: cwitty

Original creation time: 2007-03-06 06:18:40

Assignee: was

Keywords: mercurial

At least the latest version of mercurial from Debian testing (version 0.9.3-2), and possibly earlier versions as well, have a line in /etc/mercurial/hgrc.d/hgext.rc that tries to load the extension hgext/churn.  Since SAGE mercurial does not include this extension, every mercurial operation gives the following warning:

```
*** failed to import extension hgext/churn: No module named hgext/churn
```

(However, mercurial seems to work fine even with the warning.)

Perhaps SAGE's mercurial should ignore /etc/mercurial, or perhaps SAGE's mercurial should be updated to include the churn extension.

Or, of course, Debian users can remove the line from hgext.rc, or just ignore the warning message.


---

Comment by mabshoff created at 2007-09-10 03:32:57

We should discuss and decide what to do about this.

Cheers,

Michael


---

Comment by cwitty created at 2007-10-21 01:51:58

I've put up a new mercurial spkg that fixes this problem (by ignoring /etc/mercurial), and also upgrades to mercurial 0.9.5:
http://sage.math.washington.edu/home/cwitty/mercurial-0.9.5.spkg


---

Comment by malb created at 2007-10-23 17:42:36

I put the spkg linked in by cwitty in 2.8.9.alpha0.


---

Comment by malb created at 2007-10-23 17:42:36

Resolution: fixed
