# Issue 2732: cython in Debian build doesn't work

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-03-30 02:43:24

Assignee: tabbott

Doing cython builds on Debian doesn't work, because it doesn't have the right include_dirs.

There seems to be a lot of code re-use between spkg/standard/sage-2.10.5/sage/misc/cython.py and spkg/standard/sage-2.10.5/setup.py.  It might be good to merge that code into only one place; if we don't do that, we'll probably want to make the changes we made to spkg/standard/sage-2.10.5/setup.py to spkg/standard/sage-2.10.5/sage/misc/cython.py.  

Regardless, we should have a way of specifying that we've got a Debian build at runtime (currently we only have a build-time specification).  Probably this will just mean having the SAGE wrapper script in Debian set SAGE_DEBIAN=yes.


---

Comment by tabbott created at 2008-03-30 05:40:21

Well, I installed all the development libraries needed to build SAGE at runtime, and the doctests for misc/cython.py all pass at the moment.  But I suspect there will probably still be problems with the include path not having everything.


---

Comment by mabshoff created at 2008-08-22 20:05:46

Tim,

can this ticket be closed? It seems to have gone stale.

Cheers,

Michael


---

Comment by tabbott created at 2008-08-22 20:40:12

This has indeed grown stale, in part because I've not actually had any problems passing tests despite this issue and in part because I've been very busy lately.

However, I think there is a real problem if someone wants to write some code using libraries normally packaged as part of Sage in the Sage cython environment in a packaged sage.


---

Comment by jdemeyer created at 2012-04-19 10:00:22

Closing this, since we've dropped support for a Debian package.


---

Comment by jdemeyer created at 2012-04-19 10:00:22

Resolution: invalid
