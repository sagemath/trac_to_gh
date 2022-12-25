# Issue 8300: native algdep with proof option

archive/issues_008300.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein\n\nUsing the properties of LLL and a height bound, we can prove (given sufficient precision) that an integer relation of bounded height either doesn't exist or is unique. This is needed, e.g.,  for provable computations of Heegner points though could be useful elsewhere as well. It is also faster.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/8300\n\n",
    "closed_at": "2010-04-15T20:07:23Z",
    "created_at": "2010-02-19T01:41:38Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "native algdep with proof option",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8300",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

CC:  @williamstein

Using the properties of LLL and a height bound, we can prove (given sufficient precision) that an integer relation of bounded height either doesn't exist or is unique. This is needed, e.g.,  for provable computations of Heegner points though could be useful elsewhere as well. It is also faster.  

Issue created by migration from https://trac.sagemath.org/ticket/8300





---

archive/issue_comments_073398.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-19T01:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8300#issuecomment-73398",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073399.json:
```json
{
    "body": "Attachment [8300-algdep-proof.patch](tarball://root/attachments/some-uuid/ticket8300/8300-algdep-proof.patch) by @robertwb created at 2010-02-20 01:05:04",
    "created_at": "2010-02-20T01:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8300#issuecomment-73399",
    "user": "https://github.com/robertwb"
}
```

Attachment [8300-algdep-proof.patch](tarball://root/attachments/some-uuid/ticket8300/8300-algdep-proof.patch) by @robertwb created at 2010-02-20 01:05:04



---

archive/issue_comments_073400.json:
```json
{
    "body": "Looks good, applies to 4.3.5 (with a small amount of fuzz).  Tests in sage/rings all pass.  Docs build and look good.  I did some random testing of my own and the results seem fine.\n\nSmall question:  why does algdep? not display the docstring?  algdep?? works fine though.",
    "created_at": "2010-04-05T16:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8300#issuecomment-73400",
    "user": "https://github.com/JohnCremona"
}
```

Looks good, applies to 4.3.5 (with a small amount of fuzz).  Tests in sage/rings all pass.  Docs build and look good.  I did some random testing of my own and the results seem fine.

Small question:  why does algdep? not display the docstring?  algdep?? works fine though.



---

archive/issue_comments_073401.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-05T16:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8300#issuecomment-73401",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019861.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-15T20:07:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8300",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8300#event-19861"
}
```



---

archive/issue_comments_073402.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n\n- 8300-algdep-proof.patch",
    "created_at": "2010-04-15T20:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8300#issuecomment-73402",
    "user": "https://github.com/jhpalmieri"
}
```

Merged in 4.4.alpha0:

- 8300-algdep-proof.patch



---

archive/issue_comments_073403.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T20:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8300#issuecomment-73403",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
