# Issue 5286: python 2.5.4 breaks -sdist due to missing .hg repo in the sage-3.3.rc1.spkg (followup to #5218)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-16 16:03:38

Assignee: mabshoff

When merging the python-2.5.4.spkg from #5218 everything goes fine, but -sdist. In that case the .hg repo is copied into the tmp directory in spkg-dist, but it is not copied into the tar.gz created by distutils. Until this is resolved we cannot update to the latest python-2.5.4.spkg.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 02:25:15

Better luck in 3.4.1.

Cheers,

Michael


---

Comment by mhansen created at 2009-05-28 20:24:26

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2009-05-28 20:24:26

This is caused by http://bugs.python.org/issue1725737

There is a fix in the new spkg at #5218.


---

Comment by mhansen created at 2009-05-28 20:24:26

Changing status from new to assigned.


---

Comment by was created at 2009-05-29 13:38:32

Resolution: fixed
