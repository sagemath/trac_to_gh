# Issue 8554: Failed RealNumber conversion from str in base 16.

Issue created by migration from Trac.

Original creator: lfousse

Original creation time: 2010-03-17 20:04:11

Assignee: jkantor

CC:  jason

Keywords: hexadecimal, string conversion


```
sage: RealNumber("1ffef", base=16)  
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/opt/sage-4.3.3/<ipython console> in <module>()

/opt/sage-4.3.3/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.create_RealNumber (sage/rings/real_mpfr.c:25128)()

ValueError: invalid literal for int() with base 10: 'f'
```


The problem arises because 'e' is incorrectly parsed as the mantissa/exponent delimiter. If Sage wants to follow MPFR in this regard, '`@`' should be used as a delimiter for base > 10.


---

Comment by mmezzarobba created at 2014-02-02 11:12:52

See #14702.


---

Comment by mmezzarobba created at 2014-02-02 11:12:52

Changing status from new to needs_review.


---

Comment by aapitzsch created at 2014-02-09 20:58:58

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-11 21:21:58

Resolution: fixed
