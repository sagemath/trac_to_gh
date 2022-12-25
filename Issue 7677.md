# Issue 7677: sage-4.3.rc0: powerpc g5 doctest blockers

archive/issues_007677.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nI did a build test on OS X 10.5 PPC and there are some problems I think not mentioned elsewhere.  The first is a badly written doctest by somebody who didn't think about hash values being architecture dependent, and the second is valid numerical noise:\n\npdlc424:sage-4.3.rc0 wstein$         sage -t -long \"devel/sage/sage/numerical/mip.pyx\"\n**********************************************************************\nFile \"/Users/wstein/build/sage-4.3.rc0/devel/sage/sage/numerical/mip.pyx\", line 987:\n    sage: p._NormalForm(v[0] + v[1])\nExpected:\n    {0: 0, x1: 1, x0: 1}\nGot:\n    {x1: 1, 0: 0, x0: 1}\n\n\npdlc424:sage-4.3.rc0 wstein$         sage -t -long \"devel/sage/sage/rings/complex_double.pyx\"\n**********************************************************************\nFile \"/Users/wstein/build/sage-4.3.rc0/devel/sage/sage/rings/complex_double.pyx\", line 2046:\n    sage: z^2 - z + 1\nExpected:\n    -4.4408920985e-16\nGot:\n    -2.22044604925e-16 - 2.22044604925e-16*I\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7677\n\n",
    "created_at": "2009-12-13T19:19:28Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "sage-4.3.rc0: powerpc g5 doctest blockers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7677",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```
I did a build test on OS X 10.5 PPC and there are some problems I think not mentioned elsewhere.  The first is a badly written doctest by somebody who didn't think about hash values being architecture dependent, and the second is valid numerical noise:

pdlc424:sage-4.3.rc0 wstein$         sage -t -long "devel/sage/sage/numerical/mip.pyx"
**********************************************************************
File "/Users/wstein/build/sage-4.3.rc0/devel/sage/sage/numerical/mip.pyx", line 987:
    sage: p._NormalForm(v[0] + v[1])
Expected:
    {0: 0, x1: 1, x0: 1}
Got:
    {x1: 1, 0: 0, x0: 1}


pdlc424:sage-4.3.rc0 wstein$         sage -t -long "devel/sage/sage/rings/complex_double.pyx"
**********************************************************************
File "/Users/wstein/build/sage-4.3.rc0/devel/sage/sage/rings/complex_double.pyx", line 2046:
    sage: z^2 - z + 1
Expected:
    -4.4408920985e-16
Got:
    -2.22044604925e-16 - 2.22044604925e-16*I
```


Issue created by migration from https://trac.sagemath.org/ticket/7677





---

archive/issue_comments_065734.json:
```json
{
    "body": "Attachment [trac_7677.patch](tarball://root/attachments/some-uuid/ticket7677/trac_7677.patch) by @mwhansen created at 2009-12-14 17:13:47",
    "created_at": "2009-12-14T17:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7677#issuecomment-65734",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7677.patch](tarball://root/attachments/some-uuid/ticket7677/trac_7677.patch) by @mwhansen created at 2009-12-14 17:13:47



---

archive/issue_comments_065735.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-14T17:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7677#issuecomment-65735",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065736.json:
```json
{
    "body": "Merged in 4.3.rc2.",
    "created_at": "2009-12-24T07:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7677#issuecomment-65736",
    "user": "https://github.com/williamstein"
}
```

Merged in 4.3.rc2.



---

archive/issue_comments_065737.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-24T07:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7677#issuecomment-65737",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
