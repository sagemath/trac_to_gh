# Issue 5704: [with patch, positive review] Implementation of finding elliptic curves with prescribed reduction over QQ

archive/issues_005704.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: elliptic curve\n\nThis enhancement implements (over QQ only) the algorithm in  \"Finding\nall elliptic curves with good reduction outside a given set of primes\"\nby John Cremona and Mark Lingham, Experimental Mathematics 16 No.3\n(2007), 303-312.\n\nThis is a serious application of the S-integral point functions added last year.  I have a partial Magma implementation over number fields (partial since Magma does not have S-integral points over number fields either), which requires number field functionality not yet in Sage (pSelmer groups), which I know how to do but have not done;  I will put those on a separate ticket.\n\nIt is based on 3.4.1.rc0 + #5673 (2 patches) + #5685 (1 patch).\n\nIssue created by migration from https://trac.sagemath.org/ticket/5704\n\n",
    "closed_at": "2009-04-24T08:34:49Z",
    "created_at": "2009-04-07T09:40:41Z",
    "labels": [
        "component: number theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "[with patch, positive review] Implementation of finding elliptic curves with prescribed reduction over QQ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5704",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

Keywords: elliptic curve

This enhancement implements (over QQ only) the algorithm in  "Finding
all elliptic curves with good reduction outside a given set of primes"
by John Cremona and Mark Lingham, Experimental Mathematics 16 No.3
(2007), 303-312.

This is a serious application of the S-integral point functions added last year.  I have a partial Magma implementation over number fields (partial since Magma does not have S-integral points over number fields either), which requires number field functionality not yet in Sage (pSelmer groups), which I know how to do but have not done;  I will put those on a separate ticket.

It is based on 3.4.1.rc0 + #5673 (2 patches) + #5685 (1 patch).

Issue created by migration from https://trac.sagemath.org/ticket/5704





---

archive/issue_comments_044491.json:
```json
{
    "body": "Attachment [egros.patch](tarball://root/attachments/some-uuid/ticket5704/egros.patch) by @JohnCremona created at 2009-04-07 09:41:04",
    "created_at": "2009-04-07T09:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5704#issuecomment-44491",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [egros.patch](tarball://root/attachments/some-uuid/ticket5704/egros.patch) by @JohnCremona created at 2009-04-07 09:41:04



---

archive/issue_comments_044492.json:
```json
{
    "body": "Merges cleanly with sage-3.4.1.rc3, passes all tests in sage/schemes/elliptic_curves.",
    "created_at": "2009-04-22T14:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5704#issuecomment-44492",
    "user": "https://github.com/rlmill"
}
```

Merges cleanly with sage-3.4.1.rc3, passes all tests in sage/schemes/elliptic_curves.



---

archive/issue_comments_044493.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-24T08:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5704#issuecomment-44493",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_013396.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-24T08:34:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5704",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5704#event-13396"
}
```



---

archive/issue_events_013397.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-24T08:34:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5704",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5704#event-13397"
}
```



---

archive/issue_comments_044494.json:
```json
{
    "body": "Merged in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T08:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5704#issuecomment-44494",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_044495.json:
```json
{
    "body": "Ironically the new file schemes/elliptic_curves/ell_egros.py was not added to the reference manual :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T08:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5704#issuecomment-44495",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ironically the new file schemes/elliptic_curves/ell_egros.py was not added to the reference manual :)

Cheers,

Michael



---

archive/issue_comments_044496.json:
```json
{
    "body": "Replying to [comment:4 mabshoff]:\n> Ironically the new file schemes/elliptic_curves/ell_egros.py was not added to the reference manual :)\n> \n> Cheers,\n> \n> Michael\n\nOK, I will do that!   We're still working on that chapter (Chris Wuthrich is doing some too). John",
    "created_at": "2009-04-24T08:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5704#issuecomment-44496",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:4 mabshoff]:
> Ironically the new file schemes/elliptic_curves/ell_egros.py was not added to the reference manual :)
> 
> Cheers,
> 
> Michael

OK, I will do that!   We're still working on that chapter (Chris Wuthrich is doing some too). John
