# Issue 6914: update scipy to 0.7.1

Issue created by migration from Trac.

Original creator: fpatzelt

Original creation time: 2009-09-10 11:12:22

Assignee: mabshoff

Keywords: scipy 0.7.1, python 2.6

Scipy 0.7 includes known issues with python 2.6. The first Bugfix release (0.7.1) is already available. 

On [sourceforge](http://sourceforge.net/projects/scipy/files/), scipy 0.7 is only offered for use with python 2.4 or 2.5. scipy 0.7.1 on the other hand is available with support for python 2.6 which also seems to require numpy 1.3.0 or above.
Since sage now includes python 2.6, scipy should be updated to the latest version.

This ticket was created as a result of [this support thread](http://groups.google.com/group/sage-support/browse_thread/thread/e102047bfd334027/a75bd16035329155?lnk=gst&q=weave#a75bd16035329155).


---

Comment by timdumol created at 2010-01-18 19:33:01

Here's a new package: http://boxen.math.washington.edu/home/timdumol/scipy-0.7.1.spkg. It removes some obsolete patches that are superseded by changes in SciPy 0.7.1.


---

Comment by timdumol created at 2010-01-18 19:33:01

Changing status from new to needs_review.


---

Comment by jason created at 2010-01-20 08:47:53

The exact same issue is addressed in #7442.


---

Comment by jason created at 2010-01-20 10:29:24

Duplicate of #7442


---

Comment by jason created at 2010-01-20 10:29:24

Resolution: duplicate
