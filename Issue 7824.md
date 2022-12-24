# Issue 7824: cliquer-1.2.p2 - add FreeBSD support

archive/issues_007824.json:
```json
{
    "body": "Assignee: pjeremy\n\nCC:  nathann.cohen@gmail.com\n\ncliquer aborts with the error\n\n```\nCannot determine your platform or it is not supported... exiting\n```\n\nunless the platform is explicitly listed as supported.  This patch adds FreeBSD support - which is the same as Linux.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7824\n\n",
    "created_at": "2010-01-03T02:10:25Z",
    "labels": [
        "porting: BSD",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "cliquer-1.2.p2 - add FreeBSD support",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7824",
    "user": "pjeremy"
}
```
Assignee: pjeremy

CC:  nathann.cohen@gmail.com

cliquer aborts with the error

```
Cannot determine your platform or it is not supported... exiting
```

unless the platform is explicitly listed as supported.  This patch adds FreeBSD support - which is the same as Linux.

Issue created by migration from https://trac.sagemath.org/ticket/7824





---

archive/issue_comments_067726.json:
```json
{
    "body": "Attachment [7824.cliquer.patch](tarball://root/attachments/some-uuid/ticket7824/7824.cliquer.patch) by pjeremy created at 2010-01-03 02:17:31",
    "created_at": "2010-01-03T02:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7824#issuecomment-67726",
    "user": "pjeremy"
}
```

Attachment [7824.cliquer.patch](tarball://root/attachments/some-uuid/ticket7824/7824.cliquer.patch) by pjeremy created at 2010-01-03 02:17:31



---

archive/issue_comments_067727.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T02:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7824#issuecomment-67727",
    "user": "pjeremy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067728.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-12T17:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7824#issuecomment-67728",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067729.json:
```json
{
    "body": "I can't check it, not having FreeBSD installed, but it is clearly 100% safe as it only affects FreeBSD.",
    "created_at": "2010-01-12T17:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7824#issuecomment-67729",
    "user": "drkirkby"
}
```

I can't check it, not having FreeBSD installed, but it is clearly 100% safe as it only affects FreeBSD.



---

archive/issue_comments_067730.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-24T14:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7824#issuecomment-67730",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_067731.json:
```json
{
    "body": "An updated spkg is available at\n\nhttp://sage.math.washington.edu/home/mvngu/spkg/standard/cliquer/cliquer-1.2.p3.spkg\n\nAll changes are committed in pjeremy's name.",
    "created_at": "2010-01-24T14:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7824#issuecomment-67731",
    "user": "mvngu"
}
```

An updated spkg is available at

http://sage.math.washington.edu/home/mvngu/spkg/standard/cliquer/cliquer-1.2.p3.spkg

All changes are committed in pjeremy's name.
