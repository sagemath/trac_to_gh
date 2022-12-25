# Issue 5282: In %python mode in the notebook, tracebacks are not properly reported

archive/issues_005282.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5282\n\n",
    "created_at": "2009-02-16T06:29:42Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "In %python mode in the notebook, tracebacks are not properly reported",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5282",
    "user": "https://trac.sagemath.org/admin/accounts/users/wasI"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/5282





---

archive/issue_comments_040518.json:
```json
{
    "body": "OK, I'm posting a patch that fixes this problem.  I improved syseval by getting rid of the weird hack of it just raising an exception when the system doesn't provide the interface it should.  This meant fixing many of the interfaces, which had evals that didn't work if a locals var was passed in.  I think this improved the quality of those interfaces as well, since many had customized eval methods that didn't properly pass extra options up to the base class, but now do.",
    "created_at": "2009-02-16T07:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5282#issuecomment-40518",
    "user": "https://github.com/williamstein"
}
```

OK, I'm posting a patch that fixes this problem.  I improved syseval by getting rid of the weird hack of it just raising an exception when the system doesn't provide the interface it should.  This meant fixing many of the interfaces, which had evals that didn't work if a locals var was passed in.  I think this improved the quality of those interfaces as well, since many had customized eval methods that didn't properly pass extra options up to the base class, but now do.



---

archive/issue_comments_040519.json:
```json
{
    "body": "Attachment [trac_5282.patch](tarball://root/attachments/some-uuid/ticket5282/trac_5282.patch) by @williamstein created at 2009-02-16 07:00:30",
    "created_at": "2009-02-16T07:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5282#issuecomment-40519",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5282.patch](tarball://root/attachments/some-uuid/ticket5282/trac_5282.patch) by @williamstein created at 2009-02-16 07:00:30



---

archive/issue_comments_040520.json:
```json
{
    "body": "Positive review and nice cleanup.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T08:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5282#issuecomment-40520",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review and nice cleanup.

Cheers,

Michael



---

archive/issue_comments_040521.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T08:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5282#issuecomment-40521",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_events_005537.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-16T08:22:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5282",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5282#event-5537"
}
```



---

archive/issue_comments_040522.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-16T08:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5282#issuecomment-40522",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040523.json:
```json
{
    "body": "Nice patch, thanks!",
    "created_at": "2009-02-16T13:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5282#issuecomment-40523",
    "user": "https://github.com/certik"
}
```

Nice patch, thanks!
