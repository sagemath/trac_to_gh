# Issue 4269: add code to help detect which systems are used in performing a computation

archive/issues_004269.json:
```json
{
    "body": "Assignee: cwitty\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4269\n\n",
    "created_at": "2008-10-12T18:02:57Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "add code to help detect which systems are used in performing a computation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4269",
    "user": "@mwhansen"
}
```
Assignee: cwitty



Issue created by migration from https://trac.sagemath.org/ticket/4269





---

archive/issue_comments_031166.json:
```json
{
    "body": "Attachment [trac_4269.patch](tarball://root/attachments/some-uuid/ticket4269/trac_4269.patch) by @mwhansen created at 2008-10-12 18:09:02\n\nThe detection strings could probably use some refinement, but I'm going to spend some time working one something else.",
    "created_at": "2008-10-12T18:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31166",
    "user": "@mwhansen"
}
```

Attachment [trac_4269.patch](tarball://root/attachments/some-uuid/ticket4269/trac_4269.patch) by @mwhansen created at 2008-10-12 18:09:02

The detection strings could probably use some refinement, but I'm going to spend some time working one something else.



---

archive/issue_comments_031167.json:
```json
{
    "body": "Changing assignee from cwitty to @mwhansen.",
    "created_at": "2008-10-12T18:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31167",
    "user": "@mwhansen"
}
```

Changing assignee from cwitty to @mwhansen.



---

archive/issue_comments_031168.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-12T18:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31168",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031169.json:
```json
{
    "body": "Attachment [4269-referee.patch](tarball://root/attachments/some-uuid/ticket4269/4269-referee.patch) by @robertwb created at 2008-10-14 20:17:37",
    "created_at": "2008-10-14T20:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31169",
    "user": "@robertwb"
}
```

Attachment [4269-referee.patch](tarball://root/attachments/some-uuid/ticket4269/4269-referee.patch) by @robertwb created at 2008-10-14 20:17:37



---

archive/issue_comments_031170.json:
```json
{
    "body": "I added a bit more of a disclaimer, and raised a better error on non-strings (so when one types `get_systems('integrate(x^2, x)')` one doesn't get an obscure error. \n\nI give this a positive review, but someone should look at my changes.",
    "created_at": "2008-10-14T20:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31170",
    "user": "@robertwb"
}
```

I added a bit more of a disclaimer, and raised a better error on non-strings (so when one types `get_systems('integrate(x^2, x)')` one doesn't get an obscure error. 

I give this a positive review, but someone should look at my changes.



---

archive/issue_comments_031171.json:
```json
{
    "body": "I tested the type checking and ran some other example.\nMichael",
    "created_at": "2008-10-21T09:12:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31171",
    "user": "PolyBoRi"
}
```

I tested the type checking and ran some other example.
Michael



---

archive/issue_comments_031172.json:
```json
{
    "body": "Merged both patches in Sage 3.2.alpha1",
    "created_at": "2008-10-26T02:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31172",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.alpha1



---

archive/issue_comments_031173.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T02:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4269#issuecomment-31173",
    "user": "mabshoff"
}
```

Resolution: fixed
