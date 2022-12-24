# Issue 5212: [with patch, needs review] bug with numbers in names in sage.structure.parent_gens.normalize_names

archive/issues_005212.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: numbers in names normalize_names\n\nTry `PolynomialRing(QQ, 2, 'alpha0')` for hilarity.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5212\n\n",
    "created_at": "2009-02-09T04:20:51Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] bug with numbers in names in sage.structure.parent_gens.normalize_names",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5212",
    "user": "ncalexan"
}
```
Assignee: somebody

Keywords: numbers in names normalize_names

Try `PolynomialRing(QQ, 2, 'alpha0')` for hilarity.

Issue created by migration from https://trac.sagemath.org/ticket/5212





---

archive/issue_comments_039934.json:
```json
{
    "body": "Attachment [trac_5212-normalize-names.patch](tarball://root/attachments/some-uuid/ticket5212/trac_5212-normalize-names.patch) by ncalexan created at 2009-02-09 04:23:07",
    "created_at": "2009-02-09T04:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5212#issuecomment-39934",
    "user": "ncalexan"
}
```

Attachment [trac_5212-normalize-names.patch](tarball://root/attachments/some-uuid/ticket5212/trac_5212-normalize-names.patch) by ncalexan created at 2009-02-09 04:23:07



---

archive/issue_comments_039935.json:
```json
{
    "body": "With this patch applied to my current 3.3.rc0 merge tree all doctests pass.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T12:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5212#issuecomment-39935",
    "user": "mabshoff"
}
```

With this patch applied to my current 3.3.rc0 merge tree all doctests pass.

Cheers,

Michael



---

archive/issue_comments_039936.json:
```json
{
    "body": "Merged in Sage 3.3.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T06:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5212#issuecomment-39936",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc0.

Cheers,

Michael



---

archive/issue_comments_039937.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-11T06:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5212#issuecomment-39937",
    "user": "mabshoff"
}
```

Resolution: fixed
