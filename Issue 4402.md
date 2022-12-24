# Issue 4402: Sage 3.1.4: magma related optional doctest failure in tut.tex

archive/issues_004402.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage -t -long -optional devel/doc/prog/prog.tex\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.alpha1/tmp/prog.py\", line 520:\n    sage: E._magma_init_() # optional -- requires Magma\nExpected:\n    'EllipticCurve([_sage_[1]|GF(41)!0,GF(41)!0,GF(41)!0,GF(41)!2,GF(41)!5])'\nGot:\n    'EllipticCurve([GF(41)|GF(41)!0,GF(41)!0,GF(41)!0,GF(41)!2,GF(41)!5])'\n**********************************************************************\n```\n\n\nTrivial to fix since this is just a printing issue.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4402\n\n",
    "created_at": "2008-10-30T17:34:25Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Sage 3.1.4: magma related optional doctest failure in tut.tex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4402",
    "user": "mabshoff"
}
```
Assignee: was


```
sage -t -long -optional devel/doc/prog/prog.tex
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha1/tmp/prog.py", line 520:
    sage: E._magma_init_() # optional -- requires Magma
Expected:
    'EllipticCurve([_sage_[1]|GF(41)!0,GF(41)!0,GF(41)!0,GF(41)!2,GF(41)!5])'
Got:
    'EllipticCurve([GF(41)|GF(41)!0,GF(41)!0,GF(41)!0,GF(41)!2,GF(41)!5])'
**********************************************************************
```


Trivial to fix since this is just a printing issue.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4402





---

archive/issue_comments_032371.json:
```json
{
    "body": "William,\n\nthis one is still there since the TeX documentation isn't run per default. Unless you beat me to it I will fix this tomorrow.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T09:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4402#issuecomment-32371",
    "user": "mabshoff"
}
```

William,

this one is still there since the TeX documentation isn't run per default. Unless you beat me to it I will fix this tomorrow.

Cheers,

Michael



---

archive/issue_comments_032372.json:
```json
{
    "body": "Attachment [trac_4402_doc.patch](tarball://root/attachments/some-uuid/ticket4402/trac_4402_doc.patch) by was created at 2008-11-30 07:46:55",
    "created_at": "2008-11-30T07:46:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4402#issuecomment-32372",
    "user": "was"
}
```

Attachment [trac_4402_doc.patch](tarball://root/attachments/some-uuid/ticket4402/trac_4402_doc.patch) by was created at 2008-11-30 07:46:55



---

archive/issue_comments_032373.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T07:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4402#issuecomment-32373",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_032374.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-30T08:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4402#issuecomment-32374",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032375.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc1",
    "created_at": "2008-11-30T08:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4402#issuecomment-32375",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.rc1
