# Issue 2018: crap -- scipy sandbox has a bunch of .svn directories.  Delete them

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-31 23:29:23

Assignee: mabshoff


```
sage-2.10.1.rc3/spkg/standard/scipy_sandbox-20071020.p1/delaunay/.svn
sage-2.10.1.rc3/spkg/standard/scipy_sandbox-20071020.p1/delaunay/tests/.svn
sage-2.10.1.rc3/spkg/standard/scipy_sandbox-20071020.p1/arpack/tests/.svn
sage-2.10.1.rc3/spkg/standard/scipy_sandbox-20071020.p1/arpack/ARPACK/.svn
sage-2.10.1.rc3/spkg/standard/scipy_sandbox-20071020.p1/arpack/ARPACK/UTIL/.svn
sage-2.10.1.rc3/spkg/standard/scipy_sandbox-20071020.p1/arpack/ARPACK/SRC/.svn
sage-2.10.1.rc3/spkg/standard/scipy_sandbox-20071020.p1/arpack/ARPACK/LAPACK/.svn
```



---

Comment by mabshoff created at 2008-02-01 01:20:40

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-01 01:20:40

I created new spkgs with crap removed:

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc4/scipy-20071020-0.6.p3.spkg
http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc4/scipy_sandbox-20071020.p2.spkg

Both spkgs now have a proper mercurial repo.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-01 02:02:29

Merged in Sage 2.10.1.rc4


---

Comment by mabshoff created at 2008-02-01 02:02:29

Resolution: fixed
