# Issue 8525: mistake in docstring for R=Zp(3)'s R.plot method.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-03-13 17:22:55

Assignee: roed

Note max_points versus point_count (in INPUT) below:


```
File: /home/wstein/sage/local/lib/python2.6/site-packages/sage/rings/padics/padic_base_generic.py

Type: <type ‘instancemethod’>

Definition: k.plot(max_points=2500, **args)

Docstring:

    Creates a visualization of this p-adic ring as a fractal similar as a generalization of the the Sierpi’nski triangle. The resulting image attempts to capture the algebraic and topological characteristics of ℤp.

    INPUT:

        * point_count – the maximum number or points to plot, which controls the depth of recursion (default 2500)
        * **args – color, size, etc. that are passed to the underlying point graphics objects
```



---

Comment by roed created at 2011-11-09 03:48:14

Changing status from new to needs_review.


---

Attachment


---

Comment by johanbosman created at 2011-12-01 09:51:20

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-12-05 16:06:24

Resolution: fixed
