# Issue 3364: randstate interaction with GAP is broken

archive/issues_003364.json:
```json
{
    "body": "Assignee: cwitty\n\nThis is the remaining issue from #3130.  See this example:\n\n```\nsage: set_random_seed(0)\nsage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])\nsage: G.composition_series()\n\n[Permutation Group with generators [(1,2,3)(4,5), (3,4)],\n Permutation Group with generators [(1,5)(3,4), (1,5)(2,3), (1,5,3)],\n Permutation Group with generators [()]]\nsage: set_random_seed(0)\nsage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])\nsage: G.composition_series()\n\n[Permutation Group with generators [(1,2,3)(4,5), (3,4)],\n Permutation Group with generators [(1,5)(3,4), (1,5)(2,4), (1,4,5)],\n Permutation Group with generators [()]]\n```\n\n\nEven with the same random number seed, the result of .composition_series() is different.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3364\n\n",
    "created_at": "2008-06-04T16:38:05Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "randstate interaction with GAP is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3364",
    "user": "cwitty"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/3364





---

archive/issue_comments_023535.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-08T14:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3364#issuecomment-23535",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_023536.json:
```json
{
    "body": "It turns out that GAP has two random number generators, and uses both.  (I couldn't find any uses of the older generator when I first wrote randstate, but that's because I was looking for the wrong thing.)  This fixes randstate to control both generators.\n\nThis patch will conflict with #3130; it might be better to apply it first and let me rebase this patch.",
    "created_at": "2008-06-08T14:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3364#issuecomment-23536",
    "user": "cwitty"
}
```

It turns out that GAP has two random number generators, and uses both.  (I couldn't find any uses of the older generator when I first wrote randstate, but that's because I was looking for the wrong thing.)  This fixes randstate to control both generators.

This patch will conflict with #3130; it might be better to apply it first and let me rebase this patch.



---

archive/issue_comments_023537.json:
```json
{
    "body": "Well, 3130 needs rebasing too, which means I must redo it from scratch. \n\nMichael: When redoing 3130, should I take into account this fix for 3364 (ie, follow cwitty's original comments regarding \"# random output\" comments)? This is getting complicated.",
    "created_at": "2008-06-08T23:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3364#issuecomment-23537",
    "user": "wdj"
}
```

Well, 3130 needs rebasing too, which means I must redo it from scratch. 

Michael: When redoing 3130, should I take into account this fix for 3364 (ie, follow cwitty's original comments regarding "# random output" comments)? This is getting complicated.



---

archive/issue_comments_023538.json:
```json
{
    "body": "I don't seem to be able to apply this to 3.0.3.alpha1 but the error is very odd.\n\n\n```\nsage: hg_sage.add(\"/home/wdj/sagefiles/3364_randstate_fix_gap.patch\")\nAdding file /home/wdj/sagefiles/3364_randstate_fix_gap.patch\ncd \"/home/wdj/sagefiles/sage-3.0.3.alpha1/devel/sage\" && hg add  \"/home/wdj/sagefiles/3364_randstate_fix_gap.patch\"\nabort: /home/wdj/sagefiles/3364_randstate_fix_gap.patch not under root\n```\n\nDoes anyone know what this means?",
    "created_at": "2008-06-09T00:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3364#issuecomment-23538",
    "user": "wdj"
}
```

I don't seem to be able to apply this to 3.0.3.alpha1 but the error is very odd.


```
sage: hg_sage.add("/home/wdj/sagefiles/3364_randstate_fix_gap.patch")
Adding file /home/wdj/sagefiles/3364_randstate_fix_gap.patch
cd "/home/wdj/sagefiles/sage-3.0.3.alpha1/devel/sage" && hg add  "/home/wdj/sagefiles/3364_randstate_fix_gap.patch"
abort: /home/wdj/sagefiles/3364_randstate_fix_gap.patch not under root
```

Does anyone know what this means?



---

archive/issue_comments_023539.json:
```json
{
    "body": "I'll reply to my own post. The clone I created can't apply *any* patches, only create them.",
    "created_at": "2008-06-09T00:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3364#issuecomment-23539",
    "user": "wdj"
}
```

I'll reply to my own post. The clone I created can't apply *any* patches, only create them.



---

archive/issue_comments_023540.json:
```json
{
    "body": "Patch looks good to me. I did not doctest the patch since I had some rejects after applying #3130:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/devel/sage$ patch -p1 < trac_3364_randstate_fix_gap.patch \npatching file sage/groups/matrix_gps/orthogonal.py\npatching file sage/groups/matrix_gps/symplectic.py\npatching file sage/groups/matrix_gps/unitary.py\npatching file sage/groups/perm_gps/permgroup.py\nHunk #1 FAILED at 172.\nHunk #2 FAILED at 1713.\nHunk #3 FAILED at 1736.\n3 out of 3 hunks FAILED -- saving rejects to file sage/groups/perm_gps/permgroup.py.rej\npatching file sage/misc/randstate.pyx\n```\n\nI can take a look and attempt to rebase. Feel free to try my current merge tree: \n\nsage:/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/devel/sage\n\nCheers,\n\nMichael",
    "created_at": "2008-06-09T07:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3364#issuecomment-23540",
    "user": "mabshoff"
}
```

Patch looks good to me. I did not doctest the patch since I had some rejects after applying #3130:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/devel/sage$ patch -p1 < trac_3364_randstate_fix_gap.patch 
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

archive/issue_comments_023541.json:
```json
{
    "body": "I had to slightly fix the doctests in permgroup.py, but now doctests pass. New patch is attached. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-09T18:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3364#issuecomment-23541",
    "user": "mabshoff"
}
```

I had to slightly fix the doctests in permgroup.py, but now doctests pass. New patch is attached. Positive review.

Cheers,

Michael



---

archive/issue_comments_023542.json:
```json
{
    "body": "Patch with fixed permgroup.py doctests",
    "created_at": "2008-06-09T18:47:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3364#issuecomment-23542",
    "user": "mabshoff"
}
```

Patch with fixed permgroup.py doctests



---

archive/issue_comments_023543.json:
```json
{
    "body": "Attachment\n\nMerged in Sage 3.0.3.alpha2",
    "created_at": "2008-06-09T18:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3364#issuecomment-23543",
    "user": "mabshoff"
}
```

Attachment

Merged in Sage 3.0.3.alpha2



---

archive/issue_comments_023544.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-09T18:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3364#issuecomment-23544",
    "user": "mabshoff"
}
```

Resolution: fixed
