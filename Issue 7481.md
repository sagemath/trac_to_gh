# Issue 7481: upgrade phcpack optional package to version 2.3.51

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2009-11-17 18:00:49

Assignee: tbd

Keywords: phcpack, numerical, polynomials

phcpack has had many improvements since the last sage package was made.  The following spkg upgrades to the latest version, and supports intel binaries on macs for OS X 10.5 and higher. 

http://sage.math.washington.edu/home/mhampton/phc-2.3.51.p0.spkg




---

Comment by mhampton created at 2009-11-17 18:00:58

Changing status from new to needs_review.


---

Comment by mhampton created at 2009-12-04 18:34:56

Changing status from needs_review to needs_work.


---

Comment by mhampton created at 2009-12-04 18:34:56

Jan Verschelde informed mr that 2.3.51 had some problems, and I should switch this to 2.3.53, so I will do that soon.


---

Comment by mhampton created at 2009-12-04 18:53:04

New spkg for phcpack-2.3.53 up at:

http://sage.math.washington.edu/home/mhampton/phc-2.3.53.p0.spkg


---

Comment by mhampton created at 2009-12-04 18:53:04

Changing status from needs_work to needs_review.


---

Comment by mhampton created at 2009-12-04 21:24:19

I've tested this on Solaris (t2), linux, and OS X.


---

Comment by mhansen created at 2009-12-27 18:45:54

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-27 18:45:54

Looks good to me.


---

Comment by mhansen created at 2010-01-04 02:05:58

Resolution: fixed


---

Comment by mhansen created at 2010-01-04 02:05:58

I've merged this in with the optional spkgs.
