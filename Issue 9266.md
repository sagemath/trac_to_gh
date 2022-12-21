# Issue 9266: bug in global_integral_model for Elliptic Curves over Number Fields

Issue created by migration from Trac.

Original creator: wuthrich

Original creation time: 2010-06-18 13:08:05

Assignee: cremona

The following illustrates the bug. It should be easy to fix.


```
sage: K.<s> = NumberField(x^2-5)
sage: w = (1+s)/2
sage: E = EllipticCurve(K,[2,w])
sage: E.global_integral_model()
...sage/schemes/elliptic_curves/ell_number_field.pyc in global_integral_model(self)
    377                    ai = [ai[i]/pi**(e*[1,2,3,4,6][i]) for i in range(5)]
    378         for z in ai:
--> 379             assert z.denominator() == 1, "bug in global_integral_model: %s" % ai
    380         return EllipticCurve(list(ai))
    381

TypeError: not all arguments converted during string formatting
```


So there are two problems. One that the string is not correctly formatted, the other that it is raised. The latter, I believe, is just because the wrong thing is tested:


```
sage: w.denominator()
2
sage: w.is_integral()
True
```




---

Comment by cremona created at 2010-06-18 15:28:26

The test would be better written as

```
if not all([z.denominator()==1 for z in ai]):
    raise error
```


The problem with the string is that it worked when ai was a list, but now it's a tuple.

I don't understand the last part -- what is w here?


---

Comment by wuthrich created at 2010-06-18 16:21:01

_w_ is the algebraic integer (1+sqrt(5))/2 and it is the coefficient of this integral Weierstrass equation. So this is a global_integral_model. We should not check if the denominator in some basis is 1, but rather if the coefficients are integers.


---

Comment by cremona created at 2010-06-18 16:47:47

Replying to [comment:2 wuthrich]:
> _w_ is the algebraic integer (1+sqrt(5))/2 and it is the coefficient of this integral Weierstrass equation. So this is a global_integral_model. We should not check if the denominator in some basis is 1, but rather if the coefficients are integers.

OK then so we should do 

```
if not all([z.is_integral() for z in ai]):
```


I'm too busy writing lectures for SD22 to make the patch myself!


---

Comment by wuthrich created at 2010-06-18 16:50:12

That holds for me too :)
We will do it in California !

See you soon.


---

Comment by was created at 2010-06-22 04:36:54

Milestone sage-4.4.5 deleted


---

Attachment

exported against 4.4.4.alpha0


---

Comment by wuthrich created at 2010-06-22 23:57:24

Changing status from new to needs_review.


---

Comment by cremona created at 2010-06-23 04:15:29

Looks good and tests pass on 4.4.4.alpha0


---

Comment by cremona created at 2010-06-23 04:15:29

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 07:17:51

Resolution: fixed
