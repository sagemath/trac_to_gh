# Issue 6024: ecl->clisp switch

Issue created by migration from https://trac.sagemath.org/ticket/6024

Original creator: mabshoff

Original creation time: 2009-05-12 06:11:52

Assignee: mabshoff

This is required for gcc 4.4.0, Solaris and so on.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-05-12 06:14:26

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-05-15 14:45:43

The new Maxima is at 

  http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/maxima-5.16.3.p2.spkg

Note that the ecl.spkg is still missing and will be next.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-15 20:35:02

The ecl.spkg skpg that now finally works is at 

   http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/ecl-9.4.1.spkg

Cheers,

Michael


---

Comment by was created at 2009-05-16 00:14:40

Positive review pending:

   1. Remove the msvc directory for now.

   2. Put "unset MAKE" at the top of spkg-install for now, since it definitely breaks if one doesn't do that.


---

Comment by was created at 2009-05-16 00:17:31

ok, full positive review.


---

Comment by mabshoff created at 2009-05-16 00:27:14

Resolution: fixed


---

Comment by mabshoff created at 2009-05-16 00:27:14

Merged both spkgs and the patch in Sage 4.0.alpha0. 

I also fixed deps and install accordingly.

Cheers,

Michael
