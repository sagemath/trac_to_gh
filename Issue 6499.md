# Issue 6499: minor formatting and typo in the script sage-location

archive/issues_006499.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: sage-location\n\nTake a binary distribution of Sage, uncompress it, and start up Sage for the first time. You should see something similar to the following in your terminal:\n\n```\n[mvngu@sage sage-4.1.rc1-x86_64-Linux]$ ./sage \n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThe SAGE install tree may have moved.\nRegenerating Python.pyo and .pyc files that hardcode the install PATH (please wait at\nmost a few minutes)...\nDo not interrupt this.\n```\n\nThe message line starting with \"Regenerating Python.pyo...\" overflows the standard terminal width, which is 80 characters. And the name \"SAGE\" should be changed to \"Sage\". This is no big deal, I know, but it occasional annoys me, especially the said long message line.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6499\n\n",
    "created_at": "2009-07-09T11:26:43Z",
    "labels": [
        "misc",
        "trivial",
        "bug"
    ],
    "title": "minor formatting and typo in the script sage-location",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6499",
    "user": "mvngu"
}
```
Assignee: cwitty

Keywords: sage-location

Take a binary distribution of Sage, uncompress it, and start up Sage for the first time. You should see something similar to the following in your terminal:

```
[mvngu@sage sage-4.1.rc1-x86_64-Linux]$ ./sage 
----------------------------------------------------------------------
----------------------------------------------------------------------
The SAGE install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH (please wait at
most a few minutes)...
Do not interrupt this.
```

The message line starting with "Regenerating Python.pyo..." overflows the standard terminal width, which is 80 characters. And the name "SAGE" should be changed to "Sage". This is no big deal, I know, but it occasional annoys me, especially the said long message line.

Issue created by migration from https://trac.sagemath.org/ticket/6499





---

archive/issue_comments_052864.json:
```json
{
    "body": "Attachment [trac_6499.patch](tarball://root/attachments/some-uuid/ticket6499/trac_6499.patch) by mvngu created at 2009-07-09 11:46:03\n\nbased on Sage 4.1.rc1",
    "created_at": "2009-07-09T11:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6499#issuecomment-52864",
    "user": "mvngu"
}
```

Attachment [trac_6499.patch](tarball://root/attachments/some-uuid/ticket6499/trac_6499.patch) by mvngu created at 2009-07-09 11:46:03

based on Sage 4.1.rc1



---

archive/issue_comments_052865.json:
```json
{
    "body": "After applying the patch `trac_6499.patch`, you should get something like the following:\n\n```\n[mvngu@sage sage-4.1.rc1-x86_64]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThe Sage install tree may have moved.\nRegenerating Python.pyo and .pyc files that hardcode the install PATH\n(please wait at most a few minutes)...\nDo not interrupt this.\n```\n",
    "created_at": "2009-07-09T11:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6499#issuecomment-52865",
    "user": "mvngu"
}
```

After applying the patch `trac_6499.patch`, you should get something like the following:

```
[mvngu@sage sage-4.1.rc1-x86_64]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
The Sage install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH
(please wait at most a few minutes)...
Do not interrupt this.
```




---

archive/issue_comments_052866.json:
```json
{
    "body": "Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(",
    "created_at": "2009-07-16T14:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6499#issuecomment-52866",
    "user": "mvngu"
}
```

Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(



---

archive/issue_comments_052867.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-16T21:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6499",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6499#issuecomment-52867",
    "user": "mvngu"
}
```

Resolution: fixed
