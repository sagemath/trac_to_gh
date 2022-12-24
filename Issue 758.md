# Issue 758: Use NTL directly in Z/nZ polynomials

archive/issues_000758.json:
```json
{
    "body": "Assignee: somebody\n\nIt can be vastly faster. There are several layers now...stripping them out one by one. \n\n\n```\nsage: f = Integers(101)['x'](range(10))\nsage: time for _ in range(10^5): g = f*f\nCPU time: 2.97 s,  Wall time: 3.00 s\n\nsage: f = Integers(100)['x'](range(10))\nsage: time for _ in range(10^5): g = f*f\nCPU time: 0.17 s,  Wall time: 0.18 s\n```\n\n\n(This is not quite fair because one is using ZZ_p and one is using zz_p, but there is only a factor of <2 between those in NTL.) \n\nIssue created by migration from https://trac.sagemath.org/ticket/758\n\n",
    "created_at": "2007-09-28T11:52:26Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "Use NTL directly in Z/nZ polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/758",
    "user": "@robertwb"
}
```
Assignee: somebody

It can be vastly faster. There are several layers now...stripping them out one by one. 


```
sage: f = Integers(101)['x'](range(10))
sage: time for _ in range(10^5): g = f*f
CPU time: 2.97 s,  Wall time: 3.00 s

sage: f = Integers(100)['x'](range(10))
sage: time for _ in range(10^5): g = f*f
CPU time: 0.17 s,  Wall time: 0.18 s
```


(This is not quite fair because one is using ZZ_p and one is using zz_p, but there is only a factor of <2 between those in NTL.) 

Issue created by migration from https://trac.sagemath.org/ticket/758





---

archive/issue_comments_004494.json:
```json
{
    "body": "Changing assignee from somebody to @robertwb.",
    "created_at": "2007-09-28T11:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/758#issuecomment-4494",
    "user": "@robertwb"
}
```

Changing assignee from somebody to @robertwb.



---

archive/issue_comments_004495.json:
```json
{
    "body": "See also #757",
    "created_at": "2007-09-28T11:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/758#issuecomment-4495",
    "user": "@robertwb"
}
```

See also #757



---

archive/issue_comments_004496.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-28T11:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/758#issuecomment-4496",
    "user": "@robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004497.json:
```json
{
    "body": "NTL now used for all composite modn",
    "created_at": "2007-09-30T07:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/758#issuecomment-4497",
    "user": "@robertwb"
}
```

NTL now used for all composite modn



---

archive/issue_comments_004498.json:
```json
{
    "body": "Attachment [fast-modn-poly.hg](tarball://root/attachments/some-uuid/ticket758/fast-modn-poly.hg) by @robertwb created at 2007-09-30 07:52:03\n\nThe latest bundle includes improvements to Laurent series, Monsky-Waschnitzer computations MUCH faster now (just waiting on fast p-adic linear algebra).",
    "created_at": "2007-09-30T07:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/758#issuecomment-4498",
    "user": "@robertwb"
}
```

Attachment [fast-modn-poly.hg](tarball://root/attachments/some-uuid/ticket758/fast-modn-poly.hg) by @robertwb created at 2007-09-30 07:52:03

The latest bundle includes improvements to Laurent series, Monsky-Waschnitzer computations MUCH faster now (just waiting on fast p-adic linear algebra).



---

archive/issue_comments_004499.json:
```json
{
    "body": "It seems that this still could be applicable, even though it is somewhat faster (NTL rewrite, coercion?)\n\n```\nmabshoff@sage:/tmp/Work-mabshoff/sage-2.8.8$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.8, Release Date: 2007-10-20                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: sage: f = Integers(100)['x'](range(10))\nsage: sage: time for _ in range(10^5): g = f*f\nCPU times: user 0.23 s, sys: 0.04 s, total: 0.27 s\nWall time: 0.27\nsage: sage: f = Integers(101)['x'](range(10))\nsage: sage: time for _ in range(10^5): g = f*f\nCPU times: user 2.12 s, sys: 0.03 s, total: 2.15 s\nWall time: 2.15\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-10-21T14:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/758#issuecomment-4499",
    "user": "mabshoff"
}
```

It seems that this still could be applicable, even though it is somewhat faster (NTL rewrite, coercion?)

```
mabshoff@sage:/tmp/Work-mabshoff/sage-2.8.8$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.8, Release Date: 2007-10-20                       |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: f = Integers(100)['x'](range(10))
sage: sage: time for _ in range(10^5): g = f*f
CPU times: user 0.23 s, sys: 0.04 s, total: 0.27 s
Wall time: 0.27
sage: sage: f = Integers(101)['x'](range(10))
sage: sage: time for _ in range(10^5): g = f*f
CPU times: user 2.12 s, sys: 0.03 s, total: 2.15 s
Wall time: 2.15
```

Cheers,

Michael



---

archive/issue_comments_004500.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-23T21:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/758#issuecomment-4500",
    "user": "@malb"
}
```

Resolution: fixed



---

archive/issue_comments_004501.json:
```json
{
    "body": "This patch seems to be 'in' already. Closing therefor and sending e-mail to author.",
    "created_at": "2007-10-23T21:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/758#issuecomment-4501",
    "user": "@malb"
}
```

This patch seems to be 'in' already. Closing therefor and sending e-mail to author.
