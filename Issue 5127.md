# Issue 5127: relative number fields have bad names for internal coercion routines

Issue created by migration from https://trac.sagemath.org/ticket/5127

Original creator: ncalexan

Original creation time: 2009-01-29 05:09:02

Assignee: was

CC:  roed tscrim mkoeppe

Keywords: relative number fields names coercion

A naming one issue: in relative number fields, the family of functions coerce_non_number_field_element_in should probably be a convert function rather than a coerce one.



---

Comment by davidloeffler created at 2009-07-21 08:03:38

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-21 08:03:38

Changing assignee from was to davidloeffler.


---

Comment by chapoton created at 2020-07-02 13:42:04

This has been done elsewhere, so this is now invalid.


---

Comment by chapoton created at 2020-07-02 13:42:04

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-02 14:04:15

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-07-02 14:05:22

Resolution: invalid
