# Issue 5286: python 2.5.4 breaks -sdist due to missing .hg repo in the sage-3.3.rc1.spkg (followup to #5218)

archive/issues_005286.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen merging the python-2.5.4.spkg from #5218 everything goes fine, but -sdist. In that case the .hg repo is copied into the tmp directory in spkg-dist, but it is not copied into the tar.gz created by distutils. Until this is resolved we cannot update to the latest python-2.5.4.spkg.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5286\n\n",
    "created_at": "2009-02-16T16:03:38Z",
    "labels": [
        "distribution",
        "blocker",
        "bug"
    ],
    "title": "python 2.5.4 breaks -sdist due to missing .hg repo in the sage-3.3.rc1.spkg (followup to #5218)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5286",
    "user": "mabshoff"
}
```
Assignee: mabshoff

When merging the python-2.5.4.spkg from #5218 everything goes fine, but -sdist. In that case the .hg repo is copied into the tmp directory in spkg-dist, but it is not copied into the tar.gz created by distutils. Until this is resolved we cannot update to the latest python-2.5.4.spkg.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5286





---

archive/issue_comments_040624.json:
```json
{
    "body": "Better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5286#issuecomment-40624",
    "user": "mabshoff"
}
```

Better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_comments_040625.json:
```json
{
    "body": "Changing assignee from mabshoff to mhansen.",
    "created_at": "2009-05-28T20:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5286#issuecomment-40625",
    "user": "mhansen"
}
```

Changing assignee from mabshoff to mhansen.



---

archive/issue_comments_040626.json:
```json
{
    "body": "This is caused by http://bugs.python.org/issue1725737\n\nThere is a fix in the new spkg at #5218.",
    "created_at": "2009-05-28T20:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5286#issuecomment-40626",
    "user": "mhansen"
}
```

This is caused by http://bugs.python.org/issue1725737

There is a fix in the new spkg at #5218.



---

archive/issue_comments_040627.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-28T20:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5286#issuecomment-40627",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040628.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-29T13:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5286#issuecomment-40628",
    "user": "was"
}
```

Resolution: fixed
