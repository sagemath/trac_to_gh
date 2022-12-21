# Issue 6319: optional doctest failure -- mistake in constructions guide wrt maxima interface

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 14:47:30

Assignee: tbd

CC:  awebb

This was clearly *never* tested, since eval always returns a string (it can't return nothing). 


```
sage -t -long --optional devel/sage/doc/en/constructions/plotting.rst
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/plotting.rst", line 211:
    sage: maxima.eval('plotdf(x+y,[trajectory_at,2,-0.1]); ') #optional
Expected nothing
Got:
    '1'
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_11
```





---

Comment by wdj created at 2009-06-16 23:25:31

applies to 4.0.2.rc1


---

Attachment

Passes sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/. Also the builds sage -docbuild  constructions html (resp., pdf) went fine.


---

Comment by awebb created at 2009-07-16 06:31:04

I still get an error with sage -t -long --optional devel/sage/doc/en/constructions/plotting.rst, although it is with a return value of '0' instead of '1'. It passes sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/ for me as well. 

The odd thing is that if I try the test from the sage command line I don't get the string returned i.e. the test passes.  Or is it fine if 'sage -t' fails but the documentation is correct for what happens when you actually run it?

Adam
