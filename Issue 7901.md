# Issue 7901: Change $MKDIR to 'mkdir' in pari

Issue created by migration from https://trac.sagemath.org/ticket/7901

Original creator: drkirkby

Original creation time: 2010-01-12 04:33:03

Assignee: GeorgSWeber

CC:  jsp jhpalmieri

It was agreed recently that variables would not be used for very common commands like MV, MKDIR etc.

     http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot

#7818 usets these, so this package may break. The fix is to simply replace $MKDIR with 'mkdir' in spkg-install. 

An updated .spkg can be found at 

http://boxen.math.washington.edu/home/kirkby/portability/pari-2.3.3.p7/ari-2.3.3.p7.spkg


---

Comment by drkirkby created at 2010-01-12 04:36:36

Changing status from new to needs_review.


---

Comment by jsp created at 2010-01-12 10:55:50

The patch of spkg-install looks ok. Maybe the SPKG.txt should be brought up to date.

See also: [http://trac.sagemath.org/sage_trac/ticket/7738](http://trac.sagemath.org/sage_trac/ticket/7738)

Dave, can you fix that?

Jaap


---

Comment by drkirkby created at 2010-01-12 16:50:03

OK I've recreated the spkg, which again can be found at http://boxen.math.washington.edu/home/kirkby/portability/pari-2.3.3.p7/pari-2.3.3.p7.spkg Please check it again. 

I've attached the Mercurial patch, which overwrites the old one.


---

Attachment

Updated patch to fix spkg-install and SPKG.txt


---

Comment by jsp created at 2010-01-12 17:53:46

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-01-12 17:53:46

All fixed. Positive review.

Jaap


---

Comment by rlm created at 2010-01-14 03:01:28

Resolution: fixed
