# Issue 4724: expose pari's galois and finer number field interfaces

Issue created by migration from https://trac.sagemath.org/ticket/4724

Original creator: ncalexan

Original creation time: 2008-12-06 04:05:45

Assignee: was

Keywords: pari number field nf galois

I would like to use pari's galois computations (such as nfgaloisconj) and finer number field functions (such as nfroots).  The interface (in sage.libs.pari.gen) needs to be upgraded.


---

Comment by AlexGhitza created at 2009-01-23 07:07:12

Changing type from defect to enhancement.


---

Comment by ncalexan created at 2009-02-11 00:07:57

A valuable improvement would be to use polisirreducible and nfroots for polynomials defined over number fields.


---

Comment by ncalexan created at 2009-02-13 02:46:24

This is a step in the right direction -- exposes nfgaloisconj and nfroots, and adds automorphisms/updates embeddings to be much faster for number fields.

Try it with a large degree number field -- you couldn't compute K.embeddings(K) for suff. large K, but now you can.


---

Attachment


---

Comment by cremona created at 2009-03-15 22:19:52

This looks really really useful, great code!  But it needs to be rebased to 3.4: at present the patch does not merge.


---

Comment by cremona created at 2009-04-08 09:29:09

Nick, did you get the message about rebasing this?  John


---

Comment by ncalexan created at 2009-04-12 19:30:47

Yes I got messages about this but it is not a priority for me.  I will try to rebase it sometime soon.


---

Comment by AlexGhitza created at 2009-04-13 08:38:46

replaces the previous patch


---

Attachment

All I did was rebase Nick's patch against 3.4.1.rc2.  (ok, I also rest-ified a couple of his docstrings.)

One issue was that the original patch seems to have had a lot of things in double.  This is now fixed, hence the difference in size.

The code looks good to me and is nicely documented.  Positive review.


---

Comment by mabshoff created at 2009-04-13 09:02:29

Resolution: fixed


---

Comment by mabshoff created at 2009-04-13 09:02:29

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
