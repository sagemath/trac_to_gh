# Issue 5282: In %python mode in the notebook, tracebacks are not properly reported

archive/issues_005282.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5282\n\n",
    "created_at": "2009-02-16T06:29:42Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "In %python mode in the notebook, tracebacks are not properly reported",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5282",
    "user": "wasI"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/5282





---

archive/issue_comments_040597.json:
```json
{
    "body": "OK, I'm posting a patch that fixes this problem.  I improved syseval by getting rid of the weird hack of it just raising an exception when the system doesn't provide the interface it should.  This meant fixing many of the interfaces, which had evals that didn't work if a locals var was passed in.  I think this improved the quality of those interfaces as well, since many had customized eval methods that didn't properly pass extra options up to the base class, but now do.",
    "created_at": "2009-02-16T07:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5282#issuecomment-40597",
    "user": "was"
}
```

OK, I'm posting a patch that fixes this problem.  I improved syseval by getting rid of the weird hack of it just raising an exception when the system doesn't provide the interface it should.  This meant fixing many of the interfaces, which had evals that didn't work if a locals var was passed in.  I think this improved the quality of those interfaces as well, since many had customized eval methods that didn't properly pass extra options up to the base class, but now do.



---

archive/issue_comments_040598.json:
```json
{
    "body": "Attachment [trac_5282.patch](tarball://root/attachments/some-uuid/ticket5282/trac_5282.patch) by was created at 2009-02-16 07:00:30",
    "created_at": "2009-02-16T07:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5282#issuecomment-40598",
    "user": "was"
}
```

Attachment [trac_5282.patch](tarball://root/attachments/some-uuid/ticket5282/trac_5282.patch) by was created at 2009-02-16 07:00:30



---

archive/issue_comments_040599.json:
```json
{
    "body": "Positive review and nice cleanup.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T08:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5282#issuecomment-40599",
    "user": "mabshoff"
}
```

Positive review and nice cleanup.

Cheers,

Michael



---

archive/issue_comments_040600.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T08:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5282#issuecomment-40600",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_040601.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-16T08:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5282#issuecomment-40601",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040602.json:
```json
{
    "body": "Nice patch, thanks!",
    "created_at": "2009-02-16T13:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5282#issuecomment-40602",
    "user": "certik"
}
```

Nice patch, thanks!
