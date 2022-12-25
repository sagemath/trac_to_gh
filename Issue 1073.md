# Issue 1073: right after "sage -pkg" creates a package, print out some useful information

archive/issues_001073.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis would save people a lot of confusion.\n\n\n```\n$ sage -pkg foo-bar-2.3\n...\n\nCreated package foo-bar-2.3.spkg, \n\nNAME: foo\nVERSION: bar-2.3      (not version number looks suspicious)\nSIZE: 2.3MB\nHG REPO: Unchecked in changes (!)\nSPKG.txt: File is missing.\n\nPlease test this package using\n    sage -f foo-bar-2.3.spkg\nimmediately.   Also, note that you can use \n    sage -pkg_nc foo-bar-2.3\nto make an uncompressed version of the package (useful if the\npackage is full of compressed data).\n\n\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1073\n\n",
    "created_at": "2007-11-02T23:49:55Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "right after \"sage -pkg\" creates a package, print out some useful information",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1073",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This would save people a lot of confusion.


```
$ sage -pkg foo-bar-2.3
...

Created package foo-bar-2.3.spkg, 

NAME: foo
VERSION: bar-2.3      (not version number looks suspicious)
SIZE: 2.3MB
HG REPO: Unchecked in changes (!)
SPKG.txt: File is missing.

Please test this package using
    sage -f foo-bar-2.3.spkg
immediately.   Also, note that you can use 
    sage -pkg_nc foo-bar-2.3
to make an uncompressed version of the package (useful if the
package is full of compressed data).



```


Issue created by migration from https://trac.sagemath.org/ticket/1073





---

archive/issue_comments_006475.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-11-02T23:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1073#issuecomment-6475",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_006476.json:
```json
{
    "body": "Attachment [trac_1073.patch](tarball://root/attachments/some-uuid/ticket1073/trac_1073.patch) by @malb created at 2008-01-06 14:11:32\n\nI am not a bash expert but the attached patch does the job for me.",
    "created_at": "2008-01-06T14:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1073#issuecomment-6476",
    "user": "https://github.com/malb"
}
```

Attachment [trac_1073.patch](tarball://root/attachments/some-uuid/ticket1073/trac_1073.patch) by @malb created at 2008-01-06 14:11:32

I am not a bash expert but the attached patch does the job for me.



---

archive/issue_comments_006477.json:
```json
{
    "body": "Patch looks good to me. We should add the detect binary crap script, but I will open another ticket for that once William does send it to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-10T05:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1073#issuecomment-6477",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. We should add the detect binary crap script, but I will open another ticket for that once William does send it to me.

Cheers,

Michael



---

archive/issue_comments_006478.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-10T06:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1073#issuecomment-6478",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001195.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-10T06:31:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1073",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1073#event-1195"
}
```
