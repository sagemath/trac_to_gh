# Issue 5619: doctests for error messages in groebner_fan.py

Issue created by migration from https://trac.sagemath.org/ticket/5619

Original creator: mvngu

Original creation time: 2009-03-27 02:48:38

Assignee: mhampton

CC:  mhampton

Keywords: groebner_fan.py, doctest

This is a follow-up to ticket #5465. Here, we add some doctests to check the error messages being raised.


---

Comment by mvngu created at 2009-03-27 03:40:41

The patch *trac_5619-doctests.patch* adds two doctests to `groebner_fan.py`. The doctests check the error messages that can be raised by the functions `render()` and `render3d()`. Currently, these error messages are of the `NotImplementedError` type. This patch depends on ticket #5465.


---

Attachment

These make sense, and appear to work.  Positive review.


---

Comment by mabshoff created at 2009-05-21 00:31:01

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-21 00:31:01

Resolution: fixed
