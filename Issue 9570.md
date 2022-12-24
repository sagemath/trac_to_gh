# Issue 9570: Wrong LP solver ordering

archive/issues_009570.json:
```json
{
    "body": "Assignee: jason, jkantor\n\nAt the moment, GLPK is the solver used regardless of the presence of CBC or CPLEX. This is just because of a line written ten lines too high in the file !\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9570\n\n",
    "created_at": "2010-07-22T02:55:20Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Wrong LP solver ordering",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9570",
    "user": "ncohen"
}
```
Assignee: jason, jkantor

At the moment, GLPK is the solver used regardless of the presence of CBC or CPLEX. This is just because of a line written ten lines too high in the file !

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9570





---

archive/issue_comments_092418.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-22T02:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92418",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092419.json:
```json
{
    "body": "Attachment [trac_9570.patch](tarball://root/attachments/some-uuid/ticket9570/trac_9570.patch) by ncohen created at 2010-07-22 02:57:28",
    "created_at": "2010-07-22T02:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92419",
    "user": "ncohen"
}
```

Attachment [trac_9570.patch](tarball://root/attachments/some-uuid/ticket9570/trac_9570.patch) by ncohen created at 2010-07-22 02:57:28



---

archive/issue_comments_092420.json:
```json
{
    "body": "Fixes the AttributeError that was returned when no mip solver was specified by the user",
    "created_at": "2010-07-23T08:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92420",
    "user": "lsampaio"
}
```

Fixes the AttributeError that was returned when no mip solver was specified by the user



---

archive/issue_comments_092421.json:
```json
{
    "body": "Attachment [trac_9570-fix.patch](tarball://root/attachments/some-uuid/ticket9570/trac_9570-fix.patch) by lsampaio created at 2010-07-23 08:22:56\n\nI applied your patch, but while trying to solve an MIP without specifying a solver, I've got an AttributeError, since the attribute '_default_solver' was not defined.\nI just fixed this by adding a line stating that _default_solver = None.\nIf you agree with my changes, I think the patch can be said to be reviwed.",
    "created_at": "2010-07-23T08:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92421",
    "user": "lsampaio"
}
```

Attachment [trac_9570-fix.patch](tarball://root/attachments/some-uuid/ticket9570/trac_9570-fix.patch) by lsampaio created at 2010-07-23 08:22:56

I applied your patch, but while trying to solve an MIP without specifying a solver, I've got an AttributeError, since the attribute '_default_solver' was not defined.
I just fixed this by adding a line stating that _default_solver = None.
If you agree with my changes, I think the patch can be said to be reviwed.



---

archive/issue_comments_092422.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-23T09:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92422",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092423.json:
```json
{
    "body": "Excellent ! Thank you very much for your help :-)\n\nBoth apply fine and in the end, it works... Now the annoying part is #8880 because CPLEX is called by next-to-any method in the LP library XD\n\nNathann",
    "created_at": "2010-07-23T09:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92423",
    "user": "ncohen"
}
```

Excellent ! Thank you very much for your help :-)

Both apply fine and in the end, it works... Now the annoying part is #8880 because CPLEX is called by next-to-any method in the LP library XD

Nathann



---

archive/issue_comments_092424.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-26T02:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92424",
    "user": "ddrake"
}
```

Resolution: fixed



---

archive/issue_comments_092425.json:
```json
{
    "body": "Leonardo -- be sure to use informative commit messages for your patches. \"fix\" is not very helpful. :)  Always include a ticket number, too. I changed your commit message to \"ticket 9570: insure _default_solver attribute exists\".\n\nboth patches merged in 4.5.2.alpha1.",
    "created_at": "2010-07-26T02:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92425",
    "user": "ddrake"
}
```

Leonardo -- be sure to use informative commit messages for your patches. "fix" is not very helpful. :)  Always include a ticket number, too. I changed your commit message to "ticket 9570: insure _default_solver attribute exists".

both patches merged in 4.5.2.alpha1.



---

archive/issue_comments_092426.json:
```json
{
    "body": "ok, thanks for the advice =)",
    "created_at": "2010-07-26T02:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9570#issuecomment-92426",
    "user": "lsampaio"
}
```

ok, thanks for the advice =)
