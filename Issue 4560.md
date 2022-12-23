# Issue 4560: SR and containment broken

archive/issues_004560.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  mhansen\n\nThis is bad\n\n\n```\nsage: sqrt(2) in CC\nFalse\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4560\n\n",
    "created_at": "2008-11-20T01:35:11Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "SR and containment broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4560",
    "user": "robertwb"
}
```
Assignee: burcin

CC:  mhansen

This is bad


```
sage: sqrt(2) in CC
False
```


Issue created by migration from https://trac.sagemath.org/ticket/4560





---

archive/issue_comments_034161.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-23T02:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4560#issuecomment-34161",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_034162.json:
```json
{
    "body": "Though seeing `SymbolicEquation` in parent.pyx is very scary at first, this is a good solution. :)",
    "created_at": "2009-01-23T08:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4560#issuecomment-34162",
    "user": "burcin"
}
```

Though seeing `SymbolicEquation` in parent.pyx is very scary at first, this is a good solution. :)



---

archive/issue_comments_034163.json:
```json
{
    "body": "The above patch causes the following doctest failure in tut.tex:\n\n```\nThere is one subtlety in defining complex numbers: as mentioned above,\nthe symbol \\code{i} represents a square root of \\minusone, but it is a\n\\emph{formal} square root of \\minusone; it is not in the complex numbers.\nCalling \\code{CC(i)} returns the complex square root of \\minusone.\n%link\n\\begin{verbatim}\nsage: i in CC\nFalse\n```\n\nnow returns true. After some discussion with William it was decided to change the doctest.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T08:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4560#issuecomment-34163",
    "user": "mabshoff"
}
```

The above patch causes the following doctest failure in tut.tex:

```
There is one subtlety in defining complex numbers: as mentioned above,
the symbol \code{i} represents a square root of \minusone, but it is a
\emph{formal} square root of \minusone; it is not in the complex numbers.
Calling \code{CC(i)} returns the complex square root of \minusone.
%link
\begin{verbatim}
sage: i in CC
False
```

now returns true. After some discussion with William it was decided to change the doctest.

Cheers,

Michael



---

archive/issue_comments_034164.json:
```json
{
    "body": "Attachment\n\nDocumentation fix",
    "created_at": "2009-01-24T14:49:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4560#issuecomment-34164",
    "user": "roed"
}
```

Attachment

Documentation fix



---

archive/issue_comments_034165.json:
```json
{
    "body": "Rebased verison of Roed's patch",
    "created_at": "2009-01-29T02:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4560#issuecomment-34165",
    "user": "mabshoff"
}
```

Rebased verison of Roed's patch



---

archive/issue_comments_034166.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-29T02:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4560#issuecomment-34166",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034167.json:
```json
{
    "body": "Attachment\n\nMerged 4560-doc.patch and trac_4560.patch in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T02:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4560#issuecomment-34167",
    "user": "mabshoff"
}
```

Attachment

Merged 4560-doc.patch and trac_4560.patch in Sage 3.3.alpha3.

Cheers,

Michael
