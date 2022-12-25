# Issue 112: get rid of "gap_reset_workspace"

archive/issues_000112.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe whole gap_reset_workspace() idea is bad.  It just doesn't make any sense at all!\nHere's what should happen.   \n\n1. When a new gap component is installed a file in <SAGE_ROOT> is touched.\n\n2. When SAGE starts, if the user's local gap_workspace is older than the file in 1,\nthen it is recreated.\n\nThat's it!\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/112\n\n",
    "created_at": "2006-10-05T10:12:46Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "title": "get rid of \"gap_reset_workspace\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/112",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

The whole gap_reset_workspace() idea is bad.  It just doesn't make any sense at all!
Here's what should happen.   

1. When a new gap component is installed a file in <SAGE_ROOT> is touched.

2. When SAGE starts, if the user's local gap_workspace is older than the file in 1,
then it is recreated.

That's it!


Issue created by migration from https://trac.sagemath.org/ticket/112





---

archive/issue_events_000118.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2006-10-05T11:25:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/112",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/112#event-118"
}
```



---

archive/issue_comments_000534.json:
```json
{
    "body": "Done.  The fix is to store the workspace in <SAGE_ROOT>/local/lib/ and only allow\nthe admin user to change it.  That's fine since it should only be changed when\nnew packages are installed anyways.",
    "created_at": "2006-10-05T11:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/112#issuecomment-534",
    "user": "https://github.com/williamstein"
}
```

Done.  The fix is to store the workspace in <SAGE_ROOT>/local/lib/ and only allow
the admin user to change it.  That's fine since it should only be changed when
new packages are installed anyways.



---

archive/issue_comments_000535.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-05T11:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/112#issuecomment-535",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
