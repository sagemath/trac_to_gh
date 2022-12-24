# Issue 922: bug in prime_powers

archive/issues_000922.json:
```json
{
    "body": "Assignee: somebody\n\nInconsistent types:\n\n\n```\nsage: vv = prime_powers(10)\nsage: type(vv[0])\n<type 'int'>\nsage: type(vv[1])\n<type 'sage.rings.integer.Integer'>\n```\n\n\nFreebie for bug day on Saturday :-)\n\nIssue created by migration from https://trac.sagemath.org/ticket/922\n\n",
    "created_at": "2007-10-18T18:35:31Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "bug in prime_powers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/922",
    "user": "@williamstein"
}
```
Assignee: somebody

Inconsistent types:


```
sage: vv = prime_powers(10)
sage: type(vv[0])
<type 'int'>
sage: type(vv[1])
<type 'sage.rings.integer.Integer'>
```


Freebie for bug day on Saturday :-)

Issue created by migration from https://trac.sagemath.org/ticket/922





---

archive/issue_comments_005652.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-20T19:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/922#issuecomment-5652",
    "user": "@robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005653.json:
```json
{
    "body": "Changing assignee from somebody to @robertwb.",
    "created_at": "2007-10-20T19:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/922#issuecomment-5653",
    "user": "@robertwb"
}
```

Changing assignee from somebody to @robertwb.



---

archive/issue_comments_005654.json:
```json
{
    "body": "Attachment [922.patch](tarball://root/attachments/some-uuid/ticket922/922.patch) by @robertwb created at 2007-10-20 19:40:28",
    "created_at": "2007-10-20T19:40:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/922#issuecomment-5654",
    "user": "@robertwb"
}
```

Attachment [922.patch](tarball://root/attachments/some-uuid/ticket922/922.patch) by @robertwb created at 2007-10-20 19:40:28



---

archive/issue_comments_005655.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T00:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/922#issuecomment-5655",
    "user": "@williamstein"
}
```

Resolution: fixed
