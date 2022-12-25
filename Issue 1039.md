# Issue 1039: [with patch] Dokchitser L-series of number field

archive/issues_001039.json:
```json
{
    "body": "Assignee: @williamstein\n\nwrapper for Dokchitser L-series of a number field, so that one can do the following:\n\n\n```\nsage: K.<a> =NumberField(x^2+x-1)\nsage: L = K.Lseries_dokchitser()\nsage: L(-1)\n0.0333333333333333\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1039\n\n",
    "created_at": "2007-10-31T17:37:07Z",
    "labels": [
        "component: number theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "[with patch] Dokchitser L-series of number field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1039",
    "user": "https://github.com/jbalakrishnan"
}
```
Assignee: @williamstein

wrapper for Dokchitser L-series of a number field, so that one can do the following:


```
sage: K.<a> =NumberField(x^2+x-1)
sage: L = K.Lseries_dokchitser()
sage: L(-1)
0.0333333333333333
```


Issue created by migration from https://trac.sagemath.org/ticket/1039





---

archive/issue_comments_006318.json:
```json
{
    "body": "Attachment [patch.hg](tarball://root/attachments/some-uuid/ticket1039/patch.hg) by @williamstein created at 2007-10-31 17:43:21\n\nI will take a look at this soon.",
    "created_at": "2007-10-31T17:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1039#issuecomment-6318",
    "user": "https://github.com/williamstein"
}
```

Attachment [patch.hg](tarball://root/attachments/some-uuid/ticket1039/patch.hg) by @williamstein created at 2007-10-31 17:43:21

I will take a look at this soon.



---

archive/issue_comments_006319.json:
```json
{
    "body": "Apply this patch instead.",
    "created_at": "2007-11-01T08:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1039#issuecomment-6319",
    "user": "https://github.com/williamstein"
}
```

Apply this patch instead.



---

archive/issue_events_001164.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-11-01T09:27:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1039",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1039#event-1164"
}
```



---

archive/issue_comments_006320.json:
```json
{
    "body": "Attachment [trac1039.patch](tarball://root/attachments/some-uuid/ticket1039/trac1039.patch) by mabshoff created at 2007-11-01 09:27:01\n\napplied to 2.8.11.alpha0",
    "created_at": "2007-11-01T09:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1039#issuecomment-6320",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac1039.patch](tarball://root/attachments/some-uuid/ticket1039/trac1039.patch) by mabshoff created at 2007-11-01 09:27:01

applied to 2.8.11.alpha0



---

archive/issue_comments_006321.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T09:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1039#issuecomment-6321",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
