# Issue 6953: follow-up to #6950: fix warning when building reference manual

archive/issues_006953.json:
```json
{
    "body": "Assignee: tba\n\nCC:  ylchapuy @malb\n\nThis is a follow-up to ticket #6950. I got the following warning when building the reference manual with the patch at #6950:\n\n```\nWARNING: inline latex u'f(x)g(x) = 0 \\x0corall x.\\n\\n': latex exited with error:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6953\n\n",
    "created_at": "2009-09-17T23:35:08Z",
    "labels": [
        "documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "follow-up to #6950: fix warning when building reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6953",
    "user": "mvngu"
}
```
Assignee: tba

CC:  ylchapuy @malb

This is a follow-up to ticket #6950. I got the following warning when building the reference manual with the patch at #6950:

```
WARNING: inline latex u'f(x)g(x) = 0 \x0corall x.\n\n': latex exited with error:
```


Issue created by migration from https://trac.sagemath.org/ticket/6953





---

archive/issue_comments_057497.json:
```json
{
    "body": "Patch looks good except there seems to be a 'fullstop' (aka 'period') missing at the end.",
    "created_at": "2009-09-18T08:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6953#issuecomment-57497",
    "user": "@malb"
}
```

Patch looks good except there seems to be a 'fullstop' (aka 'period') missing at the end.



---

archive/issue_comments_057498.json:
```json
{
    "body": "Attachment [trac_6953-typo-fixes.patch](tarball://root/attachments/some-uuid/ticket6953/trac_6953-typo-fixes.patch) by mvngu created at 2009-09-18 09:05:35\n\ndepends on #6950",
    "created_at": "2009-09-18T09:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6953#issuecomment-57498",
    "user": "mvngu"
}
```

Attachment [trac_6953-typo-fixes.patch](tarball://root/attachments/some-uuid/ticket6953/trac_6953-typo-fixes.patch) by mvngu created at 2009-09-18 09:05:35

depends on #6950



---

archive/issue_comments_057499.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> Patch looks good except there seems to be a 'fullstop' (aka 'period') missing at the end. \nFixed. See the new patch.",
    "created_at": "2009-09-18T09:06:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6953#issuecomment-57499",
    "user": "mvngu"
}
```

Replying to [comment:2 malb]:
> Patch looks good except there seems to be a 'fullstop' (aka 'period') missing at the end. 
Fixed. See the new patch.



---

archive/issue_comments_057500.json:
```json
{
    "body": ":) I only pointed it out because I know you care about these kind of things.",
    "created_at": "2009-09-18T09:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6953#issuecomment-57500",
    "user": "@malb"
}
```

:) I only pointed it out because I know you care about these kind of things.



---

archive/issue_comments_057501.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-18T13:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6953#issuecomment-57501",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057502.json:
```json
{
    "body": "Merged patches in this order:\n\n1. the patch at #6950\n2. `trac_6953-typo-fixes.patch`",
    "created_at": "2009-09-18T13:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6953#issuecomment-57502",
    "user": "mvngu"
}
```

Merged patches in this order:

1. the patch at #6950
2. `trac_6953-typo-fixes.patch`
