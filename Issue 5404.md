# Issue 5404: deprecate numerical_sqrt

Issue created by migration from https://trac.sagemath.org/ticket/5404

Original creator: robertwb

Original creation time: 2009-02-28 21:55:42

Assignee: burcin

CC:  jason

Now we have sqrt(a, prec=1000). Also, it doesn't even do what it says. 


```
sage: numerical_sqrt(3)
sqrt(3)
```



---

Comment by robertwb created at 2009-02-28 22:02:51

Changing priority from major to minor.


---

Attachment

Not used anywhere in the Sage source.


---

Comment by burcin created at 2009-03-01 15:38:03

It would be good to mention the deprecation in the docstring of the function as well.

We could also change the doctests, which test the wrong function now anyway, to demonstrate using sqrt with the prec parameter.


---

Comment by jhpalmieri created at 2009-05-10 22:30:54

The deprecation message doesn't make sense to me:

```
sage: sqrt(10.1, prec=5)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: sqrt() got an unexpected keyword argument 'prec'
```

I think the issue here is that in real_mpfr.pyx, the sqrt method doesn't accept a 'prec' argument. If I do `search_def('sqrt')`, I see lots of sqrt methods without a prec argument.  Perhaps the sqrt function in calculus/calculus.py should check for a `TypeError` in addition to an `AttributeError`?  In any case, we can't give a deprecation message which suggests using code which doesn't work.

We also need some doctests in the sqrt function in calculus/calculus.py using all of the advertised arguments.


---

Comment by jhpalmieri created at 2009-05-31 21:41:01

See #6171 for a possible fix to the 'prec' issue.  Maybe with this fix, the patch here is okay?


---

Comment by jhpalmieri created at 2009-05-31 23:39:48

Okay, I think with #6171, my main complaint is taken care of.  Here's a new patch; the only difference is the docstring.  The code gets a positive review from me, so if you're happy with my docstring, give the ticket a positive review.

This depends on #6171, not to apply and to pass doctests, but in the sense that the deprecation message is inaccurate without #6171.


---

Attachment

apply only this patch


---

Comment by mhansen created at 2009-06-04 19:10:34

Looks good to me.

Merged numerical_sqrt.patch in 4.0.1.rc1.


---

Comment by mhansen created at 2009-06-04 19:10:34

Resolution: fixed
