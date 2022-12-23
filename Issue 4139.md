# Issue 4139: [with patch, needs review] Improvements to permutation groups

Issue created by migration from https://trac.sagemath.org/ticket/4139

Original creator: mhansen

Original creation time: 2008-09-17 07:59:44

Assignee: joyner

CC:  boothby

The primary purpose of this patch was to make it so that calls to GAP aren't needed to construct permutation group elements and symmetric groups.

This has a unintended benefit of fixing #4105.


---

Attachment


---

Comment by wdj created at 2008-09-17 10:21:16

Thanks Mike. I'll test it out.


---

Comment by mabshoff created at 2008-09-17 11:31:50

Nice work, deleting loads of crufty code, adding doctests :p

Cheers,

Michael


---

Comment by wdj created at 2008-09-17 15:21:12

I'm having trouble with applying this patch to  3.1.2:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: perm-gp
sage: hg_sage.apply("/home/wdj/sagefiles/trac_4139.patch")
cd "/home/wdj/sagefiles/sage-3.1.2/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.2/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.2/devel/sage" && hg import   "/home/wdj/sagefiles/trac_4139.patch"
applying /home/wdj/sagefiles/trac_4139.patch
patching file sage/groups/perm_gps/permgroup.py
Hunk #1 FAILED at 60
Hunk #2 succeeded at 86 with fuzz 2 (offset 2 lines).
1 out of 57 hunks FAILED -- saving rejects to file sage/groups/perm_gps/permgroup.py.rej
patching file sage/groups/perm_gps/permgroup_named.py
Hunk #8 FAILED at 508
1 out of 15 hunks FAILED -- saving rejects to file sage/groups/perm_gps/permgroup_named.py.rej
abort: patch failed to apply
```

Can anyone help decipher this message?


---

Comment by rlm created at 2008-09-17 18:35:18

When a hunk fails, it means that the piece of code the patch is expecting has changed, like getting the carpet pulled out from under you. This just means that Mike or someone needs to rebase the patch.


---

Comment by rlm created at 2008-09-17 19:15:08

After rebase, I get the following errors:

```
sage -t  devel/sage-main/sage/groups/matrix_gps/matrix_group.py
**********************************************************************
File "/Users/rlmill/sage-3.1.2/tmp/matrix_group.py", line 650:
    sage: G.as_permutation_group()
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-3.1.2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[5]>", line 1, in <module>
        G.as_permutation_group()###line 650:
    sage: G.as_permutation_group()
      File "/Users/rlmill/sage-3.1.2/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py", line 696, in as_permutation_group
        return PermutationGroup(C, from_group = True)
    TypeError: PermutationGroup() got an unexpected keyword argument 'from_group'
**********************************************************************
File "/Users/rlmill/sage-3.1.2/tmp/matrix_group.py", line 663:
    sage: G.as_permutation_group()
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-3.1.2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[15]>", line 1, in <module>
        G.as_permutation_group()###line 663:
    sage: G.as_permutation_group()
      File "/Users/rlmill/sage-3.1.2/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py", line 696, in as_permutation_group
        return PermutationGroup(C, from_group = True)
    TypeError: PermutationGroup() got an unexpected keyword argument 'from_group'
**********************************************************************
File "/Users/rlmill/sage-3.1.2/tmp/matrix_group.py", line 666:
    sage: G.as_permutation_group(method="smaller")
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-3.1.2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[17]>", line 1, in <module>
        G.as_permutation_group(method="smaller")###line 666:
    sage: G.as_permutation_group(method="smaller")
      File "/Users/rlmill/sage-3.1.2/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py", line 696, in as_permutation_group
        return PermutationGroup(C, from_group = True)
    TypeError: PermutationGroup() got an unexpected keyword argument 'from_group'
**********************************************************************
```



```
sage -t  devel/sage-main/sage/groups/perm_gps/permgroup_named.py
**********************************************************************
File "/Users/rlmill/sage-3.1.2/tmp/permgroup_named.py", line 546:
    sage: G.base_ring()
Expected:
    Finite Field of size 3
Got nothing
**********************************************************************
File "/Users/rlmill/sage-3.1.2/tmp/permgroup_named.py", line 580:
    sage: print G
Expected:
    The projective general linear group of degree 2 over Finite Field of size 3
Got:
    The projective general linear group of degree 2 over None
**********************************************************************
File "/Users/rlmill/sage-3.1.2/tmp/permgroup_named.py", line 582:
    sage: G.base_ring()
Expected:
    Finite Field of size 3
Got nothing
**********************************************************************
File "/Users/rlmill/sage-3.1.2/tmp/permgroup_named.py", line 589:
    sage: G.base_ring()
Expected:
    Finite Field in b of size 3^2
Got nothing
**********************************************************************
File "/Users/rlmill/sage-3.1.2/tmp/permgroup_named.py", line 604:
    sage: print G
Expected:
    The projective general linear group of degree 2 over Finite Field of size 3
Got:
    The projective general linear group of degree 2 over None
**********************************************************************
```



---

Attachment


---

Comment by mhansen created at 2008-09-19 07:43:38

I attached a patch which add two little things which I think got left out of the rebase.


---

Comment by rlm created at 2008-09-19 08:00:55

Bravo! I've been hoping for someone to do this! Everything applies and test long passes in sage/groups.


---

Comment by mabshoff created at 2008-09-19 14:09:31

Yes, there is some slight, easy to fix, doctest failure:

```
sage -t -long devel/sage/sage/graphs/graph.py               
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha0/tmp/graph.py", line 6234:
    sage: for g in L:
       G = g.automorphism_group()
       G.order(), G.gens()
Expected:
    (24, ((2,3), (1,2), (1,4)))
    (4, ((2,3), (1,4)))
    (2, ((1,2),))
    (8, ((1,2), (1,4)(2,3)))
    (6, ((1,2), (1,4)))
    (6, ((2,3), (1,2)))
    (2, ((1,4)(2,3),))
    (2, ((1,2),))
    (8, ((2,3), (1,4), (1,3)(2,4)))
    (4, ((2,3), (1,4)))
    (24, ((2,3), (1,2), (1,4)))
Got:
    (24, [(2,3), (1,2), (1,4)])
    (4, [(2,3), (1,4)])
    (2, [(1,2)])
    (8, [(1,2), (1,4)(2,3)])
    (6, [(1,2), (1,4)])
    (6, [(2,3), (1,2)])
    (2, [(1,4)(2,3)])
    (2, [(1,2)])
    (8, [(2,3), (1,4), (1,3)(2,4)])
    (4, [(2,3), (1,4)])
    (24, [(2,3), (1,2), (1,4)])
**********************************************************************
```


Cheers,

Michael


---

Attachment


---

Comment by rlm created at 2008-09-19 14:45:19

The fix to this doctest is currently in one of the patches at #4150.


---

Comment by mabshoff created at 2008-09-19 14:47:28

Replying to [comment:10 rlm]:
> The fix to this doctest is currently in one of the patches at #4150.

Oops, I just added and committed trac_4139_doctest-fix.patch which fixes the issue. Can you fix that in #4150?

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-19 14:48:39

Merged trac_4139-rebased-3.1.2.patch, trac_4139-rebase-fix.patch and trac_4139_doctest-fix.patch in Sage 3.1.3.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-19 14:48:39

Resolution: fixed
