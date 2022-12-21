# Issue 7708: upgrade openopt spkg to 0.27

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2009-12-16 10:40:58

Assignee: tbd

[announcement was here](http://groups.google.com/group/sage-support/browse_thread/thread/ddc22bcd971b69fd)

[http://openopt.org/](http://openopt.org/)


---

Comment by was created at 2009-12-24 07:07:47

I'm declaring a total feature freeze on sage-4.3.


---

Comment by schilly created at 2010-01-26 13:10:03

I have created an enhanced and updated version of openopt. It is a pre release of the next 0.28 release (revision 404). Once 0.28 is released, upgrade should be easy. 

 1. it now consists of 3 packages, all togehter are called the "OO-Suite". and hence I've included all three.
 1. I have to disable the preparser `preparser(False)` to get examples for all three packages working.

[openopt spkg](http://boxen.math.washington.edu/home/schilly/sage/spkg/)


---

Comment by schilly created at 2010-01-26 13:10:03

Changing status from new to needs_work.


---

Comment by schilly created at 2010-03-16 11:15:21

Changing status from needs_work to needs_review.


---

Comment by schilly created at 2010-03-16 11:15:21

I've updated openopt's spkg to 0.28 which you can find here:
[openopt spkg](http://boxen.math.washington.edu/home/schilly/sage/spkg/)

it contains the entire openopt suite and as stated above, you need to set `preparse(False)` and then test it via a script like 
[nsp_1.py](http://trac.openopt.org/openopt/browser/PythonPackages/OpenOpt/openopt/examples/nsp_1.py) .


---

Comment by schilly created at 2010-07-09 08:47:34

Changing status from needs_review to needs_work.


---

Comment by schilly created at 2010-08-02 10:49:49

Created [OpenOpt SPKG for OOSuite 0.29](http://boxen.math.washington.edu/home/schilly/sage/spkg/openopt-0.29.spkg)


---

Comment by schilly created at 2010-08-02 10:49:49

Changing status from needs_work to needs_review.


---

Comment by schilly created at 2010-08-05 13:51:56

I hereby announce myself as the maintainer of this spkg and declare it as "contributed" / "experimental". If nobody objects, I'll remove the long outdated optional one and upload this new one.


---

Comment by schilly created at 2010-08-11 19:41:12

Changing assignee from tbd to schilly.


---

Comment by schilly created at 2010-08-18 16:21:10

Resolution: fixed


---

Comment by schilly created at 2010-08-18 16:21:10

version 0.29 now in experimental and I removed the obsolete old optional spkg. ticket can be closed.
