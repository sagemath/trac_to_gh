# Issue 9314: LaTeX representation of negative symbolic fractions still broken

Issue created by migration from https://trac.sagemath.org/ticket/9314

Original creator: damm

Original creation time: 2010-06-22 18:19:43

Assignee: AlexGhitza

CC:  was

I think #9086 isn't completly fixed:

 {{{
 sage: var('x y')
 sage: latex(-x/y) 
 \frac{x}{y}
 }}}


---

Comment by leif created at 2010-06-22 19:02:29

Changing component from algebra to symbolics.


---

Comment by leif created at 2010-06-22 19:02:29

Changing assignee from AlexGhitza to burcin.


---

Comment by leif created at 2010-06-22 19:02:29

Changing keywords from "" to "latex, sign, minus, pynac".


---

Comment by leif created at 2010-06-22 19:02:29

Changing priority from major to critical.


---

Comment by leif created at 2010-06-22 19:36:11

These are correct, but don't look that nice:

```
sage: latex(-(-x^2/-x^5))
\frac{-1}{x^{3}}
sage: latex(-(x^2/x^5))
\frac{-1}{x^{3}}
sage: latex(-((-x)^2/x^5))
\frac{-1}{x^{3}}
sage: latex(x^2/-x^5)
\frac{-1}{x^{3}}
sage: latex(x^2/(-x)^5)
\frac{-1}{x^{3}}
sage: latex(-(-2*x^2/-x^5))
\frac{-2}{x^{3}}
sage: latex(-(-x^2/(-3*x^5)))
\frac{-1}{3 \, x^{3}}
```



---

Comment by leif created at 2010-06-22 19:51:02

(Note that the above are all broken, i.e. lose their sign, if one `x` is replaced by `y`.)


---

Comment by schilly created at 2010-07-06 15:34:09

i just got a report that this is also broken for

```
sage: var('a b')
sage: latex(-1 * (a/b))
```


can we make this a blocker?


---

Comment by burcin created at 2010-07-08 09:18:01

Changing priority from critical to blocker.


---

Comment by burcin created at 2010-07-08 09:18:01

This is really embarrassing. I'll fix this tonight.


---

Comment by mhansen created at 2010-07-10 09:33:03

Ping.


---

Comment by burcin created at 2010-07-10 10:14:46

It ended up begin an extended night. I'm looking at it right now.


---

Attachment


---

Comment by burcin created at 2010-07-11 16:07:08

The pynac package at

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.p4.spkg

contains a fix for this. I want to keep this as easy to review as possible, so the only change is the following simple patch:


```
diff --git a/ginac/mul.cpp b/ginac/mul.cpp
--- a/ginac/mul.cpp
+++ b/ginac/mul.cpp
@@ -268,6 +268,10 @@
 			     }
 			} else {
 			     if (numer.is_equal(_ex1) || numer.is_equal(_ex_1)) {
+			          const numeric &coeff = ex_to<numeric>(numer);
+				  if (coeff.is_equal(*_num_1_p) && !coeff.is_parent_pos_char()) {
+				        c.s<<"-";
+				  }
 			         mul(others).eval().print(c);
 			     } else {
 				 mul(numer,mul(others).eval()).hold().print(c);
```


attachment:trac_9314-latex_mul.patch has the doctest fixes for the Sage library.

I will take care of the pretty printing issues from comment:3 later.


---

Comment by burcin created at 2010-07-11 16:07:08

Changing status from new to needs_review.


---

Comment by cremona created at 2010-07-12 13:21:32

The new spkg installed fine for me on 4.5.rc0 (+patches at #7379), then the patch applied fine and tests pass ( itested the whole library but without -long).  So, while I cannot tell whether the four lines of C++ added to ginac/mul.cpp are correct, this is certainly an improvement and enough to make me give it a positive review.


---

Comment by cremona created at 2010-07-12 13:21:32

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-13 16:33:15

Resolution: fixed


---

Comment by rlm created at 2010-07-13 16:33:15

Applied

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.p4.spkg

and

attachment:trac_9314-latex_mul.patch

to sage-4.5.rc1.
