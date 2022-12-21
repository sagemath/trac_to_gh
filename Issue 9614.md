# Issue 9614: "-sdist" should complain or fail when run in a "-bdist" copy of Sage

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2010-07-28 01:29:52

Assignee: tbd

A "bdisted" copy of Sage contains only placeholders for spkg files, and does not include the directory SAGE_ROOT/spkg/base. This means it is impossible for "sage -sdist" to work on such a copy of Sage unless the sdist script somehow downloads the necessary files.

The sdist script should detect this problem and fail in this situation, preferably with instructions to the user for fixing it.


---

Attachment

apply to scripts repo


---

Comment by ddrake created at 2010-07-28 02:16:14

My proposed changes are attached. I've changed 'sage -bdist' to create an empty file spkg/standard/.from_bdist. "sage -sdist" looks for that file, and exits if it finds it. It prints some instructions as it fails; I think the instructions are correct, but please check to make sure.

We could try to have -sdist download the necessary files and put them in, but that would require always having a downloadable source for many versions of Sage on the web, and wouldn't do any good to someone working without a net connection. Telling the user how to fix the problem seems more effective in this case.


---

Comment by ddrake created at 2010-07-28 02:16:14

Changing status from new to needs_review.


---

Comment by vbraun created at 2011-02-01 01:20:50

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2011-02-01 01:20:50

I've made that mistake before and I wished that sage-sdist would have complained. This fix looks good to me! Applies fine on Sage-4.6.2.alpha3.


---

Comment by jdemeyer created at 2011-02-01 08:50:13

Changing component from distribution to scripts.


---

Comment by jdemeyer created at 2011-02-07 08:14:35

Resolution: fixed
