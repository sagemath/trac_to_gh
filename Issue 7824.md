# Issue 7824: cliquer-1.2.p2 - add FreeBSD support

Issue created by migration from Trac.

Original creator: pjeremy

Original creation time: 2010-01-03 02:10:25

Assignee: pjeremy

CC:  nathann.cohen@gmail.com

cliquer aborts with the error

```
Cannot determine your platform or it is not supported... exiting
```

unless the platform is explicitly listed as supported.  This patch adds FreeBSD support - which is the same as Linux.


---

Attachment


---

Comment by pjeremy created at 2010-01-03 02:17:31

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-12 17:44:07

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-12 17:44:07

I can't check it, not having FreeBSD installed, but it is clearly 100% safe as it only affects FreeBSD.


---

Comment by mvngu created at 2010-01-24 14:38:15

Resolution: fixed


---

Comment by mvngu created at 2010-01-24 14:38:15

An updated spkg is available at

http://sage.math.washington.edu/home/mvngu/spkg/standard/cliquer/cliquer-1.2.p3.spkg

All changes are committed in pjeremy's name.
