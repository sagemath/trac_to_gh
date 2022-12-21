# Issue 3629: givaro-3.2.11 installs its own libgmpxx.{so,a}

Issue created by migration from Trac.

Original creator: fbissey

Original creation time: 2008-07-10 04:37:50

Assignee: cpernet

The title says it all. No ideas on how to fix it apart touching
the install phase.


---

Comment by fbissey created at 2008-07-10 04:46:27

Changing priority from major to blocker.


---

Comment by cpernet created at 2008-07-10 18:49:27

This issue has been fixed by jgdumas in the upstream cvs repo and he released a 3.2.12rc0 version including this fix:
[http://ljk.imag.fr/membres/Jean-Guillaume.Dumas/Softwares/givaro-www/givaro-3.2.12rc0.tar.gz](http://ljk.imag.fr/membres/Jean-Guillaume.Dumas/Softwares/givaro-www/givaro-3.2.12rc0.tar.gz)

I upgraded the givaro spkg to the 3.2.12rc0 version:
[http://sage.math.washington.edu/home/pernet/givaro-3.2.12rc0.spkg](http://sage.math.washington.edu/home/pernet/givaro-3.2.12rc0.spkg)


---

Comment by mabshoff created at 2008-07-16 04:03:54

Positive review. The spkg no longer attempts to install the offending library.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-16 04:04:08

Merged in Sage 3.0.6.alpha0


---

Comment by mabshoff created at 2008-07-16 04:04:08

Resolution: fixed
