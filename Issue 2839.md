# Issue 2839: bug in conversion from symmetrica's longint

archive/issues_002839.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  sage-combinat\n\nThis was reported here: http://groups.google.com/group/sage-devel/tree/browse_frm/thread/718d1d2853988d13/beece4dabd2d84c8?rnum=1&_done=%2Fgroup%2Fsage-devel%2Fbrowse_frm%2Fthread%2F718d1d2853988d13%3F#doc_909abc517bb7eeb6\n\nIssue created by migration from https://trac.sagemath.org/ticket/2839\n\n",
    "created_at": "2008-04-07T07:15:33Z",
    "labels": [
        "component: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "bug in conversion from symmetrica's longint",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2839",
    "user": "https://github.com/mwhansen"
}
```
Assignee: mabshoff

CC:  sage-combinat

This was reported here: http://groups.google.com/group/sage-devel/tree/browse_frm/thread/718d1d2853988d13/beece4dabd2d84c8?rnum=1&_done=%2Fgroup%2Fsage-devel%2Fbrowse_frm%2Fthread%2F718d1d2853988d13%3F#doc_909abc517bb7eeb6

Issue created by migration from https://trac.sagemath.org/ticket/2839





---

archive/issue_comments_019431.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-07T07:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2839#issuecomment-19431",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019432.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2008-04-07T07:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2839#issuecomment-19432",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_events_006516.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-04-07T07:15:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2839",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2839#event-6516"
}
```



---

archive/issue_comments_019433.json:
```json
{
    "body": "Changing component from Cygwin to combinatorics.",
    "created_at": "2008-04-07T07:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2839#issuecomment-19433",
    "user": "https://github.com/mwhansen"
}
```

Changing component from Cygwin to combinatorics.



---

archive/issue_comments_019434.json:
```json
{
    "body": "Attachment [2839.patch](tarball://root/attachments/some-uuid/ticket2839/2839.patch) by @mwhansen created at 2008-04-07 07:16:41",
    "created_at": "2008-04-07T07:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2839#issuecomment-19434",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2839.patch](tarball://root/attachments/some-uuid/ticket2839/2839.patch) by @mwhansen created at 2008-04-07 07:16:41



---

archive/issue_comments_019435.json:
```json
{
    "body": "The patch also includes a speed up for change of bases over QQ.\n\nBefore:\n\n```\nsage: time s(p(s([17,11])))\nCPU times: user 1252.31 s, sys: 8.24 s, total: 1260.55 s\nWall time: 1259.90\ns[17, 11]\nsage: time a = s([10,10]).itensor(s([10,10]))\nCPU times: user 30.87 s, sys: 0.21 s, total: 31.09 s\nWall time: 31.09\n```\n\n\nAfter:\n\n```\nsage: time s(p(s([17,11])))\nCPU times: user 257.11 s, sys: 0.03 s, total: 257.14 s\nWall time: 257.15\ns[17, 11]\nsage: time a = s([10,10]).itensor(s([10,10]))\nCPU times: user 3.60 s, sys: 0.00 s, total: 3.60 s\nWall time: 3.60\n```\n",
    "created_at": "2008-04-07T07:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2839#issuecomment-19435",
    "user": "https://github.com/mwhansen"
}
```

The patch also includes a speed up for change of bases over QQ.

Before:

```
sage: time s(p(s([17,11])))
CPU times: user 1252.31 s, sys: 8.24 s, total: 1260.55 s
Wall time: 1259.90
s[17, 11]
sage: time a = s([10,10]).itensor(s([10,10]))
CPU times: user 30.87 s, sys: 0.21 s, total: 31.09 s
Wall time: 31.09
```


After:

```
sage: time s(p(s([17,11])))
CPU times: user 257.11 s, sys: 0.03 s, total: 257.14 s
Wall time: 257.15
s[17, 11]
sage: time a = s([10,10]).itensor(s([10,10]))
CPU times: user 3.60 s, sys: 0.00 s, total: 3.60 s
Wall time: 3.60
```




---

archive/issue_comments_019436.json:
```json
{
    "body": "The patch works for me (32-bit Ubuntu Hardy) and fixes the issues mentioned in the sage-devel thread. All tests pass on /libs/symmetrica/symmetrica.pxi.",
    "created_at": "2008-04-07T08:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2839#issuecomment-19436",
    "user": "https://github.com/dandrake"
}
```

The patch works for me (32-bit Ubuntu Hardy) and fixes the issues mentioned in the sage-devel thread. All tests pass on /libs/symmetrica/symmetrica.pxi.



---

archive/issue_comments_019437.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-07T14:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2839#issuecomment-19437",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha3



---

archive/issue_events_006517.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-07T14:22:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2839",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2839#event-6517"
}
```



---

archive/issue_comments_019438.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T14:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2839#issuecomment-19438",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
