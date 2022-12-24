# Issue 8948: add thin space between vector entries

archive/issues_008948.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  rbeezer\n\nThis patch adds a thin space between vector entries, which helps distinguish the entries from each other, especially when there are symbolic expressions, so the entries already may have thin spaces in them.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8948\n\n",
    "created_at": "2010-05-11T06:29:05Z",
    "labels": [
        "linear algebra",
        "minor",
        "enhancement"
    ],
    "title": "add thin space between vector entries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8948",
    "user": "jason"
}
```
Assignee: jason, was

CC:  rbeezer

This patch adds a thin space between vector entries, which helps distinguish the entries from each other, especially when there are symbolic expressions, so the entries already may have thin spaces in them.

Issue created by migration from https://trac.sagemath.org/ticket/8948





---

archive/issue_comments_082385.json:
```json
{
    "body": "Attachment [trac-8948-vector-printing-space.patch](tarball://root/attachments/some-uuid/ticket8948/trac-8948-vector-printing-space.patch) by jason created at 2010-05-11 06:30:03",
    "created_at": "2010-05-11T06:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82385",
    "user": "jason"
}
```

Attachment [trac-8948-vector-printing-space.patch](tarball://root/attachments/some-uuid/ticket8948/trac-8948-vector-printing-space.patch) by jason created at 2010-05-11 06:30:03



---

archive/issue_comments_082386.json:
```json
{
    "body": "Rob, you might be interested in this slight improvement to linear algebra latexing.\n\nMaybe this ticket only needs a doctest to be ready for review?",
    "created_at": "2011-01-18T17:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82386",
    "user": "jason"
}
```

Rob, you might be interested in this slight improvement to linear algebra latexing.

Maybe this ticket only needs a doctest to be ready for review?



---

archive/issue_comments_082387.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2011-01-18T17:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82387",
    "user": "jason"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_082388.json:
```json
{
    "body": "Yep, code looks good.  I *always* put a thin space into my vectors, so this will be nice to have automatically.  Doctests are updated, made two necessary fixes in the symbolic-callable tests.  Running tests right now and will report back.",
    "created_at": "2011-01-21T05:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82388",
    "user": "rbeezer"
}
```

Yep, code looks good.  I *always* put a thin space into my vectors, so this will be nice to have automatically.  Doctests are updated, made two necessary fixes in the symbolic-callable tests.  Running tests right now and will report back.



---

archive/issue_comments_082389.json:
```json
{
    "body": "Attachment [trac_8948-vector-printing-doctests.patch](tarball://root/attachments/some-uuid/ticket8948/trac_8948-vector-printing-doctests.patch) by rbeezer created at 2011-01-23 04:37:45\n\nAttachment is totally doctests that needed fixing, plus one new one.  No change to the code.  I'm fine with a positive review on the code once somebody checks my doctest changes.",
    "created_at": "2011-01-23T04:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82389",
    "user": "rbeezer"
}
```

Attachment [trac_8948-vector-printing-doctests.patch](tarball://root/attachments/some-uuid/ticket8948/trac_8948-vector-printing-doctests.patch) by rbeezer created at 2011-01-23 04:37:45

Attachment is totally doctests that needed fixing, plus one new one.  No change to the code.  I'm fine with a positive review on the code once somebody checks my doctest changes.



---

archive/issue_comments_082390.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-23T04:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82390",
    "user": "rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082391.json:
```json
{
    "body": "Doctests changes looks good, I also think that it will be a nice improvement!",
    "created_at": "2011-01-23T05:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82391",
    "user": "novoselt"
}
```

Doctests changes looks good, I also think that it will be a nice improvement!



---

archive/issue_comments_082392.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-23T05:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82392",
    "user": "novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082393.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-26T22:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8948#issuecomment-82393",
    "user": "jdemeyer"
}
```

Resolution: fixed
