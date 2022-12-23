# Issue 3502: modular symbols -- implement apply_sparse, which is needed for fast eigenvalue computation

Issue created by migration from https://trac.sagemath.org/ticket/3502

Original creator: was

Original creation time: 2008-06-24 15:40:11

Assignee: craigcitro

Implement applying Hecke operator to a single sparse vector, an operation that is needed for quick computation of systems of Hecke eigenvalues.


---

Comment by craigcitro created at 2008-09-11 09:17:33

So I looked over the code, and everything looks good. There were a handful of small touch-ups needed, missing doctests, etc., so I went ahead and took care of all of that. Someone should look over the additional patch I've posted, but after that, this looks ready to go. 

I'm also cleaning up the ticket by deleting the 12 individual patches and posting William's complete bundle (from the URL he added above), and adding my patch.


---

Comment by craigcitro created at 2008-09-11 09:21:01

William's bundle with all patches


---

Attachment


---

Attachment

(This doesn't need to go into 3.1.2, so I'm moving it to 3.1.3.)


---

Comment by was created at 2008-09-20 04:50:16

I read through the additional patch, applied it, doctested it, and I'm happy across the board.  It's very good for increasing doctest coverage.
 Thanks Craig!!


---

Comment by mabshoff created at 2008-09-20 21:59:50

Merged 3502.hg and trac-3502-addl.patch in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-20 21:59:50

Resolution: fixed
