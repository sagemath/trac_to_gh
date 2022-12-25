# Issue 9570: Wrong LP solver ordering

archive/issues_009570.json:
```json
{
    "body": "Assignee: jason, jkantor\n\nAt the moment, GLPK is the solver used regardless of the presence of CBC or CPLEX. This is just because of a line written ten lines too high in the file !\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9570\n\n",
    "created_at": "2010-07-22T02:55:20Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Wrong LP solver ordering",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9570",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jason, jkantor

At the moment, GLPK is the solver used regardless of the presence of CBC or CPLEX. This is just because of a line written ten lines too high in the file !

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9570





---

archive/issue_comments_092264.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-22T02:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92264",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092265.json:
```json
{
    "body": "Attachment [trac_9570.patch](tarball://root/attachments/some-uuid/ticket9570/trac_9570.patch) by @nathanncohen created at 2010-07-22 02:57:28",
    "created_at": "2010-07-22T02:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92265",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9570.patch](tarball://root/attachments/some-uuid/ticket9570/trac_9570.patch) by @nathanncohen created at 2010-07-22 02:57:28



---

archive/issue_comments_092266.json:
```json
{
    "body": "Fixes the AttributeError that was returned when no mip solver was specified by the user",
    "created_at": "2010-07-23T08:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92266",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

Fixes the AttributeError that was returned when no mip solver was specified by the user



---

archive/issue_comments_092267.json:
```json
{
    "body": "Attachment [trac_9570-fix.patch](tarball://root/attachments/some-uuid/ticket9570/trac_9570-fix.patch) by lsampaio created at 2010-07-23 08:22:56\n\nI applied your patch, but while trying to solve an MIP without specifying a solver, I've got an AttributeError, since the attribute '_default_solver' was not defined.\nI just fixed this by adding a line stating that _default_solver = None.\nIf you agree with my changes, I think the patch can be said to be reviwed.",
    "created_at": "2010-07-23T08:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92267",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

Attachment [trac_9570-fix.patch](tarball://root/attachments/some-uuid/ticket9570/trac_9570-fix.patch) by lsampaio created at 2010-07-23 08:22:56

I applied your patch, but while trying to solve an MIP without specifying a solver, I've got an AttributeError, since the attribute '_default_solver' was not defined.
I just fixed this by adding a line stating that _default_solver = None.
If you agree with my changes, I think the patch can be said to be reviwed.



---

archive/issue_comments_092268.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-23T09:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92268",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092269.json:
```json
{
    "body": "Excellent ! Thank you very much for your help :-)\n\nBoth apply fine and in the end, it works... Now the annoying part is #8880 because CPLEX is called by next-to-any method in the LP library XD\n\nNathann",
    "created_at": "2010-07-23T09:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92269",
    "user": "https://github.com/nathanncohen"
}
```

Excellent ! Thank you very much for your help :-)

Both apply fine and in the end, it works... Now the annoying part is #8880 because CPLEX is called by next-to-any method in the LP library XD

Nathann



---

archive/issue_comments_092270.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-26T02:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92270",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_092271.json:
```json
{
    "body": "Leonardo -- be sure to use informative commit messages for your patches. \"fix\" is not very helpful. :)  Always include a ticket number, too. I changed your commit message to \"ticket 9570: insure _default_solver attribute exists\".\n\nboth patches merged in 4.5.2.alpha1.",
    "created_at": "2010-07-26T02:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92271",
    "user": "https://github.com/dandrake"
}
```

Leonardo -- be sure to use informative commit messages for your patches. "fix" is not very helpful. :)  Always include a ticket number, too. I changed your commit message to "ticket 9570: insure _default_solver attribute exists".

both patches merged in 4.5.2.alpha1.



---

archive/issue_comments_092272.json:
```json
{
    "body": "ok, thanks for the advice =)",
    "created_at": "2010-07-26T02:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92272",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

ok, thanks for the advice =)
