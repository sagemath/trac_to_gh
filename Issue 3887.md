# Issue 3887: [with patch, needs review] Bug in determinant

archive/issues_003887.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @ClementPernet\n\nHere's a crazy bug:\n\n\n```\nsage: m = diagonal_matrix(ZZ, 68, [2]*66 + [1,1])\nsage: m.det()\n-73786800370889000442\nsage: m.det(proof=False)\n73786976294838206464\n```\n\n\nAmusingly, the `proof=False` one is correct. Fix is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3887\n\n",
    "created_at": "2008-08-18T10:48:28Z",
    "labels": [
        "component: linear algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] Bug in determinant",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3887",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

CC:  @ClementPernet

Here's a crazy bug:


```
sage: m = diagonal_matrix(ZZ, 68, [2]*66 + [1,1])
sage: m.det()
-73786800370889000442
sage: m.det(proof=False)
73786976294838206464
```


Amusingly, the `proof=False` one is correct. Fix is attached.

Issue created by migration from https://trac.sagemath.org/ticket/3887





---

archive/issue_comments_027675.json:
```json
{
    "body": "Attachment [trac-3887.patch](tarball://root/attachments/some-uuid/ticket3887/trac-3887.patch) by @craigcitro created at 2008-08-18 10:50:03\n\nOops, I forgot to mention: Nils-Peter Skoruppa was the one who reported this.",
    "created_at": "2008-08-18T10:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27675",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-3887.patch](tarball://root/attachments/some-uuid/ticket3887/trac-3887.patch) by @craigcitro created at 2008-08-18 10:50:03

Oops, I forgot to mention: Nils-Peter Skoruppa was the one who reported this.



---

archive/issue_comments_027676.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-18T10:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27676",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_events_008907.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2008-08-18T21:27:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "milestone": "sage-3.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3887#event-8907"
}
```



---

archive/issue_comments_027677.json:
```json
{
    "body": "positive review.  great find!",
    "created_at": "2008-08-23T00:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27677",
    "user": "https://github.com/williamstein"
}
```

positive review.  great find!



---

archive/issue_comments_027678.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-23T00:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27678",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027679.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha0.\n\nCraig: Did Nils find or also fix the bug, i.e. does he get credit?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-23T00:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27679",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha0.

Craig: Did Nils find or also fix the bug, i.e. does he get credit?

Cheers,

Michael



---

archive/issue_events_008908.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-23T00:10:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3887#event-8908"
}
```



---

archive/issue_comments_027680.json:
```json
{
    "body": "What hardware was this on? I'm having trouble reproducing this bug (after reverting your changes) and it immensely slows down hnf and det computations.",
    "created_at": "2008-12-17T23:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27680",
    "user": "https://github.com/robertwb"
}
```

What hardware was this on? I'm having trouble reproducing this bug (after reverting your changes) and it immensely slows down hnf and det computations.



---

archive/issue_comments_027681.json:
```json
{
    "body": "This pops up on my MacBook Pro, and whatever hardware Nils was running on (his linux laptop, not sure beyond that). \n\nI just checked -- reverting this patch gets me the same error:\n\n\n```\nsage: diagonal_matrix(ZZ, 68, [2]*66 + [1,1]).det()\n-73786800370889000442\n```\n\n\nThe bound that gets determined in that function is also wrong -- in this case, the divisor it finds is 2, and the final determinant is 2^66:\n\n\n```\nsage: 2^66\n73786976294838206464\nsage: 2^66 < 10^20\nTrue\nsage: 2^66 < 10^20//2\nFalse\n```\n",
    "created_at": "2008-12-18T00:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27681",
    "user": "https://github.com/craigcitro"
}
```

This pops up on my MacBook Pro, and whatever hardware Nils was running on (his linux laptop, not sure beyond that). 

I just checked -- reverting this patch gets me the same error:


```
sage: diagonal_matrix(ZZ, 68, [2]*66 + [1,1]).det()
-73786800370889000442
```


The bound that gets determined in that function is also wrong -- in this case, the divisor it finds is 2, and the final determinant is 2^66:


```
sage: 2^66
73786976294838206464
sage: 2^66 < 10^20
True
sage: 2^66 < 10^20//2
False
```




---

archive/issue_comments_027682.json:
```json
{
    "body": "Ah, so we just needed an extra factor of 2 in there (as we weren't taking into account the sign). I'm posting a patch.",
    "created_at": "2008-12-18T00:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27682",
    "user": "https://github.com/robertwb"
}
```

Ah, so we just needed an extra factor of 2 in there (as we weren't taking into account the sign). I'm posting a patch.



---

archive/issue_comments_027683.json:
```json
{
    "body": "Attachment [3887-faster-fix.patch](tarball://root/attachments/some-uuid/ticket3887/3887-faster-fix.patch) by @robertwb created at 2008-12-18 00:22:39",
    "created_at": "2008-12-18T00:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27683",
    "user": "https://github.com/robertwb"
}
```

Attachment [3887-faster-fix.patch](tarball://root/attachments/some-uuid/ticket3887/3887-faster-fix.patch) by @robertwb created at 2008-12-18 00:22:39



---

archive/issue_comments_027684.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-12-18T00:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27684",
    "user": "https://github.com/robertwb"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_027685.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-12-18T00:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27685",
    "user": "https://github.com/robertwb"
}
```

Changing status from closed to reopened.



---

archive/issue_events_008909.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2008-12-18T00:22:39Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3887#event-8909"
}
```



---

archive/issue_comments_027686.json:
```json
{
    "body": "I'm going to move this to a new ticket.",
    "created_at": "2008-12-18T00:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27686",
    "user": "https://github.com/robertwb"
}
```

I'm going to move this to a new ticket.



---

archive/issue_comments_027687.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-18T00:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27687",
    "user": "https://github.com/robertwb"
}
```

Resolution: fixed



---

archive/issue_events_008910.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2008-12-18T00:24:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3887#event-8910"
}
```



---

archive/issue_comments_027688.json:
```json
{
    "body": "See #4823",
    "created_at": "2008-12-18T00:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27688",
    "user": "https://github.com/robertwb"
}
```

See #4823
