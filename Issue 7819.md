# Issue 7819: RealInterval(+infinity,+infinity).is_int() blows up

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2010-01-02 15:02:56

Assignee: AlexGhitza


```
sage: RealInterval(+infinity,+infinity).is_int()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/rlmill/.sage/temp/rlm_book.local/9535/_Users_rlmill__sage_init_sage_0.py in <module>()

/Users/rlmill/sage-4.3/local/lib/python2.6/site-packages/sage/rings/real_mpfi.so in sage.rings.real_mpfi.RealIntervalFieldElement.is_int (sage/rings/real_mpfi.c:16689)()

/Users/rlmill/sage-4.3/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber.ceil (sage/rings/real_mpfr.c:14488)()

ValueError: Calling ceil() on infinity or NaN
```



---

Attachment


---

Comment by rlm created at 2010-01-02 15:03:55

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-01-04 15:53:32

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-01-04 15:53:32

Positive review.  By the way,

```
sage: a = RIF(3.9999999999999999999999999999999999,5.000000000000000000000000000000000)
sage: b = RIF(4.000000000000000000000000000000000,4.9999999999999999999999999999999999)
sage: a.is_int()
(False, None)
sage: b.is_int()
(False, None)
```

though I don't know if that's a bug (except in user input), since

```
sage: a.str(style='brackets')
'[3.9999999999999995 .. 5.0000000000000000]'
sage: b.str(style='brackets')
'[4.0000000000000000 .. 5.0000000000000000]'
```

but anyway wanted to point it out in case this is considered something that should be documented in is_int(), not just in RIF().


---

Comment by rlm created at 2010-01-13 05:14:07

Resolution: fixed
