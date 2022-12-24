# Issue 5424: Move infinity to new coercion model

archive/issues_005424.json:
```json
{
    "body": "Assignee: robertwb\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5424\n\n",
    "created_at": "2009-03-03T09:23:25Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Move infinity to new coercion model",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5424",
    "user": "robertwb"
}
```
Assignee: robertwb



Issue created by migration from https://trac.sagemath.org/ticket/5424





---

archive/issue_comments_041977.json:
```json
{
    "body": "Plus got coverage from 9% to 100%",
    "created_at": "2009-03-03T13:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5424#issuecomment-41977",
    "user": "robertwb"
}
```

Plus got coverage from 9% to 100%



---

archive/issue_comments_041978.json:
```json
{
    "body": "Attachment [5424-coerce-infinity.patch](tarball://root/attachments/some-uuid/ticket5424/5424-coerce-infinity.patch) by mhansen created at 2009-03-07 22:02:21",
    "created_at": "2009-03-07T22:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5424#issuecomment-41978",
    "user": "mhansen"
}
```

Attachment [5424-coerce-infinity.patch](tarball://root/attachments/some-uuid/ticket5424/5424-coerce-infinity.patch) by mhansen created at 2009-03-07 22:02:21



---

archive/issue_comments_041979.json:
```json
{
    "body": "Attachment [trac_5424.patch](tarball://root/attachments/some-uuid/ticket5424/trac_5424.patch) by mhansen created at 2009-03-07 22:02:57\n\nI've attached trac_5424.patch which is the original patch rebased against 3.4.rc1 (and converted  use Sphinx syntax).",
    "created_at": "2009-03-07T22:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5424#issuecomment-41979",
    "user": "mhansen"
}
```

Attachment [trac_5424.patch](tarball://root/attachments/some-uuid/ticket5424/trac_5424.patch) by mhansen created at 2009-03-07 22:02:57

I've attached trac_5424.patch which is the original patch rebased against 3.4.rc1 (and converted  use Sphinx syntax).



---

archive/issue_comments_041980.json:
```json
{
    "body": "Looks good.  Thanks for cleaning up my old code.  :-/\n\nThe only problem I saw was that the doctest on line 449 was a bit strange (though not technically wrong).",
    "created_at": "2009-03-18T08:39:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5424#issuecomment-41980",
    "user": "roed"
}
```

Looks good.  Thanks for cleaning up my old code.  :-/

The only problem I saw was that the doctest on line 449 was a bit strange (though not technically wrong).



---

archive/issue_comments_041981.json:
```json
{
    "body": "Thanks for the review. The docstring on line 449 is to test uniqueness, and seemed like the only logical thing to test for that function anyways.",
    "created_at": "2009-03-18T19:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5424#issuecomment-41981",
    "user": "robertwb"
}
```

Thanks for the review. The docstring on line 449 is to test uniqueness, and seemed like the only logical thing to test for that function anyways.



---

archive/issue_comments_041982.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-20T21:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5424#issuecomment-41982",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041983.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-20T21:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5424#issuecomment-41983",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
