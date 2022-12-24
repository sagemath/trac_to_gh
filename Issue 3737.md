# Issue 3737: backslash in verbatim environment in tut.tex breaks doctest

archive/issues_003737.json:
```json
{
    "body": "Assignee: failure\n\nKeywords: latex, verbatim, backslash\n\nI would like to include lines like these in tut.tex:\n\n```\n\\begin{verbatim}\nsage: A = Matrix([[1,2,3],[3,2,1],[1,1,1]])\nsage: Y = vector([0,-4,-1])\nsage: A \\ Y\n(-2, 1, 0)\n\\end{verbatim}\n```\n\nWhen I include these, doctesting fails on tut.tex, giving an error about something 500 lines away, and giving an error after half a second, whereas if these lines are removed, doctesting finishes successfully in about 30 seconds. \n\nI would guess that the problem is the backslash in the verbatim environment.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3737\n\n",
    "created_at": "2008-07-29T03:47:59Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "backslash in verbatim environment in tut.tex breaks doctest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3737",
    "user": "@jhpalmieri"
}
```
Assignee: failure

Keywords: latex, verbatim, backslash

I would like to include lines like these in tut.tex:

```
\begin{verbatim}
sage: A = Matrix([[1,2,3],[3,2,1],[1,1,1]])
sage: Y = vector([0,-4,-1])
sage: A \ Y
(-2, 1, 0)
\end{verbatim}
```

When I include these, doctesting fails on tut.tex, giving an error about something 500 lines away, and giving an error after half a second, whereas if these lines are removed, doctesting finishes successfully in about 30 seconds. 

I would guess that the problem is the backslash in the verbatim environment.



Issue created by migration from https://trac.sagemath.org/ticket/3737





---

archive/issue_comments_026523.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-19T07:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3737#issuecomment-26523",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026524.json:
```json
{
    "body": "Changing assignee from failure to @mwhansen.",
    "created_at": "2008-09-19T07:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3737#issuecomment-26524",
    "user": "@mwhansen"
}
```

Changing assignee from failure to @mwhansen.



---

archive/issue_comments_026525.json:
```json
{
    "body": "This might become moot with the Sphinx versions of the documentation -- I noticed that the new version of the tutorial at [http://sage.math.washington.edu/home/mhansen/doc-sphinx/](http://sage.math.washington.edu/home/mhansen/doc-sphinx/) includes an example like the one above, so if doctesting and the live version work, then once the Sphinx versions are the official documentation for the distribution, we can consider this issue solved.",
    "created_at": "2008-09-19T14:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3737#issuecomment-26525",
    "user": "@jhpalmieri"
}
```

This might become moot with the Sphinx versions of the documentation -- I noticed that the new version of the tutorial at [http://sage.math.washington.edu/home/mhansen/doc-sphinx/](http://sage.math.washington.edu/home/mhansen/doc-sphinx/) includes an example like the one above, so if doctesting and the live version work, then once the Sphinx versions are the official documentation for the distribution, we can consider this issue solved.



---

archive/issue_comments_026526.json:
```json
{
    "body": "Yep, this is fine in the Sphinx documentation.",
    "created_at": "2009-01-24T10:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3737#issuecomment-26526",
    "user": "@mwhansen"
}
```

Yep, this is fine in the Sphinx documentation.



---

archive/issue_comments_026527.json:
```json
{
    "body": "This can be closed.",
    "created_at": "2009-02-21T23:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3737#issuecomment-26527",
    "user": "@jhpalmieri"
}
```

This can be closed.



---

archive/issue_comments_026528.json:
```json
{
    "body": "Fixed by the ReST merge in 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T19:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3737#issuecomment-26528",
    "user": "mabshoff"
}
```

Fixed by the ReST merge in 3.4.alpha0.

Cheers,

Michael



---

archive/issue_comments_026529.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T19:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3737#issuecomment-26529",
    "user": "mabshoff"
}
```

Resolution: fixed
