# Issue 6874: #4135 follow-up: fix typos and docbuild warnings

Issue created by migration from https://trac.sagemath.org/ticket/6874

Original creator: mvngu

Original creation time: 2009-09-03 10:27:09

Assignee: tba

CC:  ddrake timdumol

After merging the patch `trac_4135.5.patch` at #4135, rebuilding the reference manual results in a warning:

```
WARNING: <autodoc>:0: (ERROR/3) Error in "module" directive:
no content permitted.

.. module:: sage.server.notebook.twist

    TESTS::

    It is important that this file never be imported by default on
    startup by Sage, since it is very expensive, since importing Twisted
    is expensive. This doctest verifies that twist.py isn't imported on
    startup.

    sage: os.system("sage -startuptime | grep twisted\.web2 1>/dev/null") != 0  # !=0 means not found
    True
```




---

Comment by mvngu created at 2009-09-03 10:36:43

depends on #4135


---

Attachment


---

Comment by ddrake created at 2009-09-03 12:18:34

Looks good. Positive review.


---

Comment by ddrake created at 2009-09-03 12:18:34

Changing assignee from tba to mvngu.


---

Comment by mvngu created at 2009-09-03 21:38:09

Resolution: fixed
