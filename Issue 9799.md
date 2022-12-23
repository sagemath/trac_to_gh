# Issue 9799: doctutils fails to run test suite when SAGE_CHECK=yes. Missing spkg-check

Issue created by migration from https://trac.sagemath.org/ticket/9800

Original creator: drkirkby

Original creation time: 2010-08-25 13:00:18

Assignee: drkirkby

CC:  leif mpatel

The `docutils` package, which is at version 0.5 in sage, lacks a spkg-check file, so the self-tests can't be run. But the package has a set of tests, which according to the `README.txt` is executed as below. 


```
Running the Test Suite
======================

To run the entire test suite, after installation_ open a shell and use
the following commands::

    cd <archive_directory_path>/test
    ./alltests.py
```




---

Comment by kini created at 2011-03-24 01:12:06

typo


---

Comment by kini created at 2011-03-24 01:12:06

Changing keywords from "" to "docutils".
