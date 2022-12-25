# Issue 4269: add code to help detect which systems are used in performing a computation

archive/issues_004269.json:
```json
{
    "body": "Assignee: cwitty\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4269\n\n",
    "created_at": "2008-10-12T18:02:57Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "add code to help detect which systems are used in performing a computation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4269",
    "user": "https://github.com/mwhansen"
}
```
Assignee: cwitty



Issue created by migration from https://trac.sagemath.org/ticket/4269





---

archive/issue_comments_031104.json:
```json
{
    "body": "Attachment [trac_4269.patch](tarball://root/attachments/some-uuid/ticket4269/trac_4269.patch) by @mwhansen created at 2008-10-12 18:09:02\n\nThe detection strings could probably use some refinement, but I'm going to spend some time working one something else.",
    "created_at": "2008-10-12T18:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31104",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4269.patch](tarball://root/attachments/some-uuid/ticket4269/trac_4269.patch) by @mwhansen created at 2008-10-12 18:09:02

The detection strings could probably use some refinement, but I'm going to spend some time working one something else.



---

archive/issue_comments_031105.json:
```json
{
    "body": "Changing assignee from cwitty to @mwhansen.",
    "created_at": "2008-10-12T18:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31105",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from cwitty to @mwhansen.



---

archive/issue_comments_031106.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-12T18:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31106",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031107.json:
```json
{
    "body": "Attachment [4269-referee.patch](tarball://root/attachments/some-uuid/ticket4269/4269-referee.patch) by @robertwb created at 2008-10-14 20:17:37",
    "created_at": "2008-10-14T20:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31107",
    "user": "https://github.com/robertwb"
}
```

Attachment [4269-referee.patch](tarball://root/attachments/some-uuid/ticket4269/4269-referee.patch) by @robertwb created at 2008-10-14 20:17:37



---

archive/issue_comments_031108.json:
```json
{
    "body": "I added a bit more of a disclaimer, and raised a better error on non-strings (so when one types `get_systems('integrate(x^2, x)')` one doesn't get an obscure error. \n\nI give this a positive review, but someone should look at my changes.",
    "created_at": "2008-10-14T20:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31108",
    "user": "https://github.com/robertwb"
}
```

I added a bit more of a disclaimer, and raised a better error on non-strings (so when one types `get_systems('integrate(x^2, x)')` one doesn't get an obscure error. 

I give this a positive review, but someone should look at my changes.



---

archive/issue_comments_031109.json:
```json
{
    "body": "I tested the type checking and ran some other example.\nMichael",
    "created_at": "2008-10-21T09:12:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31109",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

I tested the type checking and ran some other example.
Michael



---

archive/issue_comments_031110.json:
```json
{
    "body": "Merged both patches in Sage 3.2.alpha1",
    "created_at": "2008-10-26T02:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31110",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.2.alpha1



---

archive/issue_comments_031111.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T02:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31111",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004514.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-10-26T02:26:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4269#event-4514"
}
```
