# Issue 6989: line3d can modify its argument type

Issue created by migration from https://trac.sagemath.org/ticket/6989

Original creator: mhampton

Original creation time: 2009-09-22 17:49:16

Assignee: was

This issue could well arise in other plotting code, I haven't checked yet.  But at least for line3d:


```
sage: mypoints = [vector([1,2,3]), vector([4,5,6])]
sage: type(mypoints[0])
<type 'sage.modules.vector_integer_dense.Vector_integer_dense'>
```

but then:

```
sage: L = line3d(mypoints)
sage: type(mypoints[0])
<type 'tuple'>
```


so vectors are changed to tuples.


---

Comment by jason created at 2010-01-20 10:37:34

Changing status from new to needs_review.


---

Attachment


---

Comment by kcrisman created at 2010-01-27 15:34:58

Looks good.  Positive review, assuming it passes relevant doctests (currently checking).


---

Comment by kcrisman created at 2010-01-27 15:34:58

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-01-27 15:44:46

All is well.  And this does not occur in line2d, as far as I have tested it, because of the grid system.


---

Comment by mvngu created at 2010-01-29 22:55:25

Jason, please provide a meaningful commit message together with a ticket number. See [this section](http://www.sagemath.org/doc/developer/producing_patches.html#quick-mercurial-tutorial-for-sage) of the Developers' Guide.


---

Comment by jason created at 2010-01-30 00:39:37

argh!  I'm always forgetting that.  I'll try to do it soon (in the next two weeks).


---

Comment by mvngu created at 2010-01-31 01:00:49

Resolution: fixed
