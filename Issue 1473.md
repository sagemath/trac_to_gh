# Issue 1473: Java3D usable from command line as well as notebook

archive/issues_001473.json:
```json
{
    "body": "Assignee: @williamstein\n\nEventually we hope to have many tools (e.g. MayaVi) to help handle this, but Java3D works now and it should be easy to invoke the same code as an app rather than an applet. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1473\n\n",
    "created_at": "2007-12-12T10:49:02Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "Java3D usable from command line as well as notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1473",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

Eventually we hope to have many tools (e.g. MayaVi) to help handle this, but Java3D works now and it should be easy to invoke the same code as an app rather than an applet. 

Issue created by migration from https://trac.sagemath.org/ticket/1473





---

archive/issue_comments_009452.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-12T10:49:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9452",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009453.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2007-12-12T10:49:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9453",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_comments_009454.json:
```json
{
    "body": "Attachment [extcode-3d-cmd.hg](tarball://root/attachments/some-uuid/ticket1473/extcode-3d-cmd.hg) by @robertwb created at 2007-12-14 06:27:28",
    "created_at": "2007-12-14T06:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9454",
    "user": "https://github.com/robertwb"
}
```

Attachment [extcode-3d-cmd.hg](tarball://root/attachments/some-uuid/ticket1473/extcode-3d-cmd.hg) by @robertwb created at 2007-12-14 06:27:28



---

archive/issue_comments_009455.json:
```json
{
    "body": "Attachment [sage-main-3d-cmd.hg](tarball://root/attachments/some-uuid/ticket1473/sage-main-3d-cmd.hg) by @robertwb created at 2007-12-14 09:32:10",
    "created_at": "2007-12-14T09:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9455",
    "user": "https://github.com/robertwb"
}
```

Attachment [sage-main-3d-cmd.hg](tarball://root/attachments/some-uuid/ticket1473/sage-main-3d-cmd.hg) by @robertwb created at 2007-12-14 09:32:10



---

archive/issue_comments_009456.json:
```json
{
    "body": "Attachment [extcode-java3d-update.diff](tarball://root/attachments/some-uuid/ticket1473/extcode-java3d-update.diff) by @williamstein created at 2007-12-15 07:37:41\n\nThis works fine for me.",
    "created_at": "2007-12-15T07:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9456",
    "user": "https://github.com/williamstein"
}
```

Attachment [extcode-java3d-update.diff](tarball://root/attachments/some-uuid/ticket1473/extcode-java3d-update.diff) by @williamstein created at 2007-12-15 07:37:41

This works fine for me.



---

archive/issue_comments_009457.json:
```json
{
    "body": "If I download `java3d-1_5_1-linux-i586.zip` from the java3d web site, I can unzipit to get (among other things) `j3d-jre.zip`.  Then I can unzip `j3d-jre.zip` to get (among other things) `libj3dcore-ogl.so`.\n\nIf I put libj3dcore-ogl.so in some directory, and set my LD_LIBRARY_PATH environment variable to point to that directory before starting Sage, then the command-line java3d code works.",
    "created_at": "2007-12-15T07:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9457",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

If I download `java3d-1_5_1-linux-i586.zip` from the java3d web site, I can unzipit to get (among other things) `j3d-jre.zip`.  Then I can unzip `j3d-jre.zip` to get (among other things) `libj3dcore-ogl.so`.

If I put libj3dcore-ogl.so in some directory, and set my LD_LIBRARY_PATH environment variable to point to that directory before starting Sage, then the command-line java3d code works.



---

archive/issue_comments_009458.json:
```json
{
    "body": "Gluegen is supposed to take care of all of that (for applets it does) but maybe there's a way to rig it for apps too.",
    "created_at": "2007-12-15T07:45:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9458",
    "user": "https://github.com/robertwb"
}
```

Gluegen is supposed to take care of all of that (for applets it does) but maybe there's a way to rig it for apps too.



---

archive/issue_events_001624.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T09:56:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1473#event-1624"
}
```



---

archive/issue_comments_009459.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T09:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9459",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_009460.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T09:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9460",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
