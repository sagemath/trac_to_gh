# Issue 3308: [with patch; needs review] Update sage-sbuildhack to work with new sbuild in Debian

archive/issues_003308.json:
```json
{
    "body": "Assignee: tabbott\n\nOne of the two patches to sbuild that we're using was accepted in Debian upstream sbuild, so we no longer need a big piece of SbuildHack.pm.  The other has not yet been accepted, so we don't get to get rid of SbuildHack.pm entirely yet.\n\nI've attached a patch to sage-sbuildhack and SbuildHack.pm to work with current sbuild.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3308\n\n",
    "created_at": "2008-05-26T05:16:12Z",
    "labels": [
        "debian-package",
        "blocker",
        "enhancement"
    ],
    "title": "[with patch; needs review] Update sage-sbuildhack to work with new sbuild in Debian",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3308",
    "user": "tabbott"
}
```
Assignee: tabbott

One of the two patches to sbuild that we're using was accepted in Debian upstream sbuild, so we no longer need a big piece of SbuildHack.pm.  The other has not yet been accepted, so we don't get to get rid of SbuildHack.pm entirely yet.

I've attached a patch to sage-sbuildhack and SbuildHack.pm to work with current sbuild.

Issue created by migration from https://trac.sagemath.org/ticket/3308





---

archive/issue_comments_022881.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-26T05:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3308#issuecomment-22881",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_022882.json:
```json
{
    "body": "Patch applies cleanly. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-28T06:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3308#issuecomment-22882",
    "user": "mabshoff"
}
```

Patch applies cleanly. Positive review.

Cheers,

Michael



---

archive/issue_comments_022883.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha0",
    "created_at": "2008-05-28T06:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3308#issuecomment-22883",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha0



---

archive/issue_comments_022884.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-28T06:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3308#issuecomment-22884",
    "user": "mabshoff"
}
```

Resolution: fixed
