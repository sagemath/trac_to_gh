# Issue 7023: Upgrade to Cython 0.11.3

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-09-27 07:27:57

Assignee: mabshoff

Just released Cyton 0.11.3. 

http://groups.google.com/group/cython-users/browse_thread/thread/a63639d3246bcf48 

It would be good to have this in Sage. As well as bugfixes and better error reporting, the really nice improvement is the ability to profile Cython code with cProfile and friends. (It's not on by default yet, use the cython.profile directive to enable it for a given module/function). 

All doctests pass after applying the patch, which merely fixes some previously uncaught bugs (useless dead code). 


---

Attachment

Spkg up at http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.3.spkg


---

Comment by jason created at 2009-10-28 09:01:21

Note the upgrade to 0.12 is being tracked at #7272.  That upgrade depends on this patch too.


---

Comment by mhansen created at 2009-11-17 11:05:40

Looks good to me.  I've merged the patch in 4.3.alpha0, but used the spkg from #7272 (along with its patch).


---

Comment by mhansen created at 2009-11-17 11:05:40

Resolution: fixed
