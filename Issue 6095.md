# Issue 6095: implement sloane sequence: A060302 (digits of (pi^4+pi^5))^(1/6)

archive/issues_006095.json:
```json
{
    "body": "Assignee: @mwhansen\n\ninteresting because almost digits of e.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6095\n\n",
    "created_at": "2009-05-20T21:20:44Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "implement sloane sequence: A060302 (digits of (pi^4+pi^5))^(1/6)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6095",
    "user": "https://github.com/williamstein"
}
```
Assignee: @mwhansen

interesting because almost digits of e.

Issue created by migration from https://trac.sagemath.org/ticket/6095





---

archive/issue_comments_048507.json:
```json
{
    "body": "Attachment [12164.patch](tarball://root/attachments/some-uuid/ticket6095/12164.patch) by @williamstein created at 2009-05-20 21:48:42",
    "created_at": "2009-05-20T21:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6095#issuecomment-48507",
    "user": "https://github.com/williamstein"
}
```

Attachment [12164.patch](tarball://root/attachments/some-uuid/ticket6095/12164.patch) by @williamstein created at 2009-05-20 21:48:42



---

archive/issue_comments_048508.json:
```json
{
    "body": "The code looks good, but is this useful enough to have in Sage?",
    "created_at": "2009-05-20T21:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6095#issuecomment-48508",
    "user": "https://github.com/robertwb"
}
```

The code looks good, but is this useful enough to have in Sage?



---

archive/issue_comments_048509.json:
```json
{
    "body": "cwitty and robertwb pointed out a BUG.  If there is a sequence of more than ten 9's in a row, then this code can give a wrong answer.   One has to specifically deal with the case of 9's and use that the number is transcendental.",
    "created_at": "2009-05-21T06:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6095#issuecomment-48509",
    "user": "https://github.com/williamstein"
}
```

cwitty and robertwb pointed out a BUG.  If there is a sequence of more than ten 9's in a row, then this code can give a wrong answer.   One has to specifically deal with the case of 9's and use that the number is transcendental.
