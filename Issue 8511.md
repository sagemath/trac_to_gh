# Issue 8511: docstring fix for symbolic expressions

Issue created by migration from https://trac.sagemath.org/ticket/8511

Original creator: jhpalmieri

Original creation time: 2010-03-12 20:24:55

Assignee: burcin

Attached is a trivial fix to make the docstring for the `substitute` method for symbolic expressions look right.


---

Attachment


---

Comment by jhpalmieri created at 2010-03-12 20:34:51

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-03-12 23:27:56

Changing component from symbolics to documentation.


---

Comment by jhpalmieri created at 2010-03-12 23:28:12

apply only this patch


---

Attachment

reviewer patch; apply on top of previous


---

Attachment

With this patch, plus the ones at #8457 and #8492, the reference manual builds with no warnings.


---

Comment by jhpalmieri created at 2010-03-13 00:22:50

Changing assignee from burcin to jhpalmieri.


---

Comment by jhpalmieri created at 2010-03-13 00:22:50

Changing priority from minor to critical.


---

Comment by mvngu created at 2010-03-13 00:30:13

The patch [trac_8511-unexpected-indentation.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8511/trac_8511-unexpected-indentation.patch) solves the three warnings reported at #8492. However, note that the formatting in the following snippet won't properly render in the HTML version as one would expect TESTS and EXAMPLES block to render:

```diff
diff -r 29c870e0a9e4 -r 8851bfe046d1 sage/symbolic/expression.pyx
--- a/sage/symbolic/expression.pyx	Mon Mar 08 20:51:26 2010 -0800
+++ b/sage/symbolic/expression.pyx	Fri Mar 12 15:12:47 2010 -0800
@@ -3151,7 +3151,8 @@
             sage: t.subs({a:b, b:c})
             (x + y)^3 + b^2 + c^2
 
-        TESTS:
+        TESTS::
+
             # no arguments return the same expression
             sage: t.subs()
             (x + y)^3 + a^2 + b^2
```

This is due to the comment

```
# no arguments return the same expression
```

To get this TESTS block to render with colours as one would expect of a TESTS block, prefix that comment with "sage: ". The reviewer patch [trac_8511-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8511/trac_8511-reviewer.patch) takes care of that. So only my patch needs review by anyone but me. If it gets a positive review, the whole ticket is good to go into Sage 4.3.4.rc0.


---

Comment by jhpalmieri created at 2010-03-13 00:53:37

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-03-13 00:53:37

Looks good to me.  The TESTS block now looks right, and doctests pass.


---

Comment by mvngu created at 2010-03-14 08:28:12

Resolution: fixed


---

Comment by mvngu created at 2010-03-14 08:28:12

Merged in this order:

 1. [trac_8511-unexpected-indentation.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8511/trac_8511-unexpected-indentation.patch)
 1. [trac_8511-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8511/trac_8511-reviewer.patch)
