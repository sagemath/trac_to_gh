# Issue 3234: [with patch; needs review] cygwin -- make numpy work with cygwin

Issue created by migration from https://trac.sagemath.org/ticket/3234

Original creator: was

Original creation time: 2008-05-17 00:39:17

Assignee: mabshoff

Patch here:

http://sage.math.washington.edu/home/was/cygwin/numpy-20080104-1.0.4.p3.spkg


---

Comment by mabshoff created at 2008-05-18 13:28:50

Spkg looks good to me. I think that the core issue is with ATLAS's dynamic libraries being miscompiled on Cygwin, but we can explore that down the road. Having a working, but slightly slower,  numpy for now is better than no numpy at all on Cygwin.

I also fixed some small formatting issue in SPKG.txt. In total: positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-18 13:29:06

Merged in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-18 13:29:06

Resolution: fixed
