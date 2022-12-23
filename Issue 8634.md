# Issue 8634: Broken conversion of sage variable h1 to Maxima

Issue created by migration from https://trac.sagemath.org/ticket/8634

Original creator: robert.marik

Original creation time: 2010-03-31 09:23:12

Assignee: burcin

CC:  kcrisman burcin

h1, h2, h9 (and perhaps some others) are converted into binomial coefficients. This disallows to solve an equation involving variable h1.

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: h1=var('h1'); h1._maxima_()
binomial(n,k)*x^k
sage: h2=var('h2'); h2._maxima_()
binomial(a,k)*binomial(b,n-k)
sage: h=var('h'); h._maxima_()
h
sage: h_1=var('h_1'); h_1._maxima_()
h_1
sage: h23=var('h23'); h23._maxima_()
h23
sage: ch1=var('ch1'); ch1._maxima_()
ch1
sage: h9=var('h9'); h9._maxima_()
n!/(k!*(m+k)!*(n-m-2*k)!)
```



---

Comment by robert.marik created at 2010-03-31 11:02:17

Changing assignee from burcin to robert.marik.


---

Comment by robert.marik created at 2010-03-31 11:02:17

The discussion at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/67f0a63d00b8d835?pli=1)


---

Comment by robert.marik created at 2010-04-21 13:25:09

Duplicate of #8734 which already has first draft for the patch.


---

Comment by robert.marik created at 2010-04-21 13:25:09

Resolution: duplicate


---

Comment by robert.marik created at 2010-04-21 13:28:36

Oops, I wanted to mark this ticket as duplicate and the ticket has been closed automatically. Sorry for this, I know that only the release manager should close tickets :).


---

Comment by mvngu created at 2010-04-22 00:04:18

Close as duplicate of #8734.
