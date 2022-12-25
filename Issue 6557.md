# Issue 6557: fix bug in number field caching

archive/issues_006557.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nHere are two independent Sage 4.1 sessions which demonstrate that the\nconstruction of NumberField's is context dependent:\n\n       sage: K.<x> = CyclotomicField(5)[]\n       sage: W.<a> = NumberField(x^2 + 1)\n       sage: W\n       Number Field in a with defining polynomial x^2 + 1 over its base field\n\n       sage: W1 = NumberField(x^2+1,'a')\n       sage: K.<x> = CyclotomicField(5)[]\n       sage: W.<a> = NumberField(x^2 + 1)\n       sage: W\n       Number Field in a with defining polynomial x^2 + 1\n\nIn fact:\n\n       sage: W1 is W0\n       True\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6557\n\n",
    "created_at": "2009-07-18T22:07:13Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "fix bug in number field caching",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6557",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
Here are two independent Sage 4.1 sessions which demonstrate that the
construction of NumberField's is context dependent:

       sage: K.<x> = CyclotomicField(5)[]
       sage: W.<a> = NumberField(x^2 + 1)
       sage: W
       Number Field in a with defining polynomial x^2 + 1 over its base field

       sage: W1 = NumberField(x^2+1,'a')
       sage: K.<x> = CyclotomicField(5)[]
       sage: W.<a> = NumberField(x^2 + 1)
       sage: W
       Number Field in a with defining polynomial x^2 + 1

In fact:

       sage: W1 is W0
       True
```

Issue created by migration from https://trac.sagemath.org/ticket/6557





---

archive/issue_comments_053367.json:
```json
{
    "body": "Attachment [trac_6557.patch](tarball://root/attachments/some-uuid/ticket6557/trac_6557.patch) by @williamstein created at 2009-07-18 22:18:47",
    "created_at": "2009-07-18T22:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6557#issuecomment-53367",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6557.patch](tarball://root/attachments/some-uuid/ticket6557/trac_6557.patch) by @williamstein created at 2009-07-18 22:18:47



---

archive/issue_comments_053368.json:
```json
{
    "body": "Changing keywords from \"\" to \"Number fields\".",
    "created_at": "2009-07-19T12:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6557#issuecomment-53368",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "" to "Number fields".



---

archive/issue_comments_053369.json:
```json
{
    "body": "Positive review.  Applies to 4.1 and all tests in sage/rings/number_fields pass.",
    "created_at": "2009-07-19T12:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6557#issuecomment-53369",
    "user": "https://github.com/JohnCremona"
}
```

Positive review.  Applies to 4.1 and all tests in sage/rings/number_fields pass.



---

archive/issue_comments_053370.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-19T14:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6557#issuecomment-53370",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_015469.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-19T14:19:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6557",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6557#event-15469"
}
```
