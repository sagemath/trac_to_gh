# Issue 8967: Make extensions of general rings work in the same way as they do for number fields

Issue created by migration from https://trac.sagemath.org/ticket/8967

Original creator: fwclarke

Original creation time: 2010-05-14 18:28:12

Assignee: AlexGhitza

CC:  mstreng


```
sage: P.<t> = GF(5)[]
sage: GF(5).extension(t^2 - 2, name='a')
Univariate Quotient Polynomial Ring in a over Finite Field of size 5 with modulus a^2 + 3
sage: F.<a> = GF(5).extension(t^2 - 2)
Traceback (most recent call last)
...
ValueError: variable names must be alphanumeric, but one is '('a' which is not.
```

and


```
sage: GF(5).extension(x^2 - 2, name='a')
Traceback (most recent call last)
...
AttributeError: 'sage.symbolic.expression.Expression' object has no attribute 'list'
```

The patch solves both these problems, and provides a more useful error  message for mistakes like `GF(5).extension("not_a_poly", name='a'),` by  splicing in code from the number field version.


---

Attachment


---

Comment by mvngu created at 2010-05-15 02:58:53

Is this ready for review?


---

Comment by fwclarke created at 2010-05-15 06:35:34

Changing status from new to needs_review.


---

Comment by fwclarke created at 2010-05-15 06:35:34

Yes


---

Comment by mstreng created at 2010-07-12 14:06:08

This patch does what it says. It did however take over a bad habit of "extension" for number fields. See the examples below, where I think the behavior of QQ is preferred.

```
sage: QQ.extension(x^2-2, ('a', 'b'))
IndexError: the number of names must equal the number of generators
sage: GF(3).extension(x^2-2, ('a', 'b'))
Univariate Quotient Polynomial Ring in a over Finite Field of size 3 with modulus a^2 + 1
sage: QuadraticField(-1, 'i').extension(x^2 - 2, ('a', 'b'))
Number Field in a with defining polynomial x^2 - 2 over its base field

sage: QQ.extension(x^2 - 2, ('a', QQ))
ValueError: variable names must be alphanumeric, but one is 'Rational Field' which is not.
sage: GF(3).extension(x^2 - 2, ('a', QQ))
Univariate Quotient Polynomial Ring in a over Finite Field of size 3 with modulus a^2 + 1
sage: QuadraticField(-1, 'i').extension(x^2 - 2, ('a', QQ))
Number Field in a with defining polynomial x^2 - 2 over its base field
```



---

Comment by mstreng created at 2010-07-12 15:44:55

All tests pass, and as I said before: the patch does what it claims. I've tried a couple more examples and everything seems fine.

The bad behavior in my previous comment was there for number fields already and I don't consider it to be a blocker for this patch.


---

Comment by mstreng created at 2010-07-12 15:44:55

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 09:25:40

I've updated the Author(s) and Reviewer(s) fields, which should contain full names.  Please correct the fields, if I'm wrong.


---

Comment by mpatel created at 2010-07-20 09:25:40

Resolution: fixed
