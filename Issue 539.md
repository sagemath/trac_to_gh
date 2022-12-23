# Issue 539: Integer.__int__

Issue created by migration from https://trac.sagemath.org/ticket/539

Original creator: dmharvey

Original creation time: 2007-08-31 01:24:26

Assignee: somebody

The `Integer.__int__` method was recently changed to use the new `mpz_get_pyintlong` function. This had to be disabled for 2.8.3 because of strange problems on 64-bit architectures, relating we think somehow to the resolution of #411. Figure out what was going wrong and re-enable that functionality (since `mpz_get_pyintlong` is faster than going via a python long every time).



---

Comment by was created at 2007-09-07 03:27:43

Resolution: fixed
