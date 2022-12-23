# Issue 1039: [with patch] Dokchitser L-series of number field

archive/issues_001039.json:
```json
{
    "body": "Assignee: was\n\nwrapper for Dokchitser L-series of a number field, so that one can do the following:\n\n\n```\nsage: K.<a> =NumberField(x^2+x-1)\nsage: L = K.Lseries_dokchitser()\nsage: L(-1)\n0.0333333333333333\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1039\n\n",
    "created_at": "2007-10-31T17:37:07Z",
    "labels": [
        "number theory",
        "minor",
        "enhancement"
    ],
    "title": "[with patch] Dokchitser L-series of number field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1039",
    "user": "jen"
}
```
Assignee: was

wrapper for Dokchitser L-series of a number field, so that one can do the following:


```
sage: K.<a> =NumberField(x^2+x-1)
sage: L = K.Lseries_dokchitser()
sage: L(-1)
0.0333333333333333
```


Issue created by migration from https://trac.sagemath.org/ticket/1039





---

archive/issue_comments_006338.json:
```json
{
    "body": "Attachment\n\nI will take a look at this soon.",
    "created_at": "2007-10-31T17:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1039#issuecomment-6338",
    "user": "was"
}
```

Attachment

I will take a look at this soon.



---

archive/issue_comments_006339.json:
```json
{
    "body": "Apply this patch instead.",
    "created_at": "2007-11-01T08:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1039#issuecomment-6339",
    "user": "was"
}
```

Apply this patch instead.



---

archive/issue_comments_006340.json:
```json
{
    "body": "Attachment\n\napplied to 2.8.11.alpha0",
    "created_at": "2007-11-01T09:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1039#issuecomment-6340",
    "user": "mabshoff"
}
```

Attachment

applied to 2.8.11.alpha0



---

archive/issue_comments_006341.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T09:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1039#issuecomment-6341",
    "user": "mabshoff"
}
```

Resolution: fixed
