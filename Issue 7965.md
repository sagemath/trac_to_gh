# Issue 7965: quo_rem attribute error (probably easy to fix?)

archive/issues_007965.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @orlitzky\n\n\n```\nsage: 5.quo_rem(2/3)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/virtual/scratch/wstein/build/sage-4.3.1.rc0/<ipython console> in <module>()\n\n/virtual/scratch/wstein/build/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.quo_rem (sage/rings/integer.c:16710)()\n\n/virtual/scratch/wstein/build/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.FieldElement.quo_rem (sage/structure/element.c:15715)()\n\nAttributeError: 'sage.rings.rational.Rational' object has no attribute '_parent'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7965\n\n",
    "created_at": "2010-01-17T10:37:46Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "quo_rem attribute error (probably easy to fix?)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7965",
    "user": "https://github.com/williamstein"
}
```
Assignee: @aghitza

CC:  @orlitzky


```
sage: 5.quo_rem(2/3)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/virtual/scratch/wstein/build/sage-4.3.1.rc0/<ipython console> in <module>()

/virtual/scratch/wstein/build/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.quo_rem (sage/rings/integer.c:16710)()

/virtual/scratch/wstein/build/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.FieldElement.quo_rem (sage/structure/element.c:15715)()

AttributeError: 'sage.rings.rational.Rational' object has no attribute '_parent'
```


Issue created by migration from https://trac.sagemath.org/ticket/7965





---

archive/issue_comments_069372.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-13T19:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7965#issuecomment-69372",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069373.json:
```json
{
    "body": "This looks fixed, at least for the rationals. I've added a doctest and changed the description of the `other` input which was weird anyway.",
    "created_at": "2012-01-13T19:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7965#issuecomment-69373",
    "user": "https://github.com/orlitzky"
}
```

This looks fixed, at least for the rationals. I've added a doctest and changed the description of the `other` input which was weird anyway.



---

archive/issue_comments_069374.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-16T19:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7965#issuecomment-69374",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069375.json:
```json
{
    "body": "Rebased to #10596, added one test.",
    "created_at": "2012-01-17T16:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7965#issuecomment-69375",
    "user": "https://github.com/jdemeyer"
}
```

Rebased to #10596, added one test.



---

archive/issue_comments_069376.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-01-17T16:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7965#issuecomment-69376",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_069377.json:
```json
{
    "body": "Attachment [sage-trac_7965.patch](tarball://root/attachments/some-uuid/ticket7965/sage-trac_7965.patch) by @jdemeyer created at 2012-01-17 16:01:02\n\nAdd a doctest with the example from the description.",
    "created_at": "2012-01-17T16:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7965#issuecomment-69377",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [sage-trac_7965.patch](tarball://root/attachments/some-uuid/ticket7965/sage-trac_7965.patch) by @jdemeyer created at 2012-01-17 16:01:02

Add a doctest with the example from the description.



---

archive/issue_comments_069378.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-01-17T16:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7965#issuecomment-69378",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069379.json:
```json
{
    "body": "The ticket number is missing from the commit message, but I suppose that's how you want it? The new patch applies and tests cleanly.",
    "created_at": "2012-01-17T18:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7965#issuecomment-69379",
    "user": "https://github.com/orlitzky"
}
```

The ticket number is missing from the commit message, but I suppose that's how you want it? The new patch applies and tests cleanly.



---

archive/issue_comments_069380.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-17T18:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7965#issuecomment-69380",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069381.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-01-18T08:14:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7965#issuecomment-69381",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
