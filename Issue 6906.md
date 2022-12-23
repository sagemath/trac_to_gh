# Issue 6906: [with spkg, needs review] update Mercurial to version 1.3.1

Issue created by migration from https://trac.sagemath.org/ticket/6906

Original creator: jhpalmieri

Original creation time: 2009-09-08 23:23:33

Assignee: jhpalmieri

As the summary says.  The spkg is here: [http://sage.math.washington.edu/home/palmieri/SPKG/mercurial-1.3.1.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/mercurial-1.3.1.p0.spkg).  Please test thoroughly.

This fixes the problem at #6440, by the way.



---

Comment by jason created at 2009-09-22 16:54:09

Last year, mabshoff did:

 * Disable inotify extenion since it is broken on Itanium

I noticed you don't use the setup.py patch anymore.  Does inotify work on Itanium now?

If patches/setup.py is not needed, then it needs to be deleted from the repository.


---

Comment by jhpalmieri created at 2009-09-22 18:14:57

Sorry about that.  I created the patch and then didn't copy setup.py.  The spkg-install file now includes a line

```
$CP patches/setup.py src/setup.py
```



---

Comment by mhansen created at 2009-10-05 18:42:14

Looks good to me.


---

Comment by mhansen created at 2009-10-15 09:44:22

Resolution: fixed
