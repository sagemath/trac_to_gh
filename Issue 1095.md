# Issue 1095: [with patch] silly annoyance in sage -coverage

archive/issues_001095.json:
```json
{
    "body": "Assignee: @craigcitro\n\nI made a silly mistake when I was editing sage-coverage -- it will always tell you that a function is \"possibly wrong\" (i.e. function name doesn't occur in doctest) when there is no doctest; this is pretty obvious. This patch fixes it, so that now things only appear in the \"possibly wrong\" list if they *don't* appear in either of the other lists (missing documentation or missing doctests).\n\nIssue created by migration from https://trac.sagemath.org/ticket/1095\n\n",
    "created_at": "2007-11-04T01:15:24Z",
    "labels": [
        "component: doctest coverage",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "[with patch] silly annoyance in sage -coverage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1095",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

I made a silly mistake when I was editing sage-coverage -- it will always tell you that a function is "possibly wrong" (i.e. function name doesn't occur in doctest) when there is no doctest; this is pretty obvious. This patch fixes it, so that now things only appear in the "possibly wrong" list if they *don't* appear in either of the other lists (missing documentation or missing doctests).

Issue created by migration from https://trac.sagemath.org/ticket/1095





---

archive/issue_comments_006609.json:
```json
{
    "body": "Attachment [trac_1095.hg](tarball://root/attachments/some-uuid/ticket1095/trac_1095.hg) by @craigcitro created at 2007-11-04 01:16:06\n\nbundle for $SAGE_ROOT/local/bin",
    "created_at": "2007-11-04T01:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1095#issuecomment-6609",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_1095.hg](tarball://root/attachments/some-uuid/ticket1095/trac_1095.hg) by @craigcitro created at 2007-11-04 01:16:06

bundle for $SAGE_ROOT/local/bin



---

archive/issue_comments_006610.json:
```json
{
    "body": "applied to 2.8.12.rc0",
    "created_at": "2007-11-06T22:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1095#issuecomment-6610",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.12.rc0



---

archive/issue_comments_006611.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T22:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1095#issuecomment-6611",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001221.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-11-06T22:33:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1095",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1095#event-1221"
}
```
