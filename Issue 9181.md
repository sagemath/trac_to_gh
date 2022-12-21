# Issue 9181: Update dev-guide : __hash__ return a long

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-06-07 23:00:08

Assignee: mvngu

From sage-devel

```
> 1. I think we should update the devguide, or is there something I don't get ?

No, we should update the developers guide. Despite this sentence, the (c)
return type of "hash" has been a long since Python 2.3 at least, so I think
this wasn't ever correct for 64-bit long machines. (What was required is
that it fit into a Python int.)

> 2. I'm writing a Cython class which caches the hash value. Which type
> should I
>   use for the attribute ? int doesn't work since when trying to store the
>   hash of None in an int I get
>
>      OverflowError: value too large to convert to int
>
>   Is long ok and portable (it is was is used in a few place in sage) ?
> Should
>   we write it in the doc ?

Yes, we should be using C longs here. Under the hood

Python int = C long != C int
Python float = C double  != C float

and Python longs have no (native) C equivalent.
```



---

Comment by hivert created at 2010-06-07 23:01:02

Changing assignee from mvngu to hivert.


---

Attachment


---

Comment by hivert created at 2011-01-18 15:19:35

Changing keywords from "" to "__hash__".


---

Comment by hivert created at 2011-01-18 15:19:35

Changing status from new to needs_review.


---

Comment by hivert created at 2011-04-04 15:22:44

Any chance to get this ticket reviewed ?


---

Comment by nthiery created at 2011-04-21 01:34:32

Sounds good and harmless to me, assuming the patch applies (it should since the file did not change in the last year). Positive review!


---

Comment by nthiery created at 2011-04-21 01:34:32

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-21 19:35:21

Resolution: fixed
