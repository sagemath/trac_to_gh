# Issue 3412: sage-3.0.3.alpha2 -- two files that are ? in repo in fresh build

Issue created by migration from https://trac.sagemath.org/ticket/3412

Original creator: was

Original creation time: 2008-06-13 14:16:21

Assignee: cwitty

After building sage-3.0.3.alpha2:

```
sage: hg_sage()
cd "/home/was/build/sage-3.0.3.alpha2/devel/sage" && hg status
? sage/misc/allocator.h
? sage/server/notebook/a.txt
0
```



---

Comment by mabshoff created at 2008-06-15 19:10:48

This is the real blocker for 3.0.3 without somebody working on this as far as I know.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-06-16 18:29:56

Patch looks good to me. There is another file in tree after running doctests, but we will deal with that one on a different ticket. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-16 18:30:07

Merged in Sage 3.0.3.rc0


---

Comment by mabshoff created at 2008-06-16 18:30:07

Resolution: fixed
