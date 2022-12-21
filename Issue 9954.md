# Issue 9954: Rational(3)%Rational(-1) fails

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2010-09-20 18:20:29

Assignee: AlexGhitza

This is inconsistent


```
sage: Rational(3)%Rational(-1)
ZeroDivisionError: Inverse does not exist.
```


but


```
sage: 3%(-1)
0
```



---

Comment by cremona created at 2010-12-21 23:23:34

This is caused by the following simpler bug:

```

sage: a=Integer(3)
sage: b=Integer(-1)
sage: a.inverse_mod(b)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
...

ZeroDivisionError: Inverse does not exist.
```

which is easy to fix.  In `sage.rings.integer.Integer.inverse_mod` there is special case for modulus n=1 but not for -1.  Either ass this special case, or replace n by abs(n).


---

Comment by aapitzsch created at 2011-01-27 11:08:31

Changing status from new to needs_review.


---

Comment by cremona created at 2011-01-27 17:05:48

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2011-01-27 17:05:48

The patch looks right and I tested that it works (but did not yet test the whole library).

BUT you need to add a doctest to show that the bug has been fixed.  There's a similar doctest in the same function, so just add something similar.

Then I'll look at it again.


---

Attachment


---

Comment by aapitzsch created at 2011-01-28 08:44:41

Changing status from needs_work to needs_review.


---

Comment by aapitzsch created at 2011-01-28 08:44:41

doctest added


---

Comment by cremona created at 2011-01-28 20:45:28

Replying to [comment:4 aapitzsch]:
> doctest added

Thanks!  Positive review.


---

Comment by cremona created at 2011-01-28 20:45:28

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-02-07 08:13:53

Resolution: fixed
