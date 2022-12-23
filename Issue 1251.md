# Issue 1251: tutorial out of date

Issue created by migration from https://trac.sagemath.org/ticket/1251

Original creator: wdj

Original creation time: 2007-11-23 22:54:56

Assignee: wdj

The tut.tex file needed a few updates and corrections. The patch is at
http://sage.math.washington.edu/home/wdj/patches/tut20071123.hg
The new latex file (which passes sage -t) is at
http://sage.math.washington.edu/home/wdj/patches/tut.tex
I also tried to change the file copyright.tex (which is
in the commontex subdirectory). I don't think the changes stuck, but
the revised version is at
http://sage.math.washington.edu/home/wdj/patches/copyright.tex
(The old one said "See the end of this document for licensing
information. However, those sections were commented out, so I just
copied some lines from the start of the wiki.)



---

Comment by was created at 2007-11-24 18:44:19

Just apply the tut bundle http://sage.math.washington.edu/home/wdj/patches/tut20071123.hg 
then manually place the copyright file in commontex (it is not
part of the repo and shouldn't be for now).

William


---

Comment by was created at 2007-11-25 04:55:56

Resolution: fixed
