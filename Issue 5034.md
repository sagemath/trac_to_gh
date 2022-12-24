# Issue 5034: stupid output of sage -br:  "using n cpus"

archive/issues_005034.json:
```json
{
    "body": "Assignee: mabshoff\n\nI just noticed that when we do \"sage -br\" with \"export MAKE='make -j3'\" on a 2-core machine we get:\n\n\n```\nsteragon-2:sage-3.3.alpha0 wstein$ sage -br\n...\nExecute 4 commands (using 3 cpus)\n```\n\n\nNote the \"3 cpus\", which looks really dumb, since I have only 1 cpu in my laptop, and it has 2 cores.  To fix this bug change \"cpus\" to \"threads\".  That's it!\n\nIssue created by migration from https://trac.sagemath.org/ticket/5034\n\n",
    "created_at": "2009-01-20T06:13:23Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "stupid output of sage -br:  \"using n cpus\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5034",
    "user": "@williamstein"
}
```
Assignee: mabshoff

I just noticed that when we do "sage -br" with "export MAKE='make -j3'" on a 2-core machine we get:


```
steragon-2:sage-3.3.alpha0 wstein$ sage -br
...
Execute 4 commands (using 3 cpus)
```


Note the "3 cpus", which looks really dumb, since I have only 1 cpu in my laptop, and it has 2 cores.  To fix this bug change "cpus" to "threads".  That's it!

Issue created by migration from https://trac.sagemath.org/ticket/5034





---

archive/issue_comments_038333.json:
```json
{
    "body": "this is against sage-3.3.alpha0",
    "created_at": "2009-01-20T06:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5034#issuecomment-38333",
    "user": "@williamstein"
}
```

this is against sage-3.3.alpha0



---

archive/issue_comments_038334.json:
```json
{
    "body": "Attachment [trac_5034.patch](tarball://root/attachments/some-uuid/ticket5034/trac_5034.patch) by @williamstein created at 2009-01-20 06:39:25\n\nThe attached patch is just a textual substitution of \"threads\" for \"cpus\".",
    "created_at": "2009-01-20T06:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5034#issuecomment-38334",
    "user": "@williamstein"
}
```

Attachment [trac_5034.patch](tarball://root/attachments/some-uuid/ticket5034/trac_5034.patch) by @williamstein created at 2009-01-20 06:39:25

The attached patch is just a textual substitution of "threads" for "cpus".



---

archive/issue_comments_038335.json:
```json
{
    "body": "Of course, \"threads\" is also technically incorrect; \"processes\" would be more accurate.",
    "created_at": "2009-01-20T23:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5034#issuecomment-38335",
    "user": "cwitty"
}
```

Of course, "threads" is also technically incorrect; "processes" would be more accurate.



---

archive/issue_comments_038336.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T09:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5034#issuecomment-38336",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_comments_038337.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T09:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5034#issuecomment-38337",
    "user": "mabshoff"
}
```

Resolution: fixed
