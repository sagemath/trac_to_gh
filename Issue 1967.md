# Issue 1967: fix matplotlib local-related bugs once and for all (?)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-29 09:57:58

Assignee: was

Many people have reported issues with locale.py going boom on quite a range of different OS X (and Linux?) machines.  The very slightly patched version of 

  SAGE_ROOT/local/lib/python2.5/site-packages/matplotlib/cbook.py

attached to this ticket may very likely fix the problem.  See this thread:
  
  http://groups.google.com/group/sage-support/browse_thread/thread/edcf2740f7276e6a?hl=en#78ee7d78a0a99f12

If this really turns out to be the fix, cbook.py should be put into the matplotlib spkg as a patch. 




---

Attachment

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc4/matplotlib-0.91.1.p3.spkg

fixes this issue as well as #2014

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-01 02:00:02

Resolution: fixed


---

Comment by mabshoff created at 2008-02-01 02:00:02

Merged in Sage 2.10.1.rc4
