# Issue 2595: rubiks and polymake both have a cube binary

archive/issues_002595.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen one installs the optional polymake.spkg the cube doctest fails since somehow polymake's cube is in $PATH before rubik's cube:\n\n```\n./local/bin/cube\n./local/polymake/bin/cube\n```\n\n\nI would suggest changing the name of the binary from rubiks.spkg.\n\nCheers,\n\nMichael\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2595\n\n",
    "created_at": "2008-03-19T12:44:32Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "rubiks and polymake both have a cube binary",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2595",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

When one installs the optional polymake.spkg the cube doctest fails since somehow polymake's cube is in $PATH before rubik's cube:

```
./local/bin/cube
./local/polymake/bin/cube
```


I would suggest changing the name of the binary from rubiks.spkg.

Cheers,

Michael


Issue created by migration from https://trac.sagemath.org/ticket/2595





---

archive/issue_comments_017715.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-19T12:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2595#issuecomment-17715",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017716.json:
```json
{
    "body": "trivial patch to rename the binary in DikSolver",
    "created_at": "2008-03-21T12:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2595#issuecomment-17716",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

trivial patch to rename the binary in DikSolver



---

archive/issue_comments_017717.json:
```json
{
    "body": "Attachment [trac_2595.patch](tarball://root/attachments/some-uuid/ticket2595/trac_2595.patch) by mabshoff created at 2008-03-21 12:27:49",
    "created_at": "2008-03-21T12:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2595#issuecomment-17717",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2595.patch](tarball://root/attachments/some-uuid/ticket2595/trac_2595.patch) by mabshoff created at 2008-03-21 12:27:49



---

archive/issue_comments_017718.json:
```json
{
    "body": "Looks good",
    "created_at": "2008-03-21T12:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2595#issuecomment-17718",
    "user": "https://github.com/garyfurnish"
}
```

Looks good



---

archive/issue_comments_017719.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T12:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2595#issuecomment-17719",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002784.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-21T12:36:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2595",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2595#event-2784"
}
```



---

archive/issue_comments_017720.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1. The corresponding fix to the makefile of rubiks.spkg will be in #2287.",
    "created_at": "2008-03-21T12:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2595#issuecomment-17720",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha1. The corresponding fix to the makefile of rubiks.spkg will be in #2287.
