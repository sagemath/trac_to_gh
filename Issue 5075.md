# Issue 5075: Polynomials over inexact rings should not truncate inexact leading zeroes

Issue created by migration from https://trac.sagemath.org/ticket/5075

Original creator: kedlaya

Original creation time: 2009-01-23 19:04:16

Assignee: roed

CC:  dmharvey niles wuthrich

Keywords: polynomials, power series, inexact rings

The generic polynomial class truncates leading zeroes, and this can cause problems when working over an inexact ring in which is_zero can return True even for an inexact zero (e.g., see #2943). Here is a simple example:

```
sage: C.<t> = PowerSeriesRing(Integers())
sage: D.<s> = PolynomialRing(C)
sage: y = O(t)
sage: y
O(t^1)
sage: z = y*s
sage: z
0
sage: z.list()
[]
```

This was recognized earlier for p-adics and fixed (I'm not sure which ticket this was):

```
sage: C = pAdicField(11)
sage: D.<s> = PolynomialRing(C)
sage: y = O(11)
sage: y
O(11)
sage: z = y*s
sage: z
(O(11))*s
```

The other main class of inexact rings are interval fields, but I believe for those is_zero returns False for an inexact zero, so this doesn't come up.


---

Comment by kedlaya created at 2009-01-23 19:56:00

A closely related issue is #3979.


---

Attachment

In progress.  I think it fixes the problem, but I'm working on a larger project for p-adic polynomials that this is part of.


---

Attachment

rebased against 4.0


---

Comment by kedlaya created at 2011-08-01 08:12:00

I tried to apply this against 4.7.1.rc1 and got a bunch of merge failures in power_series_poly.pyx. Probably another trivial rebase is needed.


---

Comment by niles created at 2014-02-03 15:00:28

David, could you give us a rebase for sage 6.1?  I know you're doing a lot of other work for padics, but we're trying to solve a more basic issue with power series comparison at #9457.  Power series over padics are a confusing obstacle there, and we wanted to see if the patch here would help.

Here's the specific bug we're trying to track down (in sage 6.1):  Power series over p-adics are changing inexact zeros to exact zeros -- this looks similar to the problem with polynomials on this ticket, but notice that the problem happens even for p-adics:


```
sage: Ct.<t> = PowerSeriesRing(Qp(11))
sage: O(11^2) # inexact zero
O(11^2)
sage: Ct(O(11^2)) # coercing to power series ring looses finite precision
0
sage: Ct(1+O(11^2)) # finite precision is retained for non-zero elements
1 + O(11^2)
```


There is a problem with multiplication of a p-adic by an element of the power series ring, which might be caused by the problem above:

```
sage: 1+O(11^2)*t  # finite precision is retained
1 + O(11^20) + O(11^2)*t  

sage: O(11^2)*t  # finite precision is lost
0
```


Note that there is a similar problem for more general power series ring over power series ring:


```
sage: D.<x> = PowerSeriesRing(QQ)
sage: Ds.<s> = PowerSeriesRing(D)
sage: O(x)  # inexact zero
O(x^1)
sage: Ds(O(x)) # finite precision is lost
0
sage: Ds(1+O(x)) # finite precision is retained
1 + O(x)

sage: 1+O(x)*s # !! this is different from behavior of power series over padic ring
1
```


My hope is that starting with a rebase of this patch would be a step toward solving this problem.  Perhaps it will have to be extended to power series over inexact rings too.  Unfortunately I don't understand the current status of padics well enough to do this rebase myself.


---

Comment by kedlaya created at 2016-03-23 23:30:20

Ping. Is this issue due to be resolved by other developments on p-adics?


---

Comment by kedlaya created at 2017-09-06 03:24:49

Ping again. The original example still behaves the same way in Sage 8.0.
