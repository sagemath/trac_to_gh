# Issue 7899: Remove variable names like $LN, $MKDIR etc in ntl

Issue created by migration from https://trac.sagemath.org/ticket/7899

Original creator: drkirkby

Original creation time: 2010-01-12 03:55:50

Assignee: GeorgSWeber

CC:  jsp jhpalmieri

It was agreed recently that variables would not be used for very common commands like MV, MKDIR etc.

 http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot

#7818 usets these, so this package will break. The fix is to simply replace things like

$LN with 'ln'

An updated .spkg can be found at 

http://boxen.math.washington.edu/home/kirkby/portability/ntl-5.4.2.p10/ntl-5.4.2.p10.spkg




---

Comment by drkirkby created at 2010-01-12 03:57:09

Changing status from new to needs_review.


---

Attachment


---

Comment by jsp created at 2010-01-12 11:11:34

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-01-12 11:11:34

The new spkg looks good. Positive review.

Jaap


---

Comment by rlm created at 2010-01-14 02:57:30

Resolution: fixed
