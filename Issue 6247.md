# Issue 6247: sage -optional tries to write to SAGE_ROOT

archive/issues_006247.json:
```json
{
    "body": "Assignee: cwitty\n\nReported by `somos` on `#sage-devel` on IRC\n\n\n```\n<somos> when I do 'sage -optional' it tried to make a temp file in SAGE_ROOT\n...\n<somos> This is ok if you are running as root user.\n...\n<mvngu> From the help:\n<mvngu> -optional     -- list all optional packages that can be downloaded\n<somos> Anyway, the problem is the temp file in SAGE_ROOT.\n<somos> It should be in /tmp instead.\n<mvngu> Can you explain why it should be in /tmp ?\n<somos> Becuase SAGE_ROOT requires root permissions.\n...\n<somos> So, my suggestion is to avoid the temp file. #1\n<somos> If a temp file is needed, I suggest TMP or TMPDIR instead.\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6247\n\n",
    "created_at": "2009-06-08T14:37:40Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage -optional tries to write to SAGE_ROOT",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6247",
    "user": "https://github.com/burcin"
}
```
Assignee: cwitty

Reported by `somos` on `#sage-devel` on IRC


```
<somos> when I do 'sage -optional' it tried to make a temp file in SAGE_ROOT
...
<somos> This is ok if you are running as root user.
...
<mvngu> From the help:
<mvngu> -optional     -- list all optional packages that can be downloaded
<somos> Anyway, the problem is the temp file in SAGE_ROOT.
<somos> It should be in /tmp instead.
<mvngu> Can you explain why it should be in /tmp ?
<somos> Becuase SAGE_ROOT requires root permissions.
...
<somos> So, my suggestion is to avoid the temp file. #1
<somos> If a temp file is needed, I suggest TMP or TMPDIR instead.
```



Issue created by migration from https://trac.sagemath.org/ticket/6247





---

archive/issue_comments_049803.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-13T15:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6247#issuecomment-49803",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_049804.json:
```json
{
    "body": "Duplicate of #12018.",
    "created_at": "2013-08-13T15:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6247#issuecomment-49804",
    "user": "https://github.com/jdemeyer"
}
```

Duplicate of #12018.



---

archive/issue_comments_049805.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-08-13T15:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6247#issuecomment-49805",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_049806.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-08-16T11:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6247#issuecomment-49806",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_comments_049807.json:
```json
{
    "body": "Resolution changed from worksforme to duplicate",
    "created_at": "2013-08-16T11:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6247#issuecomment-49807",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from worksforme to duplicate
