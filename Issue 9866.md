# Issue 9866: getting rid of endianness-dependent behaviour in GAP random sources

archive/issues_009866.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  simonking\n\nin the thread [How to deal with GAP's machine dependent random generator?] on sage-devel Simon King mentioned that GAP own random source dependes on endianness of the machine.\nWhile Sage sort of takes care of this in misc/randstate.pyx,\nit still does not fix GAP internals. So, to make it good and proper, we essentially add the fix in misc/randstate.pyx to GAPROOT/src/integer.c, and remove it from misc/randstate.pyx\nThe updated gap spkg is here:\n\nhttp://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p5.spkg\n\nSo one needs to install this spkg and apply the patch attached to the ticket. I don't seem to have access to a 64-bit big-endian system, so it would be great to test it there, just in case...\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9867\n\n",
    "closed_at": "2012-10-05T08:52:31Z",
    "created_at": "2010-09-07T13:04:14Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "getting rid of endianness-dependent behaviour in GAP random sources",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9866",
    "user": "https://github.com/dimpase"
}
```
Assignee: joyner

CC:  simonking

in the thread [How to deal with GAP's machine dependent random generator?] on sage-devel Simon King mentioned that GAP own random source dependes on endianness of the machine.
While Sage sort of takes care of this in misc/randstate.pyx,
it still does not fix GAP internals. So, to make it good and proper, we essentially add the fix in misc/randstate.pyx to GAPROOT/src/integer.c, and remove it from misc/randstate.pyx
The updated gap spkg is here:

http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p5.spkg

So one needs to install this spkg and apply the patch attached to the ticket. I don't seem to have access to a 64-bit big-endian system, so it would be great to test it there, just in case...


Issue created by migration from https://trac.sagemath.org/ticket/9867





---

archive/issue_comments_097319.json:
```json
{
    "body": "Attachment [trac_9876_gap_MT_endianness.patch](tarball://root/attachments/some-uuid/ticket9867/trac_9876_gap_MT_endianness.patch) by @dimpase created at 2010-09-07 13:36:11",
    "created_at": "2010-09-07T13:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9866#issuecomment-97319",
    "user": "https://github.com/dimpase"
}
```

Attachment [trac_9876_gap_MT_endianness.patch](tarball://root/attachments/some-uuid/ticket9867/trac_9876_gap_MT_endianness.patch) by @dimpase created at 2010-09-07 13:36:11



---

archive/issue_comments_097320.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-09-25T06:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9866#issuecomment-97320",
    "user": "https://github.com/dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097321.json:
```json
{
    "body": "This will be fixed in #13211. Let us close this one as obsolete.",
    "created_at": "2012-09-25T07:00:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9866#issuecomment-97321",
    "user": "https://github.com/dimpase"
}
```

This will be fixed in #13211. Let us close this one as obsolete.



---

archive/issue_events_024850.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2012-09-25T12:22:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9866",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9866#event-24850"
}
```



---

archive/issue_comments_097322.json:
```json
{
    "body": "I can confirm that the current code is no longer needed as of #13211; see [comment:49:ticket:13211 here].",
    "created_at": "2012-09-25T12:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9866#issuecomment-97322",
    "user": "https://github.com/kcrisman"
}
```

I can confirm that the current code is no longer needed as of #13211; see [comment:49:ticket:13211 here].



---

archive/issue_comments_097323.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-09-25T12:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9866#issuecomment-97323",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_024851.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-10-05T08:52:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9866",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9866#event-24851"
}
```



---

archive/issue_comments_097324.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-10-05T08:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9866#issuecomment-97324",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
