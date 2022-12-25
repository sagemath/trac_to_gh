# Issue 9319: extend and improve "sage -merge"

archive/issues_009319.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @nexttime\n\nTwo issues and/or suggestions for \"sage -merge\":\n\n- if a ticket (like #9278) *removes* a file from the Sage library, then 'sage -merge' runs 'sage -tp 2 -long' with no argument, and this doesn't succeed.  So we should catch this case and deal with it.\n\n- 'sage -merge' should detect whether each patch file has a properly formatted commit message, and either automatically prepend \"#NUM\" to it, or allow the release manager to edit it, before applying it.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9319\n\n",
    "created_at": "2010-06-23T21:22:54Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "extend and improve \"sage -merge\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9319",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: GeorgSWeber

CC:  @nexttime

Two issues and/or suggestions for "sage -merge":

- if a ticket (like #9278) *removes* a file from the Sage library, then 'sage -merge' runs 'sage -tp 2 -long' with no argument, and this doesn't succeed.  So we should catch this case and deal with it.

- 'sage -merge' should detect whether each patch file has a properly formatted commit message, and either automatically prepend "#NUM" to it, or allow the release manager to edit it, before applying it.


Issue created by migration from https://trac.sagemath.org/ticket/9319





---

archive/issue_comments_087678.json:
```json
{
    "body": "script that checks a patch's metadata; for demonstration purposes",
    "created_at": "2010-07-22T06:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9319#issuecomment-87678",
    "user": "https://github.com/dandrake"
}
```

script that checks a patch's metadata; for demonstration purposes



---

archive/issue_comments_087679.json:
```json
{
    "body": "Attachment [check_patch_metadata.py](tarball://root/attachments/some-uuid/ticket9319/check_patch_metadata.py) by @dandrake created at 2010-07-22 06:08:39\n\nattachment:check_patch_metadata.py is a script that, given a patch file and a ticket number, will check to see that the commit message contains the ticket number in the first line, and if it doesn't, it will prepend \"ticket xxxx:\" to the commit message and save the resulting patch in a a file with \".fixed\" appended. It should be easy to integrate this into sage-apply-ticket.\n\nIt bails if it cannot find a commit message or username in the patch. It issues a warning if it can't find a date, node ID or parent but continues. As a guess, I think \"sage -merge\" should fail if there's no commit message or username, and in the other cases, issue the warning and ask the user if they want to continue.",
    "created_at": "2010-07-22T06:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9319#issuecomment-87679",
    "user": "https://github.com/dandrake"
}
```

Attachment [check_patch_metadata.py](tarball://root/attachments/some-uuid/ticket9319/check_patch_metadata.py) by @dandrake created at 2010-07-22 06:08:39

attachment:check_patch_metadata.py is a script that, given a patch file and a ticket number, will check to see that the commit message contains the ticket number in the first line, and if it doesn't, it will prepend "ticket xxxx:" to the commit message and save the resulting patch in a a file with ".fixed" appended. It should be easy to integrate this into sage-apply-ticket.

It bails if it cannot find a commit message or username in the patch. It issues a warning if it can't find a date, node ID or parent but continues. As a guess, I think "sage -merge" should fail if there's no commit message or username, and in the other cases, issue the warning and ask the user if they want to continue.



---

archive/issue_events_022964.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-19T13:17:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9319",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9319#event-22964"
}
```



---

archive/issue_comments_087680.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-19T13:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9319#issuecomment-87680",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087681.json:
```json
{
    "body": "`sage -merge` is gone (#14417).",
    "created_at": "2013-05-19T13:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9319#issuecomment-87681",
    "user": "https://github.com/jdemeyer"
}
```

`sage -merge` is gone (#14417).



---

archive/issue_comments_087682.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-19T13:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9319#issuecomment-87682",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087683.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-05-21T07:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9319#issuecomment-87683",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid



---

archive/issue_events_022965.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-21T07:22:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9319",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9319#event-22965"
}
```
