# Issue 9394: latex representation of negative coefficients broken

archive/issues_009394.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: pynac\n\nReported by Mike Witt on sage-support:\n\n\n```\nsage: latex(t)\n\\left(2 I\\right) \\, \\pi n x + \\left(-2 I\\right) \\, \\pi n\n```\n\n\n`+ (-2 I )` looks really ugly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9394\n\n",
    "created_at": "2010-06-30T12:05:02Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "latex representation of negative coefficients broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9394",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

Keywords: pynac

Reported by Mike Witt on sage-support:


```
sage: latex(t)
\left(2 I\right) \, \pi n x + \left(-2 I\right) \, \pi n
```


`+ (-2 I )` looks really ugly.

Issue created by migration from https://trac.sagemath.org/ticket/9394





---

archive/issue_comments_089292.json:
```json
{
    "body": "See recent comments in\u00a0#8938, where similar phenomena have been noted.",
    "created_at": "2010-07-02T20:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9394#issuecomment-89292",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

See recent comments in #8938, where similar phenomena have been noted.



---

archive/issue_comments_089293.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-12T11:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9394#issuecomment-89293",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089294.json:
```json
{
    "body": "Attachment [trac_9394-leading_minus.patch](tarball://root/attachments/some-uuid/ticket9394/trac_9394-leading_minus.patch) by @burcin created at 2010-09-12 11:54:10\n\nWith the new pynac package at #9901, we have:\n\n\n```\nsage: var('n')\nn\nsage: t = 2*I*n*pi*x - 2*I*n*pi\nsage: latex(t)\n2 i \\, \\pi n x - 2 i \\, \\pi n\n```\n\n\nattachment:trac_9394-leading_minus.patch contains the doctest changes. The fixes in the printing of rational functions (for #9834) are also included in this patch.\n\nThe pynac package includes patches for #9834, #9878, #9879, #9881, #9900 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.",
    "created_at": "2010-09-12T11:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9394#issuecomment-89294",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9394-leading_minus.patch](tarball://root/attachments/some-uuid/ticket9394/trac_9394-leading_minus.patch) by @burcin created at 2010-09-12 11:54:10

With the new pynac package at #9901, we have:


```
sage: var('n')
n
sage: t = 2*I*n*pi*x - 2*I*n*pi
sage: latex(t)
2 i \, \pi n x - 2 i \, \pi n
```


attachment:trac_9394-leading_minus.patch contains the doctest changes. The fixes in the printing of rational functions (for #9834) are also included in this patch.

The pynac package includes patches for #9834, #9878, #9879, #9881, #9900 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.



---

archive/issue_comments_089295.json:
```json
{
    "body": "With #9901, positive review.  Do not merge until #9901 has positive review and is merged.",
    "created_at": "2010-09-22T17:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9394#issuecomment-89295",
    "user": "https://github.com/kcrisman"
}
```

With #9901, positive review.  Do not merge until #9901 has positive review and is merged.



---

archive/issue_comments_089296.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-22T17:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9394#issuecomment-89296",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009551.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-10-06T03:20:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9394",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9394#event-9551"
}
```



---

archive/issue_comments_089297.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-06T03:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9394#issuecomment-89297",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
