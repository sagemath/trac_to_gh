# Issue 279: Add test a range of revisions

archive/issues_000279.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: test hg mercurial\n\nI often want to test only files touched by a range of revisions.  It would be nice if there was a 'test revisions' command, so sage -tr branch:tip, sage -tr 1023, etc queried hg for changes and only tested those files.\n\nIssue created by migration from https://trac.sagemath.org/ticket/279\n\n",
    "created_at": "2007-02-22T23:57:12Z",
    "labels": [
        "component: user interface",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.2",
    "title": "Add test a range of revisions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/279",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

Keywords: test hg mercurial

I often want to test only files touched by a range of revisions.  It would be nice if there was a 'test revisions' command, so sage -tr branch:tip, sage -tr 1023, etc queried hg for changes and only tested those files.

Issue created by migration from https://trac.sagemath.org/ticket/279





---

archive/issue_comments_001324.json:
```json
{
    "body": "Changeset 0e2d1b3b9389 changes sage -tnew rev to support this.\n\n```\n# By default, we compare to tip.  However, it is handy to compare against\n# a certain revision, perhaps tagged 2.2 or similar:\n#\n# EXAMPLES:\n#\n# Find things modified but not committed:\n# % sage -tnew tip\n#\n# Find things modified since 2.2:\n# % sage -tnew 2.2\n#\n# Find things modified between 2.1 and 2.2:\n# % sage -tnew 2.1:2.2\n```",
    "created_at": "2007-02-25T08:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/279#issuecomment-1324",
    "user": "https://github.com/ncalexan"
}
```

Changeset 0e2d1b3b9389 changes sage -tnew rev to support this.

```
# By default, we compare to tip.  However, it is handy to compare against
# a certain revision, perhaps tagged 2.2 or similar:
#
# EXAMPLES:
#
# Find things modified but not committed:
# % sage -tnew tip
#
# Find things modified since 2.2:
# % sage -tnew 2.2
#
# Find things modified between 2.1 and 2.2:
# % sage -tnew 2.1:2.2
```



---

archive/issue_comments_001325.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-02-25T08:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/279#issuecomment-1325",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed



---

archive/issue_events_000626.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2007-02-25T08:57:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/279",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/279#event-626"
}
```



---

archive/issue_comments_001326.json:
```json
{
    "body": "Attachment [ncalexan-scripts-tnew.hg](tarball://root/attachments/some-uuid/ticket279/ncalexan-scripts-tnew.hg) by @williamstein created at 2007-02-25 16:08:02",
    "created_at": "2007-02-25T16:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/279#issuecomment-1326",
    "user": "https://github.com/williamstein"
}
```

Attachment [ncalexan-scripts-tnew.hg](tarball://root/attachments/some-uuid/ticket279/ncalexan-scripts-tnew.hg) by @williamstein created at 2007-02-25 16:08:02



---

archive/issue_events_000627.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-02-25T16:08:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/279",
    "milestone": "sage-2.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/279#event-627"
}
```
