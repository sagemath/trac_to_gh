# Issue 7574: clean up of MIP interface

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-12-01 17:33:00

Assignee: jkantor

There are a few issues with the MIP code:
- ``max`` and ``min`` are built-in core functions in Python and shouldn't be used as variable names
- ``id`` shouldn't be used as a variable name
- I don't think we should have ``try: foo except: bar`` blocks without a specific ``except ThisandThatError``.


---

Comment by mkoeppe created at 2016-06-25 06:10:34

Changing keywords from "" to "lp".


---

Comment by mkoeppe created at 2016-06-25 06:10:34

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2016-06-25 06:10:34

This is outdated. The first issue is duplicated in #20664. Can be closed.


---

Comment by chapoton created at 2016-07-13 18:52:41

ok


---

Comment by chapoton created at 2016-07-13 18:52:41

Changing status from needs_review to positive_review.


---

Comment by embray created at 2016-08-30 13:32:25

Resolution: wontfix


---

Comment by embray created at 2016-08-30 13:32:25

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).
