# Issue 9967: Stop Dancing Links polluting the global namespace

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2010-09-22 10:13:36

Assignee: sage-combinat

Keywords: dancing links

The Dancing Links class defines a bunch of random integer variables (LEFT, RIGHT, UP, DOWN, ROOTNODE) and exports these to the global namespace. This is kind of sloppy and unprofessional: 


```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: hacking
sage: UP
2
```



---

Attachment

patch against 4.6.alpha1


---

Comment by davidloeffler created at 2010-09-22 10:17:34

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-09-22 14:57:40

I was a bit worried about the edge_coloring method for graphs which uses this algorithm, but it is still working after this patch is applied : no (related) failure in sage -testall ! 

Thankssssssssss ! `:-)`

Nathann


---

Comment by ncohen created at 2010-09-22 14:57:40

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-09-28 11:47:54

Perhaps we can get this into 4.6? It's hardly a massive change :-)


---

Comment by mpatel created at 2010-09-29 04:25:08

Resolution: fixed
