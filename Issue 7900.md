# Issue 7900: Replace variables like $RM with  'rm' in Mercurial

Issue created by migration from https://trac.sagemath.org/ticket/7900

Original creator: drkirkby

Original creation time: 2010-01-12 04:09:55

Assignee: GeorgSWeber

CC:  jsp jhpalmieri

It was agreed recently that variables would not be used for very common commands like MV, MKDIR etc.

     http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot

#7818 usets these, so this package will break. The fix is to simply replace things like

$LN with 'ln'

An updated .spkg can be found at 

http://boxen.math.washington.edu/home/kirkby/portability/mercurial-1.3.1.p1/mercurial-1.3.1.p1.spkg


---

Attachment


---

Comment by drkirkby created at 2010-01-12 04:15:32

Changing status from new to needs_review.


---

Comment by jsp created at 2010-01-12 11:16:11

The new package looks good. Positive review.

Jaap


---

Comment by jsp created at 2010-01-12 11:16:11

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-14 02:58:34

Resolution: fixed
