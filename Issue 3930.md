# Issue 3930: Check to see if we should merge the bipartite matching code from Susan Massey

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-08-22 18:13:03

Assignee: rlm

CC:  mvngu

See http://wiki.wstein.org/2008/480a/theprojects


---

Comment by mvngu created at 2009-06-27 00:48:24

CC'ing myself.


---

Comment by ncohen created at 2009-08-06 15:57:06

see #6680 for the general case


---

Comment by ncohen created at 2009-12-18 09:07:59

#6680 has now been merged, and #7274 contains another version of this algorithm. What do we make of this ticket (which is already 6 months old) ?


---

Comment by ncohen created at 2009-12-18 09:07:59

Changing status from new to needs_info.


---

Comment by jason created at 2009-12-18 16:53:39

Changing status from needs_info to needs_work.


---

Comment by jason created at 2009-12-18 16:53:39

I just opened this ticket so that we wouldn't lose track of code that had been written for eventual inclusion in Sage.  If we already have equivalent functionality now, then close this ticket as redundant or fixed or something!


---

Comment by ncohen created at 2009-12-18 16:56:07

Then we should wait for #7274 to decide it  : the version from #6680 requires GLPK to be installed :-)

Nathann


---

Comment by jason created at 2009-12-18 17:05:06

I've noted this on #7274.


---

Comment by jason created at 2009-12-18 17:06:13

Changing status from needs_work to needs_info.


---

Comment by jason created at 2009-12-18 17:06:13

I'm not sure what state these tickets that are just waiting on other tickets should be in.  It seems best to put them in needs_info (i.e., inactive, waiting on an outside something).


---

Comment by jason created at 2010-01-17 10:25:47

Changing type from defect to task.


---

Comment by ncohen created at 2010-05-16 16:33:15

Well, we now have a Python matching code #8166 . Can we close this ticket as no one as it seems abandonned ?

Nathann


---

Comment by rlm created at 2010-05-29 17:44:32

Replying to [comment:9 ncohen]:
> Well, we now have a Python matching code #8166 . Can we close this ticket as no one as it seems abandonned ?

+1


---

Comment by rlm created at 2010-05-29 17:44:32

Resolution: wontfix
