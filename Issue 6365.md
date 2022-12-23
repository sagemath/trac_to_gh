# Issue 6365: bug in constructing extensions of finite fields

Issue created by migration from https://trac.sagemath.org/ticket/6365

Original creator: was

Original creation time: 2009-06-20 15:00:13

Assignee: somebody


```
sage: F = GF(2)
sage: P.<x> = F[]
sage: f = 1+x+x^4
sage: K.<a> = F.extension(f)
Traceback (most recent call last):
...
ValueError: variable names must be alphanumeric, but one is '('a' which is not.
```



---

Comment by jen created at 2012-03-19 17:37:53

This is no longer a problem:


```

sage: F = GF(2)
sage: P.<x> = F[]
sage: f = 1+x+x^4
sage: K.<a> = F.extension(f)
sage: K
Univariate Quotient Polynomial Ring in a over Finite Field of size 2 with modulus a^4 + a + 1

```



---

Comment by jen created at 2012-03-19 17:38:20

Changing status from new to needs_review.


---

Comment by jen created at 2012-03-19 17:38:20

Changing keywords from "" to "rd2".


---

Comment by jen created at 2012-03-19 17:38:41

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-03-21 11:33:48

Resolution: worksforme
