# Issue 6819: multinomial to accept lists as argument too

Issue created by migration from https://trac.sagemath.org/ticket/6819

Original creator: rishi

Original creation time: 2009-08-24 18:23:05

Assignee: tbd

Keywords: arithmetic

I have modified multinomial to accept lists as argument too. It makes programming with it much easier


---

Attachment


---

Comment by ncohen created at 2009-08-25 07:26:39

Seems ok to me ! I Applied it, used it, and did not understand why it was not possible already !

By the way, I added some docstrings to the function, so if you think it is ok.. ;-)


---

Attachment

patch reviewed + some docstrings


---

Comment by rishi created at 2009-08-25 13:59:22

Replying to [comment:2 ncohen]:
> Seems ok to me ! I Applied it, used it, and did not understand why it was not possible already !
> 
> By the way, I added some docstrings to the function, so if you think it is ok.. ;-)

Thanks for the docstrings.


---

Attachment

ncohen's reviewer patch


---

Comment by mvngu created at 2009-08-30 08:42:46

Resolution: fixed


---

Comment by mvngu created at 2009-08-30 08:42:46

The patch `multinomial_list.patch` contains some badly formatted docstrings. But those shouldn't prevent the patch from being merged. Better to fix those formatting issues in a separate ticket. See #6845 for a follow up to fix this docstring issue.



ncohen -- Your username should be in your patches; it makes it easier to credit you for your contributions. Please also remember to put in a sensible commit message for your patches.



While merging and testing these patches:

 1. `12846.patch` -- rishi's contribution
 2. `trac_6819-reviewer.patch` -- ncohen's contribution
 
I ran into a doctest failure:

```
sage -t -long devel/sage-main/sage/misc/getusage.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/misc/getusage.py", line 69:
    sage: get_memory_usage(t)          # amount of memory more than when we defined t.
Expected:
    0.0
Got:
    0.34375
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_getusage.py
	 [2.6 s]

```

This has nothing to do with the above patches. Strangely, it crops up when I run the test on sage.math. But the test passes on mod.math and geom.math. Merged patches in this order:

 1. `12846.patch`
 2. `trac_6819-reviewer.patch`
