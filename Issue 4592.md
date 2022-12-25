# Issue 4592: new setup.py dependency checking does not handle Cython built-in pxd files

archive/issues_004592.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @robertwb\n\nI can't get #4580 to compile, and I think this is why:\n\n#4580 adds \"`from python_int cimport PyInt_AS_LONG`\" to a Sage library file.  I believe this is intended to refer to $SAGE_ROOT/local/lib/python2.5/site-packages/Cython/Includes/python_int.pxd, but the setup.py dependency checker doesn't know about these Cython built-in pxd files, so it fails with an error: \n\n```\nIOError: [Errno 2] No such file or directory: 'sage/rings/polynomial/python_int.pxd'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4592\n\n",
    "created_at": "2008-11-23T04:56:53Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "new setup.py dependency checking does not handle Cython built-in pxd files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4592",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @craigcitro

CC:  @robertwb

I can't get #4580 to compile, and I think this is why:

#4580 adds "`from python_int cimport PyInt_AS_LONG`" to a Sage library file.  I believe this is intended to refer to $SAGE_ROOT/local/lib/python2.5/site-packages/Cython/Includes/python_int.pxd, but the setup.py dependency checker doesn't know about these Cython built-in pxd files, so it fails with an error: 

```
IOError: [Errno 2] No such file or directory: 'sage/rings/polynomial/python_int.pxd'
```


Issue created by migration from https://trac.sagemath.org/ticket/4592





---

archive/issue_comments_034372.json:
```json
{
    "body": "Attachment [trac-4592.patch](tarball://root/attachments/some-uuid/ticket4592/trac-4592.patch) by @craigcitro created at 2008-11-23 08:45:11",
    "created_at": "2008-11-23T08:45:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4592#issuecomment-34372",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4592.patch](tarball://root/attachments/some-uuid/ticket4592/trac-4592.patch) by @craigcitro created at 2008-11-23 08:45:11



---

archive/issue_comments_034373.json:
```json
{
    "body": "Adds code to also check the Cython include directory for any included `.pxd` files. Raises an error if a file can't be found. (Note that sometimes, this will sneak through and be caught by Cython instead.)",
    "created_at": "2008-11-23T08:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4592#issuecomment-34373",
    "user": "https://github.com/craigcitro"
}
```

Adds code to also check the Cython include directory for any included `.pxd` files. Raises an error if a file can't be found. (Note that sometimes, this will sneak through and be caught by Cython instead.)



---

archive/issue_comments_034374.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-23T08:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4592#issuecomment-34374",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034375.json:
```json
{
    "body": "The patch looks good, and does fix a problem.\n\nPositive review.",
    "created_at": "2008-11-23T16:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4592#issuecomment-34375",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

The patch looks good, and does fix a problem.

Positive review.



---

archive/issue_comments_034376.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha1",
    "created_at": "2008-11-23T23:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4592#issuecomment-34376",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha1



---

archive/issue_comments_034377.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-23T23:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4592#issuecomment-34377",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004841.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-23T23:47:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4592",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4592#event-4841"
}
```
