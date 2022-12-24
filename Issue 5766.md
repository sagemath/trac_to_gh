# Issue 5766: improve coverage of structure/formal_sum.py

archive/issues_005766.json:
```json
{
    "body": "Assignee: somebody\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5766\n\n",
    "created_at": "2009-04-11T23:58:16Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "improve coverage of structure/formal_sum.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5766",
    "user": "was"
}
```
Assignee: somebody



Issue created by migration from https://trac.sagemath.org/ticket/5766





---

archive/issue_comments_045087.json:
```json
{
    "body": "BUGS FOUND:\n1. The reduce option to formal sum is totally ignored.\n\n```\nsage: FormalSum([(1,2/3), (3,2/3), (-5, 7)], reduce=False)\n4*2/3 - 5*7\n```\n\n\n2. Latexing formal sums is completely broken (I think this is actually #5707):\n\n```\nsage: latex(FormalSum([(1,2), (5, 8/9), (-3, 7)]))\n5\\frac{8}{9}2 - 37\n```\n",
    "created_at": "2009-04-12T01:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45087",
    "user": "was"
}
```

BUGS FOUND:
1. The reduce option to formal sum is totally ignored.

```
sage: FormalSum([(1,2/3), (3,2/3), (-5, 7)], reduce=False)
4*2/3 - 5*7
```


