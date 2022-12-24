# Issue 6126: Symmetric group algebra jucys_murphy elements incorrect

archive/issues_006126.json:
```json
{
    "body": "Assignee: @mwhansen\n\nKeywords: jucys_murphy\n\nThe error is observed on my linux box as well as sage.math.washington.edu (my version is 3.4.1, sage.math version is 3.4.2, the error is the same).  The error is in the function \"jucys_murphy\".\n\n\n```\nsage: G=SymmetricGroupAlgebra(QQ,5)\nsage: PermutationOptions(mult='l2r', display='cycle')\nsage: for i in range(2,6):\n....: G.jucys_murphy(i)\n....:\n(1,2)\n(2,3) + (1,2)\n(3,4) + (2,3) + (1,2)\n(4,5) + (3,4) + (2,3) + (1,2)\n```\n\nI believe the returned elements should be\n\n```\n(1,2)\n(2,3) + (1,3)\n(3,4) + (2,4) + (1,4)\n(4,5) + (3,5) + (2,5) + (1,5)\n```\n\nI found the relevant code.  On both machines the offending code is in\n\n/usr/local/sage/devel/sage-main/build/sage/combinat/symmetric_group_algebra.py,\n\nand\n\n/usr/local/sage/devel/sage-main/sage/combinat).  I have fixed on my machine by changing in those files the lines 180-185 from\n\n\n```\n------------\nfor i in range(1, k):\np = range(1, self.n+1)\np[i-1] = i+1\np[i] = i\nres += self(p)\nreturn res\n----------------\n```\n\n\nto\n\n\n```\n------------\nfor i in range(1, k):\np = range(1, self.n+1)\n+ p[i-1] = k\n+ p[k-1] = i\nres += self(p)\nreturn res\n----------------\n```\n\n\nThanks,\nAmps\n\nIssue created by migration from https://trac.sagemath.org/ticket/6126\n\n",
    "created_at": "2009-05-24T21:14:01Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Symmetric group algebra jucys_murphy elements incorrect",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6126",
    "user": "arattan"
}
```
Assignee: @mwhansen

Keywords: jucys_murphy

The error is observed on my linux box as well as sage.math.washington.edu (my version is 3.4.1, sage.math version is 3.4.2, the error is the same).  The error is in the function "jucys_murphy".


```
sage: G=SymmetricGroupAlgebra(QQ,5)
sage: PermutationOptions(mult='l2r', display='cycle')
sage: for i in range(2,6):
....: G.jucys_murphy(i)
....:
(1,2)
(2,3) + (1,2)
(3,4) + (2,3) + (1,2)
(4,5) + (3,4) + (2,3) + (1,2)
```

I believe the returned elements should be

```
(1,2)
(2,3) + (1,3)
(3,4) + (2,4) + (1,4)
(4,5) + (3,5) + (2,5) + (1,5)
```

I found the relevant code.  On both machines the offending code is in

/usr/local/sage/devel/sage-main/build/sage/combinat/symmetric_group_algebra.py,

and

/usr/local/sage/devel/sage-main/sage/combinat).  I have fixed on my machine by changing in those files the lines 180-185 from


```
------------
for i in range(1, k):
p = range(1, self.n+1)
p[i-1] = i+1
p[i] = i
res += self(p)
return res
----------------
```


to


```
------------
for i in range(1, k):
p = range(1, self.n+1)
+ p[i-1] = k
+ p[k-1] = i
res += self(p)
return res
----------------
```


Thanks,
Amps

Issue created by migration from https://trac.sagemath.org/ticket/6126





---

archive/issue_comments_048946.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-27T20:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6126#issuecomment-48946",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_048947.json:
```json
{
    "body": "Attachment [trac_6126.patch](tarball://root/attachments/some-uuid/ticket6126/trac_6126.patch) by @mwhansen created at 2009-05-27 20:40:27\n\nI've attached a patch with these changes, and they look good to me.",
    "created_at": "2009-05-27T20:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6126#issuecomment-48947",
    "user": "@mwhansen"
}
```

Attachment [trac_6126.patch](tarball://root/attachments/some-uuid/ticket6126/trac_6126.patch) by @mwhansen created at 2009-05-27 20:40:27

I've attached a patch with these changes, and they look good to me.



---

archive/issue_comments_048948.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-27T20:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6126#issuecomment-48948",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_048949.json:
```json
{
    "body": "Merged in 4.0.rc1.",
    "created_at": "2009-05-27T20:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6126#issuecomment-48949",
    "user": "@mwhansen"
}
```

Merged in 4.0.rc1.



---

archive/issue_comments_048950.json:
```json
{
    "body": "Please synchronize with sage-combinat-devel next time!\nWe got a conflict in the patch server.",
    "created_at": "2009-06-04T21:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6126#issuecomment-48950",
    "user": "@nthiery"
}
```

Please synchronize with sage-combinat-devel next time!
We got a conflict in the patch server.



---

archive/issue_comments_048951.json:
```json
{
    "body": "See followup on #6215 which includes the doctests that had been written for the same bug in Sage-Combinat",
    "created_at": "2009-06-04T23:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6126#issuecomment-48951",
    "user": "@nthiery"
}
```

See followup on #6215 which includes the doctests that had been written for the same bug in Sage-Combinat
