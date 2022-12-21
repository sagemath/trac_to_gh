# Issue 8864: make zeta function symbolic

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-05-03 20:58:14

Assignee: AlexGhitza

Consider:

```
sage: zeta(3)
1.20205690315959
```

We expect `zeta(3)` as answer.


---

Comment by zimmerma created at 2010-05-03 21:00:04

Note: this is a followup of #7748.


---

Attachment

With attachment:trac_8864-symbolic_zeta.patch you can do this:


```
sage: zeta(3)
zeta(3)
sage: zeta(2)
1/6*pi^2
```


Probably, the changes to `sage/symbolic/random_tests.py` depend on #6949.


---

Comment by burcin created at 2010-05-06 20:01:38

Changing component from basic arithmetic to symbolics.


---

Comment by burcin created at 2010-05-06 20:01:38

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-05-08 12:08:04

I applied that patch to 4.4.1. The new behaviour is ok, I get only one doctest failure in
`lfunctions/dokchitser.py`. With 4.4.1 we got:

```
sage:  h = RR('0.0000000000001') 
sage: (zeta(2+h) - zeta(2))/h
-0.937028232783632
```

With the patch, we get:

```
sage: h = RR('0.0000000000001') 
sage: (zeta(2+h) - zeta(2))/h
-1.66666666666667e12*pi^2 + 1.64493406684813e13
```

I guess the doctest result has to be changed, or zeta(2) changed to zeta(2.), since Sage does not
automatically propagate floats, for example `pi+1.0` remains unchanged.


---

Comment by zimmerma created at 2010-05-08 12:08:04

Changing status from needs_review to needs_work.


---

Attachment

apply only this patch


---

Comment by burcin created at 2010-05-08 22:24:13

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2010-05-08 22:24:13

I uploaded attachment:trac_8864-symbolic_zeta.take2.patch which also includes a fix for the `lfunctions/dokchitser.py` doctest. I simply replaced `zeta(2)` with `zeta(2)` to get a numeric evaluation.

I agree that `pi+1.0` looks strange, but that is not so trivial to fix. :) FWIW, maple also seems to leave that unevaluated:


```
    |\^/|     Maple 12 (IBM INTEL LINUX)
._|\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple Inc. 2008
 \  MAPLE  /  All rights reserved. Maple is a trademark of
 <____ ____>  Waterloo Maple Inc.
      |       Type ? for help.
> Pi +1.0;
                                   Pi + 1.0

> 1.0*Pi;
                                    1.0 Pi
```



---

Comment by zimmerma created at 2010-05-09 09:21:52

All tests pass now. Thus a positive review. Good work!

Paul


---

Comment by zimmerma created at 2010-05-09 09:21:52

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 07:35:03

Resolution: fixed
