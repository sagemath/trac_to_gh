# Issue 2765: [with patch, needs review] bug in graph_isom, Hoffman-Singleton constructor

Issue created by migration from https://trac.sagemath.org/ticket/2765

Original creator: rlm

Original creation time: 2008-04-01 22:53:37

Assignee: rlm

This fixes a bug in determining the canonical label of different permutations of the Hoffman-Singleton graph. As such, the constructor is included to make for a nice doctest. This bug was discovered by Godsil.


---

Attachment


---

Comment by rlm created at 2008-04-02 19:25:18

This ticket patches two problems in the algorithm:

1. In step 11, we have just found an automorphism, which means that the tree descending from where nu and zeta meet in the nu direction is isomorphic to what we have already seen. I was setting k to hb without checking that we are searching for a canonical label. hb keeps track of where nu and rho (the best so far guess at can. label) meet, and h keeps track of where nu and zeta (the first branch) meet. This is a typo in McKay's original paper.

2. In the refinement procedure, I was adding something to the invariant which depended on more than the isomorphism class of the situation, namely `invariant += t + self_col_degs[i-j-1]`. This is before the cell has been split up, so there is some randomness. I moved this instruction to after splitting, and cleaned it up a bit.


---

Comment by mhansen created at 2008-04-04 03:26:28

Looks good to me.


---

Comment by mabshoff created at 2008-04-04 03:42:33

Resolution: fixed


---

Comment by mabshoff created at 2008-04-04 03:42:33

Merged in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-04-04 03:45:17

Sorry: Merged in Sage *3.0.alpha1* - time to catch some sleep!
