# Issue 905: update the version of ipython included in sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-16 01:39:38

Assignee: was

CC:  mabshoff




---

Comment by burcin created at 2008-05-11 16:25:45

Changing assignee from was to burcin.


---

Comment by burcin created at 2008-05-11 16:25:45

Changing status from new to assigned.


---

Comment by burcin created at 2008-05-11 16:25:45

New package with upstream version 0.8.2 available here:

http://www.risc.uni-linz.ac.at/people/berocal/sage/ipython-0.8.2.spkg

It works for me.

There are quite a few entries in trac about updating ipython, see #1625, #1264, #1969.

#1625 is a duplicate of this. The problem mentioned in #1264 doesn't happen with 0.8.2. I didn't update to svn as mentioned in #1969, since I don't know if it is stable enough to distribute with Sage.


---

Comment by mabshoff created at 2008-05-11 19:31:57

A couple remarks:

 * no need to add me to the CC - I get email from all tickets anyway
 * there is no hg repo in the spkg. I am fixing that
 * "cp patches/iplib.py src/IPython/iplib.py" should be removed from spkg-install

I will do all those fixes and provided it installs I will give it a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-11 19:40:33

I did all the above cleanups in 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2/alpha0/ipython-0.8.2.p0.spkg

Positive review since it install and doctests pass. Let's hope we didn't break anything else.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-11 19:40:47

Resolution: fixed


---

Comment by mabshoff created at 2008-05-11 19:40:47

Merged in Sage 3.0.2.alpha0
