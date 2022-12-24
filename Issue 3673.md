# Issue 3673: [with patch, needs review]  NumberFieldElement

archive/issues_003673.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe present definition of the `NumberFieldElement` class unreasonably \nprivileges the polynomial variable 'x'.  As a result the following fails:\n\n```\nsage: y = polygen(QQ, 'y'); K.<a> = NumberField(y^2 - 2)\nsage: S = K.subfields()\nsage: S[0][1]\n```\n\nThe patch amends the definition of `__init__` for the \n`NumberFieldElement` class to deal with this.\n\nAn extra doctest for the `subfields` method has been included.  Two other \ndoctests have been adjusted to match the revised code.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3673\n\n",
    "created_at": "2008-07-18T11:48:36Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, needs review]  NumberFieldElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3673",
    "user": "fwclarke"
}
```
Assignee: @williamstein

The present definition of the `NumberFieldElement` class unreasonably 
privileges the polynomial variable 'x'.  As a result the following fails:

```
sage: y = polygen(QQ, 'y'); K.<a> = NumberField(y^2 - 2)
sage: S = K.subfields()
sage: S[0][1]
```

The patch amends the definition of `__init__` for the 
`NumberFieldElement` class to deal with this.

An extra doctest for the `subfields` method has been included.  Two other 
doctests have been adjusted to match the revised code.



Issue created by migration from https://trac.sagemath.org/ticket/3673





---

archive/issue_comments_025964.json:
```json
{
    "body": "Attachment [sage-3673.patch](tarball://root/attachments/some-uuid/ticket3673/sage-3673.patch) by fwclarke created at 2008-07-18 11:54:11",
    "created_at": "2008-07-18T11:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3673#issuecomment-25964",
    "user": "fwclarke"
}
```

Attachment [sage-3673.patch](tarball://root/attachments/some-uuid/ticket3673/sage-3673.patch) by fwclarke created at 2008-07-18 11:54:11



---

archive/issue_comments_025965.json:
```json
{
    "body": "The patch applies cleanly to 3.1.alpha0.  It does what it says, and all doctests in sage.rings.number_field pass.  Publish!",
    "created_at": "2008-08-10T13:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3673#issuecomment-25965",
    "user": "@JohnCremona"
}
```

The patch applies cleanly to 3.1.alpha0.  It does what it says, and all doctests in sage.rings.number_field pass.  Publish!



---

archive/issue_comments_025966.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-11T07:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3673#issuecomment-25966",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025967.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-11T07:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3673#issuecomment-25967",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha1



---

archive/issue_comments_025968.json:
```json
{
    "body": "By the way: Report 11 did not pick up this ticket since there is an extra space between \"positive\" and \"review\".\n\nCheers,\n\nMichael",
    "created_at": "2008-08-11T07:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3673#issuecomment-25968",
    "user": "mabshoff"
}
```

By the way: Report 11 did not pick up this ticket since there is an extra space between "positive" and "review".

Cheers,

Michael
