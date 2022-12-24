# Issue 279: Add test a range of revisions

archive/issues_000279.json:
```json
{
    "body": "Assignee: was\n\nKeywords: test hg mercurial\n\nI often want to test only files touched by a range of revisions.  It would be nice if there was a 'test revisions' command, so sage -tr branch:tip, sage -tr 1023, etc queried hg for changes and only tested those files.\n\nIssue created by migration from https://trac.sagemath.org/ticket/279\n\n",
    "created_at": "2007-02-22T23:57:12Z",
    "labels": [
        "user interface",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.2",
    "title": "Add test a range of revisions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/279",
    "user": "ncalexan"
}
```
Assignee: was

Keywords: test hg mercurial

I often want to test only files touched by a range of revisions.  It would be nice if there was a 'test revisions' command, so sage -tr branch:tip, sage -tr 1023, etc queried hg for changes and only tested those files.

Issue created by migration from https://trac.sagemath.org/ticket/279





---

archive/issue_comments_001328.json:
```json
{
    "body": "Changeset 0e2d1b3b9389 changes sage -tnew rev to support this.\n\n\n```\n# By default, we compare to tip.  However, it is handy to compare against\n# a certain revision, perhaps tagged 2.2 or similar:\n#\n# EXAMPLES:\n#\n# Find things modified but not committed:\n# % sage -tnew tip\n#\n# Find things modified since 2.2:\n# % sage -tnew 2.2\n#\n# Find things modified between 2.1 and 2.2:\n# % sage -tnew 2.1:2.2\n```\n",
    "created_at": "2007-02-25T08:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/279#issuecomment-1328",
    "user": "ncalexan"
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

archive/issue_comments_001329.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-02-25T08:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/279#issuecomment-1329",
    "user": "ncalexan"
}
```

Resolution: fixed



---

archive/issue_comments_001330.json:
```json
{
    "body": "Attachment [ncalexan-scripts-tnew.hg](tarball://root/attachments/some-uuid/ticket279/ncalexan-scripts-tnew.hg) by was created at 2007-02-25 16:08:02",
    "created_at": "2007-02-25T16:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/279#issuecomment-1330",
    "user": "was"
}
```

Attachment [ncalexan-scripts-tnew.hg](tarball://root/attachments/some-uuid/ticket279/ncalexan-scripts-tnew.hg) by was created at 2007-02-25 16:08:02
