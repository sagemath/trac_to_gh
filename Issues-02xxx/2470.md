# Issue 2470: [with patch, positive review] dsage docs in tutorial -- can't tex them

archive/issues_002470.json:
```json
{
    "body": "Assignee: @yqiang\n\nI can't tex tut.tex unless the dsage section is commented out.  Also there is some \"to be written...\" section in there -- this is not appropriate for the tutorial, which is meant to be a very very polished documented. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2470\n\n",
    "closed_at": "2008-03-24T16:54:58Z",
    "created_at": "2008-03-11T07:59:09Z",
    "labels": [
        "component: dsage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, positive review] dsage docs in tutorial -- can't tex them",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2470",
    "user": "https://github.com/williamstein"
}
```
Assignee: @yqiang

I can't tex tut.tex unless the dsage section is commented out.  Also there is some "to be written..." section in there -- this is not appropriate for the tutorial, which is meant to be a very very polished documented. 

Issue created by migration from https://trac.sagemath.org/ticket/2470





---

archive/issue_comments_016692.json:
```json
{
    "body": "Thanks for catching that. I will attempt to fix it and post a patch. Is David Joyner the right person to ask about TeX related questions pertaining to the tutorial? I remember that I had problems putting in indexes.",
    "created_at": "2008-03-11T20:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2470#issuecomment-16692",
    "user": "https://github.com/yqiang"
}
```

Thanks for catching that. I will attempt to fix it and post a patch. Is David Joyner the right person to ask about TeX related questions pertaining to the tutorial? I remember that I had problems putting in indexes.



---

archive/issue_comments_016693.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-11T20:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2470#issuecomment-16693",
    "user": "https://github.com/yqiang"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016694.json:
```json
{
    "body": "Attachment [tut.patch](tarball://root/attachments/some-uuid/ticket2470/tut.patch) by @yqiang created at 2008-03-22 00:00:22",
    "created_at": "2008-03-22T00:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2470#issuecomment-16694",
    "user": "https://github.com/yqiang"
}
```

Attachment [tut.patch](tarball://root/attachments/some-uuid/ticket2470/tut.patch) by @yqiang created at 2008-03-22 00:00:22



---

archive/issue_events_005822.json:
```json
{
    "actor": "https://github.com/yqiang",
    "created_at": "2008-03-22T00:00:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2470",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2470#event-5822"
}
```



---

archive/issue_comments_016695.json:
```json
{
    "body": "Patch looks good to me. Constructs like ``foo'` will likely cause trouble while TeXing, but we can deal with that once we get closer to release. Yi, feel free to post a followup patch to resolve those issues and I will merge it.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-24T16:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2470#issuecomment-16695",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. Constructs like ``foo'` will likely cause trouble while TeXing, but we can deal with that once we get closer to release. Yi, feel free to post a followup patch to resolve those issues and I will merge it.

Cheers,

Michael



---

archive/issue_comments_016696.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-24T16:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2470#issuecomment-16696",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005823.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-24T16:54:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2470",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2470#event-5823"
}
```



---

archive/issue_comments_016697.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-24T16:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2470#issuecomment-16697",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha2
