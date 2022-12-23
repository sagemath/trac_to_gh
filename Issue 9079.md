# Issue 9079: fix bug in singular polynomial interface

Issue created by migration from https://trac.sagemath.org/ticket/9079

Original creator: was

Original creation time: 2010-05-29 00:47:18

Assignee: malb


```
sage: PolynomialRing(QQ,'u_ba')._singular_init_()
...
RuntimeError: Singular error:
   ? error occurred in STDIN line 33: `if(defined(_b)>0){kill _b;};`
   ? last reserved name was `defined`
   skipping text from `)`
```


This is because the function _singular_init_ incorrectly defines _vars.  The attached patch fixes this. 



---

Attachment


---

Comment by was created at 2010-05-29 00:56:04

Changing status from new to needs_review.


---

Comment by malb created at 2010-05-29 11:55:03

Changing status from needs_review to positive_review.


---

Comment by malb created at 2010-05-29 11:55:03

patch looks good.


---

Comment by SimonKing created at 2010-05-31 08:13:17

Replying to [comment:2 malb]:
> patch looks good.

Sorry, I was a bit too late. But I agree that it looks good.


---

Comment by was created at 2010-06-03 04:27:16

Resolution: fixed
