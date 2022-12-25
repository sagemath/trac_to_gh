# Issue 4378: [with patch, positive review] 3.2.alpha1: -sdist does not copy html from template directory

archive/issues_004378.json:
```json
{
    "body": "Assignee: mabshoff\n\n-sdist needs to copy the new html files in the template directory. Otherwise Sage does not start up and all the tests fail on \"make check\"\n\nThese html files need to be added to MANIFEST.in\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4378\n\n",
    "closed_at": "2008-10-31T23:47:46Z",
    "created_at": "2008-10-28T18:31:17Z",
    "labels": [
        "component: distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, positive review] 3.2.alpha1: -sdist does not copy html from template directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4378",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

-sdist needs to copy the new html files in the template directory. Otherwise Sage does not start up and all the tests fail on "make check"

These html files need to be added to MANIFEST.in

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4378





---

archive/issue_comments_032149.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-28T18:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4378#issuecomment-32149",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032150.json:
```json
{
    "body": "With the html files added to MANIFEST.in the repo does not lack any files:\n\n```\ndist/sage-3.2.alpha2/spkg/standard/sage-3.2.alpha2$ hg stat\ndist/sage-3.2.alpha2/spkg/standard/sage-3.2.alpha2$ \n```\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T23:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4378#issuecomment-32150",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With the html files added to MANIFEST.in the repo does not lack any files:

```
dist/sage-3.2.alpha2/spkg/standard/sage-3.2.alpha2$ hg stat
dist/sage-3.2.alpha2/spkg/standard/sage-3.2.alpha2$ 
```

Cheers,

Michael



---

archive/issue_comments_032151.json:
```json
{
    "body": "Attachment [trac_4378.patch](tarball://root/attachments/some-uuid/ticket4378/trac_4378.patch) by @mwhansen created at 2008-10-31 23:41:00\n\nLooks good.",
    "created_at": "2008-10-31T23:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4378#issuecomment-32151",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4378.patch](tarball://root/attachments/some-uuid/ticket4378/trac_4378.patch) by @mwhansen created at 2008-10-31 23:41:00

Looks good.



---

archive/issue_events_009898.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T23:47:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4378",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4378#event-9898"
}
```



---

archive/issue_comments_032152.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T23:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4378#issuecomment-32152",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032153.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T23:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4378#issuecomment-32153",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha2
