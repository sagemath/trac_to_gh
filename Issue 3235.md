# Issue 3235: cygwin -- mpfi; get it to work with Cygwin by fixing configure.ac

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-17 03:55:33

Assignee: mabshoff

See also #3188.

The spkg:

  http://sage.math.washington.edu/home/was/cygwin/mpfi-1.3.4-cvs20071125.p6.spkg

SEE THE NOTES in the log.  Note that src/auto-conf-stuff is also changed.


---

Comment by mabshoff created at 2008-05-18 17:05:51

Spkg looks good to me. I added a diff of configure.ac.orig and configure.ac so that we can send the patch upstream. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-18 17:06:04

Resolution: fixed


---

Comment by mabshoff created at 2008-05-18 17:06:04

Merged in Sage 3.0.2.alpha1
