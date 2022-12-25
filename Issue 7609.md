# Issue 7609: numerical noise in doctests after pynac update

archive/issues_007609.json:
```json
{
    "body": "Assignee: @burcin\n\nThe new pynac package and patch from #7490 introduced numerical noise in some doctests. Attached patch should fix this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7609\n\n",
    "created_at": "2009-12-06T00:38:29Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "numerical noise in doctests after pynac update",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7609",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

The new pynac package and patch from #7490 introduced numerical noise in some doctests. Attached patch should fix this.

Issue created by migration from https://trac.sagemath.org/ticket/7609





---

archive/issue_comments_064870.json:
```json
{
    "body": "Attachment [trac_7609-pynac_numerical_noise.patch](tarball://root/attachments/some-uuid/ticket7609/trac_7609-pynac_numerical_noise.patch) by @burcin created at 2009-12-06 00:41:04\n\nfix numerical noise",
    "created_at": "2009-12-06T00:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7609#issuecomment-64870",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7609-pynac_numerical_noise.patch](tarball://root/attachments/some-uuid/ticket7609/trac_7609-pynac_numerical_noise.patch) by @burcin created at 2009-12-06 00:41:04

fix numerical noise



---

archive/issue_comments_064871.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-06T00:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7609#issuecomment-64871",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064872.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-06T02:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7609#issuecomment-64872",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064873.json:
```json
{
    "body": "This is fine, but there was another one in functions/trig.py (this on a 32-bit Macintel 10.5):\n\n```\nsage: float(cot(1))\n0.64209261593433065\n```\n\nbut gave\n\n```\n0.64209261593433076\n```\n",
    "created_at": "2009-12-06T02:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7609#issuecomment-64873",
    "user": "https://github.com/kcrisman"
}
```

This is fine, but there was another one in functions/trig.py (this on a 32-bit Macintel 10.5):

```
sage: float(cot(1))
0.64209261593433065
```

but gave

```
0.64209261593433076
```




---

archive/issue_comments_064874.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2009-12-06T16:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7609#issuecomment-64874",
    "user": "https://github.com/burcin"
}
```

apply only this patch



---

archive/issue_comments_064875.json:
```json
{
    "body": "Attachment [trac_7609-pynac_numerical_noise.take2.patch](tarball://root/attachments/some-uuid/ticket7609/trac_7609-pynac_numerical_noise.take2.patch) by @burcin created at 2009-12-06 16:15:51\n\nHi Karl-Dieter,\n\nattachment:trac_7609-pynac_numerical_noise.take2.patch adds a fix for the error you get as well. It is a good coincidence that you're testing on that box. :)\n\nThanks.",
    "created_at": "2009-12-06T16:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7609#issuecomment-64875",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7609-pynac_numerical_noise.take2.patch](tarball://root/attachments/some-uuid/ticket7609/trac_7609-pynac_numerical_noise.take2.patch) by @burcin created at 2009-12-06 16:15:51

Hi Karl-Dieter,

attachment:trac_7609-pynac_numerical_noise.take2.patch adds a fix for the error you get as well. It is a good coincidence that you're testing on that box. :)

Thanks.



---

archive/issue_comments_064876.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-06T16:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7609#issuecomment-64876",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064877.json:
```json
{
    "body": "Okay, this seems good.  I do still get the segfault in symbolic/expression.pyx but that is addressed elsewhere.",
    "created_at": "2009-12-07T14:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7609#issuecomment-64877",
    "user": "https://github.com/kcrisman"
}
```

Okay, this seems good.  I do still get the segfault in symbolic/expression.pyx but that is addressed elsewhere.



---

archive/issue_comments_064878.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-07T14:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7609#issuecomment-64878",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064879.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-07T23:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7609#issuecomment-64879",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_018080.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-07T23:22:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7609",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7609#event-18080"
}
```
