# Issue 7565: README.txt: enhance instructions on installing binary distribution

archive/issues_007565.json:
```json
{
    "body": "Assignee: mvngu\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/4a36a68dcd5a9190):\n\n```\n> My two-cent, but you probably know already: Say as root, you build\n> Sage and then move the resulting binary to a different directory.\n> After moving the whole Sage (binary) directory, you need to start up\n> Sage as root at least once before you use Sage as another user.\n\nI guess David's point was that this information should be stated more\nclearly in the Readme text.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7565\n\n",
    "created_at": "2009-11-30T23:04:10Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "README.txt: enhance instructions on installing binary distribution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7565",
    "user": "mvngu"
}
```
Assignee: mvngu

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/4a36a68dcd5a9190):

```
> My two-cent, but you probably know already: Say as root, you build
> Sage and then move the resulting binary to a different directory.
> After moving the whole Sage (binary) directory, you need to start up
> Sage as root at least once before you use Sage as another user.

I guess David's point was that this information should be stated more
clearly in the Readme text.
```


Issue created by migration from https://trac.sagemath.org/ticket/7565





---

archive/issue_comments_064376.json:
```json
{
    "body": "new README.txt file, based on Sage 4.3.alpha0",
    "created_at": "2009-11-30T23:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7565#issuecomment-64376",
    "user": "mvngu"
}
```

new README.txt file, based on Sage 4.3.alpha0



---

archive/issue_comments_064377.json:
```json
{
    "body": "Attachment [readme.patch](tarball://root/attachments/some-uuid/ticket7565/readme.patch) by mvngu created at 2009-11-30 23:19:39\n\ndifferences between old and new README.txt files; do not apply",
    "created_at": "2009-11-30T23:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7565#issuecomment-64377",
    "user": "mvngu"
}
```

Attachment [readme.patch](tarball://root/attachments/some-uuid/ticket7565/readme.patch) by mvngu created at 2009-11-30 23:19:39

differences between old and new README.txt files; do not apply



---

archive/issue_comments_064378.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-30T23:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7565#issuecomment-64378",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064379.json:
```json
{
    "body": "I have attached a new `README.txt` file. The patch `readme.patch` shows the differences between the old and new README.txt files. You should not apply that patch because the `SAGE_ROOT` directory is not under revision control. Instead, you should only replace the old `README.txt` with the newer, attached `README.txt`. A related ticket is #7553.",
    "created_at": "2009-11-30T23:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7565#issuecomment-64379",
    "user": "mvngu"
}
```

I have attached a new `README.txt` file. The patch `readme.patch` shows the differences between the old and new README.txt files. You should not apply that patch because the `SAGE_ROOT` directory is not under revision control. Instead, you should only replace the old `README.txt` with the newer, attached `README.txt`. A related ticket is #7553.



---

archive/issue_comments_064380.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-01T08:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7565#issuecomment-64380",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_064381.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-12-01T08:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7565#issuecomment-64381",
    "user": "@mwhansen"
}
```

Looks good.
