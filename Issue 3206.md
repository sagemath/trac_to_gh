# Issue 3206: sage -i http://url.of.an.spkg doesn't work

archive/issues_003206.json:
```json
{
    "body": "Assignee: mabshoff\n\nFor some reason nobody ever got around to implementing \"sage -i\" on URL's.  E.g.,\nthis should work but doesn't yet.  I'm amazed this still isn't done!\n\n```\nsage -i http://sagemath.org/packages/optional/database_odlyzko_zeta.spkg\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3206\n\n",
    "created_at": "2008-05-14T22:26:12Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "sage -i http://url.of.an.spkg doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3206",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

For some reason nobody ever got around to implementing "sage -i" on URL's.  E.g.,
this should work but doesn't yet.  I'm amazed this still isn't done!

```
sage -i http://sagemath.org/packages/optional/database_odlyzko_zeta.spkg
```


Issue created by migration from https://trac.sagemath.org/ticket/3206





---

archive/issue_comments_022114.json:
```json
{
    "body": "Attachment [scripts-3206.patch](tarball://root/attachments/some-uuid/ticket3206/scripts-3206.patch) by @williamstein created at 2008-05-15 00:26:50\n\nI've fixed the indicated problem, cleaned up the code, and documented the heck out of local/bin/sage-download_package/.",
    "created_at": "2008-05-15T00:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3206#issuecomment-22114",
    "user": "https://github.com/williamstein"
}
```

Attachment [scripts-3206.patch](tarball://root/attachments/some-uuid/ticket3206/scripts-3206.patch) by @williamstein created at 2008-05-15 00:26:50

I've fixed the indicated problem, cleaned up the code, and documented the heck out of local/bin/sage-download_package/.



---

archive/issue_comments_022115.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T07:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3206#issuecomment-22115",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022116.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T07:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3206#issuecomment-22116",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha0
