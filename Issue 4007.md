# Issue 4007: OSX 10.4/5: build libpng.dylib again

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-08-30 23:39:07

Assignee: mabshoff

On OSX we delete libpng.dylib due to missing symbols when building R and python. But this is causing trouble for code at #3324 for example. The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha3/libpng-1.2.22.p8.spkg

does no longer delete the old dynamic lib. But this ticket needs to be merged with the following two tickets updating R and python.


---

Comment by mabshoff created at 2008-08-30 23:43:25

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-30 23:51:57

Resolution: fixed


---

Comment by mabshoff created at 2008-08-30 23:51:57

Merged in Sage 3.1.2.alpha3
