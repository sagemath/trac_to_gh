# Issue 6013: rewrite number field relativize to be much faster

archive/issues_006013.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  was craigcitro\n\nKeywords: number field relativize speed\n\nPatch says it best.  Avoid an nfinit at all costs; allows to relativize over large number fields.\n\nThis also fixes longstanding degree one relativize bugs.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6013\n\n",
    "created_at": "2009-05-10T07:59:13Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "rewrite number field relativize to be much faster",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6013",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  was craigcitro

Keywords: number field relativize speed

Patch says it best.  Avoid an nfinit at all costs; allows to relativize over large number fields.

This also fixes longstanding degree one relativize bugs.

Issue created by migration from https://trac.sagemath.org/ticket/6013





---

archive/issue_comments_047757.json:
```json
{
    "body": "Attachment [trac_6013-relativize.patch](tarball://root/attachments/some-uuid/ticket6013/trac_6013-relativize.patch) by @ncalexan created at 2009-05-10 08:12:41\n\nThe patch is good, but I accidentally cut it from my symbolics branch.  Not really a problem, but I mangled mq so the hg changeset info is wacky.  Maybe best to use mq to review this, so the actual hg parent, etc, is not taken into account.",
    "created_at": "2009-05-10T08:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6013#issuecomment-47757",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_6013-relativize.patch](tarball://root/attachments/some-uuid/ticket6013/trac_6013-relativize.patch) by @ncalexan created at 2009-05-10 08:12:41

The patch is good, but I accidentally cut it from my symbolics branch.  Not really a problem, but I mangled mq so the hg changeset info is wacky.  Maybe best to use mq to review this, so the actual hg parent, etc, is not taken into account.



---

archive/issue_events_006268.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-12T05:52:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6013",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6013#event-6268"
}
```



---

archive/issue_comments_047758.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T05:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6013#issuecomment-47758",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_047759.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-12T05:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6013#issuecomment-47759",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
