# Issue 5073: [with spkg, needs review] Update IPython to 0.9.1

Issue created by migration from https://trac.sagemath.org/ticket/5073

Original creator: mhansen

Original creation time: 2009-01-23 13:20:45

Assignee: mabshoff

An spkg can be found at http://sage.math.washington.edu/home/mhansen/ipython-0.9.1.spkg


---

Comment by mhansen created at 2009-01-24 08:09:19

There is a patch in this package fixes #5051.


---

Comment by boothby created at 2009-01-24 11:08:52

Works for me, and #5051 is resolved as a result.


---

Comment by mabshoff created at 2009-01-24 19:12:09

Two small things to fix:

 * SPKG.txt lacks an entry for the latest version
 * SPKG.txt could also benefit from a list of the patches we apply and what they fix

I also verified that the spkg still works with -gdb under OSX.

Cheers,

Michael


---

Comment by mhansen created at 2009-01-24 22:21:23

I've updated the SPKG to address the above two concerns.


---

Comment by mhansen created at 2009-01-24 22:21:23

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-24 22:21:23

Changing assignee from mabshoff to mhansen.


---

Comment by mabshoff created at 2009-01-25 01:49:49

Positive review for the changes Mike did to SPKG.txt.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-25 01:49:59

Merged in Sage 3.3.alpha2


---

Comment by mabshoff created at 2009-01-25 01:49:59

Resolution: fixed
