# Issue 803: Tests for what kind of an element something is should test the parent

Issue created by migration from https://trac.sagemath.org/ticket/803

Original creator: roed

Original creation time: 2007-10-03 08:13:00

Assignee: somebody

Calls like:

```
algebras/algebra_order.py:        elif isinstance(x, RingElement) and x in self.base_ring():
algebras/algebra_order_ideal.py:        elif isinstance(x, RingElement) and x in self.base_ring():
algebras/free_algebra_quotient_element.py:        elif isinstance(x, RingElement) and not isinstance(x, AlgebraElement) and x in R:
rings/infinity.py:        elif isinstance(x, RingElement) or isinstance(x, (int,long,float,complex)):
rings/infinity.py:        elif isinstance(x, RingElement):
```


should actually be checking to see if the parents are of the appropriate type.  The element types are not always reliable: parents more accurately reflect the mathematical structure (mostly because they can have multiple inheritance).

There may be more instances in addition to those above (I just ran `search_src("isinstance(x, RingElement)")`)




---

Comment by was created at 2008-02-25 05:37:08

I'm dubious:

>

My immediate thought when looking at #803 is that it is the wrong
idea in the first place.  If I had looked at #803 before
now I would have considered marking it "invalid".

There are individual instances that involve "isinstance" that were
perhaps badly written.  E.g., the first example:

```
        elif isinstance(x, RingElement) and x in self.base_ring():
            return True
```

Here I think the original author (David Kohel) may have written
this at a time when "in" could raise an exception if x isn't
a RingElement.  That's no longer the case, so in this particular
example the right fix is I think to put:

```
        elif x in self.base_ring():
            return True
```

In probably hundreds of other cases the use of isinstance in
Sage is exactly right.  In some cases it could be improved,
but how will depend in each case on understanding the code.


---

Comment by mmezzarobba created at 2015-04-13 14:54:15

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2015-04-14 09:38:11

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-04-14 23:05:29

Resolution: wontfix
