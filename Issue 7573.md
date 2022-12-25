# Issue 7573: Sage crashes if insufficient data is provided for MIP

archive/issues_007573.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  @nathanncohen\n\nThis crashes Sage:\n\n```\nsage: g = graphs.PetersenGraph()\nsage: p = MixedIntegerLinearProgram(maximization=True)\nsage: b = p.new_variable()\nsage: p.set_objective(sum([b[v] for v in g]))\nsage: p.set_binary(b)\nsage: p.solve(objective_only=True)\n```\n\nDepends on #7270 !!!!!!!!!!!!!!!!!!!!\n\nIssue created by migration from https://trac.sagemath.org/ticket/7573\n\n",
    "closed_at": "2009-12-02T08:07:46Z",
    "created_at": "2009-12-01T16:00:50Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Sage crashes if insufficient data is provided for MIP",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7573",
    "user": "https://github.com/malb"
}
```
Assignee: jkantor

CC:  @nathanncohen

This crashes Sage:

```
sage: g = graphs.PetersenGraph()
sage: p = MixedIntegerLinearProgram(maximization=True)
sage: b = p.new_variable()
sage: p.set_objective(sum([b[v] for v in g]))
sage: p.set_binary(b)
sage: p.solve(objective_only=True)
```

Depends on #7270 !!!!!!!!!!!!!!!!!!!!

Issue created by migration from https://trac.sagemath.org/ticket/7573





---

archive/issue_comments_064341.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-01T16:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7573#issuecomment-64341",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064342.json:
```json
{
    "body": "The attached patch fixes the issue for me.",
    "created_at": "2009-12-01T16:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7573#issuecomment-64342",
    "user": "https://github.com/malb"
}
```

The attached patch fixes the issue for me.



---

archive/issue_comments_064343.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-12-01T16:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7573#issuecomment-64343",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_064344.json:
```json
{
    "body": "Hello !!!\n\nThis problem does not seem to exist on the version I am using, with patch #7270 and the new GLPK spkg installed... Did you test it on the current Sage version of both  ?\n\nNathann",
    "created_at": "2009-12-01T16:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7573#issuecomment-64344",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!!

This problem does not seem to exist on the version I am using, with patch #7270 and the new GLPK spkg installed... Did you test it on the current Sage version of both  ?

Nathann



---

archive/issue_comments_064345.json:
```json
{
    "body": "The problem is not fixed in #7270 but I updated the patch to work with #7270.",
    "created_at": "2009-12-01T17:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7573#issuecomment-64345",
    "user": "https://github.com/malb"
}
```

The problem is not fixed in #7270 but I updated the patch to work with #7270.



---

archive/issue_comments_064346.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-12-01T17:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7573#issuecomment-64346",
    "user": "https://github.com/malb"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_064347.json:
```json
{
    "body": "I just tested your patch and it seems Coin behaves much better than GLPK : the new doctests fails for solver=\"Coin\", as it peacefully returns an exception as it should. Could you add in your test solver=\"GLPK\" to the p.solve() call ?\n\nIt sounds like wrapping solveCoin with _sig_on and sig_off is not needed, though it can not hurt to let it stay ;-)\n\nThank you very much for your help !!!!\n\nNathann",
    "created_at": "2009-12-01T17:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7573#issuecomment-64347",
    "user": "https://github.com/nathanncohen"
}
```

I just tested your patch and it seems Coin behaves much better than GLPK : the new doctests fails for solver="Coin", as it peacefully returns an exception as it should. Could you add in your test solver="GLPK" to the p.solve() call ?

It sounds like wrapping solveCoin with _sig_on and sig_off is not needed, though it can not hurt to let it stay ;-)

Thank you very much for your help !!!!

Nathann



---

archive/issue_comments_064348.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-01T17:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7573#issuecomment-64348",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064349.json:
```json
{
    "body": "updated to fit #7270",
    "created_at": "2009-12-01T17:38:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7573#issuecomment-64349",
    "user": "https://github.com/malb"
}
```

updated to fit #7270



---

archive/issue_comments_064350.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-01T17:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7573#issuecomment-64350",
    "user": "https://github.com/malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064351.json:
```json
{
    "body": "Attachment [glpk_crash.patch](tarball://root/attachments/some-uuid/ticket7573/glpk_crash.patch) by @malb created at 2009-12-01 17:38:51\n\ndone",
    "created_at": "2009-12-01T17:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7573#issuecomment-64351",
    "user": "https://github.com/malb"
}
```

Attachment [glpk_crash.patch](tarball://root/attachments/some-uuid/ticket7573/glpk_crash.patch) by @malb created at 2009-12-01 17:38:51

done



---

archive/issue_comments_064352.json:
```json
{
    "body": "Applies fines, does its job... :-)",
    "created_at": "2009-12-01T17:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7573#issuecomment-64352",
    "user": "https://github.com/nathanncohen"
}
```

Applies fines, does its job... :-)



---

archive/issue_comments_064353.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-01T17:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7573#issuecomment-64353",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064354.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-02T08:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7573#issuecomment-64354",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017957.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-02T08:07:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7573",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7573#event-17957"
}
```
