# Issue 7603: add methods to query representation of symbolic expressions

Issue created by migration from https://trac.sagemath.org/ticket/7603

Original creator: burcin

Original creation time: 2009-12-04 13:07:45

Assignee: burcin

CC:  fmaltey@nerim.fr

Attached patch adds `_is_symbol()`, `_is_constant()` and `_is_numeric()` methods to `sage.symbolic.expression.Expression` objects.

These methods are just a thin wrapper around the `is_a<*>()` methods from pynac. They should provide a straightforward interface to query the internal representation of a symbolic expression when `.operator()` returns None.

Some relevant discussion on sage-devel:

http://groups.google.com/group/sage-devel/msg/6323b473af195bc7



---

Attachment


---

Comment by burcin created at 2009-12-04 13:18:09

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-12-06 08:31:01

Looks good.


---

Comment by mhansen created at 2009-12-06 08:31:01

Resolution: fixed
