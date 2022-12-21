# Issue 7591: Boolean Polynomial Ring coercion broken

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-12-03 12:53:02

Assignee: malb

CC:  burcin

This is really bad


```
sage: B.<a,b,c> = BooleanPolynomialRing(order='lex')
sage: P.<a,b,c> = BooleanPolynomialRing(order='degrevlex')
sage: P(B('a')) # good
a
sage: B(P('c')) # urgh!
a
```



---

Comment by malb created at 2009-12-04 15:07:39

Changing status from new to needs_review.


---

Comment by malb created at 2009-12-04 15:07:39

The attached patch fixes the issue for me. Burcin, can I ask you to review this patch?


---

Comment by burcin created at 2009-12-06 17:39:02

Changing status from needs_review to positive_review.


---

Attachment

Looks good to me.


---

Comment by mhansen created at 2009-12-07 08:09:21

Resolution: fixed
