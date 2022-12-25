# Issue 5027: [with patch, positive review] doctest failure for rings/polynomial/toy_d_basis.py

archive/issues_005027.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: groebner, toy, toy_d_basis\n\nI get this failure on an intel mac:\n\n```\nsage -t  \"devel/sage/sage/rings/polynomial/toy_d_basis.py\"\n**********************************************************************\nFile \".../devel/sage/sage/rings/polynomial/toy_d_basis.py\", line 91:\n    sage: d_basis(I)\nExpected:\n    [x + 170269749119, y + 2149906854, z + 735710619426, 282687803443]\nGot:\n    [x + 170269749119, y + 2149906854, z + 170335012540, 282687803443]\n********************************************************************** \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5027\n\n",
    "closed_at": "2009-02-05T23:40:29Z",
    "created_at": "2009-01-19T16:13:02Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, positive review] doctest failure for rings/polynomial/toy_d_basis.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5027",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: mabshoff

Keywords: groebner, toy, toy_d_basis

I get this failure on an intel mac:

```
sage -t  "devel/sage/sage/rings/polynomial/toy_d_basis.py"
**********************************************************************
File ".../devel/sage/sage/rings/polynomial/toy_d_basis.py", line 91:
    sage: d_basis(I)
Expected:
    [x + 170269749119, y + 2149906854, z + 735710619426, 282687803443]
Got:
    [x + 170269749119, y + 2149906854, z + 170335012540, 282687803443]
********************************************************************** 
```

Issue created by migration from https://trac.sagemath.org/ticket/5027





---

archive/issue_comments_038222.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-04T14:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5027#issuecomment-38222",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038223.json:
```json
{
    "body": "After chatting with malb we decided to dot out the constant since it is the same GBasis.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-04T14:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5027#issuecomment-38223",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

After chatting with malb we decided to dot out the constant since it is the same GBasis.

Cheers,

Michael



---

archive/issue_comments_038224.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2009-02-04T14:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5027#issuecomment-38224",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_038225.json:
```json
{
    "body": "Attachment [trac_5027.patch](tarball://root/attachments/some-uuid/ticket5027/trac_5027.patch) by mabshoff created at 2009-02-05 13:07:58",
    "created_at": "2009-02-05T13:07:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5027#issuecomment-38225",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5027.patch](tarball://root/attachments/some-uuid/ticket5027/trac_5027.patch) by mabshoff created at 2009-02-05 13:07:58



---

archive/issue_comments_038226.json:
```json
{
    "body": "After applying the patch:\n\n```\nsage -t  \"devel/sage/sage/rings/polynomial/toy_d_basis.py\"  \n\t [9.5 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 9.5 seconds\n[jaap@paix sage-3.3.alpha4]$ \n\n```\n\nOn fedora 9, 32 bits.\n\nJaap",
    "created_at": "2009-02-05T15:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5027#issuecomment-38226",
    "user": "https://github.com/jaapspies"
}
```

After applying the patch:

```
sage -t  "devel/sage/sage/rings/polynomial/toy_d_basis.py"  
	 [9.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 9.5 seconds
[jaap@paix sage-3.3.alpha4]$ 

```

On fedora 9, 32 bits.

Jaap



---

archive/issue_events_011604.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-05T23:40:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5027#event-11604"
}
```



---

archive/issue_comments_038227.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-05T23:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5027#issuecomment-38227",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_comments_038228.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-05T23:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5027#issuecomment-38228",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
