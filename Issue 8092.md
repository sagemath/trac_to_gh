# Issue 8092: init.sage not attached in worksheets

archive/issues_008092.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein\n\nFrom the main notebook help page:\n\n   The file `$HOME/.sage/init.sage` is attached on startup if it exists.\n\nBut the file is not `attach`ed --- try evaluating `attached_files()`.  This is a follow-up to #7514.\n\nSee [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/856f02edb25e8781#), [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/320d494175d46012).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8092\n\n",
    "created_at": "2010-01-27T10:09:52Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "init.sage not attached in worksheets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8092",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

CC:  @williamstein

From the main notebook help page:

   The file `$HOME/.sage/init.sage` is attached on startup if it exists.

But the file is not `attach`ed --- try evaluating `attached_files()`.  This is a follow-up to #7514.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/856f02edb25e8781#), [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/320d494175d46012).

Issue created by migration from https://trac.sagemath.org/ticket/8092





---

archive/issue_comments_070785.json:
```json
{
    "body": "Attach `DOT_SAGE/init.sage`.  sagenb repo.",
    "created_at": "2010-01-27T13:05:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8092#issuecomment-70785",
    "user": "https://github.com/qed777"
}
```

Attach `DOT_SAGE/init.sage`.  sagenb repo.



---

archive/issue_comments_070786.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-27T13:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8092#issuecomment-70786",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070787.json:
```json
{
    "body": "Attachment [trac_8092-init_sage.patch](tarball://root/attachments/some-uuid/ticket8092/trac_8092-init_sage.patch) by @qed777 created at 2010-01-27 13:09:54\n\nThe attached patch seems to work for me.\u00a0 `DOT_SAGE/init.sage` is equivalent to `os.environ['SAGE_STARTUP_FILE']` (see `SAGE_LOCAL/bin/ipy_profile_sage.py`).",
    "created_at": "2010-01-27T13:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8092#issuecomment-70787",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8092-init_sage.patch](tarball://root/attachments/some-uuid/ticket8092/trac_8092-init_sage.patch) by @qed777 created at 2010-01-27 13:09:54

The attached patch seems to work for me.  `DOT_SAGE/init.sage` is equivalent to `os.environ['SAGE_STARTUP_FILE']` (see `SAGE_LOCAL/bin/ipy_profile_sage.py`).



---

archive/issue_comments_070788.json:
```json
{
    "body": "Oops!\n\n```\nexcept KeyError, IOError:\n```\n\nshould be\n\n```\nexcept (KeyError, IOError):\n```\n\n\nThis is one of those very annoying tricky mistakes people make with Python exceptions...",
    "created_at": "2010-01-27T18:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8092#issuecomment-70788",
    "user": "https://github.com/williamstein"
}
```

Oops!

```
except KeyError, IOError:
```

should be

```
except (KeyError, IOError):
```


This is one of those very annoying tricky mistakes people make with Python exceptions...



---

archive/issue_comments_070789.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-27T18:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8092#issuecomment-70789",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070790.json:
```json
{
    "body": "Attachment [trac_8092-init_sage.2.patch](tarball://root/attachments/some-uuid/ticket8092/trac_8092-init_sage.2.patch) by @qed777 created at 2010-01-28 01:47:57\n\nFixes Oops!  Replaces previous.",
    "created_at": "2010-01-28T01:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8092#issuecomment-70790",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8092-init_sage.2.patch](tarball://root/attachments/some-uuid/ticket8092/trac_8092-init_sage.2.patch) by @qed777 created at 2010-01-28 01:47:57

Fixes Oops!  Replaces previous.



---

archive/issue_comments_070791.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-28T01:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8092#issuecomment-70791",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070792.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-03-19T08:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8092#issuecomment-70792",
    "user": "https://github.com/TimDumol"
}
```

LGTM.



---

archive/issue_comments_070793.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-19T08:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8092#issuecomment-70793",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070794.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-04T04:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8092#issuecomment-70794",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed



---

archive/issue_events_008300.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-05-04T04:44:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8092",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8092#event-8300"
}
```
