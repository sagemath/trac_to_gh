# Issue 6584: Use pari to do ideal intersections

archive/issues_006584.json:
```json
{
    "body": "Assignee: davidloeffler\n\nCC:  davidloeffler ncalexan\n\nKeywords: ideal, intersecton, pari\n\nAs an addendum to #6457, I propose reworking the code to use the pari function `idealintersect`.   The patch does this.  The result is a significantly faster function. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6584\n\n",
    "created_at": "2009-07-21T21:33:28Z",
    "labels": [
        "number fields",
        "minor",
        "enhancement"
    ],
    "title": "Use pari to do ideal intersections",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6584",
    "user": "fwclarke"
}
```
Assignee: davidloeffler

CC:  davidloeffler ncalexan

Keywords: ideal, intersecton, pari

As an addendum to #6457, I propose reworking the code to use the pari function `idealintersect`.   The patch does this.  The result is a significantly faster function. 

Issue created by migration from https://trac.sagemath.org/ticket/6584





---

archive/issue_comments_053797.json:
```json
{
    "body": "patch against 4.1.1.alpha0",
    "created_at": "2009-07-21T21:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6584#issuecomment-53797",
    "user": "fwclarke"
}
```

patch against 4.1.1.alpha0



---

archive/issue_comments_053798.json:
```json
{
    "body": "Attachment [trac_6584.patch](tarball://root/attachments/some-uuid/ticket6584/trac_6584.patch) by cremona created at 2010-01-18 20:34:03\n\nThe patch still applies to 4.3.1.rc0 (miracle!) and all tests in rings/number_field and libs/pari pass.",
    "created_at": "2010-01-18T20:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6584#issuecomment-53798",
    "user": "cremona"
}
```

Attachment [trac_6584.patch](tarball://root/attachments/some-uuid/ticket6584/trac_6584.patch) by cremona created at 2010-01-18 20:34:03

The patch still applies to 4.3.1.rc0 (miracle!) and all tests in rings/number_field and libs/pari pass.



---

archive/issue_comments_053799.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T20:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6584#issuecomment-53799",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053800.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T20:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6584#issuecomment-53800",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053801.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T00:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6584#issuecomment-53801",
    "user": "rlm"
}
```

Resolution: fixed
