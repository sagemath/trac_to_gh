# Issue 8001: Stronger category tests

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-01-19 18:20:02

Assignee: nthiery

CC:  sage-combinat

Keywords: TestSuite, Category

*- More category tests: _test_category, _test_elements
 - Improvements to TestSuite
   - Partial support for nested test suites
   - Support for basic TestSuite(x) for x any Python object
 - Added TestSuite call for Spec and ref to #7946
 - Corresponding doctest updates

Depends on #7921



---

Attachment


---

Comment by nthiery created at 2010-01-19 18:32:02

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-01-19 20:31:28

I briefly glanced at the patch when doing #7921, and what I saw looks good (though I didn't read it all thoroughly enough to call it a review).


---

Comment by hivert created at 2010-01-23 10:59:47

I'm uploading a small trivial review patch. Here are the comment:
 - Add a missing "`";
 - Improve the layout of an enumeration;
 - replace `ZZ._tester` with `QQ._tester` to show that the gadget is automatically attached (Noting to do with the previous call on `ZZ`.

Otherwise the patch is ready to go. 

Nicolas: You can add positive review once you had a look on my review patch.


---

Attachment


---

Comment by nthiery created at 2010-01-23 14:28:03

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-01-23 14:28:03

Replying to [comment:3 hivert]:
> I'm uploading a small trivial review patch. Here are the comment:
>  - Add a missing "`";
>  - Improve the layout of an enumeration;
>  - replace `ZZ._tester` with `QQ._tester` to show that the gadget is automatically attached (Noting to do with the previous call on `ZZ`.
> 
> Otherwise the patch is ready to go. 

Thanks for the review!

> Nicolas: You can add positive review once you had a look on my review patch.  

Done!


---

Comment by mvngu created at 2010-01-23 14:58:58

Resolution: fixed


---

Comment by mvngu created at 2010-01-23 14:58:58

Merged in this order:

 1. [trac_8001-categories_testsuite-nt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8001/trac_8001-categories_testsuite-nt.patch)
 1. [trac_8001-categories_testsuite-review-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8001/trac_8001-categories_testsuite-review-fh.patch)
