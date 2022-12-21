# Issue 5979: Parent: fixes broken (implicit) invariant between ._element_constructor and self._element_init_pass_parent

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-05-04 16:40:54

Assignee: nthiery

CC:  sage-combinat

Keywords: coercion, parents, element_constructor

In Parent, there is an implicit invariant, namely that

	self._element_init_pass_parent == guess_pass_parent(between ._element_constructor)

This invariant was broken when self._element_constructor was set from
self._element_constructor_ by __call__. This made the parent not to be
passed properly to _element_constructor.

The category patch #5891 depends heavily on this one, as this way of
setting _element_constructor becomes the default one for simple
parents.

By the way, this patch makes a related trivial fix to a line that is
apparently never used in coerce_maps, and adds a comment about it.


---

Attachment


---

Comment by nthiery created at 2009-05-04 18:48:02

I should mention that sage -testall passes smoothly with sage-3.4.2-alpha0 (except for a trivial broken test in interfaces.r which also fails before applying the patch).
Haven't tried it with sage-3.4.2 final (under compilation)


---

Comment by nthiery created at 2009-05-19 06:25:44

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-01 00:04:48

Resolution: fixed


---

Comment by mhansen created at 2009-06-01 00:04:48

Merged in 4.0.1.alpha0.
