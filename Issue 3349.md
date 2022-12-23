# Issue 3349: OSX: make sure LDFLAGS are set for linking purposes

archive/issues_003349.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn OSX it seems that using DYLD_LIBRARY_PATH on OSX is not equivalent to using LD_LIBRARY_PATH on Linux for example since there the linker takes that into consideration as a last resort when not finding libraries. I tried to figure out if there is some magic mode for the OSX ld to consider DYLD_LIBRARY_PATH, but I couldn't find anything. Either way, I can systematically fix those issues, but it will take some time to get this right and tested since this appears to be an OSX specific issue. \n\nThis is somewhat of a META ticket and will take some time to fix.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3349\n\n",
    "created_at": "2008-06-02T00:44:24Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "OSX: make sure LDFLAGS are set for linking purposes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3349",
    "user": "mabshoff"
}
```
Assignee: mabshoff

On OSX it seems that using DYLD_LIBRARY_PATH on OSX is not equivalent to using LD_LIBRARY_PATH on Linux for example since there the linker takes that into consideration as a last resort when not finding libraries. I tried to figure out if there is some magic mode for the OSX ld to consider DYLD_LIBRARY_PATH, but I couldn't find anything. Either way, I can systematically fix those issues, but it will take some time to get this right and tested since this appears to be an OSX specific issue. 

This is somewhat of a META ticket and will take some time to fix.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3349





---

archive/issue_comments_023281.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-02T00:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3349#issuecomment-23281",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023282.json:
```json
{
    "body": "This ticket is very vague, and we have been dealing with these issues on a per-spkg basis, I think - not to mention that it has gotten no comments in four years.  I'm recommending to close this, though the release manager could have another view.",
    "created_at": "2012-06-01T17:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3349#issuecomment-23282",
    "user": "kcrisman"
}
```

This ticket is very vague, and we have been dealing with these issues on a per-spkg basis, I think - not to mention that it has gotten no comments in four years.  I'm recommending to close this, though the release manager could have another view.



---

archive/issue_comments_023283.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-01T17:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3349#issuecomment-23283",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_023284.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-01T17:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3349#issuecomment-23284",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_023285.json:
```json
{
    "body": "Sage is building perfectly fine now on a lot of OS X machines.  The ticket doesn't mention any *concrete* instance of the issue.",
    "created_at": "2012-06-02T12:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3349#issuecomment-23285",
    "user": "jdemeyer"
}
```

Sage is building perfectly fine now on a lot of OS X machines.  The ticket doesn't mention any *concrete* instance of the issue.



---

archive/issue_comments_023286.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-06-02T12:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3349#issuecomment-23286",
    "user": "jdemeyer"
}
```

Resolution: invalid
