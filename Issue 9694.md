# Issue 9694: Implement direct product of cyclic groups

Issue created by migration from https://trac.sagemath.org/ticket/9694

Original creator: rbeezer

Original creation time: 2010-08-06 02:59:40

Assignee: joyner

CC:  was davidloeffler cremona

This will be a straightforward implementation of a direct product of cyclic groups, allowing students to experiment with basic notions of order, cyclicness, subgroups, etc.


---

Comment by rbeezer created at 2010-08-06 03:04:04

Preliminary version, no doctests, etc


---

Attachment

Patch is a rough cut. Requires something in the 4.5.2 alpha/rc series to work.

Posted here because of the hack to avoid having the `__call__` function in the derived class not get called during the initialization.

Somewhere (once per invariant, I think) the creation of the optimized quotient module has a "self()" call that reaches all the way down into this class and if the optimized module is used for conversion, it just causes infinite recursion.  (Also happens with saving _orig_gens but that is more obvious).

Need for the conversion is described more fully at #9695.  Help or advice needed!


---

Comment by rbeezer created at 2010-08-06 03:25:50

Changing status from new to needs_info.


---

Comment by rbeezer created at 2010-08-23 06:53:50

This ticket can be killed.  Work at #9773 supersedes it, while comments at #9695 explains some of my confusion.


---

Comment by rbeezer created at 2010-08-23 06:53:50

Changing status from needs_info to needs_work.
