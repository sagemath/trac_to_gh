# Issue 3359: bug/inconsistency in multivariate polynomial substitution

Issue created by migration from https://trac.sagemath.org/ticket/3359

Original creator: was

Original creation time: 2008-06-04 15:46:35

Assignee: malb


```
Dear Andrey,

On Jun 4, 7:21 am, Andrey Novoseltsev <novos...@gmail.com> wrote:
> What is wrong with the code below and how to fix it?

I don't know what precisely is wrong with that code, but a very
similar code works.

First, i can reproduce the trouble:
sage: Rt.<t> = PolynomialRing(QQ,1)
sage: p = 1+t
sage: R.<u,v> = PolynomialRing(QQ, 2)
sage: p(u/v)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call
last)
...

The following works:
sage: Rt2.<t> = PolynomialRing(QQ)
sage: p2 = 1+t
sage: p2(u/v)
(u + v)/v

The difference is that Rt is a Multivariate Polynomial Ring (with one
variable, though), but Rt2 is a genuine Univariate Polynomial Ring.

So, at least there is a work-around.
```



---

Attachment

The attached patch fixes this issue.


---

Comment by malb created at 2008-08-24 12:26:28

was, can I ask you to review the patch since you reported the issue?


---

Attachment

Looks good to me.  Apply both patches.


---

Comment by mabshoff created at 2008-08-26 23:17:47

Merged both patches in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-26 23:17:47

Resolution: fixed
