# Issue 8381: typo in documentation of rational_reconstruction

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-02-26 23:00:00

Assignee: mvngu

CC:  burcin


```
sage: rational_reconstruction?
...
            `(x,y)=(|v2|,v3*mathrm{sign}(v2))` is then the unique
```

The `mathrm` should be removed.


---

Comment by jason created at 2010-05-26 15:18:53

Changing keywords from "" to "beginner".


---

Attachment

Remove \mathop and \mathrm when displaying docs in python


---

Comment by fdiebold created at 2011-05-22 20:12:00

It seems to me that the sage help function should remove these latex commands (\mathrm and \mathop, which also occurs in some documentation in that file). The attached patch does that.


---

Comment by fdiebold created at 2011-05-22 20:12:00

Changing status from new to needs_review.


---

Comment by zimmerma created at 2011-05-23 11:59:09

good work! Positive review.

Paul


---

Comment by zimmerma created at 2011-05-23 11:59:09

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-05-30 15:06:53

fdiebold: please add your real name as Author and also add yourself to [http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames)


---

Comment by jdemeyer created at 2011-05-30 15:06:53

Changing status from positive_review to needs_info.


---

Comment by fdiebold created at 2011-05-30 16:11:21

Done.


---

Comment by jdemeyer created at 2011-05-31 09:21:56

Resolution: fixed
