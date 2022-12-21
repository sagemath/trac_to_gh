# Issue 5495: type: "A mysterious error (perphaps a memory error?)"   *PERP*HAPS!!!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-12 02:38:25

Assignee: cwitty

There is a typo in the error message below (not a "perp"haps):


```
wstein`@`debian32:/space/wstein/farm/sage-3.4/devel/sage/sage/matrix$ sage -t matrix2.pyx
sage -t  "devel/sage-main/sage/matrix/matrix2.pyx"          
*** glibc detected *** double free or corruption (fasttop): 0x0a41a380 ***
A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
	 [2.4 s]
```



---

Comment by jhpalmieri created at 2009-03-22 22:11:19

Trivial patch.


---

Comment by jhpalmieri created at 2009-03-22 22:11:19

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-03-22 22:11:19

Changing assignee from cwitty to jhpalmieri.


---

Attachment


---

Comment by mvngu created at 2009-03-24 08:24:46

The patch *5495.patch* fails to apply at all against Sage 3.4:

```
sage: hg_sage.apply("/home/mvngu/patch/5495/5495.patch")
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg import   "/home/mvngu/patch/5495/5495.patch"
applying /home/mvngu/patch/5495/5495.patch
unable to find 'sage-doctest' for patching
1 out of 1 hunks FAILED -- saving rejects to file sage-doctest.rej
abort: patch failed to apply
```



---

Comment by jhpalmieri created at 2009-03-24 15:19:38

Try using "hg_scripts" instead of "hg_sage".


---

Comment by mvngu created at 2009-03-26 07:23:09

Replying to [comment:4 jhpalmieri]:
> Try using "hg_scripts" instead of "hg_sage".


Yep, it now applies OK against Sage 3.4. Looks good, and I doctested `sage/matrix/matrix2.pyx` hoping to get a similar error as reported above. But no "mysterious error" popped up. Anyway, positive review for the typo fix.


---

Comment by mabshoff created at 2009-03-26 23:02:52

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-26 23:02:52

Resolution: fixed
