# Issue 3349: OSX: make sure LDFLAGS are set for linking purposes

archive/issues_003349.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn OSX it seems that using DYLD_LIBRARY_PATH on OSX is not equivalent to using LD_LIBRARY_PATH on Linux for example since there the linker takes that into consideration as a last resort when not finding libraries. I tried to figure out if there is some magic mode for the OSX ld to consider DYLD_LIBRARY_PATH, but I couldn't find anything. Either way, I can systematically fix those issues, but it will take some time to get this right and tested since this appears to be an OSX specific issue. \n\nThis is somewhat of a META ticket and will take some time to fix.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3349\n\n",
    "closed_at": "2012-06-02T12:37:26Z",
    "created_at": "2008-06-02T00:44:24Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "OSX: make sure LDFLAGS are set for linking purposes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3349",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

On OSX it seems that using DYLD_LIBRARY_PATH on OSX is not equivalent to using LD_LIBRARY_PATH on Linux for example since there the linker takes that into consideration as a last resort when not finding libraries. I tried to figure out if there is some magic mode for the OSX ld to consider DYLD_LIBRARY_PATH, but I couldn't find anything. Either way, I can systematically fix those issues, but it will take some time to get this right and tested since this appears to be an OSX specific issue. 

This is somewhat of a META ticket and will take some time to fix.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3349





---

archive/issue_comments_023233.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-02T00:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3349#issuecomment-23233",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023234.json:
```json
{
    "body": "This ticket is very vague, and we have been dealing with these issues on a per-spkg basis, I think - not to mention that it has gotten no comments in four years.  I'm recommending to close this, though the release manager could have another view.",
    "created_at": "2012-06-01T17:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3349#issuecomment-23234",
    "user": "https://github.com/kcrisman"
}
```

This ticket is very vague, and we have been dealing with these issues on a per-spkg basis, I think - not to mention that it has gotten no comments in four years.  I'm recommending to close this, though the release manager could have another view.



---

archive/issue_comments_023235.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-01T17:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3349#issuecomment-23235",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_023236.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-01T17:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3349#issuecomment-23236",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007499.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2012-06-01T17:56:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3349",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3349#event-7499"
}
```



---

archive/issue_comments_023237.json:
```json
{
    "body": "Sage is building perfectly fine now on a lot of OS X machines.  The ticket doesn't mention any *concrete* instance of the issue.",
    "created_at": "2012-06-02T12:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3349#issuecomment-23237",
    "user": "https://github.com/jdemeyer"
}
```

Sage is building perfectly fine now on a lot of OS X machines.  The ticket doesn't mention any *concrete* instance of the issue.



---

archive/issue_comments_023238.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-06-02T12:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3349#issuecomment-23238",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid



---

archive/issue_events_007500.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-06-02T12:37:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3349",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3349#event-7500"
}
```
