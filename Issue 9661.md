# Issue 9661: pari(string) and gp(string) always returns a value, even when it should not

archive/issues_009661.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen executing a PARI or GP command from Sage, a value of 0 is returned when None would be expected.  For example, in a gp shell (started with sage -gp for example):\n\n```\ngp> kill(x)   /* No output */\n```\n\nBut in Sage:\n\n```\nsage: gp('kill(x)')\n0\nsage: pari('kill(x)')\n0\n```\n\nIt should be possible to fix this by checking for `gnil` as return value.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9661\n\n",
    "created_at": "2010-08-01T16:47:28Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "pari(string) and gp(string) always returns a value, even when it should not",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9661",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: @williamstein

When executing a PARI or GP command from Sage, a value of 0 is returned when None would be expected.  For example, in a gp shell (started with sage -gp for example):

```
gp> kill(x)   /* No output */
```

But in Sage:

```
sage: gp('kill(x)')
0
sage: pari('kill(x)')
0
```

It should be possible to fix this by checking for `gnil` as return value.

Issue created by migration from https://trac.sagemath.org/ticket/9661





---

archive/issue_comments_093616.json:
```json
{
    "body": "Attachment [9661.patch](tarball://root/attachments/some-uuid/ticket9661/9661.patch) by @jdemeyer created at 2010-08-02 07:15:18",
    "created_at": "2010-08-02T07:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9661#issuecomment-93616",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9661.patch](tarball://root/attachments/some-uuid/ticket9661/9661.patch) by @jdemeyer created at 2010-08-02 07:15:18



---

archive/issue_comments_093617.json:
```json
{
    "body": "Changing assignee from @williamstein to @jdemeyer.",
    "created_at": "2010-08-02T07:23:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9661#issuecomment-93617",
    "user": "https://github.com/jdemeyer"
}
```

Changing assignee from @williamstein to @jdemeyer.



---

archive/issue_comments_093618.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-02T07:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9661#issuecomment-93618",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093619.json:
```json
{
    "body": "I'm testing this now on 4.5.2.rc0.  Can you say why you included _sig_off ?  (I do not claim to understand how Sage/pari signal handling works.)  Without this patch there is a return with no _sig_off (unless the call to new_gen does that.)",
    "created_at": "2010-08-03T01:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9661#issuecomment-93619",
    "user": "https://github.com/JohnCremona"
}
```

I'm testing this now on 4.5.2.rc0.  Can you say why you included _sig_off ?  (I do not claim to understand how Sage/pari signal handling works.)  Without this patch there is a return with no _sig_off (unless the call to new_gen does that.)



---

archive/issue_comments_093620.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-03T02:08:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9661#issuecomment-93620",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093621.json:
```json
{
    "body": "Tests all pass on 4.5.2.rc0 (64-bit ubuntu).",
    "created_at": "2010-08-03T02:08:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9661#issuecomment-93621",
    "user": "https://github.com/JohnCremona"
}
```

Tests all pass on 4.5.2.rc0 (64-bit ubuntu).



---

archive/issue_comments_093622.json:
```json
{
    "body": "Replying to [comment:5 cremona]:\n> I'm testing this now on 4.5.2.rc0.  Can you say why you included _sig_off ?  (I do not claim to understand how Sage/pari signal handling works.)  Without this patch there is a return with no _sig_off (unless the call to new_gen does that.)\n\n\nIt's exactly as you say, new_gen() calls _sig_off.",
    "created_at": "2010-08-03T07:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9661#issuecomment-93622",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:5 cremona]:
> I'm testing this now on 4.5.2.rc0.  Can you say why you included _sig_off ?  (I do not claim to understand how Sage/pari signal handling works.)  Without this patch there is a return with no _sig_off (unless the call to new_gen does that.)


It's exactly as you say, new_gen() calls _sig_off.



---

archive/issue_events_024099.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-08-03T07:07:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9661",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9661#event-24099"
}
```



---

archive/issue_events_024100.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-09T09:42:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9661",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9661#event-24100"
}
```



---

archive/issue_comments_093623.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9661#issuecomment-93623",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
