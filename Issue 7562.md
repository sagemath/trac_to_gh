# Issue 7562: Another (new?) binomial bug

Issue created by migration from https://trac.sagemath.org/ticket/7562

Original creator: kcrisman

Original creation time: 2009-11-30 18:16:36

Assignee: AlexGhitza

CC:  hgranath

From sage-devel:

```
In [143]: [binomial(1,1),binomial(1,2),binomial(1,3),binomial(1,4)] 
Out[143]: [1, 0, 0, 0] 
In [144]: [binomial(1.0,1),binomial(1.0,2),binomial(1.0,3),binomial 
(1.0,4)] 
Out[144]: [1.00000000000000, 0.000000000000000, NaN, NaN] 
```

The problem is this:

```
sage: x = RealNumber('1.0')
sage: P = x.parent()
sage: P
Real Field with 53 bits of precision
sage: gamma(x+1)/gamma(P(Integer(4)+1))/gamma(x-Integer(4)+1)
NaN
sage: gamma(x-Integer(4)+1)
NaN
```

So we'll have to put in yet another check...


---

Comment by hgranath created at 2009-12-02 06:13:28

Here is a patch that should fix this issue. Note that for x a
negative floating point integer we hit gamma function poles both
in the numerator and denominator. An alternative formula is used
in the patch to avoid this.

By the way, is the cc field above supposed to notify me by mail?
I did not get any.


---

Comment by hgranath created at 2009-12-02 06:13:28

Changing status from new to needs_review.


---

Comment by hgranath created at 2009-12-02 06:56:26

Changing status from needs_review to needs_work.


---

Comment by hgranath created at 2009-12-02 06:56:26

Sorry, my patch is off for negative x. I will send an updated patch later.


---

Comment by kcrisman created at 2009-12-02 14:19:14

> By the way, is the cc field above supposed to notify me by mail?
> I did not get any.

Yes, and it does usually work, but perhaps you don't have a correct email associated to your account.  I don't know how to fix this, you may want to ask on sage-devel.


---

Comment by hgranath created at 2009-12-02 14:53:06

Replying to [comment:3 kcrisman]:

> Yes, and it does usually work, but perhaps you don't have a correct email associated to your account.  I don't know how to fix this, you may want to ask on sage-devel.

Thanks for the info, I found some place to enter my email so probably it will work now.


---

Comment by hgranath created at 2009-12-02 20:03:45

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2009-12-04 15:48:17

This seems to work fine, and agrees with integer calculations.  Obviously passes tests.

But:

```
sage: binomial(0,0)
1
sage: binomial(0.,0)
NaN
```


I don't know which is the usual convention, but they should probably agree.


---

Comment by kcrisman created at 2009-12-04 15:48:17

Changing status from needs_review to needs_work.


---

Attachment

New breakpoint


---

Comment by hgranath created at 2009-12-04 16:13:17

Thanks for spotting this, new version is up.


---

Comment by hgranath created at 2009-12-04 16:13:17

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2009-12-04 17:45:52

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-12-04 17:45:52

Great, positive review!


---

Comment by mhansen created at 2009-12-06 08:51:53

Resolution: fixed
