# Issue 6746: cliquer doesn't build under 64-bit mode

archive/issues_006746.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @jhpalmieri @nathanncohen\n\nAt this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/9b8016e17cc81128) thread, Kiran Kedlaya reported a problem with building cliquer under a 64-bit platform:\n\n```\nOn 64-bit Fedora 10, I get a build failure in cliquer. The relevant\nsnippet from the install log is below.\n\nThis looks like a case of 32/64 confusion, which I am no stranger to.\nThis machine runs on a primarily 32-bit network, and in the past we've\ndiscovered various build problems due to this. For instance, the local\ngcc in /usr/bin is 64-bit, but the NFS one in /usr/local/bin is 32-\nbit, so I have to configure my path appropriately. In this case, it's\nsomehow trying to find stubs-32.h instead of stubs-64.h, but I don't\nknow why.\n```\n\nJohn Palmieri also reported at ticket #6681 a similar problem with 64-bit OS X.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6746\n\n",
    "created_at": "2009-08-14T17:22:13Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cliquer doesn't build under 64-bit mode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6746",
    "user": "mvngu"
}
```
Assignee: mabshoff

CC:  @jhpalmieri @nathanncohen

At this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/9b8016e17cc81128) thread, Kiran Kedlaya reported a problem with building cliquer under a 64-bit platform:

```
On 64-bit Fedora 10, I get a build failure in cliquer. The relevant
snippet from the install log is below.

This looks like a case of 32/64 confusion, which I am no stranger to.
This machine runs on a primarily 32-bit network, and in the past we've
discovered various build problems due to this. For instance, the local
gcc in /usr/bin is 64-bit, but the NFS one in /usr/local/bin is 32-
bit, so I have to configure my path appropriately. In this case, it's
somehow trying to find stubs-32.h instead of stubs-64.h, but I don't
know why.
```

John Palmieri also reported at ticket #6681 a similar problem with 64-bit OS X.

Issue created by migration from https://trac.sagemath.org/ticket/6746





---

archive/issue_comments_055500.json:
```json
{
    "body": "See ticket #6681 for an updated cliquer spkg. If that package also builds on 64-bit Fedora 10, then this ticket should be closed as a duplicate of #6681.",
    "created_at": "2009-09-13T09:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6746#issuecomment-55500",
    "user": "mvngu"
}
```

See ticket #6681 for an updated cliquer spkg. If that package also builds on 64-bit Fedora 10, then this ticket should be closed as a duplicate of #6681.



---

archive/issue_comments_055501.json:
```json
{
    "body": "Replying to [comment:1 mvngu]:\n> See ticket #6681 for an updated cliquer spkg. If that package also builds on 64-bit Fedora 10, then this ticket should be closed as a duplicate of #6681.\n\nIt does indeed build on 64-bit Fedora 10, as part of a full build of 4.1.2.alpha2.",
    "created_at": "2009-09-22T19:08:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6746#issuecomment-55501",
    "user": "@kedlaya"
}
```

Replying to [comment:1 mvngu]:
> See ticket #6681 for an updated cliquer spkg. If that package also builds on 64-bit Fedora 10, then this ticket should be closed as a duplicate of #6681.

It does indeed build on 64-bit Fedora 10, as part of a full build of 4.1.2.alpha2.



---

archive/issue_comments_055502.json:
```json
{
    "body": "Duplicate of #6681",
    "created_at": "2009-09-25T08:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6746#issuecomment-55502",
    "user": "@mwhansen"
}
```

Duplicate of #6681



---

archive/issue_comments_055503.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-09-25T08:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6746#issuecomment-55503",
    "user": "@mwhansen"
}
```

Resolution: duplicate
