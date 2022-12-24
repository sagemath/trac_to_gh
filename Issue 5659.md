# Issue 5659: [with patch, needs review] Use CRT to speed up solve_mod

archive/issues_005659.json:
```json
{
    "body": "Assignee: whuss\n\nThe attached patch uses the Chinese Remainder Theorem to speed up \nsolve_mod if the modulus can be factorized into small numbers.\n\nIt also adds the option solution_dict for consistency with solve.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5659\n\n",
    "created_at": "2009-04-01T15:41:31Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] Use CRT to speed up solve_mod",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5659",
    "user": "whuss"
}
```
Assignee: whuss

The attached patch uses the Chinese Remainder Theorem to speed up 
solve_mod if the modulus can be factorized into small numbers.

It also adds the option solution_dict for consistency with solve.

Issue created by migration from https://trac.sagemath.org/ticket/5659





---

archive/issue_comments_044243.json:
```json
{
    "body": "Attachment [solve_mod.patch](tarball://root/attachments/some-uuid/ticket5659/solve_mod.patch) by was created at 2009-04-12 04:25:02",
    "created_at": "2009-04-12T04:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5659#issuecomment-44243",
    "user": "was"
}
```

Attachment [solve_mod.patch](tarball://root/attachments/some-uuid/ticket5659/solve_mod.patch) by was created at 2009-04-12 04:25:02



---

archive/issue_comments_044244.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T02:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5659#issuecomment-44244",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044245.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T02:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5659#issuecomment-44245",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
