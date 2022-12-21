# Issue 4254: [with patch, needs review] better parameter parsing for mq.SR

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-10-08 14:18:45

Assignee: malb

`correct_only` is only valid for GF(2). Make sure it is passed on correctly.


---

Comment by cwitty created at 2008-11-23 15:40:05

This patch should probably have some doctests.


---

Comment by malb created at 2008-11-23 22:25:31

apply before other patch


---

Attachment

added doctests


---

Attachment

I added doctests and the patch this patch depends on which I forgot to submit last time.


---

Comment by was created at 2008-11-28 22:11:43

REFEREE REPORT:
I tried to figure out how to apply the above patches in their confusing order, but I guess I failed or something. See below (last patch fails to apply).  Please clarify, and I'll referee this:

```
was`@`sage:~/build/sage-3.2.1.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
hgsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_convenience.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_convenience.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/15295/tmp_0.patch"
applying /home/was/.sage/temp/sage/15295/tmp_0.patch
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_parameters.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_parameters.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/15295/tmp_1.patch"
applying /home/was/.sage/temp/sage/15295/tmp_1.patch
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_parameters.2.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_parameters.2.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/15295/tmp_2.patch"
applying /home/was/.sage/temp/sage/15295/tmp_2.patch
patching file sage/crypto/mq/sr.py
Hunk #2 FAILED at 288
1 out of 2 hunks FAILED -- saving rejects to file sage/crypto/mq/sr.py.rej
abort: patch failed to apply
```

| Sage Version 3.2.1.alpha1, Release Date: 2008-11-26                |
| Type notebook() for the GUI, and license() for information.        |
and 

```
was`@`sage:~/build/sage-3.2.1.alpha1$ more devel/sage/sage/crypto/mq/sr.py.rej
--- sr.py
+++ sr.py
`@``@` -284,8 +289,20 `@``@`
             polybori = self._polybori
         except AttributeError:
             polybori = False
+        kwds.setdefault("polybori", polybori)
 
-        kwds.setdefault("polybori", polybori)
+        try:
+            correct_only = self._correct_only
+        except AttributeError:
+            correct_only = False
+        kwds.setdefault("correct_only", correct_only)
+
+        try:
+            biaffine_only = self._biaffine_only
+        except AttributeError:
+            biaffine_only = False
+        kwds.setdefault("biaffine_only", biaffine_only)
+
         return SR(**kwds)
 
     def __getattr__(self, attr):
```



---

Comment by malb created at 2008-11-30 20:27:39

Here is how to apply the patches:


```
$ hg qimport sr_convenience.patch
adding sr_convenience.patch to series file
$ hg qpush
applying sr_convenience.patch
Now at: sr_convenience.patch
$ hg qimport sr_parameters.patch
adding sr_parameters.patch to series file
$ hg qpush
applying sr_parameters.patch
Now at: sr_parameters.patch
$ sage -b
```


Note that `sr_parameters.2.patch` is `sr_parameters.patch`


---

Comment by was created at 2008-11-30 23:30:35

If this passes doctests, then I give it a positive review.


---

Comment by mabshoff created at 2008-11-30 23:49:41

Doctests pass, so this is a positive review by William.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-30 23:49:56

Merged in Sage 3.2.1.rc1


---

Comment by mabshoff created at 2008-11-30 23:49:56

Resolution: fixed
