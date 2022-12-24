# Issue 1041: latex representation of fractional ideals in a number field is totally stupid

archive/issues_001041.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: K.<a> = NumberField(x^2 + 1)\nsage: latex(K.fractional_ideal(3, a))\n\\left(3, a\\right)\\mathbf{Q}[a]/(a^{2} + 1)     \n```\n\n\n'nuff said. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1041\n\n",
    "created_at": "2007-10-31T20:47:32Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "latex representation of fractional ideals in a number field is totally stupid",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1041",
    "user": "was"
}
```
Assignee: was


```
sage: K.<a> = NumberField(x^2 + 1)
sage: latex(K.fractional_ideal(3, a))
\left(3, a\right)\mathbf{Q}[a]/(a^{2} + 1)     
```


'nuff said. 

Issue created by migration from https://trac.sagemath.org/ticket/1041





---

archive/issue_comments_006346.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T23:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1041#issuecomment-6346",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_006347.json:
```json
{
    "body": "Attachment [trac1041.patch](tarball://root/attachments/some-uuid/ticket1041/trac1041.patch) by was created at 2007-11-03 23:18:49",
    "created_at": "2007-11-03T23:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1041#issuecomment-6347",
    "user": "was"
}
```

Attachment [trac1041.patch](tarball://root/attachments/some-uuid/ticket1041/trac1041.patch) by was created at 2007-11-03 23:18:49
