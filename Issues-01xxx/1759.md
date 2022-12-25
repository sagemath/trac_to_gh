# Issue 1759: [with patch, positive review] Various files still mention GPL V2 [only]

archive/issues_001759.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following files mention/are under GPL V2 implying V2 only:\n\n* c_lib/src/mpn_pylong.c: License: GPL v2\n* c_lib/src/mpz_pylong.c: License: GPL v2\n* sage/misc/banner.py\n\nThis ought to be fixed before 2.10 since we will merge GPL V3 or later packages. IIRC all the copyright holders agreed to GPL V2 or later, but we should be careful with this and double check.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1759\n\n",
    "closed_at": "2008-01-15T04:19:43Z",
    "created_at": "2008-01-11T19:54:35Z",
    "labels": [
        "component: distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "[with patch, positive review] Various files still mention GPL V2 [only]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1759",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

The following files mention/are under GPL V2 implying V2 only:

* c_lib/src/mpn_pylong.c: License: GPL v2
* c_lib/src/mpz_pylong.c: License: GPL v2
* sage/misc/banner.py

This ought to be fixed before 2.10 since we will merge GPL V3 or later packages. IIRC all the copyright holders agreed to GPL V2 or later, but we should be careful with this and double check.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1759





---

archive/issue_comments_011069.json:
```json
{
    "body": "Gonzalo Tornaria whose copyright is at the top of those files *definitely* agreed to GPL \"V2 or later\".  So we're good.\n\nWilliam",
    "created_at": "2008-01-11T20:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1759#issuecomment-11069",
    "user": "https://github.com/williamstein"
}
```

Gonzalo Tornaria whose copyright is at the top of those files *definitely* agreed to GPL "V2 or later".  So we're good.

William



---

archive/issue_comments_011070.json:
```json
{
    "body": "See toward the end of\n\nhttps://groups.google.com/group/sage-devel/browse_thread/thread/2fac21e76cbcbfa3/21068f934515e4e9\n\nfor Gonzalo's statements.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-15T04:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1759#issuecomment-11070",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

See toward the end of

https://groups.google.com/group/sage-devel/browse_thread/thread/2fac21e76cbcbfa3/21068f934515e4e9

for Gonzalo's statements.

Cheers,

Michael



---

archive/issue_comments_011071.json:
```json
{
    "body": "Attachment [Sage-2.10.alpha3-update-license.patch](tarball://root/attachments/some-uuid/ticket1759/Sage-2.10.alpha3-update-license.patch) by mabshoff created at 2008-01-15 04:09:13",
    "created_at": "2008-01-15T04:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1759#issuecomment-11071",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.10.alpha3-update-license.patch](tarball://root/attachments/some-uuid/ticket1759/Sage-2.10.alpha3-update-license.patch) by mabshoff created at 2008-01-15 04:09:13



---

archive/issue_comments_011072.json:
```json
{
    "body": "I have applied the patch to Sage 2.10.alpha3 due to the following statement from the last post in the thread linked above:\n\n```\n> Wait, are you saying that you would not allow your code to be re-licensed\n> \"GPL v2 or later\" for Sage?   Or, are you just saying you don't like it,\n> but you would do it.\n\nAt this time I'm just saying that I don't like it. \n```\n\nI have also send an email to Gonzalo asking for explicit confirmation - but I do not think that the above line could be misinterpreted to mean anything but an agreement to relicense under \"GPL v2 or later\". \n\nCheers,\n\nMichael",
    "created_at": "2008-01-15T04:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1759#issuecomment-11072",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I have applied the patch to Sage 2.10.alpha3 due to the following statement from the last post in the thread linked above:

```
> Wait, are you saying that you would not allow your code to be re-licensed
> "GPL v2 or later" for Sage?   Or, are you just saying you don't like it,
> but you would do it.

At this time I'm just saying that I don't like it. 
```

I have also send an email to Gonzalo asking for explicit confirmation - but I do not think that the above line could be misinterpreted to mean anything but an agreement to relicense under "GPL v2 or later". 

Cheers,

Michael



---

archive/issue_events_004271.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-15T04:19:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1759",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1759#event-4271"
}
```



---

archive/issue_comments_011073.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-15T04:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1759#issuecomment-11073",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011074.json:
```json
{
    "body": "For the record, I agree to the relicensing under \"GPL v2 or later\". Please apply the patch suggested by mabshoff on my behalf.",
    "created_at": "2008-01-15T05:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1759#issuecomment-11074",
    "user": "https://github.com/tornaria"
}
```

For the record, I agree to the relicensing under "GPL v2 or later". Please apply the patch suggested by mabshoff on my behalf.
