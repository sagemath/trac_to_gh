# Issue 5608: Mertens' constant is named wrongly

Issue created by migration from Trac.

Original creator: fredrik.johansson

Original creation time: 2009-03-25 12:56:31

Assignee: cwitty

sage.functions.constants.Merten is named wrongly, as the mathematician's name is Franz Mertens and not Merten. The class and default instance should be renamed and "Merten constant" and "Merten's second theorem" in the docstring should be fixed.


---

Comment by burcin created at 2009-06-23 22:16:25

#6200 has a fix for this. I would also like to see the wrongly named `merten` constant deprecated, though I don't know how we can do this.


---

Comment by chapoton created at 2013-08-21 16:23:31

Changing keywords from "" to "documentation, typo".


---

Comment by chapoton created at 2013-08-21 16:23:31

here is a patch


---

Comment by chapoton created at 2013-08-21 16:23:31

Changing status from new to needs_review.


---

Comment by tscrim created at 2013-08-28 02:33:18

Changing status from needs_review to needs_work.


---

Comment by tscrim created at 2013-08-28 02:33:18

Hey Frederic,

This was never deprecated, so we (unfortunately) cannot simply remove it. Instead we need to set a `deprecated_function_alias`.

Best,

Travis


---

Comment by chapoton created at 2013-08-28 06:49:49

ok, done


---

Comment by chapoton created at 2013-08-28 06:49:49

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2013-08-28 07:01:36

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2013-08-28 07:01:36

this does not work. working now on the problem


---

Comment by chapoton created at 2013-08-28 07:27:56

well, it is more complicated than expected.

merten is a constant, belonging to the symbolic ring.

It is not possible to use deprecated_function_alias, because it is not a function.

So far, I have found no way to deprecate merten. I would be tempted to remove it with no deprecation, even if this is not an orthodox procedure.


---

Comment by tscrim created at 2013-08-28 16:40:43

Hmmm...I think you're right; it's best to simply remove it. I don't think changing the API by turning it into a function with a deprecation for that is a good idea as well.


---

Attachment

ok, back to the original version of the patch


---

Comment by chapoton created at 2013-08-28 16:50:56

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2013-08-28 17:00:05

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-09-02 10:21:04

Resolution: fixed
