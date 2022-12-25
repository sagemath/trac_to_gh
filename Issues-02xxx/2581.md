# Issue 2581: [with patch, with positive review] extend solve_right to all cases; implement solve_left

archive/issues_002581.json:
```json
{
    "body": "Assignee: @williamstein\n\nA.solve_right only worked for A nonsingular, and there was no solve_left.  Now A.solve_right should work for any A and there is a solve_left. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2581\n\n",
    "closed_at": "2008-03-19T23:58:43Z",
    "created_at": "2008-03-18T02:30:42Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, with positive review] extend solve_right to all cases; implement solve_left",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2581",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

A.solve_right only worked for A nonsingular, and there was no solve_left.  Now A.solve_right should work for any A and there is a solve_left. 

Issue created by migration from https://trac.sagemath.org/ticket/2581





---

archive/issue_comments_017616.json:
```json
{
    "body": "Attachment [sage-2581.patch](tarball://root/attachments/some-uuid/ticket2581/sage-2581.patch) by @williamstein created at 2008-03-18 02:31:22",
    "created_at": "2008-03-18T02:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17616",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2581.patch](tarball://root/attachments/some-uuid/ticket2581/sage-2581.patch) by @williamstein created at 2008-03-18 02:31:22



---

archive/issue_comments_017617.json:
```json
{
    "body": "WARNING:     def restrict_codomain(self, V) is not done yet (it's just a copy of restrict_domain).  I'll create a patch later tonight that correctly implements this.",
    "created_at": "2008-03-18T02:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17617",
    "user": "https://github.com/williamstein"
}
```

WARNING:     def restrict_codomain(self, V) is not done yet (it's just a copy of restrict_domain).  I'll create a patch later tonight that correctly implements this.



---

archive/issue_comments_017618.json:
```json
{
    "body": "this provides the extra restrict_codomain functionality.",
    "created_at": "2008-03-18T07:22:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17618",
    "user": "https://github.com/williamstein"
}
```

this provides the extra restrict_codomain functionality.



---

archive/issue_comments_017619.json:
```json
{
    "body": "Attachment [sage-2581_part2-restrict_codomain.patch](tarball://root/attachments/some-uuid/ticket2581/sage-2581_part2-restrict_codomain.patch) by @craigcitro created at 2008-03-18 07:46:24\n\nLooks great. Merge this right away!",
    "created_at": "2008-03-18T07:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17619",
    "user": "https://github.com/craigcitro"
}
```

Attachment [sage-2581_part2-restrict_codomain.patch](tarball://root/attachments/some-uuid/ticket2581/sage-2581_part2-restrict_codomain.patch) by @craigcitro created at 2008-03-18 07:46:24

Looks great. Merge this right away!



---

archive/issue_comments_017620.json:
```json
{
    "body": "Merged both patches in Sage 2.11.alpha0",
    "created_at": "2008-03-18T10:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17620",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 2.11.alpha0



---

archive/issue_events_006033.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-18T10:23:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2581#event-6033"
}
```



---

archive/issue_comments_017621.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-18T10:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17621",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017622.json:
```json
{
    "body": "An unexpected problem: `solve_right` is defined in `matrix_integer_dense` and the versions don't provide the same functionality.  This could happen more places.\n\nIs there any hope for a `solution_space_right` that handles under-determined systems?",
    "created_at": "2008-03-18T23:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17622",
    "user": "https://github.com/ncalexan"
}
```

An unexpected problem: `solve_right` is defined in `matrix_integer_dense` and the versions don't provide the same functionality.  This could happen more places.

Is there any hope for a `solution_space_right` that handles under-determined systems?



---

archive/issue_comments_017623.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-03-18T23:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17623",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_006034.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-03-18T23:55:59Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2581#event-6034"
}
```



---

archive/issue_comments_017624.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-03-18T23:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17624",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_017625.json:
```json
{
    "body": "> An unexpected problem: solve_right is defined in \n> matrix_integer_dense and the versions don't provide \n> the same functionality. This could happen more places.\n\n\nGood point -- I had meant to address that but fell asleep and forgot. \nA patch will be forthcoming. \n\n> Is there any hope for a solution_space_right that handles under-determined systems?\n\n\nNot in this patch.  Make a trac ticket and somebody will get to it.",
    "created_at": "2008-03-18T23:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17625",
    "user": "https://github.com/williamstein"
}
```

> An unexpected problem: solve_right is defined in 
> matrix_integer_dense and the versions don't provide 
> the same functionality. This could happen more places.


Good point -- I had meant to address that but fell asleep and forgot. 
A patch will be forthcoming. 

> Is there any hope for a solution_space_right that handles under-determined systems?


Not in this patch.  Make a trac ticket and somebody will get to it.



---

archive/issue_comments_017626.json:
```json
{
    "body": "For the record: This ticket was reopened after sage-2581.patch and sage-2581_part2-restrict_codomain.patch had been merged. So any additional patch should make clear how it should be applied.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-19T00:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17626",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: This ticket was reopened after sage-2581.patch and sage-2581_part2-restrict_codomain.patch had been merged. So any additional patch should make clear how it should be applied.

Cheers,

Michael



---

archive/issue_comments_017627.json:
```json
{
    "body": "I'm attaching a patch that:\n\n1. addresses Nick's concern about derived classes overloading solve_right.\n\n2. I found that Clement recently introduced a solve right for sparse modn matrices for some reason, and that it had several bugs.  I've fixed those as well in this patch.",
    "created_at": "2008-03-19T01:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17627",
    "user": "https://github.com/williamstein"
}
```

I'm attaching a patch that:

1. addresses Nick's concern about derived classes overloading solve_right.

2. I found that Clement recently introduced a solve right for sparse modn matrices for some reason, and that it had several bugs.  I've fixed those as well in this patch.



---

archive/issue_comments_017628.json:
```json
{
    "body": "Attachment [sage-2581_part3.patch](tarball://root/attachments/some-uuid/ticket2581/sage-2581_part3.patch) by @williamstein created at 2008-03-19 01:07:54",
    "created_at": "2008-03-19T01:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17628",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2581_part3.patch](tarball://root/attachments/some-uuid/ticket2581/sage-2581_part3.patch) by @williamstein created at 2008-03-19 01:07:54



---

archive/issue_comments_017629.json:
```json
{
    "body": "I think this looks good and should be applied.  I think that means part3 should be applied since the other two already have been.",
    "created_at": "2008-03-19T19:26:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17629",
    "user": "https://github.com/ncalexan"
}
```

I think this looks good and should be applied.  I think that means part3 should be applied since the other two already have been.



---

archive/issue_events_006035.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-19T23:58:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2581#event-6035"
}
```



---

archive/issue_comments_017630.json:
```json
{
    "body": "Merged sage-2581_part3.patch in Sage 2.11.alpha0.",
    "created_at": "2008-03-19T23:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17630",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged sage-2581_part3.patch in Sage 2.11.alpha0.



---

archive/issue_comments_017631.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-19T23:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17631",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
