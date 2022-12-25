# Issue 7887: Fast function field arithmetic

archive/issues_007887.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @roed314\n\nWrapping zmod_poly directly should be much faster than the current implementation of Frac(GF(p)['t'])\n\nSee also #7585\n\nIssue created by migration from https://trac.sagemath.org/ticket/7887\n\n",
    "created_at": "2010-01-10T00:10:13Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Fast function field arithmetic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7887",
    "user": "https://github.com/robertwb"
}
```
Assignee: @aghitza

CC:  @roed314

Wrapping zmod_poly directly should be much faster than the current implementation of Frac(GF(p)['t'])

See also #7585

Issue created by migration from https://trac.sagemath.org/ticket/7887





---

archive/issue_comments_068460.json:
```json
{
    "body": "Attachment [7887-FpT.patch](tarball://root/attachments/some-uuid/ticket7887/7887-FpT.patch) by @robertwb created at 2010-01-10 00:13:04",
    "created_at": "2010-01-10T00:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7887#issuecomment-68460",
    "user": "https://github.com/robertwb"
}
```

Attachment [7887-FpT.patch](tarball://root/attachments/some-uuid/ticket7887/7887-FpT.patch) by @robertwb created at 2010-01-10 00:13:04



---

archive/issue_comments_068461.json:
```json
{
    "body": "Attachment [7887-FpT-update.patch](tarball://root/attachments/some-uuid/ticket7887/7887-FpT-update.patch) by @robertwb created at 2010-01-10 00:13:43\n\napply on top of previous",
    "created_at": "2010-01-10T00:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7887#issuecomment-68461",
    "user": "https://github.com/robertwb"
}
```

Attachment [7887-FpT-update.patch](tarball://root/attachments/some-uuid/ticket7887/7887-FpT-update.patch) by @robertwb created at 2010-01-10 00:13:43

apply on top of previous



---

archive/issue_comments_068462.json:
```json
{
    "body": "I know it's way to early for review, but maybe you could be inspired by ticket #7857 and implement directly Henrici's algorithms.\n\nYann",
    "created_at": "2010-01-10T07:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7887#issuecomment-68462",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

I know it's way to early for review, but maybe you could be inspired by ticket #7857 and implement directly Henrici's algorithms.

Yann



---

archive/issue_comments_068463.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-10-20T07:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7887#issuecomment-68463",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068464.json:
```json
{
    "body": "I guess this should be closed as a duplicate of #9051",
    "created_at": "2010-10-20T07:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7887#issuecomment-68464",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

I guess this should be closed as a duplicate of #9051



---

archive/issue_events_018861.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2010-10-20T15:53:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7887",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7887#event-18861"
}
```



---

archive/issue_comments_068465.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-10-20T15:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7887#issuecomment-68465",
    "user": "https://github.com/robertwb"
}
```

Resolution: duplicate



---

archive/issue_events_018862.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2010-10-20T15:53:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7887",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7887#event-18862"
}
```



---

archive/issue_comments_068466.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-10-20T15:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7887#issuecomment-68466",
    "user": "https://github.com/robertwb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_068467.json:
```json
{
    "body": "Correct.",
    "created_at": "2010-10-20T15:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7887#issuecomment-68467",
    "user": "https://github.com/robertwb"
}
```

Correct.
