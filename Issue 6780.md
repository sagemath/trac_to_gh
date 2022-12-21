# Issue 6780: Stability improvement for lattice_polytope

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2009-08-20 03:30:22

Assignee: mhampton

As it was already observed before, there are problems with using LatticePolytope for polytopes with many vertices/points. The problem occurs during pipe calls to PALP for single polytopes and can be avoided using lattice_polytope.all_* functions which work with files. 

This patch switches all interaction with PALP to files by default, while allowing the old method as an option.

It may affect the speed, but I cannot detect the difference on sage.math. On the other hand, in many cases I had to deal with polytopes which worked fine and fast through files and lead to hang-ups with pipes.


---

Attachment


---

Comment by mhampton created at 2009-10-24 15:25:33

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2009-10-24 15:25:33

This passes all tests and definitely seems like an improvement.  The solution does seem a little complicated, and it seems unlikely that the always_use_files(False) option will be used by anyone, but that's OK.  Its always hard to say what people actually use, so leaving that in as an option is good.


---

Comment by novoselt created at 2009-10-30 05:35:38

This patch is included as a part of a rebased patch for #6831.


---

Comment by mhansen created at 2009-11-02 04:36:04

Fixed in #6831.


---

Comment by mhansen created at 2009-11-02 04:36:04

Resolution: fixed
