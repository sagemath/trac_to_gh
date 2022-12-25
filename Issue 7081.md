# Issue 7081: sage -c "..." runs from the local/bin/ directory.  ugh

archive/issues_007081.json:
```json
{
    "body": "Assignee: cwitty\n\nThis is not good:\n\n\n```\nflat:sagenb wstein$ pwd\n/Users/wstein/sage/nb/sagenb\nflat:sagenb wstein$ sage -c \"print os.path.abspath('.')\"\n/Users/wstein/sage/build/64bit/sage/local/bin\n```\n\n\nIt should be when one runs \"sage -c\" that it runs in the *current* directory.  The actual behavior is very confusing.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7081\n\n",
    "created_at": "2009-09-30T09:10:31Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "sage -c \"...\" runs from the local/bin/ directory.  ugh",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7081",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

This is not good:


```
flat:sagenb wstein$ pwd
/Users/wstein/sage/nb/sagenb
flat:sagenb wstein$ sage -c "print os.path.abspath('.')"
/Users/wstein/sage/build/64bit/sage/local/bin
```


It should be when one runs "sage -c" that it runs in the *current* directory.  The actual behavior is very confusing.

Issue created by migration from https://trac.sagemath.org/ticket/7081





---

archive/issue_comments_058432.json:
```json
{
    "body": "Attachment [trac_7081-chdir-fix.patch](tarball://root/attachments/some-uuid/ticket7081/trac_7081-chdir-fix.patch) by @TimDumol created at 2009-09-30 09:16:43\n\nApply to scripts repo.",
    "created_at": "2009-09-30T09:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7081#issuecomment-58432",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7081-chdir-fix.patch](tarball://root/attachments/some-uuid/ticket7081/trac_7081-chdir-fix.patch) by @TimDumol created at 2009-09-30 09:16:43

Apply to scripts repo.



---

archive/issue_comments_058433.json:
```json
{
    "body": "Editing $SAGE_LOCAL/bin/sage-eval to os.chdir(os.getenv('CUR')) before evalutation fixes the problem.",
    "created_at": "2009-09-30T09:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7081#issuecomment-58433",
    "user": "https://github.com/TimDumol"
}
```

Editing $SAGE_LOCAL/bin/sage-eval to os.chdir(os.getenv('CUR')) before evalutation fixes the problem.



---

archive/issue_events_016748.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-15T08:57:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7081",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7081#event-16748"
}
```



---

archive/issue_comments_058434.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T08:57:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7081#issuecomment-58434",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
