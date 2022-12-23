# Issue 8985: update COPYING.txt

Issue created by migration from https://trac.sagemath.org/ticket/8985

Original creator: was

Original creation time: 2010-05-18 05:24:32

Assignee: mvngu

I looked in COPYING.txt in SAGE_ROOT and it has:

```
...
gmp                                  LGPL
...
mpfi                                 GPL
mpfr                                 LGPL
...
```


so it includes gmp, but shouldn't, and it doesn't include mpir.  It might be out of date in other ways.


---

Comment by mmezzarobba created at 2015-04-13 14:41:18

Fixed in #12447.


---

Comment by mmezzarobba created at 2015-04-13 14:41:18

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2015-04-14 09:38:54

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-04-14 23:03:44

Resolution: fixed