2. Latexing formal sums is completely broken (I think this is actually #5707):

```
sage: latex(FormalSum([(1,2), (5, 8/9), (-3, 7)]))
5\frac{8}{9}2 - 37
```




---

archive/issue_comments_045088.json:
```json
{
    "body": "Attachment [trac_5766.patch](tarball://root/attachments/some-uuid/ticket5766/trac_5766.patch) by was created at 2009-04-12 01:40:24",
    "created_at": "2009-04-12T01:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45088",
    "user": "was"
}
```

Attachment [trac_5766.patch](tarball://root/attachments/some-uuid/ticket5766/trac_5766.patch) by was created at 2009-04-12 01:40:24



---

archive/issue_comments_045089.json:
```json
{
    "body": "There's an `indirect doctest` missing from nonzero and a typoed `indirect doctest` on len, but other than that this looks good.",
    "created_at": "2009-04-12T05:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45089",
    "user": "ncalexan"
}
```

There's an `indirect doctest` missing from nonzero and a typoed `indirect doctest` on len, but other than that this looks good.



---

archive/issue_comments_045090.json:
```json
{
    "body": "Mhh, ther seems to be a 32 vs. 64 bit issue here:\n\n```\nsage -t -long \"devel/sage/sage/structure/formal_sum.py\"     \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/structure/formal_sum.py\", line 333:\n    sage: a\nExpected:\n    2/3 - 3*4/5 + 7*2\nGot:\n    7*2 + 2/3 - 3*4/5\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/structure/formal_sum.py\", line 335:\n    sage: a._repr_()\nExpected:\n    '2/3 - 3*4/5 + 7*2'\nGot:\n    '7*2 + 2/3 - 3*4/5'\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T01:39:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45090",
    "user": "mabshoff"
}
```

Mhh, ther seems to be a 32 vs. 64 bit issue here:

```
sage -t -long "devel/sage/sage/structure/formal_sum.py"     
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/structure/formal_sum.py", line 333:
    sage: a
Expected:
    2/3 - 3*4/5 + 7*2
Got:
    7*2 + 2/3 - 3*4/5
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/structure/formal_sum.py", line 335:
    sage: a._repr_()
Expected:
    '2/3 - 3*4/5 + 7*2'
Got:
    '7*2 + 2/3 - 3*4/5'
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_045091.json:
```json
{
    "body": "Attachment [trac_5766-doctest_fix.patch](tarball://root/attachments/some-uuid/ticket5766/trac_5766-doctest_fix.patch) by was created at 2009-04-13 14:15:35",
    "created_at": "2009-04-13T14:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45091",
    "user": "was"
}
```

Attachment [trac_5766-doctest_fix.patch](tarball://root/attachments/some-uuid/ticket5766/trac_5766-doctest_fix.patch) by was created at 2009-04-13 14:15:35



---

archive/issue_comments_045092.json:
```json
{
    "body": "Sorry, but on my 32-bit laptop I get\n\n```\n**********************************************************************\nFile \"/home/john/sage-3.4.2.alpha0/devel/sage-tests/sage/structure/formal_sum.py\", line 333:\n    sage: a\nExpected:\n    2/3 - 3*4/5 + 7*2                       -- comparing Mod(2,3) and rationals ill-defined\nGot:\n    7*2 + 2/3 - 3*4/5\n**********************************************************************\nFile \"/home/john/sage-3.4.2.alpha0/devel/sage-tests/sage/structure/formal_sum.py\", line 336:\n    sage: a._repr_()\nExpected:\n    '2/3 - 3*4/5 + 7*2'                    \nGot:\n    '7*2 + 2/3 - 3*4/5'\n**********************************************************************\n```\n\n\nPerhaps all formal sums should be sorted?  As part of the reduce() method (which should then be called after creation)?",
    "created_at": "2009-04-27T20:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45092",
    "user": "cremona"
}
```

Sorry, but on my 32-bit laptop I get

```
**********************************************************************
File "/home/john/sage-3.4.2.alpha0/devel/sage-tests/sage/structure/formal_sum.py", line 333:
    sage: a
Expected:
    2/3 - 3*4/5 + 7*2                       -- comparing Mod(2,3) and rationals ill-defined
Got:
    7*2 + 2/3 - 3*4/5
**********************************************************************
File "/home/john/sage-3.4.2.alpha0/devel/sage-tests/sage/structure/formal_sum.py", line 336:
    sage: a._repr_()
Expected:
    '2/3 - 3*4/5 + 7*2'                    
Got:
    '7*2 + 2/3 - 3*4/5'
**********************************************************************
```


Perhaps all formal sums should be sorted?  As part of the reduce() method (which should then be called after creation)?



---

archive/issue_comments_045093.json:
```json
{
    "body": "> Perhaps all formal sums should be sorted? As part of the reduce() method (which should then be called after creation)? \n\nThey are sorted.  That's why the doctests failed for you -- because sort is not well defined as indicated in the comment.",
    "created_at": "2009-04-28T14:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45093",
    "user": "was"
}
```

> Perhaps all formal sums should be sorted? As part of the reduce() method (which should then be called after creation)? 

They are sorted.  That's why the doctests failed for you -- because sort is not well defined as indicated in the comment.



---

archive/issue_comments_045094.json:
```json
{
    "body": "Attachment [trac_5766-part3.patch](tarball://root/attachments/some-uuid/ticket5766/trac_5766-part3.patch) by was created at 2009-04-28 14:10:30",
    "created_at": "2009-04-28T14:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45094",
    "user": "was"
}
```

Attachment [trac_5766-part3.patch](tarball://root/attachments/some-uuid/ticket5766/trac_5766-part3.patch) by was created at 2009-04-28 14:10:30



---

archive/issue_comments_045095.json:
```json
{
    "body": "OK with all three patches the tests pass.  It's a pity we cannot make it deterministic but the only thing I could think of was sorting on the strong representations (of the base of each pair) and that would take too long I suppose.",
    "created_at": "2009-04-28T16:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45095",
    "user": "cremona"
}
```

OK with all three patches the tests pass.  It's a pity we cannot make it deterministic but the only thing I could think of was sorting on the strong representations (of the base of each pair) and that would take too long I suppose.



---

archive/issue_comments_045096.json:
```json
{
    "body": "With all three patch applied I am seeing the following doctest failure:\n\n```\nsage -t -long \"devel/sage/sage/misc/latex.py\"               \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.2.rc0/devel/sage/sage/misc/latex.py\", line 942:\n    sage: repr_lincomb([1,5,-3],[2,8/9,7])\nExpected:\n    '2*1 + 8/9*5 + 7*-3'\nGot:\n    '21 + \\\\frac{8}{9}5 + 7-3'\n**********************************************************************\n```\n\nSince this seems to be the correct LaTeX representation I am fixing this failure.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T00:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45096",
    "user": "mabshoff"
}
```

With all three patch applied I am seeing the following doctest failure:

```
sage -t -long "devel/sage/sage/misc/latex.py"               
**********************************************************************
File "/scratch/mabshoff/sage-3.4.2.rc0/devel/sage/sage/misc/latex.py", line 942:
    sage: repr_lincomb([1,5,-3],[2,8/9,7])
Expected:
    '2*1 + 8/9*5 + 7*-3'
Got:
    '21 + \\frac{8}{9}5 + 7-3'
**********************************************************************
```

Since this seems to be the correct LaTeX representation I am fixing this failure.

Cheers,

Michael



---

archive/issue_comments_045097.json:
```json
{
    "body": "Actually, the above seems broken, i.e. notice the missing ***** - so 'needs work'.\n\nCheers,\n\nMichaek",
    "created_at": "2009-04-30T00:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45097",
    "user": "mabshoff"
}
```

Actually, the above seems broken, i.e. notice the missing ***** - so 'needs work'.

Cheers,

Michaek



---

archive/issue_comments_045098.json:
```json
{
    "body": "I have folded William's patches and rebased them against 4.0.alpha0.\n\nI made an attempt to fix the latex-ing, see the patch.",
    "created_at": "2009-06-04T01:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45098",
    "user": "AlexGhitza"
}
```

I have folded William's patches and rebased them against 4.0.alpha0.

I made an attempt to fix the latex-ing, see the patch.



---

archive/issue_comments_045099.json:
```json
{
    "body": "apply instead of the other patches",
    "created_at": "2009-06-04T01:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45099",
    "user": "AlexGhitza"
}
```

apply instead of the other patches



---

archive/issue_comments_045100.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T18:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45100",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_045101.json:
```json
{
    "body": "Attachment [trac_5766-rebased.patch](tarball://root/attachments/some-uuid/ticket5766/trac_5766-rebased.patch) by mhansen created at 2009-06-04 18:33:58\n\nLooks good to me.\n\nMerged trac_5766-rebased.patch in 4.0.1.rc1.",
    "created_at": "2009-06-04T18:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5766#issuecomment-45101",
    "user": "mhansen"
}
```

Attachment [trac_5766-rebased.patch](tarball://root/attachments/some-uuid/ticket5766/trac_5766-rebased.patch) by mhansen created at 2009-06-04 18:33:58

Looks good to me.

Merged trac_5766-rebased.patch in 4.0.1.rc1.
