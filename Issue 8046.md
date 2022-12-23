# Issue 8046: Add matrix/matrix_double_dense.py to documentation

Issue created by migration from https://trac.sagemath.org/ticket/8046

Original creator: rbeezer

Original creation time: 2010-01-23 23:03:56

Assignee: mvngu

The source file `matrix/matrix_double_dense.py` is not included in the documentation.  It appears that it should be, since it has functions that are of interest to users.  Patch simply adds it to the right place in the documentation tree.

The file itself needs some love.  After #4756 goes in, the following four functions should be in good shape.  The remainder needs work.


```
left_eigenvectors()
right_eigenvectors()
eigenspaces_left()
eigenspaces_right()
```



---

Comment by jason created at 2011-02-24 05:47:58

Changing status from new to needs_work.


---

Attachment

I get some errors on 4.6.1 when building the docs:


```
docstring of sage.matrix.matrix_double_dense.Matrix_double_dense.condition:11: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
docstring of sage.matrix.matrix_double_dense:7: (ERROR/3) Unexpected indentation.
docstring of sage.matrix.matrix_double_dense.Matrix_double_dense.numpy:11: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
docstring of sage.matrix.matrix_double_dense:13: (ERROR/3) Unexpected indentation.
docstring of sage.matrix.matrix_double_dense:13: (ERROR/3) Unexpected indentation.
<autodoc>:0: (ERROR/3) Unexpected indentation.
```



---

Comment by rbeezer created at 2011-02-24 06:53:18

Replying to [comment:1 jason]:

Yes, the file "needs_work".  I went through it a couple days ago and cleaned up lots of little things (documentation mostly), but then went off and made a few patches with code changes.  I'll get back to it very soon and insert into the other work I'm doing.


---

Comment by kcrisman created at 2012-01-11 16:23:42

Changing keywords from "" to "beginner sd35.5".


---

Comment by ksmith created at 2012-01-11 20:28:34

I made a new patch. This one includes the matrix double dense to the documentation like the last one, and it also edits the file a lot to get rid of almost all of the syntax errors. I am still getting 2 warnings however:

One is:

docstring of sage.matrix.matrix_double_dense:8: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.

I cannot, however find what the error message is talking about, even after multiple people examined it for quite a while.

The other one is:

WARNING: dvipng command 'dvipng' cannot be run (needed for math display), check the pngmath_dvipng setting

which I am told can be ignored.

So really there is just one warning that could still be fixed.


---

Attachment

I'm attaching a 'referee' patch to fix up some docstrings.  The first change in that patch fixes the warning message about the unexpected unindent; the others just tidy some things up.


---

Attachment


---

Comment by kcrisman created at 2012-01-12 14:26:24

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2012-01-12 14:52:48

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-01-12 14:52:48

Looks great!  Thanks for catching this, John.


---

Comment by jason created at 2012-01-12 15:17:46

If you build the documentation with "-j", it will use jsmath, and should not give the error about dvipng: `sage -docbuild reference html -j`


---

Comment by kcrisman created at 2012-01-12 15:33:21

> If you build the documentation with "-j", it will use jsmath, and should not give the error about dvipng: `sage -docbuild reference html -j`
Interesting.  In any case, that was clearly an unrelated error.


---

Comment by jdemeyer created at 2012-01-18 08:14:49

Resolution: fixed
