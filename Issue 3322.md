# Issue 3322: [with spkg needs review] new python spkg with -j enabled

Issue created by migration from https://trac.sagemath.org/ticket/3322

Original creator: gfurnish

Original creation time: 2008-05-28 14:05:59

Assignee: mabshoff

Keywords: python

Using -j with make for python seems to be fixed.  It passes stress tests on both my machine and sage-math.  The spkg is based off of the one in #3318 and is located at http://sage.math.washington.edu/home/gfurnish/spkg/python-2.5.2.p1.spkg


---

Comment by mabshoff created at 2008-05-28 14:27:38

A properly updated spkg is at:

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/python-2.5.2.p2.spkg

Since this is Gary's fix I give it a positive review. I did multiple runs with "-j64".

Cheers,

Michael


---

Attachment

Merged in Sage 3.0.3.alpha0


---

Comment by mabshoff created at 2008-05-28 14:29:42

Resolution: fixed
