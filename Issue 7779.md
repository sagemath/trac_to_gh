# Issue 7779: typo in comment of Sage script

archive/issues_007779.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @JohnCremona\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/da735a05781e3945):\n\n```\nAt the end of the script which runs sage there is this:\n\n# This should kill all children of this process too.\n# Uncomment this if you have trouble with orphans.\n# Note that you'll get an annoying \"Killed\" message\n# whenver Sage exists.\n# kill -9 -$$\n\nwhere the last but one line should read\n\n# whenever Sage exits.\n\n(2 typos!)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7779\n\n",
    "closed_at": "2010-01-03T20:45:35Z",
    "created_at": "2009-12-28T15:42:19Z",
    "labels": [
        "component: documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "typo in comment of Sage script",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7779",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  @JohnCremona

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/da735a05781e3945):

```
At the end of the script which runs sage there is this:

# This should kill all children of this process too.
# Uncomment this if you have trouble with orphans.
# Note that you'll get an annoying "Killed" message
# whenver Sage exists.
# kill -9 -$$

where the last but one line should read

# whenever Sage exits.

(2 typos!)
```


Issue created by migration from https://trac.sagemath.org/ticket/7779





---

archive/issue_comments_066957.json:
```json
{
    "body": "Attachment [sage](tarball://root/attachments/some-uuid/ticket7779/sage) by mvngu created at 2009-12-28 15:44:16\n\nbased on Sage 4.3",
    "created_at": "2009-12-28T15:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7779#issuecomment-66957",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [sage](tarball://root/attachments/some-uuid/ticket7779/sage) by mvngu created at 2009-12-28 15:44:16

based on Sage 4.3



---

archive/issue_comments_066958.json:
```json
{
    "body": "previous version of sage script",
    "created_at": "2009-12-28T15:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7779#issuecomment-66958",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

previous version of sage script



---

archive/issue_comments_066959.json:
```json
{
    "body": "Attachment [sage.patch](tarball://root/attachments/some-uuid/ticket7779/sage.patch) by mvngu created at 2009-12-28 15:44:57\n\ndifferences between sage.old and sage",
    "created_at": "2009-12-28T15:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7779#issuecomment-66959",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [sage.patch](tarball://root/attachments/some-uuid/ticket7779/sage.patch) by mvngu created at 2009-12-28 15:44:57

differences between sage.old and sage



---

archive/issue_comments_066960.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-28T15:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7779#issuecomment-66960",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066961.json:
```json
{
    "body": "The script `sage` is found under `SAGE_ROOT` so it is not under revision control. I have attached a new script `sage` which fixes the two typos reported above by cremona. The previous version of this script is attached as `sage.old`. And the differences between `sage.old` and `sage` are contained in `sage.patch`. Only the file `sage` needs to be applied; don't apply the patch file.",
    "created_at": "2009-12-28T15:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7779#issuecomment-66961",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The script `sage` is found under `SAGE_ROOT` so it is not under revision control. I have attached a new script `sage` which fixes the two typos reported above by cremona. The previous version of this script is attached as `sage.old`. And the differences between `sage.old` and `sage` are contained in `sage.patch`. Only the file `sage` needs to be applied; don't apply the patch file.



---

archive/issue_comments_066962.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-28T15:51:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7779#issuecomment-66962",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066963.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T20:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7779#issuecomment-66963",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_018606.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-01-03T20:45:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7779",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7779#event-18606"
}
```
