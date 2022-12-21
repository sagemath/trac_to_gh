# Issue 9306: round incoherent with ceil/floor on rational numbers

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-06-22 09:20:05

Assignee: AlexGhitza

Consider the following:

```
sage: q=2^200/3^50
sage: q.floor()
2238393297946874000179418290327143433
sage: q.ceil()
2238393297946874000179418290327143434
sage: q.round()
2238393297946874000179418290327143433
```

This is fine so far. However:

```
sage: floor(q)
2238393297946874000179418290327143433
sage: ceil(q)
2238393297946874000179418290327143434
sage: round(q)
2.23839329795e+36
```

We would expect `round(q)` to behave like `q.round()`.


---

Attachment

Changes the round() command to defer to an element's .round() method if no precision is specified.


---

Comment by spice created at 2011-03-22 21:20:21

The above change alters the behaviour of sage's round() command. Before it *always* returned a real double field element; now it defers to an element's .round() method if no precision is specified, i.e. a sage Integer is returned in these cases. This makes round(x) and x.round() agree whenever x has a .round() method.


---

Comment by spice created at 2011-03-22 21:20:21

Changing status from new to needs_review.


---

Comment by spice created at 2011-03-22 21:20:21

Changing keywords from "" to "round".


---

Comment by kini created at 2011-03-23 01:30:47

Five doctests failed, then failed to fail when I retested them, including devel/sage/sage/tests/startup.py . Code is easy to read and clearly does what it is intended to do, which intent I agree with. Everything looks good!


---

Comment by kini created at 2011-03-23 01:30:47

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-07 13:48:34

Resolution: fixed
