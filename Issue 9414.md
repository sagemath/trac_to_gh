# Issue 9414: make the rational number field, consistent with other number fields

Issue created by migration from https://trac.sagemath.org/ticket/9414

Original creator: rkirov

Original creation time: 2010-07-03 02:38:31

Assignee: davidloeffler

Keywords: number field, rationals

Currently QQ behaves different than a generic number field. This forces number theory functions to treat QQ separately, which is inconvenient.


```
K = QQ
I = K.ideal(7)
```


This creates ideal that does not have the functions I.denominator, I.numerator, I.prime_ideals() ... which a fractional ideal in a number field should have


```
K.<a> = NumberField(x^2+2)
I = K.ideal(7)
```


Similarly, QQ.places() is not implemented; it should return the one infinite place for Q. Although there seems to be QQ.embeddings().


```
QQ.places()
```



---

Comment by mderickx created at 2011-02-10 14:07:48

This is a duplicate of #7596. I'm putting it as positive review so that someone with the right abilities will see it an close this as duplicate ticket.


---

Comment by mderickx created at 2011-02-10 14:07:48

Changing status from new to needs_review.


---

Comment by mderickx created at 2011-02-10 14:08:09

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-02-16 09:36:18

Resolution: duplicate
