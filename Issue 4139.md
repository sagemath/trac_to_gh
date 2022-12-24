# Issue 4139: [with patch, needs review] Improvements to permutation groups

archive/issues_004139.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  boothby\n\nThe primary purpose of this patch was to make it so that calls to GAP aren't needed to construct permutation group elements and symmetric groups.\n\nThis has a unintended benefit of fixing #4105.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4139\n\n",
    "created_at": "2008-09-17T07:59:44Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, needs review] Improvements to permutation groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4139",
    "user": "@mwhansen"
}
```
Assignee: joyner

CC:  boothby

The primary purpose of this patch was to make it so that calls to GAP aren't needed to construct permutation group elements and symmetric groups.

This has a unintended benefit of fixing #4105.

Issue created by migration from https://trac.sagemath.org/ticket/4139





---

archive/issue_comments_030046.json:
```json
{
    "body": "Attachment [trac_4139.patch](tarball://root/attachments/some-uuid/ticket4139/trac_4139.patch) by @mwhansen created at 2008-09-17 09:04:00",
    "created_at": "2008-09-17T09:04:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30046",
    "user": "@mwhansen"
}
```

Attachment [trac_4139.patch](tarball://root/attachments/some-uuid/ticket4139/trac_4139.patch) by @mwhansen created at 2008-09-17 09:04:00



---

archive/issue_comments_030047.json:
```json
{
    "body": "Thanks Mike. I'll test it out.",
    "created_at": "2008-09-17T10:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30047",
    "user": "@wdjoyner"
}
```

Thanks Mike. I'll test it out.



---

archive/issue_comments_030048.json:
```json
{
    "body": "Nice work, deleting loads of crufty code, adding doctests :p\n\nCheers,\n\nMichael",
    "created_at": "2008-09-17T11:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30048",
    "user": "mabshoff"
}
```

Nice work, deleting loads of crufty code, adding doctests :p

Cheers,

Michael



---

archive/issue_comments_030049.json:
```json
{
    "body": "I'm having trouble with applying this patch to  3.1.2:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: perm-gp\nsage: hg_sage.apply(\"/home/wdj/sagefiles/trac_4139.patch\")\ncd \"/home/wdj/sagefiles/sage-3.1.2/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.2/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.2/devel/sage\" && hg import   \"/home/wdj/sagefiles/trac_4139.patch\"\napplying /home/wdj/sagefiles/trac_4139.patch\npatching file sage/groups/perm_gps/permgroup.py\nHunk #1 FAILED at 60\nHunk #2 succeeded at 86 with fuzz 2 (offset 2 lines).\n1 out of 57 hunks FAILED -- saving rejects to file sage/groups/perm_gps/permgroup.py.rej\npatching file sage/groups/perm_gps/permgroup_named.py\nHunk #8 FAILED at 508\n1 out of 15 hunks FAILED -- saving rejects to file sage/groups/perm_gps/permgroup_named.py.rej\nabort: patch failed to apply\n```\n\nCan anyone help decipher this message?",
    "created_at": "2008-09-17T15:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30049",
    "user": "@wdjoyner"
}
```

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

archive/issue_comments_030050.json:
```json
{
    "body": "When a hunk fails, it means that the piece of code the patch is expecting has changed, like getting the carpet pulled out from under you. This just means that Mike or someone needs to rebase the patch.",
    "created_at": "2008-09-17T18:35:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30050",
    "user": "@rlmill"
}
```

When a hunk fails, it means that the piece of code the patch is expecting has changed, like getting the carpet pulled out from under you. This just means that Mike or someone needs to rebase the patch.



---

archive/issue_comments_030051.json:
```json
{
    "body": "After rebase, I get the following errors:\n\n```\nsage -t  devel/sage-main/sage/groups/matrix_gps/matrix_group.py\n**********************************************************************\nFile \"/Users/rlmill/sage-3.1.2/tmp/matrix_group.py\", line 650:\n    sage: G.as_permutation_group()\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/rlmill/sage-3.1.2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_24[5]>\", line 1, in <module>\n        G.as_permutation_group()###line 650:\n    sage: G.as_permutation_group()\n      File \"/Users/rlmill/sage-3.1.2/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py\", line 696, in as_permutation_group\n        return PermutationGroup(C, from_group = True)\n    TypeError: PermutationGroup() got an unexpected keyword argument 'from_group'\n**********************************************************************\nFile \"/Users/rlmill/sage-3.1.2/tmp/matrix_group.py\", line 663:\n    sage: G.as_permutation_group()\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/rlmill/sage-3.1.2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_24[15]>\", line 1, in <module>\n        G.as_permutation_group()###line 663:\n    sage: G.as_permutation_group()\n      File \"/Users/rlmill/sage-3.1.2/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py\", line 696, in as_permutation_group\n        return PermutationGroup(C, from_group = True)\n    TypeError: PermutationGroup() got an unexpected keyword argument 'from_group'\n**********************************************************************\nFile \"/Users/rlmill/sage-3.1.2/tmp/matrix_group.py\", line 666:\n    sage: G.as_permutation_group(method=\"smaller\")\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/rlmill/sage-3.1.2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_24[17]>\", line 1, in <module>\n        G.as_permutation_group(method=\"smaller\")###line 666:\n    sage: G.as_permutation_group(method=\"smaller\")\n      File \"/Users/rlmill/sage-3.1.2/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py\", line 696, in as_permutation_group\n        return PermutationGroup(C, from_group = True)\n    TypeError: PermutationGroup() got an unexpected keyword argument 'from_group'\n**********************************************************************\n```\n\n\n\n```\nsage -t  devel/sage-main/sage/groups/perm_gps/permgroup_named.py\n**********************************************************************\nFile \"/Users/rlmill/sage-3.1.2/tmp/permgroup_named.py\", line 546:\n    sage: G.base_ring()\nExpected:\n    Finite Field of size 3\nGot nothing\n**********************************************************************\nFile \"/Users/rlmill/sage-3.1.2/tmp/permgroup_named.py\", line 580:\n    sage: print G\nExpected:\n    The projective general linear group of degree 2 over Finite Field of size 3\nGot:\n    The projective general linear group of degree 2 over None\n**********************************************************************\nFile \"/Users/rlmill/sage-3.1.2/tmp/permgroup_named.py\", line 582:\n    sage: G.base_ring()\nExpected:\n    Finite Field of size 3\nGot nothing\n**********************************************************************\nFile \"/Users/rlmill/sage-3.1.2/tmp/permgroup_named.py\", line 589:\n    sage: G.base_ring()\nExpected:\n    Finite Field in b of size 3^2\nGot nothing\n**********************************************************************\nFile \"/Users/rlmill/sage-3.1.2/tmp/permgroup_named.py\", line 604:\n    sage: print G\nExpected:\n    The projective general linear group of degree 2 over Finite Field of size 3\nGot:\n    The projective general linear group of degree 2 over None\n**********************************************************************\n```\n",
    "created_at": "2008-09-17T19:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30051",
    "user": "@rlmill"
}
```

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

archive/issue_comments_030052.json:
```json
{
    "body": "Attachment [trac_4139-rebase-fix.patch](tarball://root/attachments/some-uuid/ticket4139/trac_4139-rebase-fix.patch) by @mwhansen created at 2008-09-19 07:43:07",
    "created_at": "2008-09-19T07:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30052",
    "user": "@mwhansen"
}
```

Attachment [trac_4139-rebase-fix.patch](tarball://root/attachments/some-uuid/ticket4139/trac_4139-rebase-fix.patch) by @mwhansen created at 2008-09-19 07:43:07



---

archive/issue_comments_030053.json:
```json
{
    "body": "I attached a patch which add two little things which I think got left out of the rebase.",
    "created_at": "2008-09-19T07:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30053",
    "user": "@mwhansen"
}
```

I attached a patch which add two little things which I think got left out of the rebase.



---

archive/issue_comments_030054.json:
```json
{
    "body": "Bravo! I've been hoping for someone to do this! Everything applies and test long passes in sage/groups.",
    "created_at": "2008-09-19T08:00:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30054",
    "user": "@rlmill"
}
```

Bravo! I've been hoping for someone to do this! Everything applies and test long passes in sage/groups.



---

archive/issue_comments_030055.json:
```json
{
    "body": "Yes, there is some slight, easy to fix, doctest failure:\n\n```\nsage -t -long devel/sage/sage/graphs/graph.py               \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.alpha0/tmp/graph.py\", line 6234:\n    sage: for g in L:\n       G = g.automorphism_group()\n       G.order(), G.gens()\nExpected:\n    (24, ((2,3), (1,2), (1,4)))\n    (4, ((2,3), (1,4)))\n    (2, ((1,2),))\n    (8, ((1,2), (1,4)(2,3)))\n    (6, ((1,2), (1,4)))\n    (6, ((2,3), (1,2)))\n    (2, ((1,4)(2,3),))\n    (2, ((1,2),))\n    (8, ((2,3), (1,4), (1,3)(2,4)))\n    (4, ((2,3), (1,4)))\n    (24, ((2,3), (1,2), (1,4)))\nGot:\n    (24, [(2,3), (1,2), (1,4)])\n    (4, [(2,3), (1,4)])\n    (2, [(1,2)])\n    (8, [(1,2), (1,4)(2,3)])\n    (6, [(1,2), (1,4)])\n    (6, [(2,3), (1,2)])\n    (2, [(1,4)(2,3)])\n    (2, [(1,2)])\n    (8, [(2,3), (1,4), (1,3)(2,4)])\n    (4, [(2,3), (1,4)])\n    (24, [(2,3), (1,2), (1,4)])\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-09-19T14:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30055",
    "user": "mabshoff"
}
```

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

archive/issue_comments_030056.json:
```json
{
    "body": "Attachment [trac_4139_doctest-fix.patch](tarball://root/attachments/some-uuid/ticket4139/trac_4139_doctest-fix.patch) by mabshoff created at 2008-09-19 14:45:13",
    "created_at": "2008-09-19T14:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30056",
    "user": "mabshoff"
}
```

Attachment [trac_4139_doctest-fix.patch](tarball://root/attachments/some-uuid/ticket4139/trac_4139_doctest-fix.patch) by mabshoff created at 2008-09-19 14:45:13



---

archive/issue_comments_030057.json:
```json
{
    "body": "The fix to this doctest is currently in one of the patches at #4150.",
    "created_at": "2008-09-19T14:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30057",
    "user": "@rlmill"
}
```

The fix to this doctest is currently in one of the patches at #4150.



---

archive/issue_comments_030058.json:
```json
{
    "body": "Replying to [comment:10 rlm]:\n> The fix to this doctest is currently in one of the patches at #4150.\n\nOops, I just added and committed trac_4139_doctest-fix.patch which fixes the issue. Can you fix that in #4150?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-19T14:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30058",
    "user": "mabshoff"
}
```

Replying to [comment:10 rlm]:
> The fix to this doctest is currently in one of the patches at #4150.

Oops, I just added and committed trac_4139_doctest-fix.patch which fixes the issue. Can you fix that in #4150?

Cheers,

Michael



---

archive/issue_comments_030059.json:
```json
{
    "body": "Merged trac_4139-rebased-3.1.2.patch, trac_4139-rebase-fix.patch and trac_4139_doctest-fix.patch in Sage 3.1.3.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-19T14:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30059",
    "user": "mabshoff"
}
```

Merged trac_4139-rebased-3.1.2.patch, trac_4139-rebase-fix.patch and trac_4139_doctest-fix.patch in Sage 3.1.3.alpha0.

Cheers,

Michael



---

archive/issue_comments_030060.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-19T14:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4139#issuecomment-30060",
    "user": "mabshoff"
}
```

Resolution: fixed
