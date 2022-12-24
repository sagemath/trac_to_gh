# Issue 2581: extend solve_right to all cases; implement solve_left

archive/issues_002581.json:
```json
{
    "body": "Assignee: was\n\nA.solve_right only worked for A nonsingular, and there was no solve_left.  Now A.solve_right should work for any A and there is a solve_left. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2581\n\n",
    "created_at": "2008-03-18T02:30:42Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "extend solve_right to all cases; implement solve_left",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2581",
    "user": "was"
}
```
Assignee: was

A.solve_right only worked for A nonsingular, and there was no solve_left.  Now A.solve_right should work for any A and there is a solve_left. 

Issue created by migration from https://trac.sagemath.org/ticket/2581





---

archive/issue_comments_017654.json:
```json
{
    "body": "Attachment [sage-2581.patch](tarball://root/attachments/some-uuid/ticket2581/sage-2581.patch) by was created at 2008-03-18 02:31:22",
    "created_at": "2008-03-18T02:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17654",
    "user": "was"
}
```

Attachment [sage-2581.patch](tarball://root/attachments/some-uuid/ticket2581/sage-2581.patch) by was created at 2008-03-18 02:31:22



---

archive/issue_comments_017655.json:
```json
{
    "body": "WARNING:     def restrict_codomain(self, V) is not done yet (it's just a copy of restrict_domain).  I'll create a patch later tonight that correctly implements this.",
    "created_at": "2008-03-18T02:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17655",
    "user": "was"
}
```

WARNING:     def restrict_codomain(self, V) is not done yet (it's just a copy of restrict_domain).  I'll create a patch later tonight that correctly implements this.



---

archive/issue_comments_017656.json:
```json
{
    "body": "this provides the extra restrict_codomain functionality.",
    "created_at": "2008-03-18T07:22:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17656",
    "user": "was"
}
```

this provides the extra restrict_codomain functionality.



---

archive/issue_comments_017657.json:
```json
{
    "body": "Attachment [sage-2581_part2-restrict_codomain.patch](tarball://root/attachments/some-uuid/ticket2581/sage-2581_part2-restrict_codomain.patch) by craigcitro created at 2008-03-18 07:46:24\n\nLooks great. Merge this right away!",
    "created_at": "2008-03-18T07:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17657",
    "user": "craigcitro"
}
```

Attachment [sage-2581_part2-restrict_codomain.patch](tarball://root/attachments/some-uuid/ticket2581/sage-2581_part2-restrict_codomain.patch) by craigcitro created at 2008-03-18 07:46:24

Looks great. Merge this right away!



---

archive/issue_comments_017658.json:
```json
{
    "body": "Merged both patches in Sage 2.11.alpha0",
    "created_at": "2008-03-18T10:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17658",
    "user": "mabshoff"
}
```

Merged both patches in Sage 2.11.alpha0



---

archive/issue_comments_017659.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-18T10:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17659",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017660.json:
```json
{
    "body": "An unexpected problem: `solve_right` is defined in `matrix_integer_dense` and the versions don't provide the same functionality.  This could happen more places.\n\nIs there any hope for a `solution_space_right` that handles under-determined systems?",
    "created_at": "2008-03-18T23:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17660",
    "user": "ncalexan"
}
```

An unexpected problem: `solve_right` is defined in `matrix_integer_dense` and the versions don't provide the same functionality.  This could happen more places.

Is there any hope for a `solution_space_right` that handles under-determined systems?



---

archive/issue_comments_017661.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-03-18T23:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17661",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_017662.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-03-18T23:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17662",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_017663.json:
```json
{
    "body": "> An unexpected problem: solve_right is defined in \n> matrix_integer_dense and the versions don't provide \n> the same functionality. This could happen more places.\n\nGood point -- I had meant to address that but fell asleep and forgot. \nA patch will be forthcoming. \n\n> Is there any hope for a solution_space_right that handles under-determined systems?\n\nNot in this patch.  Make a trac ticket and somebody will get to it.",
    "created_at": "2008-03-18T23:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17663",
    "user": "was"
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

archive/issue_comments_017664.json:
```json
{
    "body": "For the record: This ticket was reopened after sage-2581.patch and sage-2581_part2-restrict_codomain.patch had been merged. So any additional patch should make clear how it should be applied.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-19T00:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17664",
    "user": "mabshoff"
}
```

For the record: This ticket was reopened after sage-2581.patch and sage-2581_part2-restrict_codomain.patch had been merged. So any additional patch should make clear how it should be applied.

Cheers,

Michael



---

archive/issue_comments_017665.json:
```json
{
    "body": "I'm attaching a patch that:\n\n1. addresses Nick's concern about derived classes overloading solve_right.\n\n2. I found that Clement recently introduced a solve right for sparse modn matrices for some reason, and that it had several bugs.  I've fixed those as well in this patch.",
    "created_at": "2008-03-19T01:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17665",
    "user": "was"
}
```

I'm attaching a patch that:

1. addresses Nick's concern about derived classes overloading solve_right.

2. I found that Clement recently introduced a solve right for sparse modn matrices for some reason, and that it had several bugs.  I've fixed those as well in this patch.



---

archive/issue_comments_017666.json:
```json
{
    "body": "Attachment [sage-2581_part3.patch](tarball://root/attachments/some-uuid/ticket2581/sage-2581_part3.patch) by was created at 2008-03-19 01:07:54",
    "created_at": "2008-03-19T01:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17666",
    "user": "was"
}
```

Attachment [sage-2581_part3.patch](tarball://root/attachments/some-uuid/ticket2581/sage-2581_part3.patch) by was created at 2008-03-19 01:07:54



---

archive/issue_comments_017667.json:
```json
{
    "body": "I think this looks good and should be applied.  I think that means part3 should be applied since the other two already have been.",
    "created_at": "2008-03-19T19:26:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17667",
    "user": "ncalexan"
}
```

I think this looks good and should be applied.  I think that means part3 should be applied since the other two already have been.



---

archive/issue_comments_017668.json:
```json
{
    "body": "Merged sage-2581_part3.patch in Sage 2.11.alpha0.",
    "created_at": "2008-03-19T23:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17668",
    "user": "mabshoff"
}
```

Merged sage-2581_part3.patch in Sage 2.11.alpha0.



---

archive/issue_comments_017669.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-19T23:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2581#issuecomment-17669",
    "user": "mabshoff"
}
```

Resolution: fixed
