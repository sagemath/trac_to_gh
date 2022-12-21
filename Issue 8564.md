# Issue 8564: fix atan2() conversions between Sage and SymPy

Issue created by migration from Trac.

Original creator: certik

Original creation time: 2010-03-20 02:29:43

Assignee: AlexGhitza

Hi,

please apply the attached patch. The corresponding test is in sympy in sympy/test_external/test_sage.py. It'd be cool to execute that file automatically in sage doctests, not sure currently how to do it.


---

Attachment

ondrej's patch with a header


---

Attachment

doctest


---

Comment by burcin created at 2010-04-02 16:54:31

Changing component from algebra to interfaces.


---

Comment by burcin created at 2010-04-02 16:54:31

I uploaded two patches, 
 * attachment:trac_8564-atan2_conversion.patch is Ondrej's fix including a header with a commit message 
 * attachment:trac_8564-doctests.patch adds a doctest.

I give a positive review to Ondrej's patch, if someone can review the doctest I added this will be ready to go.

The patches to be merged are (in this order):
 * attachment:trac_8564-atan2_conversion.patch
 * attachment:trac_8564-doctests.patch

The doctest patch depends on #8565.


---

Comment by burcin created at 2010-04-02 16:54:31

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-06-10 01:40:37

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-06-10 01:40:37

This seems fine, works well and tests the appropriate thing (i.e. not arctan2(2,3), but the symbolic thing).  Positive review to both.

Question about the Sympy doctest file Ondrej mentions above - it doesn't have 

```
check_expression("atan2(y,x)", "y x")
```

or whatever would work, in test_functions or something like that.  Should it?


---

Comment by certik created at 2010-06-10 02:10:55

Thanks!

Btw, the check_expression() for atan2 is in the latest git sympy, so I need to update the Sage package for it. There were some unrelated mpmath problems with it, that I have to solve first.

Ondrej


---

Comment by mpatel created at 2010-07-21 03:31:39

Resolution: fixed
