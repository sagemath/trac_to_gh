# Issue 6029: [with patch, needs review] bug in floor() for python types

Issue created by migration from https://trac.sagemath.org/ticket/6029

Original creator: robertwb

Original creation time: 2009-05-12 10:15:40

Assignee: somebody

sage: floor(int(10^50))
100000000000000007629769841091887003294964970946560


---

Attachment

Some hunk failures:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 6029
sage: hg_sage.apply("/home/mvngu/patch/6029/6029-int-long-floor.patch")
cd "/scratch/mvngu/sage-3.4.2/devel/sage" && hg status
cd "/scratch/mvngu/sage-3.4.2/devel/sage" && hg status
cd "/scratch/mvngu/sage-3.4.2/devel/sage" && hg import   "/home/mvngu/patch/6029/6029-int-long-floor.patch"
applying /home/mvngu/patch/6029/6029-int-long-floor.patch
unable to find 'sage/functions/other.py' for patching
3 out of 3 hunks FAILED -- saving rejects to file sage/functions/other.py.rej
abort: patch failed to apply
```



---

Comment by robertwb created at 2009-05-13 03:52:03

This is to be applied on top of the pynac branch.


---

Comment by mhansen created at 2009-05-19 05:07:33

This is included in the patch at #5930.


---

Comment by mabshoff created at 2009-05-20 23:48:14

Resolution: fixed


---

Comment by mabshoff created at 2009-05-20 23:48:14

Merged in Sage 4.0.rc0.

Cheers,

Michael
