# Issue 6013: rewrite number field relativize to be much faster

archive/issues_006013.json:
```json
{
    "body": "Assignee: was\n\nCC:  was craigcitro\n\nKeywords: number field relativize speed\n\nPatch says it best.  Avoid an nfinit at all costs; allows to relativize over large number fields.\n\nThis also fixes longstanding degree one relativize bugs.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6013\n\n",
    "created_at": "2009-05-10T07:59:13Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "rewrite number field relativize to be much faster",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6013",
    "user": "ncalexan"
}
```
Assignee: was

CC:  was craigcitro

Keywords: number field relativize speed

Patch says it best.  Avoid an nfinit at all costs; allows to relativize over large number fields.

This also fixes longstanding degree one relativize bugs.

Issue created by migration from https://trac.sagemath.org/ticket/6013





---

archive/issue_comments_047848.json:
```json
{
    "body": "Attachment [trac_6013-relativize.patch](tarball://root/attachments/some-uuid/ticket6013/trac_6013-relativize.patch) by ncalexan created at 2009-05-10 08:12:41\n\nThe patch is good, but I accidentally cut it from my symbolics branch.  Not really a problem, but I mangled mq so the hg changeset info is wacky.  Maybe best to use mq to review this, so the actual hg parent, etc, is not taken into account.",
    "created_at": "2009-05-10T08:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6013#issuecomment-47848",
    "user": "ncalexan"
}
```

Attachment [trac_6013-relativize.patch](tarball://root/attachments/some-uuid/ticket6013/trac_6013-relativize.patch) by ncalexan created at 2009-05-10 08:12:41

The patch is good, but I accidentally cut it from my symbolics branch.  Not really a problem, but I mangled mq so the hg changeset info is wacky.  Maybe best to use mq to review this, so the actual hg parent, etc, is not taken into account.



---

archive/issue_comments_047849.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T05:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6013#issuecomment-47849",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_047850.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-12T05:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6013#issuecomment-47850",
    "user": "mabshoff"
}
```

Resolution: fixed
