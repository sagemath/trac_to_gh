# Issue 9480: Sage mixes Infinity and +Infinity

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-07-12 12:48:51

Assignee: burcin

This is related to #8942. The limit function can output either
`+Infinity`, `-Infinity`, or `Infinity`, the later
meaning a complex infinity. For example:

```
sage: limit(1/x, x=0, dir='above')
+Infinity
sage: limit(1/x, x=0, dir='below')
-Infinity
sage: limit(1/x, x=0)             
Infinity
```

However Sage does not distinguish `+Infinity` and `Infinity`:

```
sage: l1=limit(1/x, x=0, dir='above')
sage: l2=limit(1/x, x=0, dir='below')
sage: l3=limit(1/x, x=0)
sage: l1==l3
True
```



---

Comment by burcin created at 2010-08-29 10:54:14

This is more of a problem with the equality checking rules in Sage and the coercion system than symbolics, so I'm changing the component to coercion.

If the arguments compare equal when coerced to a common parent, Sage returns `True` for the equality. In this case, the coercion goes to the `UnsignedInfinityRing`, where `+Infinity` is mapped to `unsigned_infinity`.


```
sage: UnsignedInfinityRing.has_coerce_map_from(InfinityRing)
True
sage: Infinity
+Infinity
sage: UnsignedInfinityRing.coerce(Infinity)
Infinity
```


BTW, isn't there an inconsistency in the capitalization of `Infinity`. Shouldn't it be lowercase according to Python conventions?


---

Comment by burcin created at 2010-08-29 10:54:14

Changing assignee from burcin to robertwb.


---

Comment by burcin created at 2010-08-29 10:54:14

Changing keywords from "" to "infinity, equality".


---

Comment by burcin created at 2010-08-29 10:54:14

Changing component from calculus to coercion.


---

Comment by tscrim created at 2012-05-11 13:39:10

Sometimes it's `infinity` and others its `Infinity`. At the very least this should be consistent. Also there are other issues with infinity: #11506 #9547.


---

Comment by zimmerma created at 2013-08-25 13:45:01

in Sage 5.11 we get:

```
sage: l1=limit(1/x, x=0, dir='right'); l1
+Infinity
sage: l2=limit(1/x, x=0, dir='left'); l2 
-Infinity
sage: l3=limit(1/x, x=0); l3             
Infinity
sage: bool(l1==l2), bool(l2==l3), bool(l3==l1)
(False, False, False)
```

however the objects returned are in SR and not in the `infinity` class:

```
sage: type(l1), l1.parent()
(sage.symbolic.expression.Expression, Symbolic Ring)
sage: p1=+Infinity
sage: type(p1), p1.parent()
(sage.rings.infinity.PlusInfinity, The Infinity Ring)
```

I propose to close that ticket, and open a new one about the above issue (or add it to an existing ticket).

Paul


---

Comment by zimmerma created at 2013-08-25 13:45:01

Changing status from new to needs_review.


---

Comment by zimmerma created at 2013-08-25 13:59:34

> or add it to an existing ticket

I've added a comment in #14857

Paul


---

Comment by ncohen created at 2013-12-26 19:26:33

Changing status from needs_review to needs_info.


---

Comment by ncohen created at 2013-12-26 19:26:33

No patch to review on this ticket...

Paul : when you want to close a ticket, you should set its milestone to wontfix/duplicate, say why on a comment, and change the status to `positive_review` so that the release manager will see it.

Nathann


---

Comment by zimmerma created at 2014-01-03 09:36:30

in Sage 6.0 we get:

```
sage: l1=limit(1/x, x=0, dir='above')
sage: l3=limit(1/x, x=0)
sage: bool(l1==l3)
False
```

thus the issue is fixed now, and I change the status to "fixed".

Paul


---

Comment by zimmerma created at 2014-01-03 09:36:30

Resolution: fixed


---

Comment by zimmerma created at 2014-01-03 09:38:05

sorry when changing to "fixed" (which made more sense to me than invalid or wontfix) the status was changed automatically to "closed"...

Paul


---

Comment by tscrim created at 2014-01-03 15:09:06

I also verified that it works in `6.1.beta2`.
