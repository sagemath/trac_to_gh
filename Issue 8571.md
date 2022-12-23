# Issue 8571: Fix the documentation of abstract methods.

Issue created by migration from https://trac.sagemath.org/ticket/8571

Original creator: hivert

Original creation time: 2010-03-21 18:47:03

Assignee: mvngu

CC:  nthiery

Keywords: abstract methods

Currently, the documentation of abstract methods has two annoying problems:
 - it doesn't appear when asked with "?" 
 - nothing says that they are abstract method in the doc.
This should be fixed.


---

Comment by nthiery created at 2010-04-17 10:19:55

We should also think about if/how to merge with Python's new abstractmethods:

http://docs.python.org/library/abc.html
