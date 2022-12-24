# Issue 3887: [with patch, needs review] Bug in determinant

archive/issues_003887.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  cpernet\n\nHere's a crazy bug:\n\n\n```\nsage: m = diagonal_matrix(ZZ, 68, [2]*66 + [1,1])\nsage: m.det()\n-73786800370889000442\nsage: m.det(proof=False)\n73786976294838206464\n```\n\n\nAmusingly, the `proof=False` one is correct. Fix is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3887\n\n",
    "created_at": "2008-08-18T10:48:28Z",
    "labels": [
        "linear algebra",
        "blocker",
        "bug"
    ],
    "title": "[with patch, needs review] Bug in determinant",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3887",
    "user": "craigcitro"
}
```
Assignee: craigcitro

CC:  cpernet

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

archive/issue_comments_027733.json:
```json
{
    "body": "Attachment [trac-3887.patch](tarball://root/attachments/some-uuid/ticket3887/trac-3887.patch) by craigcitro created at 2008-08-18 10:50:03\n\nOops, I forgot to mention: Nils-Peter Skoruppa was the one who reported this.",
    "created_at": "2008-08-18T10:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27733",
    "user": "craigcitro"
}
```

Attachment [trac-3887.patch](tarball://root/attachments/some-uuid/ticket3887/trac-3887.patch) by craigcitro created at 2008-08-18 10:50:03

Oops, I forgot to mention: Nils-Peter Skoruppa was the one who reported this.



---

archive/issue_comments_027734.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-18T10:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27734",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_027735.json:
```json
{
    "body": "positive review.  great find!",
    "created_at": "2008-08-23T00:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27735",
    "user": "was"
}
```

positive review.  great find!



---

archive/issue_comments_027736.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-23T00:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27736",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027737.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha0.\n\nCraig: Did Nils find or also fix the bug, i.e. does he get credit?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-23T00:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27737",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha0.

Craig: Did Nils find or also fix the bug, i.e. does he get credit?

Cheers,

Michael



---

archive/issue_comments_027738.json:
```json
{
    "body": "What hardware was this on? I'm having trouble reproducing this bug (after reverting your changes) and it immensely slows down hnf and det computations.",
    "created_at": "2008-12-17T23:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27738",
    "user": "robertwb"
}
```

What hardware was this on? I'm having trouble reproducing this bug (after reverting your changes) and it immensely slows down hnf and det computations.



---

archive/issue_comments_027739.json:
```json
{
    "body": "This pops up on my MacBook Pro, and whatever hardware Nils was running on (his linux laptop, not sure beyond that). \n\nI just checked -- reverting this patch gets me the same error:\n\n\n```\nsage: diagonal_matrix(ZZ, 68, [2]*66 + [1,1]).det()\n-73786800370889000442\n```\n\n\nThe bound that gets determined in that function is also wrong -- in this case, the divisor it finds is 2, and the final determinant is 2^66:\n\n\n```\nsage: 2^66\n73786976294838206464\nsage: 2^66 < 10^20\nTrue\nsage: 2^66 < 10^20//2\nFalse\n```\n",
    "created_at": "2008-12-18T00:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27739",
    "user": "craigcitro"
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

archive/issue_comments_027740.json:
```json
{
    "body": "Ah, so we just needed an extra factor of 2 in there (as we weren't taking into account the sign). I'm posting a patch.",
    "created_at": "2008-12-18T00:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27740",
    "user": "robertwb"
}
```

Ah, so we just needed an extra factor of 2 in there (as we weren't taking into account the sign). I'm posting a patch.



---

archive/issue_comments_027741.json:
```json
{
    "body": "Attachment [3887-faster-fix.patch](tarball://root/attachments/some-uuid/ticket3887/3887-faster-fix.patch) by robertwb created at 2008-12-18 00:22:39",
    "created_at": "2008-12-18T00:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27741",
    "user": "robertwb"
}
```

Attachment [3887-faster-fix.patch](tarball://root/attachments/some-uuid/ticket3887/3887-faster-fix.patch) by robertwb created at 2008-12-18 00:22:39



---

archive/issue_comments_027742.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-12-18T00:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27742",
    "user": "robertwb"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_027743.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-12-18T00:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27743",
    "user": "robertwb"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_027744.json:
```json
{
    "body": "I'm going to move this to a new ticket.",
    "created_at": "2008-12-18T00:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27744",
    "user": "robertwb"
}
```

I'm going to move this to a new ticket.



---

archive/issue_comments_027745.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-18T00:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27745",
    "user": "robertwb"
}
```

Resolution: fixed



---

archive/issue_comments_027746.json:
```json
{
    "body": "See #4823",
    "created_at": "2008-12-18T00:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3887#issuecomment-27746",
    "user": "robertwb"
}
```

See #4823
