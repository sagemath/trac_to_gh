# Issue 7875: sage -preparse fails

archive/issues_007875.json:
```json
{
    "body": "Assignee: tbd\n\nRunning `sage -preparse somefile.sage` fails with\n\n```\nTraceback (most recent call last):\n  File \"/Users/gvol/vcs/cur-sage/local/bin/sage-preparse\", line 230, in <module>\n    do_preparse(f)\n  File \"/Users/gvol/vcs/cur-sage/local/bin/sage-preparse\", line 119, in do_preparse\n    G = preparse_file(F, magic=False, do_time=True, ignore_prompts=False)\nTypeError: preparse_file() got an unexpected keyword argument 'magic'\n```\n\n\nIt looks like local/bin/sage-preparse wasn't updated to remove magic and ignore_prompts when sage/misc/preparser.py was.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7875\n\n",
    "created_at": "2010-01-09T13:41:58Z",
    "labels": [
        "misc",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "sage -preparse fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7875",
    "user": "@gvol"
}
```
Assignee: tbd

Running `sage -preparse somefile.sage` fails with

```
Traceback (most recent call last):
  File "/Users/gvol/vcs/cur-sage/local/bin/sage-preparse", line 230, in <module>
    do_preparse(f)
  File "/Users/gvol/vcs/cur-sage/local/bin/sage-preparse", line 119, in do_preparse
    G = preparse_file(F, magic=False, do_time=True, ignore_prompts=False)
TypeError: preparse_file() got an unexpected keyword argument 'magic'
```


It looks like local/bin/sage-preparse wasn't updated to remove magic and ignore_prompts when sage/misc/preparser.py was.


Issue created by migration from https://trac.sagemath.org/ticket/7875





---

archive/issue_comments_068415.json:
```json
{
    "body": "Attachment [sage-scripts-7875.patch](tarball://root/attachments/some-uuid/ticket7875/sage-scripts-7875.patch) by @williamstein created at 2010-01-10 22:26:28",
    "created_at": "2010-01-10T22:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7875#issuecomment-68415",
    "user": "@williamstein"
}
```

Attachment [sage-scripts-7875.patch](tarball://root/attachments/some-uuid/ticket7875/sage-scripts-7875.patch) by @williamstein created at 2010-01-10 22:26:28



---

archive/issue_comments_068416.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2010-01-10T22:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7875#issuecomment-68416",
    "user": "@williamstein"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_068417.json:
```json
{
    "body": "This was caused by a change to the preparse_file function.",
    "created_at": "2010-01-10T22:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7875#issuecomment-68417",
    "user": "@williamstein"
}
```

This was caused by a change to the preparse_file function.



---

archive/issue_comments_068418.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-10T22:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7875#issuecomment-68418",
    "user": "@williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068419.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-12T15:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7875#issuecomment-68419",
    "user": "@qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068420.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T04:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7875#issuecomment-68420",
    "user": "@rlmill"
}
```

Resolution: fixed
