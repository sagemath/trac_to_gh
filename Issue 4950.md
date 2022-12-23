# Issue 4950: Sage-3.2.3 won't build on mandriva 32-bit due to an issue with numpy

Issue created by migration from https://trac.sagemath.org/ticket/4950

Original creator: was

Original creation time: 2009-01-07 15:53:41

Assignee: mabshoff


```
Michael: Only one has failed to build so far -- mandriva 32-bit.   It
fails thus, and as you can see below, the numpy install fails maybe
due to an ATLAS issue.  This is actually a pretty serious build issue,
and should go in trac, if you agree:

gcc version 4.3.2 (GCC)
****************************************************
============================================================================
BUILDING MATPLOTLIB
           matplotlib: 0.98.3
               python: 2.5.2 (r252:60911, Jan  6 2009, 18:03:10)  [GCC
                       4.3.2]
             platform: linux2

REQUIRED DEPENDENCIES
                numpy: no
                       * You must install numpy 1.1 or later to build
                       * matplotlib.
Error building matplotlib package.
Command exited with non-zero status 1
0.08user 0.44system 0:12.28elapsed 4%CPU (0avgtext+0avgdata 0maxresident)k
42304inputs+360outputs (17major+4611minor)pagefaults 0swaps
sage: An error occurred while installing matplotlib-0.98.3.p4
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/wstein/build/mandriva32/build/sage-3.2.3/install.log.
Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/home/wstein/build/mandriva32/build/sage-3.2.3/spkg/build/matplotlib-0.98.3.p4
and type 'make'.
Instead type "/home/wstein/build/mandriva32/build/sage-3.2.3/sage -sh"
in order to set all environment variables correctly, then cd to
/home/wstein/build/mandriva32/build/sage-3.2.3/spkg/build/matplotlib-0.98.3.p4
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/matplotlib-0.98.3.p4] Error 1
make[1]: Leaving directory `/home/wstein/build/mandriva32/build/sage-3.2.3/spkg'
Command exited with non-zero status 2
2.83user 6.96system 23:46.58elapsed 0%CPU (0avgtext+0avgdata 0maxresident)k
52520inputs+41128outputs (22major+14379minor)pagefaults 0swaps

NOTE THAT:

wstein@mandriva32:~/build/mandriva32/build/sage-3.2.3$ ./sage -python
Python 2.5.2 (r252:60911, Jan  6 2009, 18:03:10)
[GCC 4.3.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/home/wstein/build/mandriva32/build/sage-3.2.3/local/lib/python2.5/site-packages/numpy/__init__.py",
line 138, in <module>
   import linalg
 File "/home/wstein/build/mandriva32/build/sage-3.2.3/local/lib/python2.5/site-packages/numpy/linalg/__init__.py",
line 47, in <module>
   from linalg import *
 File "/home/wstein/build/mandriva32/build/sage-3.2.3/local/lib/python2.5/site-packages/numpy/linalg/linalg.py",
line 29, in <module>
   from numpy.linalg import lapack_lite
ImportError: /home/wstein/build/mandriva32/build/sage-3.2.3/local/lib/liblapack.so:
undefined symbol: zhpr_

```


I made this a blocker since Mandriva is in our "officially supported" list according to README.txt


---

Comment by mabshoff created at 2009-02-14 15:55:27

William,

wasn't this a nohup problem? What is the status here?

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-16 05:07:30

This will either come out in testing of 3.3.rc1 on the build farm as fixed or we will need to fix it, so move it against 3.3

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 02:15:29

I don't care about this enough to keep this a blocker against 3.4, so make this critical against 3.4.1. This is an interaction between nohup and gcc, so it is an upstream bug.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 02:15:29

Changing priority from blocker to critical.


---

Comment by thisch created at 2010-04-05 21:20:06

I have the same problem on Fedora 12 (64bit) with matplotlib version 0.99.1 and Sage 4.3.5

Regards
Thomas


---

Comment by jdemeyer created at 2013-11-28 11:06:52

Resolution: invalid


---

Comment by jdemeyer created at 2013-11-28 11:06:52

Closing as obsolete...
