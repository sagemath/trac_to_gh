# Issue 3668: Functionality of "Set"

Issue created by migration from https://trac.sagemath.org/ticket/3668

Original creator: ljpk

Original creation time: 2008-07-16 22:25:58

Assignee: tba

CC:  sage-combinat

In the documentation for the function "Set" (Reference Manual 11.8) it would be helpful to explicitly point out that Set allows objects of different types, so 


```
sage: Set([Sequence(my_seq),3,QQ])
{Rational Field, 3, [2, 3]}}}}

is perfectly OK.

Also, it would be nice if Set allowed one to use lists, so

`Set([[2,3]])`

worked, rather than giving the error message ``TypeError: list objects are unhashable''.


---

Comment by tscrim created at 2012-11-18 04:50:03

Added documentation that `Set` can take arbitrary hashable objects and raises an exception if one of the objects is not. Also cleaned up some of the documentation. Based on the (one line change) #11366.


---

Comment by tscrim created at 2012-11-18 04:50:03

Changing keywords from "" to "documentation".


---

Comment by tscrim created at 2012-11-18 04:50:03

Changing status from new to needs_review.


---

Comment by tscrim created at 2012-11-26 06:41:01

Changing assignee from tba to tscrim.


---

Comment by ncohen created at 2013-04-21 19:17:21

Good to go !

Nathann


---

Comment by ncohen created at 2013-04-21 19:17:29

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2013-04-21 20:57:32

Thanks for the review Nathann.


---

Comment by jdemeyer created at 2013-04-22 05:58:21

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-04-22 05:58:21

What's the point of tests like

```
sage: hash(s) == hash(s) 
True
```


I prefer to keep the actual hash in this case:

```
sage: hash(s)
1234   # 32-bit
56789  # 64-bit
```


Minor comment: `#indirect doctest` isn't needed for `_underscored_` methods.


---

Comment by tscrim created at 2013-04-22 21:47:22

Replying to [comment:9 jdemeyer]:
> What's the point of tests like
> {{{
> sage: hash(s) == hash(s) 
> True
> }}}
> 
> I prefer to keep the actual hash in this case:
> {{{
> sage: hash(s)
> 1234   # 32-bit
> 56789  # 64-bit
> }}}

The main reason is so that the output does not change if the hash value of the underlying object changes, but it still tests that it is hashable. (Plus it means we don't need to find a 32 and 64 bit machine to test.) I remember there being a discussion about this, but I don't remember/can't find which ticket this came up in (I believe there was a sage-devel topic on this, but I can't find it either).

However I can reset the one doctest back and change the other one to reflect the behavior of the `__hash__()` function.

> Minor comment: `#indirect doctest` isn't needed for `_underscored_` methods.

I wrote this before the switch to the new doctesting framework and were needed then if `_underscored_` methods weren't explicity called. I'll remove them on the next version of the patch.


---

Comment by tscrim created at 2013-07-12 09:41:02

Changing status from needs_work to needs_review.


---

Attachment

New version which keeps the actual hash and removes now unneeded `#indirect doctests`.


---

Comment by ncohen created at 2013-07-12 10:19:02

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2013-07-12 10:19:02

Wellllllll, then `:-)`

Nathann


---

Comment by jdemeyer created at 2013-08-16 21:17:12

Resolution: fixed
