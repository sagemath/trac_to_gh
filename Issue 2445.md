# Issue 2445: algebras module lacks many docstrings and tests (score 15.7%)

archive/issues_002445.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: algebras modules\n\nMost files in sage/algebras have little or no docstrings and almost no doctests.  This patch makes a start on remedying this, but there is a lot more to be done.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2445\n\n",
    "created_at": "2008-03-09T21:22:10Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "algebras module lacks many docstrings and tests (score 15.7%)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2445",
    "user": "@JohnCremona"
}
```
Assignee: @malb

Keywords: algebras modules

Most files in sage/algebras have little or no docstrings and almost no doctests.  This patch makes a start on remedying this, but there is a lot more to be done.


Issue created by migration from https://trac.sagemath.org/ticket/2445





---

archive/issue_comments_016531.json:
```json
{
    "body": "Attachment [8821.patch](tarball://root/attachments/some-uuid/ticket2445/8821.patch) by @JohnCremona created at 2008-03-09 21:22:26",
    "created_at": "2008-03-09T21:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2445#issuecomment-16531",
    "user": "@JohnCremona"
}
```

Attachment [8821.patch](tarball://root/attachments/some-uuid/ticket2445/8821.patch) by @JohnCremona created at 2008-03-09 21:22:26



---

archive/issue_comments_016532.json:
```json
{
    "body": "This does not pass sage -t algebra.py",
    "created_at": "2008-03-10T08:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2445#issuecomment-16532",
    "user": "@garyfurnish"
}
```

This does not pass sage -t algebra.py



---

archive/issue_comments_016533.json:
```json
{
    "body": "This just needs a True statement added in the doctest in algebra.py",
    "created_at": "2008-03-10T08:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2445#issuecomment-16533",
    "user": "@garyfurnish"
}
```

This just needs a True statement added in the doctest in algebra.py



---

archive/issue_comments_016534.json:
```json
{
    "body": "Attachment [trac_8821.patch](tarball://root/attachments/some-uuid/ticket2445/trac_8821.patch) by @garyfurnish created at 2008-03-10 13:45:35\n\nFix for trivial algebra.py failure",
    "created_at": "2008-03-10T13:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2445#issuecomment-16534",
    "user": "@garyfurnish"
}
```

Attachment [trac_8821.patch](tarball://root/attachments/some-uuid/ticket2445/trac_8821.patch) by @garyfurnish created at 2008-03-10 13:45:35

Fix for trivial algebra.py failure



---

archive/issue_comments_016535.json:
```json
{
    "body": "Merged both patches in Sage 2.10.3.rc4",
    "created_at": "2008-03-10T13:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2445#issuecomment-16535",
    "user": "mabshoff"
}
```

Merged both patches in Sage 2.10.3.rc4



---

archive/issue_comments_016536.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-10T13:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2445#issuecomment-16536",
    "user": "mabshoff"
}
```

Resolution: fixed
