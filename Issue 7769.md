# Issue 7769: delete some rst files

archive/issues_007769.json:
```json
{
    "body": "Assignee: mvngu\n\nThis is a follow-up to #7466, and it may also be related to #7764.  In order to get rid of some of the warnings when building the reference manual: delete (by hand) everything in the directory SAGE_ROOT/devel/sage/doc/en/reference/sage/server/ *except* for\n\n```\ntrac/trac.rst\nwiki/moin.rst\n```\n\nNone of the files in this directory are tracked by Mercurial, so we have to delete them by hand, as far as I can tell, therefore there is no patch file.\n\n(This was given a positive review as part of #7466, but this part was never merged, so I'm giving it a positive review again.)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7769\n\n",
    "created_at": "2009-12-26T16:11:44Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "delete some rst files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7769",
    "user": "@jhpalmieri"
}
```
Assignee: mvngu

This is a follow-up to #7466, and it may also be related to #7764.  In order to get rid of some of the warnings when building the reference manual: delete (by hand) everything in the directory SAGE_ROOT/devel/sage/doc/en/reference/sage/server/ *except* for

```
trac/trac.rst
wiki/moin.rst
```

None of the files in this directory are tracked by Mercurial, so we have to delete them by hand, as far as I can tell, therefore there is no patch file.

(This was given a positive review as part of #7466, but this part was never merged, so I'm giving it a positive review again.)



Issue created by migration from https://trac.sagemath.org/ticket/7769





---

archive/issue_comments_066965.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-26T16:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7769#issuecomment-66965",
    "user": "@jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066966.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-26T16:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7769#issuecomment-66966",
    "user": "@jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066967.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T20:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7769#issuecomment-66967",
    "user": "@mwhansen"
}
```

Resolution: fixed
