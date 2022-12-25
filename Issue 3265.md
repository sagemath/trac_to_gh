# Issue 3265: some doctests leave files in $SAGE_ROOT/devel/sage

archive/issues_003265.json:
```json
{
    "body": "Assignee: failure\n\nSome doctests [likely notebook related] leave files in $SAGE_ROOT/devel/sage:\n\n```\nhg status\n? sage/server/docs-0.html\n? sage/server/docs-1.html\n? sage/server/docs-2.html\n? sage/server/notebook/a.txt\n```\n\nThis is problematic for two reasons:\n* temp files should be written to SAGE_TESTDIR since that is guaranteed to be writable, i.e. when you run doctests on an install that is not owned by the current user\n* it leaves crap in the default tree ;)\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3265\n\n",
    "created_at": "2008-05-21T13:35:15Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "some doctests leave files in $SAGE_ROOT/devel/sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3265",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: failure

Some doctests [likely notebook related] leave files in $SAGE_ROOT/devel/sage:

```
hg status
? sage/server/docs-0.html
? sage/server/docs-1.html
? sage/server/docs-2.html
? sage/server/notebook/a.txt
```

This is problematic for two reasons:
* temp files should be written to SAGE_TESTDIR since that is guaranteed to be writable, i.e. when you run doctests on an install that is not owned by the current user
* it leaves crap in the default tree ;)

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3265





---

archive/issue_comments_022563.json:
```json
{
    "body": "Mmmh, with the proto patch from #3267 the \"sage/server/docs-X.html\" files are no longer created.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-21T14:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3265#issuecomment-22563",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mmmh, with the proto patch from #3267 the "sage/server/docs-X.html" files are no longer created.

Cheers,

Michael



---

archive/issue_comments_022564.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-06-13T18:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3265#issuecomment-22564",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_022565.json:
```json
{
    "body": "This is a dupe of #3412.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-13T18:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3265#issuecomment-22565",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a dupe of #3412.

Cheers,

Michael
