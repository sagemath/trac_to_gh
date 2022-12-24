# Issue 3811: number fields in different polynomials compare differently

archive/issues_003811.json:
```json
{
    "body": "Assignee: was\n\nKeywords: number field comparison cmp\n\nThe doctests describe it best, but it was the case that\n\n\n```\nsage: NumberField(ZZ['x'].0^4 + 23, 'a') == NumberField(ZZ['y'].0^4 + 23, 'a')\nTrue\nsage: NumberField(ZZ['x'].0^4 + 23, 'a') == NumberField(QQ['y'].0^4 + 23, 'a')\nFalse\nsage: NumberField(QQ['x'].0^4 + 23, 'a') == NumberField(QQ['y'].0^4 + 23, 'a')\nFalse\n```\n\n\nNot good.  The variable of the defining polynomial should not matter.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3811\n\n",
    "created_at": "2008-08-12T05:06:52Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "number fields in different polynomials compare differently",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3811",
    "user": "ncalexan"
}
```
Assignee: was

Keywords: number field comparison cmp

The doctests describe it best, but it was the case that


```
sage: NumberField(ZZ['x'].0^4 + 23, 'a') == NumberField(ZZ['y'].0^4 + 23, 'a')
True
sage: NumberField(ZZ['x'].0^4 + 23, 'a') == NumberField(QQ['y'].0^4 + 23, 'a')
False
sage: NumberField(QQ['x'].0^4 + 23, 'a') == NumberField(QQ['y'].0^4 + 23, 'a')
False
```


Not good.  The variable of the defining polynomial should not matter.

Issue created by migration from https://trac.sagemath.org/ticket/3811





---

archive/issue_comments_027089.json:
```json
{
    "body": "Attachment [3811-ncalexan-number-field-comparision.patch](tarball://root/attachments/some-uuid/ticket3811/3811-ncalexan-number-field-comparision.patch) by ncalexan created at 2008-08-12 05:07:27",
    "created_at": "2008-08-12T05:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3811#issuecomment-27089",
    "user": "ncalexan"
}
```

Attachment [3811-ncalexan-number-field-comparision.patch](tarball://root/attachments/some-uuid/ticket3811/3811-ncalexan-number-field-comparision.patch) by ncalexan created at 2008-08-12 05:07:27



---

archive/issue_comments_027090.json:
```json
{
    "body": "EXCELLENT PATCH!\n\n\nRequest: Please stop exporting plain text patches.  Export hg patches instead, or there will be no commit messages in the hg log, and the default is to check the patch in as the person applying it.",
    "created_at": "2008-08-13T02:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3811#issuecomment-27090",
    "user": "was"
}
```

EXCELLENT PATCH!


Request: Please stop exporting plain text patches.  Export hg patches instead, or there will be no commit messages in the hg log, and the default is to check the patch in as the person applying it.



---

archive/issue_comments_027091.json:
```json
{
    "body": "Nick,\n\nthere is a qexport command that you should use. It will produce proper patches.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-13T02:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3811#issuecomment-27091",
    "user": "mabshoff"
}
```

Nick,

there is a qexport command that you should use. It will produce proper patches.

Cheers,

Michael



---

archive/issue_comments_027092.json:
```json
{
    "body": "Merged in Nick's name in Sage 3.1.alpha2",
    "created_at": "2008-08-13T08:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3811#issuecomment-27092",
    "user": "mabshoff"
}
```

Merged in Nick's name in Sage 3.1.alpha2



---

archive/issue_comments_027093.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-13T08:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3811#issuecomment-27093",
    "user": "mabshoff"
}
```

Resolution: fixed
