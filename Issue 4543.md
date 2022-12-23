# Issue 4543: sage -sh fails to start

archive/issues_004543.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  craigcitro\n\nWith 3.2.rc1, I get this:\n\n\n```\nburcin@karr ~/sage/sage-3.2.rc1 $ ./sage -sh\n\nStarting subshell with Sage environment variables set.\nBe sure to exit when you are done and do not do anything\nwith other copies of Sage!\n\nbasename: invalid option -- a\nTry `basename --help' for more information.\nExited Sage subshell.\n```\n\n\nOn my system `basename` does not accept a parameter `-a`.\n\n\n```\nburcin@karr ~/sage/sage-3.2.rc1 $ basename --version\nbasename (GNU coreutils) 6.10\nCopyright (C) 2008 Free Software Foundation, Inc.\nLicense GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>\nThis is free software: you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.\n\nWritten by FIXME unknown.\n```\n\n\nThis can be fixed by removing the `-a` parameter on line 375 of the `sage-sage` script.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4543\n\n",
    "created_at": "2008-11-18T08:36:12Z",
    "labels": [
        "misc",
        "blocker",
        "bug"
    ],
    "title": "sage -sh fails to start",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4543",
    "user": "burcin"
}
```
Assignee: burcin

CC:  craigcitro

With 3.2.rc1, I get this:


```
burcin@karr ~/sage/sage-3.2.rc1 $ ./sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

basename: invalid option -- a
Try `basename --help' for more information.
Exited Sage subshell.
```


On my system `basename` does not accept a parameter `-a`.


```
burcin@karr ~/sage/sage-3.2.rc1 $ basename --version
basename (GNU coreutils) 6.10
Copyright (C) 2008 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by FIXME unknown.
```


This can be fixed by removing the `-a` parameter on line 375 of the `sage-sage` script.

Issue created by migration from https://trac.sagemath.org/ticket/4543





---

archive/issue_comments_034032.json:
```json
{
    "body": "Attachment\n\nattachment:trac_4543.patch removes the `-a` parameter from `basename` in the `sage-sage` script. This fixes the problem on my system.",
    "created_at": "2008-11-18T08:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4543#issuecomment-34032",
    "user": "burcin"
}
```

Attachment

attachment:trac_4543.patch removes the `-a` parameter from `basename` in the `sage-sage` script. This fixes the problem on my system.



---

archive/issue_comments_034033.json:
```json
{
    "body": "I don't really know where I got the `-a` argument -- I think I was copying it from somewhere else. Deleting it seems to work fine on my system, too, and I don't see why we'd need it. Positive review.",
    "created_at": "2008-11-18T08:48:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4543#issuecomment-34033",
    "user": "craigcitro"
}
```

I don't really know where I got the `-a` argument -- I think I was copying it from somewhere else. Deleting it seems to work fine on my system, too, and I don't see why we'd need it. Positive review.



---

archive/issue_comments_034034.json:
```json
{
    "body": "Merged in Sage 3.2.rc2",
    "created_at": "2008-11-18T18:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4543#issuecomment-34034",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.rc2



---

archive/issue_comments_034035.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-18T18:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4543#issuecomment-34035",
    "user": "mabshoff"
}
```

Resolution: fixed
