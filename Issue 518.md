# Issue 518: fix the indentation in monsky_washnitzer.py to be *FOUR* spaces not two.

Issue created by migration from https://trac.sagemath.org/ticket/518

Original creator: was

Original creation time: 2007-08-29 21:51:35

Assignee: dmharvey




---

Comment by dmharvey created at 2007-08-30 04:28:39

fix indentation


---

Comment by dmharvey created at 2007-08-30 12:11:25

Changing status from new to assigned.


---

Attachment


---

Comment by was created at 2007-09-05 04:42:59

I am unable to apply this patch:

```
hg_sage.sage: hg_sage.apply('mw-indentation.patch')
cd "/home/was/s/devel/sage" && hg status
cd "/home/was/s/devel/sage" && hg status
cd "/home/was/s/devel/sage" && hg import   "/home/was/Desktop/mw-indentation.patch"
applying /home/was/Desktop/mw-indentation.patch
sage/schemes/elliptic_curves/monsky_washnitzer.py
Hunk #1 FAILED at 60.
Hunk #7 FAILED at 1150.
Hunk #8 FAILED at 1215.
3 out of 9 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/monsky_washnitzer.py.rej
abort: patch command failed: exited with status 1
sage:
```


And it really genuinely is mostly not applied.


---

Comment by was created at 2007-09-06 18:22:58


```
[11:18] <dmharvey> #518: okay, I guess I'll just go through and do it again at some point. I think the real problem here is to do with trac. I posted the patch a while back, but it didn't get rolled into the repository until now. But meanwhile you and robert had done a bunch of things.
```



---

Comment by dmharvey created at 2007-09-07 01:32:35

let's try that again


---

Comment by was created at 2007-09-07 04:31:08

Resolution: fixed


---

Attachment
