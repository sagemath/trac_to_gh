# Issue 2421: .round(), .floor(), .ceil(), and .trunc() on RealNumber should have the same return type

archive/issues_002421.json:
```json
{
    "body": "Assignee: somebody\n\nCurrently the `RealNumber` methods .round() and .trunc() return `RealNumber`, but .floor() and .ceil() return `Integer`.  I think that all four methods should return `Integer`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2421\n\n",
    "created_at": "2008-03-07T15:23:43Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": ".round(), .floor(), .ceil(), and .trunc() on RealNumber should have the same return type",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2421",
    "user": "cwitty"
}
```
Assignee: somebody

Currently the `RealNumber` methods .round() and .trunc() return `RealNumber`, but .floor() and .ceil() return `Integer`.  I think that all four methods should return `Integer`.

Issue created by migration from https://trac.sagemath.org/ticket/2421





---

archive/issue_comments_016382.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-10T20:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2421#issuecomment-16382",
    "user": "dfdeshom"
}
```

Attachment



---

archive/issue_comments_016383.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-10T20:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2421#issuecomment-16383",
    "user": "dfdeshom"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016384.json:
```json
{
    "body": "Changing assignee from somebody to dfdeshom.",
    "created_at": "2008-03-10T20:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2421#issuecomment-16384",
    "user": "dfdeshom"
}
```

Changing assignee from somebody to dfdeshom.



---

archive/issue_comments_016385.json:
```json
{
    "body": "patch looks good. I say apply.",
    "created_at": "2008-03-12T09:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2421#issuecomment-16385",
    "user": "malb"
}
```

patch looks good. I say apply.



---

archive/issue_comments_016386.json:
```json
{
    "body": "Didier, please submit mercurial patches in the future so you will get proper credit for your patches in the changelog. In this case it was too late and now credit goes to me :(\n\nCheers,\n\nMichael",
    "created_at": "2008-03-12T19:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2421#issuecomment-16386",
    "user": "mabshoff"
}
```

Didier, please submit mercurial patches in the future so you will get proper credit for your patches in the changelog. In this case it was too late and now credit goes to me :(

Cheers,

Michael



---

archive/issue_comments_016387.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-12T19:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2421#issuecomment-16387",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016388.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-12T19:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2421#issuecomment-16388",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
