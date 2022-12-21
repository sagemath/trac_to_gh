# Issue 3390: update numpy to the 1.1.0 release

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-06-10 19:05:17

Assignee: mabshoff




---

Comment by jason created at 2008-07-14 20:44:41

An spkg for this is up at:

http://sage.math.washington.edu/home/jason/numpy-1.1.0.spkg

There are lots of doctest errors stemming I believe from matplotlib referencing things in old locations.  See #3392 for the matplotlib upgrading ticket.


---

Attachment


---

Comment by mabshoff created at 2008-08-27 10:29:12

Spkg looks good to me. I did some cleanups in the patches directory. That spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha1/numpy-1.1.0.p0.spkg

Also positive review for the patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-27 11:29:52

Resolution: fixed


---

Comment by mabshoff created at 2008-08-27 11:29:52

Merged in Sage 3.1.2.alpha1
