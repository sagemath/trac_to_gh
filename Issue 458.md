# Issue 458: plot.py: NameError: name 'p1' is not defined

Issue created by migration from https://trac.sagemath.org/ticket/458

Original creator: mhansen

Original creation time: 2007-08-19 14:25:13

Assignee: was


And this is the last one:

**********************************************************************
File "plot.py", line 2836:
   sage: g = graphics_array([p1, p2]); g
Exception raised:
   Traceback (most recent call last):
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/
doctest.py", line 1212, in __run
       compileflags, 1) in test.globs
     File "<doctest __main__.example_60[11]>", line 1, in <module>
       g = graphics_array([p1, p2]); g###line 2836:
   sage: g = graphics_array([p1, p2]); g
   NameError: name 'p1' is not defined
**********************************************************************

Cheers,

Michael




---

Comment by rlm created at 2007-08-19 16:44:40

Fix is here:

http://sage.math.washington.edu/home/rlmill/plot.patch


---

Comment by rlm created at 2007-08-19 16:44:40

Resolution: fixed
