# Issue 3629: givaro-3.2.11 installs its own libgmpxx.{so,a}

archive/issues_003629.json:
```json
{
    "body": "Assignee: @ClementPernet\n\nThe title says it all. No ideas on how to fix it apart touching\nthe install phase.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3629\n\n",
    "created_at": "2008-07-10T04:37:50Z",
    "labels": [
        "component: finite rings",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "givaro-3.2.11 installs its own libgmpxx.{so,a}",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3629",
    "user": "https://github.com/kiwifb"
}
```
Assignee: @ClementPernet

The title says it all. No ideas on how to fix it apart touching
the install phase.

Issue created by migration from https://trac.sagemath.org/ticket/3629





---

archive/issue_comments_025627.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-07-10T04:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3629#issuecomment-25627",
    "user": "https://github.com/kiwifb"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_025628.json:
```json
{
    "body": "This issue has been fixed by jgdumas in the upstream cvs repo and he released a 3.2.12rc0 version including this fix:\n[http://ljk.imag.fr/membres/Jean-Guillaume.Dumas/Softwares/givaro-www/givaro-3.2.12rc0.tar.gz](http://ljk.imag.fr/membres/Jean-Guillaume.Dumas/Softwares/givaro-www/givaro-3.2.12rc0.tar.gz)\n\nI upgraded the givaro spkg to the 3.2.12rc0 version:\n[http://sage.math.washington.edu/home/pernet/givaro-3.2.12rc0.spkg](http://sage.math.washington.edu/home/pernet/givaro-3.2.12rc0.spkg)",
    "created_at": "2008-07-10T18:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3629#issuecomment-25628",
    "user": "https://github.com/ClementPernet"
}
```

This issue has been fixed by jgdumas in the upstream cvs repo and he released a 3.2.12rc0 version including this fix:
[http://ljk.imag.fr/membres/Jean-Guillaume.Dumas/Softwares/givaro-www/givaro-3.2.12rc0.tar.gz](http://ljk.imag.fr/membres/Jean-Guillaume.Dumas/Softwares/givaro-www/givaro-3.2.12rc0.tar.gz)

I upgraded the givaro spkg to the 3.2.12rc0 version:
[http://sage.math.washington.edu/home/pernet/givaro-3.2.12rc0.spkg](http://sage.math.washington.edu/home/pernet/givaro-3.2.12rc0.spkg)



---

archive/issue_comments_025629.json:
```json
{
    "body": "Positive review. The spkg no longer attempts to install the offending library.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-16T04:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3629#issuecomment-25629",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. The spkg no longer attempts to install the offending library.

Cheers,

Michael



---

archive/issue_comments_025630.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-16T04:04:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3629#issuecomment-25630",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.6.alpha0



---

archive/issue_comments_025631.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-16T04:04:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3629#issuecomment-25631",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008332.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-16T04:04:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3629",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3629#event-8332"
}
```
