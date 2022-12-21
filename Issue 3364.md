# Issue 3364: randstate interaction with GAP is broken

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-06-04 16:38:05

Assignee: cwitty

This is the remaining issue from #3130.  See this example:

```
sage: set_random_seed(0)
sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
sage: G.composition_series()

[Permutation Group with generators [(1,2,3)(4,5), (3,4)],
 Permutation Group with generators [(1,5)(3,4), (1,5)(2,3), (1,5,3)],
 Permutation Group with generators [()]]
sage: set_random_seed(0)
sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
sage: G.composition_series()

[Permutation Group with generators [(1,2,3)(4,5), (3,4)],
 Permutation Group with generators [(1,5)(3,4), (1,5)(2,4), (1,4,5)],
 Permutation Group with generators [()]]
```


Even with the same random number seed, the result of .composition_series() is different.


---

Attachment


---

Comment by cwitty created at 2008-06-08 14:12:35

It turns out that GAP has two random number generators, and uses both.  (I couldn't find any uses of the older generator when I first wrote randstate, but that's because I was looking for the wrong thing.)  This fixes randstate to control both generators.

This patch will conflict with #3130; it might be better to apply it first and let me rebase this patch.


---

Comment by wdj created at 2008-06-08 23:31:40

Well, 3130 needs rebasing too, which means I must redo it from scratch. 

Michael: When redoing 3130, should I take into account this fix for 3364 (ie, follow cwitty's original comments regarding "# random output" comments)? This is getting complicated.


---

Comment by wdj created at 2008-06-09 00:06:50

I don't seem to be able to apply this to 3.0.3.alpha1 but the error is very odd.


```
sage: hg_sage.add("/home/wdj/sagefiles/3364_randstate_fix_gap.patch")
Adding file /home/wdj/sagefiles/3364_randstate_fix_gap.patch
cd "/home/wdj/sagefiles/sage-3.0.3.alpha1/devel/sage" && hg add  "/home/wdj/sagefiles/3364_randstate_fix_gap.patch"
abort: /home/wdj/sagefiles/3364_randstate_fix_gap.patch not under root
```

Does anyone know what this means?


---

Comment by wdj created at 2008-06-09 00:14:21

I'll reply to my own post. The clone I created can't apply *any* patches, only create them.


---

Comment by mabshoff created at 2008-06-09 07:25:57

Patch looks good to me. I did not doctest the patch since I had some rejects after applying #3130:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/devel/sage$ patch -p1 < trac_3364_randstate_fix_gap.patch 
patching file sage/groups/matrix_gps/orthogonal.py
patching file sage/groups/matrix_gps/symplectic.py
patching file sage/groups/matrix_gps/unitary.py
patching file sage/groups/perm_gps/permgroup.py
Hunk #1 FAILED at 172.
Hunk #2 FAILED at 1713.
Hunk #3 FAILED at 1736.
3 out of 3 hunks FAILED -- saving rejects to file sage/groups/perm_gps/permgroup.py.rej
patching file sage/misc/randstate.pyx
```

I can take a look and attempt to rebase. Feel free to try my current merge tree: 

sage:/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/devel/sage

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-09 18:44:34

I had to slightly fix the doctests in permgroup.py, but now doctests pass. New patch is attached. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-09 18:47:02

Patch with fixed permgroup.py doctests


---

Attachment

Merged in Sage 3.0.3.alpha2


---

Comment by mabshoff created at 2008-06-09 18:47:46

Resolution: fixed
