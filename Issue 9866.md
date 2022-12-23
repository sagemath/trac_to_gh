# Issue 9866: getting rid of endianness-dependent behaviour in GAP random sources

archive/issues_009866.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  simonking\n\nin the thread [How to deal with GAP's machine dependent random generator?] on sage-devel Simon King mentioned that GAP own random source dependes on endianness of the machine.\nWhile Sage sort of takes care of this in misc/randstate.pyx,\nit still does not fix GAP internals. So, to make it good and proper, we essentially add the fix in misc/randstate.pyx to GAPROOT/src/integer.c, and remove it from misc/randstate.pyx\nThe updated gap spkg is here:\n\nhttp://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p5.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/9867\n\n",
    "created_at": "2010-09-07T13:04:14Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "title": "getting rid of endianness-dependent behaviour in GAP random sources",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9866",
    "user": "dimpase"
}
```
Assignee: joyner

CC:  simonking

in the thread [How to deal with GAP's machine dependent random generator?] on sage-devel Simon King mentioned that GAP own random source dependes on endianness of the machine.
While Sage sort of takes care of this in misc/randstate.pyx,
it still does not fix GAP internals. So, to make it good and proper, we essentially add the fix in misc/randstate.pyx to GAPROOT/src/integer.c, and remove it from misc/randstate.pyx
The updated gap spkg is here:

http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p5.spkg

Issue created by migration from https://trac.sagemath.org/ticket/9867





---

archive/issue_comments_097481.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-09-07T13:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9866#issuecomment-97481",
    "user": "dimpase"
}
```

Attachment



---

archive/issue_comments_097482.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-09-25T06:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9866#issuecomment-97482",
    "user": "dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097483.json:
```json
{
    "body": "This will be fixed in #13211. Let us close this one as obsolete.",
    "created_at": "2012-09-25T07:00:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9866#issuecomment-97483",
    "user": "dimpase"
}
```

This will be fixed in #13211. Let us close this one as obsolete.



---

archive/issue_comments_097484.json:
```json
{
    "body": "I can confirm that the current code is no longer needed as of #13211; see [comment:49:ticket:13211 here].",
    "created_at": "2012-09-25T12:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9866#issuecomment-97484",
    "user": "kcrisman"
}
```

I can confirm that the current code is no longer needed as of #13211; see [comment:49:ticket:13211 here].



---

archive/issue_comments_097485.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-09-25T12:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9866#issuecomment-97485",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097486.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-10-05T08:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9866#issuecomment-97486",
    "user": "jdemeyer"
}
```

Resolution: duplicate
