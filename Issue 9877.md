# Issue 9877: symbolic zeta(1) should return unsigned infinity

archive/issues_009877.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: pynac\n\nAfter exposing the symbolic zeta function at the top level in #8864, we get:\n\n\n```\nsage: zeta(1)\nzeta(1)\n```\n\n\nWe should return unsigned infinity in this case.\n\nSee also #5739.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9878\n\n",
    "created_at": "2010-09-09T08:19:55Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "symbolic zeta(1) should return unsigned infinity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9877",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

Keywords: pynac

After exposing the symbolic zeta function at the top level in #8864, we get:


```
sage: zeta(1)
zeta(1)
```


We should return unsigned infinity in this case.

See also #5739.

Issue created by migration from https://trac.sagemath.org/ticket/9878





---

archive/issue_comments_097628.json:
```json
{
    "body": "Attachment [trac_9878-zeta_infinity.patch](tarball://root/attachments/some-uuid/ticket9878/trac_9878-zeta_infinity.patch) by @burcin created at 2010-09-12 12:15:07\n\nWith the new pynac package at #9201, we have:\n\n\n```\nsage: zeta(1)\nInfinity\n```\n\n\nattachment:trac_9878-zeta_infinity.patch adds doctests for this change.\n\nThe pynac package includes patches for #9394, #9834, #9879, #9881, #9900 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.",
    "created_at": "2010-09-12T12:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9877#issuecomment-97628",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9878-zeta_infinity.patch](tarball://root/attachments/some-uuid/ticket9878/trac_9878-zeta_infinity.patch) by @burcin created at 2010-09-12 12:15:07

With the new pynac package at #9201, we have:


```
sage: zeta(1)
Infinity
```


attachment:trac_9878-zeta_infinity.patch adds doctests for this change.

The pynac package includes patches for #9394, #9834, #9879, #9881, #9900 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.



---

archive/issue_comments_097629.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-12T12:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9877#issuecomment-97629",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097630.json:
```json
{
    "body": "Replying to [comment:1 burcin]:\n> With the new pynac package at #9201, we have:\n\nat #9901. Sorry for the noise.",
    "created_at": "2010-09-12T12:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9877#issuecomment-97630",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:1 burcin]:
> With the new pynac package at #9201, we have:

at #9901. Sorry for the noise.



---

archive/issue_comments_097631.json:
```json
{
    "body": "With #9901, positive review.  Do not merge until #9901 also has positive review and is merged.",
    "created_at": "2010-09-22T18:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9877#issuecomment-97631",
    "user": "https://github.com/kcrisman"
}
```

With #9901, positive review.  Do not merge until #9901 also has positive review and is merged.



---

archive/issue_comments_097632.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-22T18:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9877#issuecomment-97632",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_024885.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-10-06T03:20:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9877",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9877#event-24885"
}
```



---

archive/issue_comments_097633.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-06T03:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9877#issuecomment-97633",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
