# Issue 3236: [with patch; needs review] cygwin -- quaddouble -- get it to work with cygwin

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-17 05:39:12

Assignee: mabshoff

Here it is:

   http://sage.math.washington.edu/home/was/cygwin/quaddouble-2.2.p8.spkg

I also fixed up the internals of the spkg some, etc. 


---

Comment by mabshoff created at 2008-05-18 13:08:21

Spkg looks good to me. The src directory is potentially a mess, but that is not due to the work on this ticket. We need to update the source to the latest release anyway, so we will deal with that issue then, i.e. #1631.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-18 13:08:37

Merged in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-18 13:08:37

Resolution: fixed
