# Issue 8174: maxima_methods wrapper for symbolic expressions

Issue created by migration from https://trac.sagemath.org/ticket/8174

Original creator: burcin

Original creation time: 2010-02-03 14:56:36

Assignee: burcin

CC:  kcrisman jason robert.marik

Attached patch provides a `.maxima_methods()` function in symbolic expressions to give access to various methods of simplification, etc. available in Maxima. The return values of functions called through this interface are Sage expressions. Tab completion and docstrings work as expected.

This was proposed on sage-devel:

http://groups.google.com/group/sage-devel/t/3899a578da747009


---

Attachment


---

Comment by burcin created at 2010-02-03 14:58:13

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-02-04 18:25:01

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-02-04 18:25:01

Overall this is very nice.  I have two questions.

1. If I do type(u) (for instance), I just get 'instance' as the type, whereas for something like t._maxima_() I get type giving a Maxima interface element or something.  Is there any way to make type(u) give something more useful (perhaps inheriting from another class?  I don't know.).

2. Tab-completion works great, and just like as with other Maxima things (which means getting functions which don't actually apply, such as triangularize, but whatever, since it's the same behavior).  But one of the doctests for it doesn't seem to work - I get [] instead of the appropriate list.  Do you have some extra initialization in your Maxima that allows u.trigs to complete to the appropriate thing, but not u.simplify (this is the one that returns [] for me)?  I should point out that u.simplify[tab] doesn't work either for me, so the doctest is behaving 'correctly in that sense.


---

Comment by burcin created at 2010-02-20 12:28:49

Replying to [comment:2 kcrisman]:
> 1. If I do type(u) (for instance), I just get 'instance' as the type, whereas for something like t._maxima_() I get type giving a Maxima interface element or something.  Is there any way to make type(u) give something more useful (perhaps inheriting from another class?  I don't know.).

Inheriting from `SageObject` fixed this. I also added `_repr_` and `__reduce__` methods.

> 2. Tab-completion works great, and just like as with other Maxima things (which means getting functions which don't actually apply, such as triangularize, but whatever, since it's the same behavior).  But one of the doctests for it doesn't seem to work - I get [] instead of the appropriate list.  Do you have some extra initialization in your Maxima that allows u.trigs to complete to the appropriate thing, but not u.simplify (this is the one that returns [] for me)?  I should point out that u.simplify[tab] doesn't work either for me, so the doctest is behaving 'correctly in that sense.

On 4.3.3.alpha1, `u.trigs` was triggering different completions for me too. I changed the doctest to look for completions to `airy_` and `elliptic_`. The output of these is less likely to change between maxima versions. I don't know why tab completion with `simplify` doesn't work for you, perhaps this was related to #8223.


---

Comment by burcin created at 2010-02-20 12:28:49

Changing status from needs_work to needs_review.


---

Attachment

apply only this patch


---

Comment by robert.marik created at 2010-04-29 05:56:56

Very useful patch, thanks. Long tests passed on 4.4.rc0.

Positive review. Apply only trac_8174-maxima_methods.take2.patch


---

Comment by robert.marik created at 2010-04-29 05:56:56

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-08 22:08:43

Merged [trac_8174-maxima_methods.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8174/trac_8174-maxima_methods.take2.patch).


---

Comment by mvngu created at 2010-05-08 22:08:43

Resolution: fixed
