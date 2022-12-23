# Issue 6343: Adds SageObject.check() generic testing framework

Issue created by migration from https://trac.sagemath.org/ticket/6343

Original creator: nthiery

Original creation time: 2009-06-16 22:21:54

Assignee: nthiery

CC:  sage-combinat cwitty roed saliola mvngu

This patch adds a .check() method in SageObject which runs systematic checks on the object. Here is a typical call:

     sage: ZZ.check(verbose = True)
     running test_an_element ... done
     running test_element_pickling ... done
     running test_not_implemented_methods ... done
     running test_pickling ... done

In practice, o.check() runs all the methods named test_* of the object o.

The test_* methods are typically implemented by abstract super classes and in particular via categories, in order to enforce standard behavior and API (test_pickling, test_an_element), or provide mathematical sanity checks (test_associativity).

For consistent error reporting, the test_* methods in turn must use the gadget sage.misc.instance_tester.InstanceTester to actually run the tests.

This patch is a prerequisite for #5891 (category framework), which uses it intensively. Some examples in the patch illustrate this, and are therefore temporarily disabled.


---

Comment by was created at 2009-06-18 14:40:35

Change the name from obj.check() to obj._check().  It is not reasonable that if one does obj.<tab> on *any* Sage object, one sees check.  

William


---

Comment by nthiery created at 2009-06-18 16:12:42

Changing status from new to assigned.


---

Comment by was created at 2009-06-20 14:41:47

Change the name from obj.check() to obj._check(). It is not reasonable that if one does obj.<tab> on *any* Sage object, one sees check.


---

Comment by nthiery created at 2009-06-26 08:48:20

Changing keywords from "" to "testunit".


---

Comment by nthiery created at 2009-06-26 08:51:02

Patch reworked, after the discussion on sage-devel.

Note: After peeking again into the testunit framework, I finally went for TestSuite(object).run() which
is most consistent with it, while being meaningful.

The otherwise discussed functionality TestSuite(object).associativity() will be implemented in a later patch
(if deemed useful in the meantime).


---

Comment by was created at 2009-07-08 14:37:46

I like the new design and class/function names.


---

Attachment

Oops, the doctests were broken (I had forgotten to rename stuff in there)


---

Comment by mhansen created at 2009-07-16 21:04:03

Looks good to me.  We just have to make sure to re-enable the missing tests when the category stuff is added.


---

Comment by nthiery created at 2009-07-16 21:09:32

Thanks for the review!
I just fixed my name to please my grand father :-)


---

Comment by mhansen created at 2009-07-16 21:11:19

No worries.  I really should just add key tomy keyboard layout :-)


---

Comment by mvngu created at 2009-07-16 23:54:20

reviewer patch; fixes typos and docstring formatting


---

Attachment

The patch `trac_6343-reviewer.patch` fixes some typos and copy the docstring for `__init__()` in the class `InstanceTester` to the class itself. This is necessary as docstring in methods whose names begin with an underscore (i.e. `_`) would not show up in the reference manual.



Apart from that, here's a small issue. Can you provide examples and/or tests for the function `_test_pickling()` in `sage/structure/sage_object.pyx`? The doctest coverage for `sage/structure/sage_object.pyx` is very short of 50% and we don't want to make it more difficult to reach 100% coverage.


---

Attachment

Replying to [comment:13 mvngu]:
> The patch `trac_6343-reviewer.patch` fixes some typos and copy the docstring for `__init__()` in the class `InstanceTester` to the class itself. This is necessary as docstring in methods whose names begin with an underscore (i.e. `_`) would not show up in the reference manual.

Agreed, that's better (but not for that argument: my opinion is that _* methods, or at least _*_ and __*__ methods should show up in the manual; but that's another discussion).

Thanks for your doc fixes! I double checked them.

> Apart from that, here's a small issue. Can you provide examples and/or tests for the function `_test_pickling()` in `sage/structure/sage_object.pyx`? The doctest coverage for `sage/structure/sage_object.pyx` is very short of 50% and we don't want to make it more difficult to reach 100% coverage.

Thanks also for spotting the missing doctest. The attached patch fixes this.


---

Comment by mhansen created at 2009-09-08 07:13:44

Everything looks good to me now.  Apply all patches.


---

Comment by mvngu created at 2009-09-08 11:09:27

Merged patches in this order:

 1. `trac_6343-sage_object-test-nt.patch`
 1. `trac_6343-reviewer.patch`
 1. `trac_6343-reviewer-nt.patch`


---

Comment by mvngu created at 2009-09-08 11:09:27

Resolution: fixed


---

Comment by nthiery created at 2009-09-08 11:13:07

Thanks Mike, thanks Minh!
