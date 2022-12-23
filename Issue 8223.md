# Issue 8223: tab completion broken for many parent objects

Issue created by migration from https://trac.sagemath.org/ticket/8223

Original creator: was

Original creation time: 2010-02-09 20:34:02

Assignee: tbd

CC:  novoselt


```


---

Comment by nthiery created at 2010-02-09 20:54:45

Changing assignee from tbd to nthiery.


---

Attachment

The attached patch should fix the issue. That being said, I would love to see a more robust implementation of ``sage.structure.parent.dir_with_other_class``.


---

Comment by schilly created at 2010-02-10 08:55:55

on #sage-devel

```
00:39 < logix> fwiw, for me the patch in #8223 makes k.[TAB] work again (where e.g. k.<a>=GF(8) )
```



---

Comment by nthiery created at 2010-02-15 22:49:36

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-02-15 23:07:42

Looks good to me.


---

Comment by novoselt created at 2010-02-15 23:07:42

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-17 20:41:35

Resolution: fixed


---

Comment by mvngu created at 2010-02-17 20:41:35

Merged [trac_8223-fix_dir-nt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8223/trac_8223-fix_dir-nt.patch) with a sensible commit message containing the ticket number.
