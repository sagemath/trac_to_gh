# Issue 4826: change return type of G.cusps() for G a congruence subgroup

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-12-18 10:42:22

Assignee: craigcitro

As pointed out on [this](http://groups.google.com/group/sage-nt/browse_thread/thread/f0a95b54181ba6c5) thread on sage-nt, it might be more reasonable to have `G.cusps()` return a list instead of a set (for `G` a congruence subgroup). In particular, seeing an ordered list as output makes it easier to look through.

The attached patch changes this return type, as well as making a few small fixes so that this is just as fast as before (or faster, in some cases). 

This patch depends on #4747.


---

Comment by craigcitro created at 2008-12-18 10:44:10

Changing status from new to assigned.


---

Attachment


---

Comment by cremona created at 2008-12-18 17:46:58

Patch applied cleanly to 3.2.2.rc1 (after removing the e-acute in Thiery's name in sage/combinat/ranker.py).

All tests in sage/modular pass, as well as some other testing that I did.

Positive review!


---

Comment by mabshoff created at 2008-12-21 11:45:21

Resolution: fixed


---

Comment by mabshoff created at 2008-12-21 11:45:21

Merged in Sage 3.2.3.alpha0
