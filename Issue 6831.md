# Issue 6831: [with patch, needs review] No more maximal dimension requirement for lattice polytopes

Issue created by migration from https://trac.sagemath.org/ticket/6831

Original creator: novoselt

Original creation time: 2009-08-27 06:29:37

Assignee: mhampton

Since PALP requires polytopes to have the same dimension as the ambient space, LatticePolytope class required it as well. This patch drops this requirement by storing an internal copy of the same polytope in some sublattice basis and using it when necessary to call PALP. Quite a few functions had to be updated, I tried to add new doctests to check most of the new branches of code.

This patch will be a prerequisite for some code for working with nef partitions which I hope to submit in the future.


---

Attachment

Can you rebase this against sage-4.2?  I reviewed some of your patches previously, and some made them in, which means this doesn't apply against the current version.  Sorry about that, I'm hoping to finish up reviewing your patches for 4.2.1.

-Marshall


---

Comment by novoselt created at 2009-10-29 19:04:39

Actually, I have written this patch after all the previous ones were applied, I am not even sure if it will work without them.

I'll check and rebase if it does not work for 4.2, but it will take me some time. 

Thanks for all the other reviews!
Andrey


---

Comment by mhampton created at 2009-10-30 02:15:02

My mercurial-foo is not that strong, so perhaps I made a mistake trying to apply the patch.  But I don't understand it if so.  It would be OK to have a rebased patch that included other changes - even if they aren't positively reviewed yet I could do them all at once, assuming they mainly affected lattice_polytope.py.

-Marshall


---

Comment by novoselt created at 2009-10-30 05:28:52

Rebased patch, also includes patches for tickets 6779, 6780, and 6805


---

Attachment

This patch should work on 4.2 without any prior requirements, it includes changes made in 3 other small tickets which you have already given a positive review - I will put comments in those tickets. Let me know if I should do anything else.

Andrey


---

Comment by mhampton created at 2009-10-30 15:38:26

Great, thanks.  I can't do it today but I'll try to review it this weekend.

-Marshall


---

Comment by mhampton created at 2009-11-01 12:59:13

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2009-11-01 12:59:13

OK, this looks good, positive review.  I've looked it over, did some manual tests, it passes its own doctests and has 100% coverage.  I rebuilt the reference manual and it looks good there.  Seems like all the changes are for the better.


---

Comment by mhansen created at 2009-11-02 04:35:25

Resolution: fixed
