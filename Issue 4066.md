# Issue 4066: [with patch, needs review] Sage 3.1.2.alpha3: Solaris build fixes for the Sage library

archive/issues_004066.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @robertwb\n\nThere are two small fixes needed for the Sage library.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4066\n\n",
    "created_at": "2008-09-05T06:42:16Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] Sage 3.1.2.alpha3: Solaris build fixes for the Sage library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4066",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @robertwb

There are two small fixes needed for the Sage library.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4066





---

archive/issue_comments_029286.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-05T06:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4066#issuecomment-29286",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_009283.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-05T06:42:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4066",
    "milestone": "sage-3.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4066#event-9283"
}
```



---

archive/issue_comments_029287.json:
```json
{
    "body": "Oops, this patch is not ready for review since some doctests fail. I will post an updated patch shortly.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-05T07:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4066#issuecomment-29287",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oops, this patch is not ready for review since some doctests fail. I will post an updated patch shortly.

Cheers,

Michael



---

archive/issue_comments_029288.json:
```json
{
    "body": "Attachment [trac_4066_solaris_fixes.patch](tarball://root/attachments/some-uuid/ticket4066/trac_4066_solaris_fixes.patch) by mabshoff created at 2008-09-05 09:49:36\n\nOk, I have attached an updated patch that \n\n* passes -ba\n* builds fine on Solaris, OSX and Linux and passes doctests on OSX and Linux\n\nNote that _[A-Z] are numerical constants on BSD and Solaris and should not be used as variable names.\n\nI am CCing Robert since he was involved in writing that code (I think :))\n\nCheers,\n\nMichael",
    "created_at": "2008-09-05T09:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4066#issuecomment-29288",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4066_solaris_fixes.patch](tarball://root/attachments/some-uuid/ticket4066/trac_4066_solaris_fixes.patch) by mabshoff created at 2008-09-05 09:49:36

Ok, I have attached an updated patch that 

* passes -ba
* builds fine on Solaris, OSX and Linux and passes doctests on OSX and Linux

Note that _[A-Z] are numerical constants on BSD and Solaris and should not be used as variable names.

I am CCing Robert since he was involved in writing that code (I think :))

Cheers,

Michael



---

archive/issue_comments_029289.json:
```json
{
    "body": "It applies cleanly against my alpha3, it builds on my 64-bit Linux box, `sage -t rings` passes which should use this functionality (?)\n\nIt SEGFAULTS with `sage -tp 2 sage/rings` in bernouli_mod_p.pyx though. If that can't be reproduced it might just be a weird combination of patches on my machine.",
    "created_at": "2008-09-05T12:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4066#issuecomment-29289",
    "user": "https://github.com/malb"
}
```

It applies cleanly against my alpha3, it builds on my 64-bit Linux box, `sage -t rings` passes which should use this functionality (?)

It SEGFAULTS with `sage -tp 2 sage/rings` in bernouli_mod_p.pyx though. If that can't be reproduced it might just be a weird combination of patches on my machine.



---

archive/issue_events_009284.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-05T16:59:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4066",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4066#event-9284"
}
```



---

archive/issue_comments_029290.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-05T16:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4066#issuecomment-29290",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029291.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0",
    "created_at": "2008-09-05T16:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4066#issuecomment-29291",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc0
