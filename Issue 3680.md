# Issue 3680: NumberFieldFractionalIdeal should not be a subclass of Ideal_generic

Issue created by migration from https://trac.sagemath.org/ticket/3680

Original creator: dmharvey

Original creation time: 2008-07-19 13:36:55

Assignee: tbd

CC:  alexghitza pbruin

Why is `NumberFieldFractionalIdeal` a subclass of `Ideal_generic`?

A fractional ideal is *not* an ideal.

This makes about as much as sense as having `Rational` be a subclass of `Integer`.

This has been discussed before:

http://groups.google.com/group/sage-devel/browse_thread/thread/0b01d58d8c3565c2/c081ba96b5fed6eb?#c081ba96b5fed6eb

And it came up again recently in #1367.

There seem to be serious design issues with the whole algebraic number theory setup in Sage which make it very frustrating to do any serious work on things like #1367.



---

Comment by AlexGhitza created at 2009-01-28 22:01:29

Changing component from algebra to number theory.


---

Comment by AlexGhitza created at 2009-01-28 22:01:29

Changing assignee from tbd to was.


---

Comment by davidloeffler created at 2009-07-20 20:08:09

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-20 20:08:09

Changing assignee from was to davidloeffler.
