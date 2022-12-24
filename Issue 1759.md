# Issue 1759: Various files still mention GPL V2 [only]

archive/issues_001759.json:
```json
{
    "body": "Assignee: was\n\nThe following files mention/are under GPL V2 implying V2 only:\n\n* c_lib/src/mpn_pylong.c: License: GPL v2\n* c_lib/src/mpz_pylong.c: License: GPL v2\n* sage/misc/banner.py\n\nThis ought to be fixed before 2.10 since we will merge GPL V3 or later packages. IIRC all the copyright holders agreed to GPL V2 or later, but we should be careful with this and double check.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1759\n\n",
    "created_at": "2008-01-11T19:54:35Z",
    "labels": [
        "distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "Various files still mention GPL V2 [only]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1759",
    "user": "mabshoff"
}
```
Assignee: was

The following files mention/are under GPL V2 implying V2 only:

* c_lib/src/mpn_pylong.c: License: GPL v2
* c_lib/src/mpz_pylong.c: License: GPL v2
* sage/misc/banner.py

This ought to be fixed before 2.10 since we will merge GPL V3 or later packages. IIRC all the copyright holders agreed to GPL V2 or later, but we should be careful with this and double check.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1759





---

archive/issue_comments_011096.json:
```json
{
    "body": "Gonzalo Tornaria whose copyright is at the top of those files *definitely* agreed to GPL \"V2 or later\".  So we're good.\n\nWilliam",
    "created_at": "2008-01-11T20:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1759#issuecomment-11096",
    "user": "was"
}
```

Gonzalo Tornaria whose copyright is at the top of those files *definitely* agreed to GPL "V2 or later".  So we're good.

William



---

archive/issue_comments_011097.json:
```json
{
    "body": "See toward the end of\n\nhttps://groups.google.com/group/sage-devel/browse_thread/thread/2fac21e76cbcbfa3/21068f934515e4e9\n\nfor Gonzalo's statements.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-15T04:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1759#issuecomment-11097",
    "user": "mabshoff"
}
```

See toward the end of

https://groups.google.com/group/sage-devel/browse_thread/thread/2fac21e76cbcbfa3/21068f934515e4e9

for Gonzalo's statements.

Cheers,

Michael



---

archive/issue_comments_011098.json:
```json
{
    "body": "Attachment [Sage-2.10.alpha3-update-license.patch](tarball://root/attachments/some-uuid/ticket1759/Sage-2.10.alpha3-update-license.patch) by mabshoff created at 2008-01-15 04:09:13",
    "created_at": "2008-01-15T04:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1759#issuecomment-11098",
    "user": "mabshoff"
}
```

Attachment [Sage-2.10.alpha3-update-license.patch](tarball://root/attachments/some-uuid/ticket1759/Sage-2.10.alpha3-update-license.patch) by mabshoff created at 2008-01-15 04:09:13



---

archive/issue_comments_011099.json:
```json
{
    "body": "I have applied the patch to Sage 2.10.alpha3 due to the following statement from the last post in the thread linked above:\n\n```\n> Wait, are you saying that you would not allow your code to be re-licensed\n> \"GPL v2 or later\" for Sage?   Or, are you just saying you don't like it,\n> but you would do it.\n\nAt this time I'm just saying that I don't like it. \n```\n\n\nI have also send an email to Gonzalo asking for explicit confirmation - but I do not think that the above line could be misinterpreted to mean anything but an agreement to relicense under \"GPL v2 or later\". \n\nCheers,\n\nMichael",
    "created_at": "2008-01-15T04:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1759#issuecomment-11099",
    "user": "mabshoff"
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

archive/issue_comments_011100.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-15T04:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1759#issuecomment-11100",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011101.json:
```json
{
    "body": "For the record, I agree to the relicensing under \"GPL v2 or later\". Please apply the patch suggested by mabshoff on my behalf.",
    "created_at": "2008-01-15T05:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1759#issuecomment-11101",
    "user": "tornaria"
}
```

For the record, I agree to the relicensing under "GPL v2 or later". Please apply the patch suggested by mabshoff on my behalf.
