# Issue 5161: [with patch, needs review] Remove outdated SHAREDFLAGS and Solaris specific injected flags from sage-env

archive/issues_005161.json:
```json
{
    "body": "Assignee: mabshoff\n\nsage-env sets a bunch of environment variables like SHAREFLAGS that cause trouble on Cygwin and Solaris and are also pretty outdated. Setting global flags should be handled in a cleaner matter in case they are required, so for now remove the code from sage-env. It does break previously working setups and has cost me considerable time to work around before I discovered that the problem was introduced by sage-env.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5161\n\n",
    "created_at": "2009-02-02T19:59:15Z",
    "labels": [
        "component: distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] Remove outdated SHAREDFLAGS and Solaris specific injected flags from sage-env",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5161",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

sage-env sets a bunch of environment variables like SHAREFLAGS that cause trouble on Cygwin and Solaris and are also pretty outdated. Setting global flags should be handled in a cleaner matter in case they are required, so for now remove the code from sage-env. It does break previously working setups and has cost me considerable time to work around before I discovered that the problem was introduced by sage-env.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5161





---

archive/issue_comments_039484.json:
```json
{
    "body": "Attachment [trac_5161.patch](tarball://root/attachments/some-uuid/ticket5161/trac_5161.patch) by @mwhansen created at 2009-02-03 01:00:39\n\nLooks good to me.",
    "created_at": "2009-02-03T01:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5161#issuecomment-39484",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5161.patch](tarball://root/attachments/some-uuid/ticket5161/trac_5161.patch) by @mwhansen created at 2009-02-03 01:00:39

Looks good to me.



---

archive/issue_comments_039485.json:
```json
{
    "body": "Merged in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T01:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5161#issuecomment-39485",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha4.

Cheers,

Michael



---

archive/issue_comments_039486.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-03T01:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5161#issuecomment-39486",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
