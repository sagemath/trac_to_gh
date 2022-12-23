# Issue 6271: upgrade to mpir-1.3.0

archive/issues_006271.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  craigcitro\n\npackages are on sage.math, Craig knows where.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6271\n\n",
    "created_at": "2009-06-12T18:49:57Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "title": "upgrade to mpir-1.3.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6271",
    "user": "ncalexan"
}
```
Assignee: tbd

CC:  craigcitro

packages are on sage.math, Craig knows where.

Issue created by migration from https://trac.sagemath.org/ticket/6271





---

archive/issue_comments_050099.json:
```json
{
    "body": "This looks good, with the same caveat that we need to remember to remove the `spkg-check` before we release. (Is there an obvious reason there isn't just a flag for these we set somewhere in the sage build process?)",
    "created_at": "2009-06-14T08:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6271#issuecomment-50099",
    "user": "craigcitro"
}
```

This looks good, with the same caveat that we need to remember to remove the `spkg-check` before we release. (Is there an obvious reason there isn't just a flag for these we set somewhere in the sage build process?)



---

archive/issue_comments_050100.json:
```json
{
    "body": "> (Is there an obvious reason there isn't just a flag for these we set somewhere in the sage build process?) \n\nThere is such a flag.  It's SAGE_CHECK.  See http://trac.sagemath.org/sage_trac/ticket/6282.  It's just not documented, so nobody seems to know about it.",
    "created_at": "2009-06-14T09:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6271#issuecomment-50100",
    "user": "was"
}
```

> (Is there an obvious reason there isn't just a flag for these we set somewhere in the sage build process?) 

There is such a flag.  It's SAGE_CHECK.  See http://trac.sagemath.org/sage_trac/ticket/6282.  It's just not documented, so nobody seems to know about it.



---

archive/issue_comments_050101.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-14T22:31:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6271#issuecomment-50101",
    "user": "craigcitro"
}
```

Resolution: fixed
