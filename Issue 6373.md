# Issue 6373: AA and QQbar have no is_square method

Issue created by migration from https://trac.sagemath.org/ticket/6373

Original creator: ncalexan

Original creation time: 2009-06-20 19:48:21

Assignee: was

CC:  cwitty jcooley

Keywords: algebraic field is square


```
sage: QQbar(5).is_square()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

...

AttributeError: 'AlgebraicNumber' object has no attribute 'is_square'
```


but of course:


```
sage: QQbar(5).sqrt()
2.236067977499790?
```



---

Attachment


---

Comment by cremona created at 2009-09-24 12:20:19

The attached patch adds this trivial function.  It also corrects a typo which I discovered when testing it (specifically, now that this function exists you can do more with elliptic curves over QQbar;  see also #6879).


---

Comment by jason created at 2009-09-25 05:46:14

Looks good; positive review.


---

Comment by mvngu created at 2009-09-25 14:35:32

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:35:12

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
