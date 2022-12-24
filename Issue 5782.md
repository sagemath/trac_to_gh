# Issue 5782: Failure of __pow__ in RDF for noninteger powers of  zero

archive/issues_005782.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: RDF, __pow__, zero\n\nPositive noninteger powers of RDF(0) give nan rather than zero:\n\n```\n  sage: RDF(0)^.5\n  nan\n\n  sage: RDF(0)^(1/2)\n  nan\n```\n\n\nIn contrast, noninteger powers of CDF(0) have the correct value:\n\n```\n  sage: CDF(0)^.5\n  0\n\n  sage: CDF(0)^(1/2)\n  0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5782\n\n",
    "created_at": "2009-04-14T00:00:05Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "Failure of __pow__ in RDF for noninteger powers of  zero",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5782",
    "user": "kbaker"
}
```
Assignee: somebody

Keywords: RDF, __pow__, zero

Positive noninteger powers of RDF(0) give nan rather than zero:

```
  sage: RDF(0)^.5
  nan

  sage: RDF(0)^(1/2)
  nan
```


In contrast, noninteger powers of CDF(0) have the correct value:

```
  sage: CDF(0)^.5
  0

  sage: CDF(0)^(1/2)
  0
```


Issue created by migration from https://trac.sagemath.org/ticket/5782





---

archive/issue_comments_045260.json:
```json
{
    "body": "Hmm, we have some trivial doctest failures:\n\n```\nsage -t -long \"devel/sage/sage/rings/real_double.pyx\"       \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/rings/real_double.pyx\", line 1543:\n    sage: RDF(0)^.5\nExpected:\n    0\nGot:\n    0.0\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/rings/real_double.pyx\", line 1545:\n    sage: RDF(0)^(1/2)\nExpected:\n    0\nGot:\n    0.0\n**********************************************************************\n```\n\n\nI think other than that this is good to go.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T03:04:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5782#issuecomment-45260",
    "user": "mabshoff"
}
```

Hmm, we have some trivial doctest failures:

```
sage -t -long "devel/sage/sage/rings/real_double.pyx"       
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/rings/real_double.pyx", line 1543:
    sage: RDF(0)^.5
Expected:
    0
Got:
    0.0
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/rings/real_double.pyx", line 1545:
    sage: RDF(0)^(1/2)
Expected:
    0
Got:
    0.0
**********************************************************************
```


I think other than that this is good to go.

Cheers,

Michael



---

archive/issue_comments_045261.json:
```json
{
    "body": "Attachment [5782-rdf-pow.patch](tarball://root/attachments/some-uuid/ticket5782/5782-rdf-pow.patch) by robertwb created at 2009-04-16 04:58:55",
    "created_at": "2009-04-16T04:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5782#issuecomment-45261",
    "user": "robertwb"
}
```

Attachment [5782-rdf-pow.patch](tarball://root/attachments/some-uuid/ticket5782/5782-rdf-pow.patch) by robertwb created at 2009-04-16 04:58:55



---

archive/issue_comments_045262.json:
```json
{
    "body": "Doh! Patch updated.",
    "created_at": "2009-04-16T04:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5782#issuecomment-45262",
    "user": "robertwb"
}
```

Doh! Patch updated.



---

archive/issue_comments_045263.json:
```json
{
    "body": "Second patch looks good to me. Positive review. It also passes doctests :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T07:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5782#issuecomment-45263",
    "user": "mabshoff"
}
```

Second patch looks good to me. Positive review. It also passes doctests :)

Cheers,

Michael



---

archive/issue_comments_045264.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T07:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5782#issuecomment-45264",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_045265.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-16T07:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5782#issuecomment-45265",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045266.json:
```json
{
    "body": "Does this fix #5785?",
    "created_at": "2009-04-16T17:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5782#issuecomment-45266",
    "user": "jason"
}
```

Does this fix #5785?



---

archive/issue_comments_045267.json:
```json
{
    "body": "Replying to [comment:6 jason]:\n> Does this fix #5785?\n\nYes.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T21:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5782#issuecomment-45267",
    "user": "mabshoff"
}
```

Replying to [comment:6 jason]:
> Does this fix #5785?

Yes.

Cheers,

Michael
