# Issue 1514: fix breakage and lameness in foo? and foo?? especially in the notebook.

Issue created by migration from https://trac.sagemath.org/ticket/1514

Original creator: was

Original creation time: 2007-12-15 00:17:52

Assignee: boothby

I'm sick of foo? or foo?? failing with tracebacks.  They should never do that.


---

Attachment


---

Comment by was created at 2007-12-15 05:28:52

Changing priority from major to blocker.


---

Comment by was created at 2007-12-15 05:47:50


```
[9:43pm] cwitty-rvw-1514: wstein-rvw-1119, it looks like #1514 does not have any doctests for whatever bugs you are fixing?
[9:43pm] craigcitro: gmp comes before pari in the build order for libcsage
[9:44pm] wstein-rvw-1119: cwitty-1514 -- the buginess is that nothing works at all.
[9:44pm] wstein-rvw-1119: it's hard to have a doctest for that.
[9:44pm] wstein-rvw-1119: However, notice the first line of the patch, which turns *on* doctesting for the sageinspect.py file
[9:44pm] wstein-rvw-1119: So there are many new doctests as a result.
[9:45pm] wstein-rvw-1119: It's really a design change anyway -- to use the files in SAGE_ROOT/devel/sage/sage instead of SAGE_ROOT/local/lib/python/site-packages/sage/,
[9:45pm] wstein-rvw-1119: since for some reason often some .pyx files or other files that are relevant don't get copied over there.
[9:45pm] wstein-rvw-1119: But SAGE_ROOT/devel/sage/sage does.
```



---

Attachment


---

Comment by cwitty created at 2007-12-15 06:08:38

Looks good to me; fixes doctests.

Apply both patches.


---

Comment by mabshoff created at 2007-12-15 07:21:37

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 07:21:37

Merged in 2.9.rc0.
