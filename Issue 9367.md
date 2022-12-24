# Issue 9367: S_unit return type is incorrect,

archive/issues_009367.json:
```json
{
    "body": "Assignee: davidloeffler\n\nCC:  mjo\n\nKeywords: S_units\n\nHere is a sample error:\n\n```\nsage: _.<x>=QQ[]\nsage: L.<alpha>=NumberField(x^3+x+1)\nsage: p=L.S_units([ L.ideal(7) ] )\nsage: p[0].parent()\nRational Field\n```\n\nThe correct output should be\n\n```\nNumber Field in alpha with defining polynomial x^3 + x + 1\n```\n\n\nThe attached patch solves this problem.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9367\n\n",
    "created_at": "2010-06-28T21:54:48Z",
    "labels": [
        "number fields",
        "major",
        "bug"
    ],
    "title": "S_unit return type is incorrect,",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9367",
    "user": "syazdani"
}
```
Assignee: davidloeffler

CC:  mjo

Keywords: S_units

Here is a sample error:

```
sage: _.<x>=QQ[]
sage: L.<alpha>=NumberField(x^3+x+1)
sage: p=L.S_units([ L.ideal(7) ] )
sage: p[0].parent()
Rational Field
```

The correct output should be

```
Number Field in alpha with defining polynomial x^3 + x + 1
```


The attached patch solves this problem.

Issue created by migration from https://trac.sagemath.org/ticket/9367





---

archive/issue_comments_088972.json:
```json
{
    "body": "Attachment [patch-9367.patch](tarball://root/attachments/some-uuid/ticket9367/patch-9367.patch) by syazdani created at 2010-06-28 22:08:33\n\nFixes the return type.",
    "created_at": "2010-06-28T22:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9367#issuecomment-88972",
    "user": "syazdani"
}
```

Attachment [patch-9367.patch](tarball://root/attachments/some-uuid/ticket9367/patch-9367.patch) by syazdani created at 2010-06-28 22:08:33

Fixes the return type.



---

archive/issue_comments_088973.json:
```json
{
    "body": "Add a doctest for the correct behavior.",
    "created_at": "2012-01-16T04:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9367#issuecomment-88973",
    "user": "mjo"
}
```

Add a doctest for the correct behavior.



---

archive/issue_comments_088974.json:
```json
{
    "body": "Attachment [sage-trac_9367.patch](tarball://root/attachments/some-uuid/ticket9367/sage-trac_9367.patch) by mjo created at 2012-01-16 04:22:20\n\nIt looks like someone beat you to it! I get the correct answer with 4.8.alpha6, so I've added a doctest for it.",
    "created_at": "2012-01-16T04:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9367#issuecomment-88974",
    "user": "mjo"
}
```

Attachment [sage-trac_9367.patch](tarball://root/attachments/some-uuid/ticket9367/sage-trac_9367.patch) by mjo created at 2012-01-16 04:22:20

It looks like someone beat you to it! I get the correct answer with 4.8.alpha6, so I've added a doctest for it.



---

archive/issue_comments_088975.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-16T04:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9367#issuecomment-88975",
    "user": "mjo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088976.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-12T20:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9367#issuecomment-88976",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088977.json:
```json
{
    "body": "Apply sage-trac_9367.patch\n\n(for patchbot).",
    "created_at": "2012-03-12T20:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9367#issuecomment-88977",
    "user": "davidloeffler"
}
```

Apply sage-trac_9367.patch

(for patchbot).



---

archive/issue_comments_088978.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2012-03-12T20:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9367#issuecomment-88978",
    "user": "davidloeffler"
}
```

Changing priority from major to minor.



---

archive/issue_comments_088979.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-21T22:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9367#issuecomment-88979",
    "user": "jdemeyer"
}
```

Resolution: fixed
