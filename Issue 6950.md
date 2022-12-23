# Issue 6950: computing algebraic immunity

Issue created by migration from https://trac.sagemath.org/ticket/6950

Original creator: ylchapuy

Original creation time: 2009-09-17 19:28:30

Assignee: somebody

CC:  malb

It would be nice to have an efficient implementation for computing the algebraic immunity of a Boolean function and finding annihilators.


---

Comment by ylchapuy created at 2009-09-17 19:34:41

Changing priority from major to minor.


---

Comment by ylchapuy created at 2009-09-17 19:34:41

This is a toy implementation, but still better than nothing. I also added a way of constructing a random Boolean function, I hope it's ok to put both in this ticket.

PS: Is it ok if I cc you Martin?


---

Comment by malb created at 2009-09-17 20:33:53

Of course, its okay :) I'll try to do the review before I go on holiday on Saturday.


---

Comment by malb created at 2009-09-17 20:34:38

I noticed `def random_BooleanFunction(n)` while skimming the patch, the convention seems to be `random_boolean_function`, i.e. lower case for functions.


---

Comment by ylchapuy created at 2009-09-17 20:54:40

Patch updated.


---

Comment by malb created at 2009-09-17 21:50:15

*Review*

 * patch applies cleanly against alpha1
 * you shouldn't need `#random` in the doctest because the random seed should be reset before each doctest to make sure that the result is reproducible. 
 * there are some very minor line break problems in the HTML reference manual: http://sage.math.washington.edu/home/malb/scratch/sage-4.1.2.alpha1/devel/sage/doc/output/html/en/reference/sage/crypto/boolean_function.html
 * also `..math::` is not properly typesetted (cf. same link)
 * doctests pass on sage.math

So almost positive review, module the nitpicks above. Feel free to change it to a positive review once those are addressed.


---

Comment by ylchapuy created at 2009-09-17 22:44:59

based on sage 4.1.2.alpha0 (needs #6877)


---

Attachment

Thanks for that quick review, and enjoy your holidays!


---

Comment by mvngu created at 2009-09-18 02:10:03

See #6953 for a follow-up to this ticket.


---

Comment by mvngu created at 2009-09-18 02:10:03

Resolution: fixed
