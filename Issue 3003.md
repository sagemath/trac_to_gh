# Issue 3003: Bugfix for to_tableau() method of CrystalOfTableaux elements (with patch; needs review)

Issue created by migration from https://trac.sagemath.org/ticket/3003

Original creator: jbandlow

Original creation time: 2008-04-22 17:14:31

Assignee: mhansen

CC:  sage-combinat

Keywords: crystals, tableaux

Current behaviour:
    sage: C = CrystalOfTableaux(['A',3],shape=[2,1])
    sage: h = C.highest_weight_vector()
    sage: t = h.to_tableau()
    sage: w = t.to_word(); w
    [2, 1, 1]
    sage: type(w[0])
    <class 'sage.combinat.crystals.letters.Crystal_of_letters_type_A_element'>
    sage: t.evaluation()
    <BOOM>

This patch ensures we get a tableau of integers instead of a tableau of crystal elements.


---

Attachment


---

Comment by bump created at 2008-04-22 17:49:09

The elements of crystals of letters look like integers because their __repr__ method returns an integer string but they are not. Before the patch it is possible to accidentally build tableaux whose entries are crystal of letter elements. The patch looks obviously correct to me. I'm not sure  this bugfix requires a doctest.


---

Comment by mabshoff created at 2008-04-22 20:25:02

I know that Dan did a review, but we still need a formal vote. Since there is a test case that Jason posted we should add it as a doctest. If it runs long we should add #long to it.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-04-22 22:45:44

Looks good to me.  I added a little test in 3003.patch -- that's the one that should be applied.


---

Comment by mabshoff created at 2008-04-23 11:42:12

Resolution: fixed


---

Comment by mabshoff created at 2008-04-23 11:42:12

Merged in Sage 3.0.1.alpha0
