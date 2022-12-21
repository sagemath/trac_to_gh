# Issue 9767: Fix PolyBoRi's broken dynamic libraries

Issue created by migration from Trac.

Original creator: AlexanderDreyer

Original creation time: 2010-08-19 20:17:16

Assignee: AlexanderDreyer

CC:  polybori malb wjp mvngu

In #8830 wqe worked around PolyBoRi's broken dynamic libraries by removing them after build, hence using the static ones instead. The problem was caused by improper handling of a global variable which was fixed for upcoming PolyBoRi 0.7.

The package at http://sage.math.washington.edu/home/dreyer/pb/polybori-0.6.4.p5.spkg backports this fix and reintroduces the dynamic libraries. The spkg is based on #9717 and assumes its sage-library patch to be applied. It installs, runs and passed testall on boxen.


---

Attachment

Diffs of the new package


---

Comment by AlexanderDreyer created at 2010-08-19 20:27:45

Changing status from new to needs_review.


---

Comment by malb created at 2010-08-20 13:33:33

The SPKG looks good, I'm running installation + doctests on a few platforms right now, so far that also looks good.

A somewhat related issue (feel free to ignore): It seems scons doesn't touch for example polybori.h if that didn't change. It would thus be nice to touch this file at the end of spkg-install to inform the Sage build system that it needs to rebuild the extensions. If you agree I can provide a patch.


---

Comment by malb created at 2010-08-22 15:36:15

I built this SPKG and ran long doctests on bsd.math, sage.math and t2.math. They all worked fine, thus I'm giving this a positive review.


---

Comment by malb created at 2010-08-22 15:36:15

Changing status from needs_review to positive_review.


---

Comment by AlexanderDreyer created at 2010-08-22 21:19:57

> A somewhat related issue (feel free to ignore): It seems scons doesn't touch for example polybori.h if that didn't change. It would thus be nice to touch this file at the end of spkg-install to inform the Sage build system that it needs to rebuild the extensions. If you agree I can provide a patch.

Feel free to provide such a patch (even tough it's a little bit against the philosopy that a build system should take care of the remaining dependencies automatically).


---

Comment by mpatel created at 2010-09-15 10:55:02

Changing component from algebra to packages.


---

Comment by mpatel created at 2010-09-16 00:53:58

Resolution: fixed


---

Comment by mpatel created at 2010-09-16 00:53:58

I have not merged the p5 package.  Instead, I've merged #9872's p6 package, which [comment:ticket:9872:17 includes the changes made here].
