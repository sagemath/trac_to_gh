# Issue 3969: Matrix_mod2_dense hashs follow-up (see #3724)

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-08-27 19:52:53

Assignee: was

Robert wrote:
"""

```
Matrix hashes are specifically designed to be compatible with each other: 
sage: M = random_matrix(GF(2), 10, 10)
sage: M.set_immutable()
sage: hash(M)
561
sage: MZ = M.change_ring(ZZ)
sage: MZ.set_immutable()
sage: hash(MZ)
561
sage: MS = M.sparse_matrix()
sage: MS.set_immutable()
sage: hash(MS)
561
```

This patch seems to break that. At a minimum, it seems sparse and dense should hash to the same thing. If we want to change this policy, we should at least ask on sage-devel.
"""


---

Attachment

This is not as fast as xoring all the matrix entries, but is still very fast, and compatible (as possible) with the all the other matrices. 


```
sage: M = random_matrix(GF(2), 3500, 3500)
sage: M.set_immutable()
sage: time hash(M)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
1523294
sage: M = random_matrix(GF(2), 10000, 10000)
sage: M.set_immutable()
sage: time hash(M)
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
37785898
```



---

Attachment


---

Comment by malb created at 2008-08-31 19:39:40

I rebased the patch to 3.1.2.alpha3 and fixed a small typo in a comment. I get the overall idea of the algorithm, which I find a rather elegant approach. Doctests pass. Positive review. I'm not sure if there could be an issue with 32-bit machines and matching hashs.


---

Comment by mabshoff created at 2008-09-01 12:06:28

malb's patch has a stray `32bit` in it that causes the following failure:

```
sage -t  devel/sage/sage/matrix/matrix_mod2_dense.pyx       
**********************************************************************
File "/Users/mabshoff/sage-3.1.2.alpha3/tmp/matrix_mod2_dense.py", line 284:
    sage: {B:0} # indirect doctest
Expected:
    {[0 1 0]
    [0 1 1]
    [0 0 0]: 0}
    '-0x21524113' 
Got:
    {[0 1 0]
    [0 1 1]
    [0 0 0]: 0}
**********************************************************************
```

This is obviously trivial to fix :)

Cheers,

Michael


---

Comment by malb created at 2008-09-01 12:09:17

Looks like a merge error, IMHO.


---

Comment by mabshoff created at 2008-09-01 12:21:05

Merged 3969-fast-matmod2-hash-rebased.patch (minus the one line doctest merge accident) in Sage 3.1.2.alpha4


---

Comment by mabshoff created at 2008-09-01 12:21:05

Resolution: fixed
