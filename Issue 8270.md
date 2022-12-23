# Issue 8270: 'make check' on exits with 0 on a failure.

Issue created by migration from https://trac.sagemath.org/ticket/8270

Original creator: drkirkby

Original creation time: 2010-02-15 10:23:56

Assignee: GeorgSWeber

The iconv package, which will soon be added to sage (#8191) has the facility to run 

```
make check
```


However, despite getting a test failure on Solaris 10 (SPARC), the makefile is still exiting with an exit code of 0, so any scripts which rely on testing iconv by relying on a failure of 'make check' to exit properly with a non-zero exit code will not work as desired. 

I'll report this to the iconv developers. 




---

Attachment

The file spkg/install  The iconv package is added.


---

Attachment

Diff between the old spkg/install and the updated spkg/install for iconv support


---

Comment by drkirkby created at 2010-02-15 11:47:49

spkg/standard/deps to show packages which depend on iconv.


---

Attachment

Diff between the old spkg/standard/deps and the new one with iconv


---

Attachment

Ignore all these file - they were attached to the wrong ticket!! 
Sorry about that.


---

Comment by drkirkby created at 2010-02-16 23:30:14

Resolution: invalid


---

Comment by drkirkby created at 2010-02-16 23:30:14

I'm told by the iconv developers this is not a bug. The core dumps are expected and ignored.
