# Issue 5456: remove 32/64 bit dependency in modular symbols base enumerations

Issue created by migration from https://trac.sagemath.org/ticket/5456

Original creator: GeorgSWeber

Original creation time: 2009-03-08 10:05:57

Assignee: was

CC:  was

This is a follow-up ticket to #5428.

See the discussion there, I'll attach a preliminary patch (untested) for the "root cause". However, this change will break many doctests (see #5428). These are easy to fix, but make necessary a much larger patch (touching more than a dozen files) than the preliminary one.


---

Comment by GeorgSWeber created at 2009-03-08 10:10:48

don't use (preliminary only)


---

Attachment


---

Comment by davidloeffler created at 2013-07-25 17:28:41

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2013-07-25 17:28:41

Changing component from number theory to modular forms.
