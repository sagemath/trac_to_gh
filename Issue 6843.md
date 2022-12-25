# Issue 6843: Permission problem when uploading worksheet

archive/issues_006843.json:
```json
{
    "body": "Assignee: boothby\n\nWhen trying to upload a .sws that contains directories with permission 700, the unpacked directories are still 700 and owned by the user running the notebook.\n\nWhen running the notebook with `server_pool=['other_user`@`localhost']`, evaluating the cells then fails with\n\n```\nIOError: [Errno 13] Permission denied:\n'/home/other_user/sage_notebook/worksheets/user/7/code/1.py'\n```\n\nbecause `.../7/code/` is 700.\n\nWhen creating a new worksheet manually this directory is 755 and evaluating cells in that worksheet works properly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6843\n\n",
    "created_at": "2009-08-29T17:21:25Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Permission problem when uploading worksheet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6843",
    "user": "https://github.com/wjp"
}
```
Assignee: boothby

When trying to upload a .sws that contains directories with permission 700, the unpacked directories are still 700 and owned by the user running the notebook.

When running the notebook with `server_pool=['other_user`@`localhost']`, evaluating the cells then fails with

```
IOError: [Errno 13] Permission denied:
'/home/other_user/sage_notebook/worksheets/user/7/code/1.py'
```

because `.../7/code/` is 700.

When creating a new worksheet manually this directory is 755 and evaluating cells in that worksheet works properly.

Issue created by migration from https://trac.sagemath.org/ticket/6843





---

archive/issue_comments_056344.json:
```json
{
    "body": "Attachment [trac6843.sws](tarball://root/attachments/some-uuid/ticket6843/trac6843.sws) by @wjp created at 2009-08-29 17:37:07\n\nsws that shows this problem",
    "created_at": "2009-08-29T17:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6843#issuecomment-56344",
    "user": "https://github.com/wjp"
}
```

Attachment [trac6843.sws](tarball://root/attachments/some-uuid/ticket6843/trac6843.sws) by @wjp created at 2009-08-29 17:37:07

sws that shows this problem



---

archive/issue_comments_056345.json:
```json
{
    "body": "Attachment [trac_6843-sws_permissions.patch](tarball://root/attachments/some-uuid/ticket6843/trac_6843-sws_permissions.patch) by @wjp created at 2009-08-31 16:22:43\n\nI attached a patch that does a `chmod -R go-rwx,+rwX *` on the untarred sws file, to make the unpacked files match the current umask. (Both in the restrictive and permissive directions.)",
    "created_at": "2009-08-31T16:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6843#issuecomment-56345",
    "user": "https://github.com/wjp"
}
```

Attachment [trac_6843-sws_permissions.patch](tarball://root/attachments/some-uuid/ticket6843/trac_6843-sws_permissions.patch) by @wjp created at 2009-08-31 16:22:43

I attached a patch that does a `chmod -R go-rwx,+rwX *` on the untarred sws file, to make the unpacked files match the current umask. (Both in the restrictive and permissive directions.)



---

archive/issue_comments_056346.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-31T12:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6843#issuecomment-56346",
    "user": "https://github.com/gvol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056347.json:
```json
{
    "body": "I think we should use && instead of ; to ensure sure that we don't change the permissions of other files if we can't cd to the directory.",
    "created_at": "2009-10-31T12:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6843#issuecomment-56347",
    "user": "https://github.com/gvol"
}
```

I think we should use && instead of ; to ensure sure that we don't change the permissions of other files if we can't cd to the directory.



---

archive/issue_comments_056348.json:
```json
{
    "body": "If tmp_dir() failed to create a directory we can cd to, tmp_dir would/should already have thrown an exception. If it doesn't, that's a different issue than the one this patch addresses, and should be solved by fixing tmp_dir, in my opinion.",
    "created_at": "2009-10-31T12:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6843#issuecomment-56348",
    "user": "https://github.com/wjp"
}
```

If tmp_dir() failed to create a directory we can cd to, tmp_dir would/should already have thrown an exception. If it doesn't, that's a different issue than the one this patch addresses, and should be solved by fixing tmp_dir, in my opinion.



---

archive/issue_comments_056349.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-31T12:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6843#issuecomment-56349",
    "user": "https://github.com/wjp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056350.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-08T20:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6843#issuecomment-56350",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_056351.json:
```json
{
    "body": "This was fixed in my rewrite of how notebook evaluates code.  In particular \"When creating a new worksheet manually this directory is 755 and evaluating cells in that worksheet works properly.\" isn't an issue since all code gets evaluated in a special /tmp directory that is created by the server and has permissions carefully set.  Moreover, the code in the worksheet storage directory now has all permissions very carefully set using platform independent Python functions.",
    "created_at": "2009-12-08T20:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6843#issuecomment-56351",
    "user": "https://github.com/williamstein"
}
```

This was fixed in my rewrite of how notebook evaluates code.  In particular "When creating a new worksheet manually this directory is 755 and evaluating cells in that worksheet works properly." isn't an issue since all code gets evaluated in a special /tmp directory that is created by the server and has permissions carefully set.  Moreover, the code in the worksheet storage directory now has all permissions very carefully set using platform independent Python functions.



---

archive/issue_events_016108.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-12-08T20:08:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6843",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6843#event-16108"
}
```
