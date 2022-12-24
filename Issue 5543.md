# Issue 5543: [with patch, needs review] RealIntervalField parents are not unique

archive/issues_005543.json:
```json
{
    "body": "Assignee: somebody\n\nNote that the attached patch has an apparently-spurious chunk that adds a single space to rings/polynomial/real_roots.pyx.  This is to force a recompilation for that file (to work around a bug in the dependency tracker); otherwise you end up with a broken Sage because the real_roots module won't load.  (I'll report the dependency tracker bug as a separate ticket in a minute.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5543\n\n",
    "created_at": "2009-03-17T06:14:11Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] RealIntervalField parents are not unique",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5543",
    "user": "cwitty"
}
```
Assignee: somebody

Note that the attached patch has an apparently-spurious chunk that adds a single space to rings/polynomial/real_roots.pyx.  This is to force a recompilation for that file (to work around a bug in the dependency tracker); otherwise you end up with a broken Sage because the real_roots module won't load.  (I'll report the dependency tracker bug as a separate ticket in a minute.)

Issue created by migration from https://trac.sagemath.org/ticket/5543





---

archive/issue_comments_043131.json:
```json
{
    "body": "Attachment [rif-unique-parents.patch](tarball://root/attachments/some-uuid/ticket5543/rif-unique-parents.patch) by was created at 2009-04-12 04:20:16",
    "created_at": "2009-04-12T04:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5543#issuecomment-43131",
    "user": "was"
}
```

Attachment [rif-unique-parents.patch](tarball://root/attachments/some-uuid/ticket5543/rif-unique-parents.patch) by was created at 2009-04-12 04:20:16



---

archive/issue_comments_043132.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T02:39:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5543#issuecomment-43132",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043133.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T02:39:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5543#issuecomment-43133",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
