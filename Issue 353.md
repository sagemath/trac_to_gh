# Issue 353: public sage notebook robustness

Issue created by migration from https://trac.sagemath.org/ticket/353

Original creator: was

Original creation time: 2007-04-20 15:05:22

Assignee: boothby

Thanks.  It turns out that the chroot jail that runs the notebooks
ran out of disk space.  I've cleared off some files and now it works
again.  Interestingly, there are over 4000 worksheets at sagenb.org
and an additional over 4000 worksheets at sagenb.com.  Some are
weird things like index_asp.

We should make creating a new worksheet require clicking a button
or something in addition to just typing in a new url.  Also, there should
be an easy way to dele


---

Comment by was created at 2007-04-20 15:05:34

Changing assignee from boothby to was.


---

Comment by mabshoff created at 2008-03-18 10:15:35

Resolution: invalid
