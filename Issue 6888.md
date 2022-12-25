# Issue 6888: sage-env complain about bad SAGE_ROOT environment variable with no reason

archive/issues_006888.json:
```json
{
    "body": "Assignee: tbd\n\nthe $SAGE_ROOT/local/bin/sage-env has 2 small flaws.\n\n1) the script prints the following message: \n\n```\n    You must set the SAGE_ROOT environment variable or\n    run this script from the SAGE_ROOT or\n    SAGE_ROOT/local/bin/ directory.\n```\n\neven if SAGE_ROOT is set correctly.\n\n2) if SAGE_ROOT is set to a wrong path, it doesn't stop,\n\nThe attached patch fixes them. \n\nI am not a shell expert, so please test it.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6888\n\n",
    "created_at": "2009-09-04T12:59:01Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "title": "sage-env complain about bad SAGE_ROOT environment variable with no reason",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6888",
    "user": "https://trac.sagemath.org/admin/accounts/users/sbarthelemy"
}
```
Assignee: tbd

the $SAGE_ROOT/local/bin/sage-env has 2 small flaws.

1) the script prints the following message: 

```
    You must set the SAGE_ROOT environment variable or
    run this script from the SAGE_ROOT or
    SAGE_ROOT/local/bin/ directory.
```

even if SAGE_ROOT is set correctly.

2) if SAGE_ROOT is set to a wrong path, it doesn't stop,

The attached patch fixes them. 

I am not a shell expert, so please test it.



Issue created by migration from https://trac.sagemath.org/ticket/6888





---

archive/issue_comments_056820.json:
```json
{
    "body": "Attachment [sage-env.patch](tarball://root/attachments/some-uuid/ticket6888/sage-env.patch) by @mwhansen created at 2009-09-07 23:03:49",
    "created_at": "2009-09-07T23:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6888#issuecomment-56820",
    "user": "https://github.com/mwhansen"
}
```

Attachment [sage-env.patch](tarball://root/attachments/some-uuid/ticket6888/sage-env.patch) by @mwhansen created at 2009-09-07 23:03:49



---

archive/issue_comments_056821.json:
```json
{
    "body": "Looks good. Good job.",
    "created_at": "2009-09-22T13:30:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6888#issuecomment-56821",
    "user": "https://github.com/TimDumol"
}
```

Looks good. Good job.



---

archive/issue_comments_056822.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T09:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6888#issuecomment-56822",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_056823.json:
```json
{
    "body": "full author name",
    "created_at": "2017-07-19T09:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6888#issuecomment-56823",
    "user": "https://github.com/fchapoton"
}
```

full author name
