# Issue 2267: [with patch, needs review] Sage 2.10.2: fix latex errors when generating the documentation

archive/issues_002267.json:
```json
{
    "body": "Assignee: @williamstein\n\nAs a last step after merging all the patches we need to regenerate the documentation. That does involve fixing a bunch of LaTeX errors from the docstrings.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2267\n\n",
    "created_at": "2008-02-22T21:54:45Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, needs review] Sage 2.10.2: fix latex errors when generating the documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2267",
    "user": "mabshoff"
}
```
Assignee: @williamstein

As a last step after merging all the patches we need to regenerate the documentation. That does involve fixing a bunch of LaTeX errors from the docstrings.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2267





---

archive/issue_comments_015016.json:
```json
{
    "body": "Changing component from algebraic geometry to documentation.",
    "created_at": "2008-02-22T21:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2267#issuecomment-15016",
    "user": "mabshoff"
}
```

Changing component from algebraic geometry to documentation.



---

archive/issue_comments_015017.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-22T21:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2267#issuecomment-15017",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015018.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-02-22T21:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2267#issuecomment-15018",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_015019.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-02-22T21:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2267#issuecomment-15019",
    "user": "mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_015020.json:
```json
{
    "body": "Attachment [trac_2267.patch](tarball://root/attachments/some-uuid/ticket2267/trac_2267.patch) by mabshoff created at 2008-02-22 21:57:54",
    "created_at": "2008-02-22T21:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2267#issuecomment-15020",
    "user": "mabshoff"
}
```

Attachment [trac_2267.patch](tarball://root/attachments/some-uuid/ticket2267/trac_2267.patch) by mabshoff created at 2008-02-22 21:57:54



---

archive/issue_comments_015021.json:
```json
{
    "body": "`$hnf(transpose(A))^(-1)*A$` that looks wrong and probably should be: `$hnf(transpose(A))^{-1} * A$`",
    "created_at": "2008-02-22T22:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2267#issuecomment-15021",
    "user": "@malb"
}
```

`$hnf(transpose(A))^(-1)*A$` that looks wrong and probably should be: `$hnf(transpose(A))^{-1} * A$`



---

archive/issue_comments_015022.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> `$hnf(transpose(A))^(-1)*A$` that looks wrong and probably should be: `$hnf(transpose(A))^{-1} * A$`\n\nAre you sure that makes a difference? I think in math mode all spaces will be eaten by the TeX parser anyway.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-22T23:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2267#issuecomment-15022",
    "user": "mabshoff"
}
```

Replying to [comment:2 malb]:
> `$hnf(transpose(A))^(-1)*A$` that looks wrong and probably should be: `$hnf(transpose(A))^{-1} * A$`

Are you sure that makes a difference? I think in math mode all spaces will be eaten by the TeX parser anyway.

Cheers,

Michael



---

archive/issue_comments_015023.json:
```json
{
    "body": "Merged in Sage 2.10.2.final",
    "created_at": "2008-02-22T23:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2267#issuecomment-15023",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.final



---

archive/issue_comments_015024.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-22T23:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2267#issuecomment-15024",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015025.json:
```json
{
    "body": "Yes my comment makes a difference because `^{-1`} is different from `^(-1)` :-)",
    "created_at": "2008-02-22T23:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2267#issuecomment-15025",
    "user": "@malb"
}
```

Yes my comment makes a difference because `^{-1`} is different from `^(-1)` :-)



---

archive/issue_comments_015026.json:
```json
{
    "body": "Replying to [comment:6 malb]:\n> Yes my comment makes a difference because `^{-1`} is different from `^(-1)` :-) \n\nD'oh - I will fix it in the sources. Maybe I should get new glasses and sleep more. Thanks malb.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-22T23:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2267#issuecomment-15026",
    "user": "mabshoff"
}
```

Replying to [comment:6 malb]:
> Yes my comment makes a difference because `^{-1`} is different from `^(-1)` :-) 

D'oh - I will fix it in the sources. Maybe I should get new glasses and sleep more. Thanks malb.

Cheers,

Michael
