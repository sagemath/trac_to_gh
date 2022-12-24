# Issue 8270: 'make check' on exits with 0 on a failure.

archive/issues_008270.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nThe iconv package, which will soon be added to sage (#8191) has the facility to run \n\n```\nmake check\n```\n\n\nHowever, despite getting a test failure on Solaris 10 (SPARC), the makefile is still exiting with an exit code of 0, so any scripts which rely on testing iconv by relying on a failure of 'make check' to exit properly with a non-zero exit code will not work as desired. \n\nI'll report this to the iconv developers. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8270\n\n",
    "created_at": "2010-02-15T10:23:56Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "'make check' on exits with 0 on a failure.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8270",
    "user": "drkirkby"
}
```
Assignee: GeorgSWeber

The iconv package, which will soon be added to sage (#8191) has the facility to run 

```
make check
```


However, despite getting a test failure on Solaris 10 (SPARC), the makefile is still exiting with an exit code of 0, so any scripts which rely on testing iconv by relying on a failure of 'make check' to exit properly with a non-zero exit code will not work as desired. 

I'll report this to the iconv developers. 



Issue created by migration from https://trac.sagemath.org/ticket/8270





---

archive/issue_comments_073208.json:
```json
{
    "body": "Attachment [install](tarball://root/attachments/some-uuid/ticket8270/install) by drkirkby created at 2010-02-15 11:46:21\n\nThe file spkg/install  The iconv package is added.",
    "created_at": "2010-02-15T11:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8270#issuecomment-73208",
    "user": "drkirkby"
}
```

Attachment [install](tarball://root/attachments/some-uuid/ticket8270/install) by drkirkby created at 2010-02-15 11:46:21

The file spkg/install  The iconv package is added.



---

archive/issue_comments_073209.json:
```json
{
    "body": "Attachment [install.diff](tarball://root/attachments/some-uuid/ticket8270/install.diff) by drkirkby created at 2010-02-15 11:47:06\n\nDiff between the old spkg/install and the updated spkg/install for iconv support",
    "created_at": "2010-02-15T11:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8270#issuecomment-73209",
    "user": "drkirkby"
}
```

Attachment [install.diff](tarball://root/attachments/some-uuid/ticket8270/install.diff) by drkirkby created at 2010-02-15 11:47:06

Diff between the old spkg/install and the updated spkg/install for iconv support



---

archive/issue_comments_073210.json:
```json
{
    "body": "spkg/standard/deps to show packages which depend on iconv.",
    "created_at": "2010-02-15T11:47:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8270#issuecomment-73210",
    "user": "drkirkby"
}
```

spkg/standard/deps to show packages which depend on iconv.



---

archive/issue_comments_073211.json:
```json
{
    "body": "Attachment [deps](tarball://root/attachments/some-uuid/ticket8270/deps) by drkirkby created at 2010-02-15 11:48:36\n\nDiff between the old spkg/standard/deps and the new one with iconv",
    "created_at": "2010-02-15T11:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8270#issuecomment-73211",
    "user": "drkirkby"
}
```

Attachment [deps](tarball://root/attachments/some-uuid/ticket8270/deps) by drkirkby created at 2010-02-15 11:48:36

Diff between the old spkg/standard/deps and the new one with iconv



---

archive/issue_comments_073212.json:
```json
{
    "body": "Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket8270/deps.diff) by drkirkby created at 2010-02-15 11:49:49\n\nIgnore all these file - they were attached to the wrong ticket!! \nSorry about that.",
    "created_at": "2010-02-15T11:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8270#issuecomment-73212",
    "user": "drkirkby"
}
```

Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket8270/deps.diff) by drkirkby created at 2010-02-15 11:49:49

Ignore all these file - they were attached to the wrong ticket!! 
Sorry about that.



---

archive/issue_comments_073213.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-02-16T23:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8270#issuecomment-73213",
    "user": "drkirkby"
}
```

Resolution: invalid



---

archive/issue_comments_073214.json:
```json
{
    "body": "I'm told by the iconv developers this is not a bug. The core dumps are expected and ignored.",
    "created_at": "2010-02-16T23:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8270#issuecomment-73214",
    "user": "drkirkby"
}
```

I'm told by the iconv developers this is not a bug. The core dumps are expected and ignored.
