# Issue 3744: Coercion between isomorphic parents should result in an element of the left operand's parent

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-07-30 05:00:58

Assignee: robertwb

This is in accordance with the programming guide. 


---

Attachment


---

Comment by cremona created at 2008-08-10 10:29:33

This patch does not apply cleanly to 3.1.alpha0:

```
sage: hg_sage.apply ("/home/john/3744-coercion-left.patch")
cd "/home/john/tmp/sage-3.1.alpha0/devel/sage" && hg status
cd "/home/john/tmp/sage-3.1.alpha0/devel/sage" && hg status
cd "/home/john/tmp/sage-3.1.alpha0/devel/sage" && hg import   "/home/john/3744-coercion-left.patch"
applying /home/john/3744-coercion-left.patch
patching file sage/structure/coerce.pyx
Hunk #1 FAILED at 737
Hunk #2 FAILED at 754
2 out of 2 hunks FAILED -- saving rejects to file sage/structure/coerce.pyx.rej
abort: patch failed to apply
```


I'm not sure how it fits in with the main coercion model patches though.


---

Comment by robertwb created at 2008-08-11 16:32:36

Let's wait until #3738 gets in.


---

Comment by cremona created at 2008-08-14 20:14:22

Still does not apply cleanly to 3.1.alpha2:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: 3744
sage: hg_sage.apply("/home/john/3744-coercion-left.patch")
cd "/home/john/sage-3.1.alpha2/devel/sage" && hg status
cd "/home/john/sage-3.1.alpha2/devel/sage" && hg status
cd "/home/john/sage-3.1.alpha2/devel/sage" && hg import   "/home/john/3744-coercion-left.patch"
applying /home/john/3744-coercion-left.patch
patching file sage/structure/coerce.pyx
Hunk #1 succeeded at 845 with fuzz 2 (offset 105 lines).
Hunk #2 FAILED at 780
1 out of 2 hunks FAILED -- saving rejects to file sage/structure/coerce.pyx.rej
abort: patch failed to apply
```



---

Comment by mabshoff created at 2008-08-14 23:49:43

This is actually in 3.1.alpha2 and has been reviewed via #3738, so I am giving this a positive reivew.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-14 23:49:53

Resolution: fixed


---

Comment by mabshoff created at 2008-08-14 23:49:53

Merged in Sage 3.1.alpha2


---

Comment by mabshoff created at 2008-08-14 23:51:48

Well, I really ought to change the subject, too.

Cheers,

Michael
