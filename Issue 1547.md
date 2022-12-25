# Issue 1547: Add pre-tuned settings for ATLAS for certain CPUs

archive/issues_001547.json:
```json
{
    "body": "Assignee: mabshoff\n\nWilliam says:\n\n```\nMichael,\n\nCan we add new machines to the ATLAS database of pre-tuned machines?\nI ask, because my Thinkpad laptop -- a Pentium M, is taking literally\nseveral *hours* to build ATLAS, which sucks.\n\nWilliam\n```\n\n\nI will look into this. I am also afraid that compiling ATLAS on PPC/Linux for example will be a rather long, painful experience, so we ought to get on top of this and submit profiles of those CPUs that are missing upstream.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1547\n\n",
    "created_at": "2007-12-17T04:11:09Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Add pre-tuned settings for ATLAS for certain CPUs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1547",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

William says:

```
Michael,

Can we add new machines to the ATLAS database of pre-tuned machines?
I ask, because my Thinkpad laptop -- a Pentium M, is taking literally
several *hours* to build ATLAS, which sucks.

William
```


I will look into this. I am also afraid that compiling ATLAS on PPC/Linux for example will be a rather long, painful experience, so we ought to get on top of this and submit profiles of those CPUs that are missing upstream.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1547





---

archive/issue_comments_009843.json:
```json
{
    "body": "See\n\nhttp://math-atlas.sourceforge.net/devel/atlas_devel/atlas_devel.html#SECTION00070000000000000000\n\nfor details.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-15T20:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1547#issuecomment-9843",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

See

http://math-atlas.sourceforge.net/devel/atlas_devel/atlas_devel.html#SECTION00070000000000000000

for details.

Cheers,

Michael



---

archive/issue_comments_009844.json:
```json
{
    "body": "There is an atlas.spkg with tuning information for Pentium M and Athlon MP added at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc5/atlas-3.8.p11.spkg\n\nSee also #1886.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-02T09:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1547#issuecomment-9844",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There is an atlas.spkg with tuning information for Pentium M and Athlon MP added at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc5/atlas-3.8.p11.spkg

See also #1886.

Cheers,

Michael



---

archive/issue_events_001701.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-02T09:58:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1547",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1547#event-1701"
}
```



---

archive/issue_comments_009845.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-02T09:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1547#issuecomment-9845",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009846.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc5",
    "created_at": "2008-02-02T09:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1547#issuecomment-9846",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc5
