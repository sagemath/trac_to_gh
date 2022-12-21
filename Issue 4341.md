# Issue 4341: [with patch, needs review] Optimisations + corrections to latin.py

Issue created by migration from Trac.

Original creator: carlohamalainen

Original creation time: 2008-10-22 19:53:25

Assignee: mhansen

CC:  sage-combinat

* Removed code that used gap.Representative in an unsafe manner (assumed that the ordering would be the same on each execution but the GAP manual says that this may not be the case). Previous code did work but was not safe.

* Replacement tau_to_bitrade uses correct and straightforward combinatorial approach.

* Replacement of p3_group_bitrade_generators is orders of magnitude faster; uses GAP's IsomorphismPermGroup instead of explicitly constructing a natural homomorphism.


---

Comment by wdj created at 2008-11-22 02:34:50

This applies cleanly to 3.2 and passes sage -testall. However, I have several (possibly very stupid) questions about the docstrings, which I've passed on to the author off-list (to save myself the embarrassment of asking dumb questions:-). I prefer to wait until I hear back to give an appraisal.


---

Attachment

Regarding the "to do" using nauty: please don't. Robert Miller's code NICE does this fine:


```
sage: from sage.combinat.matrices.latin import *
sage: M = matrix([(0, 1, 2, 3), (2, 3, 0, 1), (3, 2, 1, 0), (1, 0, 3, 2)])
sage: L = LatinSquare(M)
sage: L.is_latin_square()
True
sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct
sage: A = MatrixStruct(M)
sage: autgp = A.automorphism_group()
sage: gens = [[j+1 for j in autgp[0][i]] for i in range(len(autgp[0]))]
sage: S4 = SymmetricGroup(4)
sage: G = PermutationGroup([S4(x) for x in gens]); G
Permutation Group with generators [(1,2)(3,4)]
```

An easy "to do": take the very short MOLS codes in Guava (included in Sage), at
http://sage.math.washington.edu/home/wdj/guava/lib/matrices.gi,
and translate it into Python/Sage/latin.py code. (MOLS are used to construct optimal non-linear codes, but non-linear codes have not yet been implemented in Sage.)

I'm currently running tests on this (second) patch and will post again soon.


---

Comment by wdj created at 2008-11-23 15:01:36

This looks good to me. Applies cleanly to 3.2.alpha0 and passes sage -testall.


---

Comment by mabshoff created at 2008-11-24 00:19:35

Resolution: fixed


---

Comment by mabshoff created at 2008-11-24 00:19:35

Merged in Sage 3.2.1.alpha1
