# Issue 1041: latex representation of fractional ideals in a number field is totally stupid

archive/issues_001041.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nsage: K.<a> = NumberField(x^2 + 1)\nsage: latex(K.fractional_ideal(3, a))\n\\left(3, a\\right)\\mathbf{Q}[a]/(a^{2} + 1)     \n```\n\n'nuff said. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1041\n\n",
    "closed_at": "2007-11-03T23:18:49Z",
    "created_at": "2007-10-31T20:47:32Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "latex representation of fractional ideals in a number field is totally stupid",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1041",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
sage: K.<a> = NumberField(x^2 + 1)
sage: latex(K.fractional_ideal(3, a))
\left(3, a\right)\mathbf{Q}[a]/(a^{2} + 1)     
```

'nuff said. 

Issue created by migration from https://trac.sagemath.org/ticket/1041





---

archive/issue_events_002835.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-03T15:31:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1041",
    "milestone": "sage-2.8.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1041#event-2835"
}
```



---

archive/issue_comments_006326.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T23:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1041#issuecomment-6326",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_002836.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-03T23:18:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1041",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1041#event-2836"
}
```



---

archive/issue_comments_006327.json:
```json
{
    "body": "Attachment [trac1041.patch](tarball://root/attachments/some-uuid/ticket1041/trac1041.patch) by @williamstein created at 2007-11-03 23:18:49",
    "created_at": "2007-11-03T23:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1041#issuecomment-6327",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac1041.patch](tarball://root/attachments/some-uuid/ticket1041/trac1041.patch) by @williamstein created at 2007-11-03 23:18:49
