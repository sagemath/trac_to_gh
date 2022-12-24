# Issue 1213: strange unused file sage/plot/mpl_wrapper.py should be fixed or deleted

archive/issues_001213.json:
```json
{
    "body": "Assignee: was\n\nI think that mpl_wrapper.py is obsolete, dead code.  Nothing else in Sage refers to it, it talks about an optional matplotlib package (when matplotlib has been standard in Sage for quite a while), and it mentions downloading matplotlib from UCSD.\n\nAlso, in mpl_wrapper.py it mentions the \"sage -mpl\" option.  In sage-sage, it says\n\n```\n    echo \"  -mpl          -- run with matplotlib support (requires optional matplotlib package)\"\n```\n\nbut \"sage -mpl\" does not act obviously different than just \"sage\".  I'm guessing that all the \"-mpl\" stuff should be removed from sage-sage, as well.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1213\n\n",
    "created_at": "2007-11-20T05:16:21Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "title": "strange unused file sage/plot/mpl_wrapper.py should be fixed or deleted",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1213",
    "user": "cwitty"
}
```
Assignee: was

I think that mpl_wrapper.py is obsolete, dead code.  Nothing else in Sage refers to it, it talks about an optional matplotlib package (when matplotlib has been standard in Sage for quite a while), and it mentions downloading matplotlib from UCSD.

Also, in mpl_wrapper.py it mentions the "sage -mpl" option.  In sage-sage, it says

```
    echo "  -mpl          -- run with matplotlib support (requires optional matplotlib package)"
```

but "sage -mpl" does not act obviously different than just "sage".  I'm guessing that all the "-mpl" stuff should be removed from sage-sage, as well.

Issue created by migration from https://trac.sagemath.org/ticket/1213





---

archive/issue_comments_007525.json:
```json
{
    "body": "This is easy enough to do and still a problem with 2.9.1.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-26T02:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1213#issuecomment-7525",
    "user": "mabshoff"
}
```

This is easy enough to do and still a problem with 2.9.1.

Cheers,

Michael



---

archive/issue_comments_007526.json:
```json
{
    "body": "Bug Day 10 material?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T22:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1213#issuecomment-7526",
    "user": "mabshoff"
}
```

Bug Day 10 material?

Cheers,

Michael



---

archive/issue_comments_007527.json:
```json
{
    "body": "We should probably also nuke\n\n```\n-rw-r--r-- 1 mabshoff 1090 16115 2007-12-20 17:13 plot3dsoya.py\n-rw-r--r-- 1 mabshoff 1090  3054 2007-12-20 17:13 plot3dsoya_wrap.py\n```\n\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-05-24T02:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1213#issuecomment-7527",
    "user": "mabshoff"
}
```

We should probably also nuke

```
-rw-r--r-- 1 mabshoff 1090 16115 2007-12-20 17:13 plot3dsoya.py
-rw-r--r-- 1 mabshoff 1090  3054 2007-12-20 17:13 plot3dsoya_wrap.py
```


Thoughts?

Cheers,

Michael



---

archive/issue_comments_007528.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2008-05-24T02:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1213#issuecomment-7528",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_007529.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-24T02:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1213#issuecomment-7529",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007530.json:
```json
{
    "body": "Attachment [nuke_mpl_wrapper.patch](tarball://root/attachments/some-uuid/ticket1213/nuke_mpl_wrapper.patch) by jwmerrill created at 2008-08-31 04:50:34\n\nI tried deleting this file, and all indications are good.  Here's a patch that kills it.",
    "created_at": "2008-08-31T04:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1213#issuecomment-7530",
    "user": "jwmerrill"
}
```

Attachment [nuke_mpl_wrapper.patch](tarball://root/attachments/some-uuid/ticket1213/nuke_mpl_wrapper.patch) by jwmerrill created at 2008-08-31 04:50:34

I tried deleting this file, and all indications are good.  Here's a patch that kills it.



---

archive/issue_comments_007531.json:
```json
{
    "body": "Patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-31T04:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1213#issuecomment-7531",
    "user": "mabshoff"
}
```

Patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_007532.json:
```json
{
    "body": "Attachment [nuke_mpl_cmdline_option.patch](tarball://root/attachments/some-uuid/ticket1213/nuke_mpl_cmdline_option.patch) by jwmerrill created at 2008-08-31 05:09:11",
    "created_at": "2008-08-31T05:09:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1213#issuecomment-7532",
    "user": "jwmerrill"
}
```

Attachment [nuke_mpl_cmdline_option.patch](tarball://root/attachments/some-uuid/ticket1213/nuke_mpl_cmdline_option.patch) by jwmerrill created at 2008-08-31 05:09:11



---

archive/issue_comments_007533.json:
```json
{
    "body": "The new patch also gets rid of the -mpl command line argument, since it doesn't appear to do anything.",
    "created_at": "2008-08-31T05:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1213#issuecomment-7533",
    "user": "jwmerrill"
}
```

The new patch also gets rid of the -mpl command line argument, since it doesn't appear to do anything.



---

archive/issue_comments_007534.json:
```json
{
    "body": "Positive review on the scripts repo patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-31T05:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1213#issuecomment-7534",
    "user": "mabshoff"
}
```

Positive review on the scripts repo patch.

Cheers,

Michael



---

archive/issue_comments_007535.json:
```json
{
    "body": "Merged both patches in Sage 3.1.2.alpha3",
    "created_at": "2008-08-31T05:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1213#issuecomment-7535",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.1.2.alpha3



---

archive/issue_comments_007536.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-31T05:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1213#issuecomment-7536",
    "user": "mabshoff"
}
```

Resolution: fixed
