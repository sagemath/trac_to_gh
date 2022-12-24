# Issue 4840: FLINT: call the stack cleanup function at exit

archive/issues_004840.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @burcin\n\nFLINT uses its own memory pool. In order to clean up Sage's valgrind log call  flint_stack_cleanup() right before unloading FLINT.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4840\n\n",
    "created_at": "2008-12-20T22:11:53Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "FLINT: call the stack cleanup function at exit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4840",
    "user": "mabshoff"
}
```
Assignee: @williamstein

CC:  @burcin

FLINT uses its own memory pool. In order to clean up Sage's valgrind log call  flint_stack_cleanup() right before unloading FLINT.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4840





---

archive/issue_comments_036704.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-20T22:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4840#issuecomment-36704",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036705.json:
```json
{
    "body": "Changing component from linear algebra to memleak.",
    "created_at": "2008-12-20T22:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4840#issuecomment-36705",
    "user": "mabshoff"
}
```

Changing component from linear algebra to memleak.



---

archive/issue_comments_036706.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-12-20T22:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4840#issuecomment-36706",
    "user": "mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_036707.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-01-23T08:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4840#issuecomment-36707",
    "user": "@burcin"
}
```

Changing status from assigned to new.



---

archive/issue_comments_036708.json:
```json
{
    "body": "attachment:trac_4840-flint_free.patch should fix this.",
    "created_at": "2009-01-23T08:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4840#issuecomment-36708",
    "user": "@burcin"
}
```

attachment:trac_4840-flint_free.patch should fix this.



---

archive/issue_comments_036709.json:
```json
{
    "body": "Changing assignee from mabshoff to @burcin.",
    "created_at": "2009-01-23T08:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4840#issuecomment-36709",
    "user": "@burcin"
}
```

Changing assignee from mabshoff to @burcin.



---

archive/issue_comments_036710.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-01-24T02:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4840#issuecomment-36710",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_036711.json:
```json
{
    "body": "This patch does not apply to my tree? I am also curious why this is a git style patch considering that the history is messed up anyway with git style patches:\n\n```\nmabshoff@geom:/scratch/mabshoff/sage-3.3.alpha2/devel/sage$ hg import trac_4840-flint_free.patch \napplying trac_4840-flint_free.patch\nunable to find 'sage/libs/flint/flint.pxi' for patching\n1 out of 1 hunks FAILED -- saving rejects to file sage/libs/flint/flint.pxi.rej\nsage/libs/flint/flint.pxi: No such file or directory\nabort: patch failed to apply\n```\n\nWhat is going on here? Does this depend on something else?\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T14:09:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4840#issuecomment-36711",
    "user": "mabshoff"
}
```

This patch does not apply to my tree? I am also curious why this is a git style patch considering that the history is messed up anyway with git style patches:

```
mabshoff@geom:/scratch/mabshoff/sage-3.3.alpha2/devel/sage$ hg import trac_4840-flint_free.patch 
applying trac_4840-flint_free.patch
unable to find 'sage/libs/flint/flint.pxi' for patching
1 out of 1 hunks FAILED -- saving rejects to file sage/libs/flint/flint.pxi.rej
sage/libs/flint/flint.pxi: No such file or directory
abort: patch failed to apply
```

What is going on here? Does this depend on something else?

Cheers,

Michael



---

archive/issue_comments_036712.json:
```json
{
    "body": "Attachment [trac_4840-flint_free.patch](tarball://root/attachments/some-uuid/ticket4840/trac_4840-flint_free.patch) by @burcin created at 2009-01-24 17:34:06\n\nNew patch fixes merge failure.",
    "created_at": "2009-01-24T17:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4840#issuecomment-36712",
    "user": "@burcin"
}
```

Attachment [trac_4840-flint_free.patch](tarball://root/attachments/some-uuid/ticket4840/trac_4840-flint_free.patch) by @burcin created at 2009-01-24 17:34:06

New patch fixes merge failure.



---

archive/issue_comments_036713.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T17:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4840#issuecomment-36713",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036714.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T17:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4840#issuecomment-36714",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2
