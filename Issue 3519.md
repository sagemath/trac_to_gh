# Issue 3519: Update clisp to 2.45 release

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-06-27 04:13:27

Assignee: mabshoff

The current clisp.spkg is broken on SLES 10/Itanium, i.e. does not compile. I could not find a ticket for this, so I am opening a new one.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-27 04:13:32

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-04 07:07:06

An updated clisp 2.46 spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha2/clisp-2.46.spkg

It is likely broken on Cygwin (but I will fix that) and builds and doctests fine on 

 * 32 bit OSX 10.5
 * x86-64 Linux
 * Itanium SLES 10 and RHEL 5 Linux

Cheers,

Michael


---

Comment by mhampton created at 2008-07-05 23:50:50

Builds OK on OS X 10.4, ppc, but something is wrong.  After rebuilding Maxima, all calculus doc tests with trig functions fail.  Running in maxima mode, trig functions seem OK, but in Sage when evaluated on symbolic variables a TypeError is raised: float required.


---

Comment by mabshoff created at 2008-07-06 10:57:56

Changing keywords from "" to "editor_mabshoff".


---

Comment by mabshoff created at 2008-07-06 11:53:50

Replying to [comment:3 mhampton]:
> Builds OK on OS X 10.4, ppc, but something is wrong.  After rebuilding Maxima, all calculus doc tests with trig functions fail.  Running in maxima mode, trig functions seem OK, but in Sage when evaluated on symbolic variables a TypeError is raised: float required.

For the record: This was with Sage 2.11. With Sage 3.0.3 on OSX 10.5 PPC all the calculus doctest pass. I will dig out my OSX 10.4 iBook and test it there.

Cheers,

Michael


---

Comment by was created at 2008-07-07 18:55:50

it built on my test platforms, so positive review.


---

Comment by was created at 2008-07-07 21:56:29

Resolution: fixed


---

Comment by mabshoff created at 2008-07-07 22:06:16

Merged in Sage 3.0.4.rc0
