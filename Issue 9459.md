# Issue 9459: Implement a generic radical() function

Issue created by migration from Trac.

Original creator: jdemeyer

Original creation time: 2010-07-08 21:43:40

Assignee: was

CC:  mhansen

Right now, there is a function radical() as member of IntegerRing_class.  But there is no generic radical() function:

```
sage: radical(100)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/usr/local/src/sage-4.4.4/devel/sage-test/<ipython console> in <module>()

NameError: name 'radical' is not defined
```



---

Comment by jdemeyer created at 2010-07-10 14:57:02

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-07-10 14:57:02

The attached patch adds a radical() function, functions Factorization.radical() and Factorization.radical_value().  It also fixes a bug in the radical of a polynomial where the content was not accounted for.

It also changes the output of radical(), in a way which I think makes more sense: radical(0) now gives an error instead of returning 1 and the radical of a negative number is positive (instead of negative).

In order for all doctests to succeed, you need to apply also the patches for #9450.


---

Comment by kcrisman created at 2010-08-06 19:56:42

For what it's worth, groups and algebras have radicals too, so it might be worth putting a `#TODO` in the main definition that one might want `radical(G,type='nilpotent')` to work here if that ever is implemented/wrapped nicely (e.g. see [here](http://www.gap-system.org/Manuals/doc/htm/ref/CHAP037.htm#SSEC012.9)), so that future developers do not break the possibility of that syntax.


---

Comment by cremona created at 2010-11-21 16:49:37

Applies well to 4.6.1.alpha1 and all tests pass.


---

Comment by cremona created at 2010-11-21 16:49:37

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-21 17:03:18

Thanks, this is something I did in Leiden and totally forgot about.


---

Comment by cremona created at 2010-11-21 17:11:57

Replying to [comment:5 jdemeyer]:
> Thanks, this is something I did in Leiden and totally forgot about.

I cannot see a reason not to include it, despite the comment from kcrisman.


---

Comment by jdemeyer created at 2011-01-12 06:32:30

Resolution: fixed


---

Attachment
