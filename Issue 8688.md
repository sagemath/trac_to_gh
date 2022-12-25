# Issue 8688: extra parenthesis when typesetting fractions

archive/issues_008688.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: pynac\n\n```\nsage: latex((x+2)/(x^3+1))\n\\frac{{\\left(x + 2\\right)}}{{\\left(x^{3} + 1\\right)}}\n```\n\nNote the extra parenthesis in the numerator and denominator.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8688\n\n",
    "closed_at": "2010-05-26T03:03:43Z",
    "created_at": "2010-04-14T22:31:13Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "extra parenthesis when typesetting fractions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8688",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

Keywords: pynac

```
sage: latex((x+2)/(x^3+1))
\frac{{\left(x + 2\right)}}{{\left(x^{3} + 1\right)}}
```

Note the extra parenthesis in the numerator and denominator.

Issue created by migration from https://trac.sagemath.org/ticket/8688





---

archive/issue_comments_079031.json:
```json
{
    "body": "Changing keywords from \"\" to \"pynac\".",
    "created_at": "2010-05-06T04:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8688#issuecomment-79031",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "pynac".



---

archive/issue_comments_079032.json:
```json
{
    "body": "Attachment [trac_8688-typeset_fraction.patch](tarball://root/attachments/some-uuid/ticket8688/trac_8688-typeset_fraction.patch) by @burcin created at 2010-05-06 04:24:37\n\nThis is fixed by the pynac package in #8903. attachment:trac_8688-typeset_fraction.patch contains doctests.\n\nNote that #8542, #8651 and #8775 is also fixed by the new pynac version. Patches from these tickets should be applied before doctesting.",
    "created_at": "2010-05-06T04:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8688#issuecomment-79032",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8688-typeset_fraction.patch](tarball://root/attachments/some-uuid/ticket8688/trac_8688-typeset_fraction.patch) by @burcin created at 2010-05-06 04:24:37

This is fixed by the pynac package in #8903. attachment:trac_8688-typeset_fraction.patch contains doctests.

Note that #8542, #8651 and #8775 is also fixed by the new pynac version. Patches from these tickets should be applied before doctesting.



---

archive/issue_comments_079033.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-06T04:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8688#issuecomment-79033",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_events_021067.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-05-26T03:03:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8688",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8688#event-21067"
}
```



---

archive/issue_comments_079034.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-26T03:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8688#issuecomment-79034",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
