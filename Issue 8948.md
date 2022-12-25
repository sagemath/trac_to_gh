# Issue 8948: add thin space between vector entries

archive/issues_008948.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @rbeezer\n\nThis patch adds a thin space between vector entries, which helps distinguish the entries from each other, especially when there are symbolic expressions, so the entries already may have thin spaces in them.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8948\n\n",
    "closed_at": "2011-01-26T22:26:33Z",
    "created_at": "2010-05-11T06:29:05Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "add thin space between vector entries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8948",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, was

CC:  @rbeezer

This patch adds a thin space between vector entries, which helps distinguish the entries from each other, especially when there are symbolic expressions, so the entries already may have thin spaces in them.

Issue created by migration from https://trac.sagemath.org/ticket/8948





---

archive/issue_comments_082250.json:
```json
{
    "body": "Attachment [trac-8948-vector-printing-space.patch](tarball://root/attachments/some-uuid/ticket8948/trac-8948-vector-printing-space.patch) by @jasongrout created at 2010-05-11 06:30:03",
    "created_at": "2010-05-11T06:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82250",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8948-vector-printing-space.patch](tarball://root/attachments/some-uuid/ticket8948/trac-8948-vector-printing-space.patch) by @jasongrout created at 2010-05-11 06:30:03



---

archive/issue_comments_082251.json:
```json
{
    "body": "Rob, you might be interested in this slight improvement to linear algebra latexing.\n\nMaybe this ticket only needs a doctest to be ready for review?",
    "created_at": "2011-01-18T17:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82251",
    "user": "https://github.com/jasongrout"
}
```

Rob, you might be interested in this slight improvement to linear algebra latexing.

Maybe this ticket only needs a doctest to be ready for review?



---

archive/issue_comments_082252.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2011-01-18T17:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82252",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_082253.json:
```json
{
    "body": "Yep, code looks good.  I *always* put a thin space into my vectors, so this will be nice to have automatically.  Doctests are updated, made two necessary fixes in the symbolic-callable tests.  Running tests right now and will report back.",
    "created_at": "2011-01-21T05:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82253",
    "user": "https://github.com/rbeezer"
}
```

Yep, code looks good.  I *always* put a thin space into my vectors, so this will be nice to have automatically.  Doctests are updated, made two necessary fixes in the symbolic-callable tests.  Running tests right now and will report back.



---

archive/issue_comments_082254.json:
```json
{
    "body": "Attachment [trac_8948-vector-printing-doctests.patch](tarball://root/attachments/some-uuid/ticket8948/trac_8948-vector-printing-doctests.patch) by @rbeezer created at 2011-01-23 04:37:45\n\nAttachment is totally doctests that needed fixing, plus one new one.  No change to the code.  I'm fine with a positive review on the code once somebody checks my doctest changes.",
    "created_at": "2011-01-23T04:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82254",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_8948-vector-printing-doctests.patch](tarball://root/attachments/some-uuid/ticket8948/trac_8948-vector-printing-doctests.patch) by @rbeezer created at 2011-01-23 04:37:45

Attachment is totally doctests that needed fixing, plus one new one.  No change to the code.  I'm fine with a positive review on the code once somebody checks my doctest changes.



---

archive/issue_comments_082255.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-23T04:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82255",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082256.json:
```json
{
    "body": "Doctests changes looks good, I also think that it will be a nice improvement!",
    "created_at": "2011-01-23T05:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82256",
    "user": "https://github.com/novoselt"
}
```

Doctests changes looks good, I also think that it will be a nice improvement!



---

archive/issue_comments_082257.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-23T05:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82257",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_021854.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-26T22:26:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8948#event-21854"
}
```



---

archive/issue_comments_082258.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-26T22:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82258",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
