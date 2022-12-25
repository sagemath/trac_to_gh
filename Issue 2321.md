# Issue 2321: remove dsage_server.py

archive/issues_002321.json:
```json
{
    "body": "Assignee: @williamstein\n\ndsage switched from using dsage_server.py to using a .tac located in .sage/dsage. When we roll out the next version of sage (2.10.3) we need to remove SAGE_ROOT/local/bin/dsage_server.py.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2321\n\n",
    "created_at": "2008-02-26T17:47:20Z",
    "labels": [
        "component: dsage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "remove dsage_server.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2321",
    "user": "https://github.com/yqiang"
}
```
Assignee: @williamstein

dsage switched from using dsage_server.py to using a .tac located in .sage/dsage. When we roll out the next version of sage (2.10.3) we need to remove SAGE_ROOT/local/bin/dsage_server.py.

Issue created by migration from https://trac.sagemath.org/ticket/2321





---

archive/issue_comments_015404.json:
```json
{
    "body": "Yi: Does this depend on any patches still getting merged for 2.10.3 from your end or can I nuke the file now? A patch for this is obviously trivial.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-26T17:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2321#issuecomment-15404",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yi: Does this depend on any patches still getting merged for 2.10.3 from your end or can I nuke the file now? A patch for this is obviously trivial.

Cheers,

Michael



---

archive/issue_comments_015405.json:
```json
{
    "body": "Yes, we should not nuke dsage_server.py until we've successfully merged in the huge dsage changes for 2.10.3.",
    "created_at": "2008-02-26T18:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2321#issuecomment-15405",
    "user": "https://github.com/yqiang"
}
```

Yes, we should not nuke dsage_server.py until we've successfully merged in the huge dsage changes for 2.10.3.



---

archive/issue_comments_015406.json:
```json
{
    "body": "The file has been removed, probably in 2.11. Ergo it is fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-14T00:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2321#issuecomment-15406",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The file has been removed, probably in 2.11. Ergo it is fixed.

Cheers,

Michael



---

archive/issue_comments_015407.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-14T00:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2321#issuecomment-15407",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
