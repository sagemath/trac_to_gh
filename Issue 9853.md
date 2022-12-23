# Issue 9853: make networkx compatibel with numpy-1.4.1

archive/issues_009853.json:
```json
{
    "body": "Assignee: tbd\n\nIn order to finish Ticket #9808 (http://trac.sagemath.org/sage_trac/ticket/9808) there have to be a small patch applied to networks\n\nIssue created by migration from https://trac.sagemath.org/ticket/9854\n\n",
    "created_at": "2010-09-04T00:11:18Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "make networkx compatibel with numpy-1.4.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9853",
    "user": "maldun"
}
```
Assignee: tbd

In order to finish Ticket #9808 (http://trac.sagemath.org/sage_trac/ticket/9808) there have to be a small patch applied to networks

Issue created by migration from https://trac.sagemath.org/ticket/9854





---

archive/issue_comments_097249.json:
```json
{
    "body": "Attachment\n\nchanges",
    "created_at": "2010-09-04T00:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9853#issuecomment-97249",
    "user": "maldun"
}
```

Attachment

changes



---

archive/issue_comments_097250.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-04T00:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9853#issuecomment-97250",
    "user": "maldun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097251.json:
```json
{
    "body": "Attachment\n\nDownward compatibel patch",
    "created_at": "2010-09-04T01:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9853#issuecomment-97251",
    "user": "maldun"
}
```

Attachment

Downward compatibel patch



---

archive/issue_comments_097252.json:
```json
{
    "body": "modified version for networkx to make numpy-1.4.1 compatible",
    "created_at": "2010-09-04T01:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9853#issuecomment-97252",
    "user": "maldun"
}
```

modified version for networkx to make numpy-1.4.1 compatible



---

archive/issue_comments_097253.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-09-04T01:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9853#issuecomment-97253",
    "user": "maldun"
}
```

Attachment



---

archive/issue_comments_097254.json:
```json
{
    "body": "As I mentioned in the numpy upgrade bug we are moving to networkx-1.2.\nSo this bug may be invalid. Check have to be done against networkx-1.2 not 1.0.1.",
    "created_at": "2010-09-04T08:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9853#issuecomment-97254",
    "user": "fbissey"
}
```

As I mentioned in the numpy upgrade bug we are moving to networkx-1.2.
So this bug may be invalid. Check have to be done against networkx-1.2 not 1.0.1.



---

archive/issue_comments_097255.json:
```json
{
    "body": "Ok like mentioned in #9808 networkx-1.2 works with the numpy packages just fine.\nBut I had to install a new version, because I was not able to just install networkx-1.2 into my old version of sage-4.2. After intalling it and applying the patches it still didn't work correctly. But the patch of 1.0.1 above worked well for me. So it could still be usefull.\nBut I think we could close this ticket then.",
    "created_at": "2010-09-04T20:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9853#issuecomment-97255",
    "user": "maldun"
}
```

Ok like mentioned in #9808 networkx-1.2 works with the numpy packages just fine.
But I had to install a new version, because I was not able to just install networkx-1.2 into my old version of sage-4.2. After intalling it and applying the patches it still didn't work correctly. But the patch of 1.0.1 above worked well for me. So it could still be usefull.
But I think we could close this ticket then.



---

archive/issue_comments_097256.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-04T20:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9853#issuecomment-97256",
    "user": "maldun"
}
```

Resolution: fixed



---

archive/issue_comments_097257.json:
```json
{
    "body": "How is this ticket considered fixed? Do you want the attached NetworkX package to be merged in the Sage standard repository? If so, has it been merged yet? If not, you need to explain why you closed this ticket.",
    "created_at": "2010-09-05T05:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9853#issuecomment-97257",
    "user": "mvngu"
}
```

How is this ticket considered fixed? Do you want the attached NetworkX package to be merged in the Sage standard repository? If so, has it been merged yet? If not, you need to explain why you closed this ticket.



---

archive/issue_comments_097258.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-09-05T05:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9853#issuecomment-97258",
    "user": "mvngu"
}
```

Changing status from closed to needs_work.



---

archive/issue_comments_097259.json:
```json
{
    "body": "Replying to [comment:8 mvngu]:\n> How is this ticket considered fixed? Do you want the attached NetworkX package to be merged in the Sage standard repository? If so, has it been merged yet? If not, you need to explain why you closed this ticket.\n\nIt should have been closed invalid. Numpy-1.4.1 and networkx-1.0.1 don't go along\nvery well together. But it doesn't matter since next sage release will use networkx-1.2 which works well with numpy-1.4.1. I am changing it to \"invalid\".",
    "created_at": "2010-09-05T08:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9853#issuecomment-97259",
    "user": "fbissey"
}
```

Replying to [comment:8 mvngu]:
> How is this ticket considered fixed? Do you want the attached NetworkX package to be merged in the Sage standard repository? If so, has it been merged yet? If not, you need to explain why you closed this ticket.

It should have been closed invalid. Numpy-1.4.1 and networkx-1.0.1 don't go along
very well together. But it doesn't matter since next sage release will use networkx-1.2 which works well with numpy-1.4.1. I am changing it to "invalid".



---

archive/issue_comments_097260.json:
```json
{
    "body": "Resolution changed from fixed to invalid",
    "created_at": "2010-09-05T08:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9853#issuecomment-97260",
    "user": "fbissey"
}
```

Resolution changed from fixed to invalid
