# Issue 5110: rewrite diagonal_matrix to be more general

archive/issues_005110.json:
```json
{
    "body": "Assignee: @williamstein\n\nSee the patches at #3704, which rewrite diagonal_matrix.  On that ticket, however, we finally just went with a basic patch that fixed the specific bug mentioned.  There is good code in the other patches that ought to be used, though.  This ticket is here so that we eventually use the cleaner rewrite contained in the first patches at #3704.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5110\n\n",
    "created_at": "2009-01-27T03:54:59Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "rewrite diagonal_matrix to be more general",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5110",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

See the patches at #3704, which rewrite diagonal_matrix.  On that ticket, however, we finally just went with a basic patch that fixed the specific bug mentioned.  There is good code in the other patches that ought to be used, though.  This ticket is here so that we eventually use the cleaner rewrite contained in the first patches at #3704.

Issue created by migration from https://trac.sagemath.org/ticket/5110





---

archive/issue_comments_039039.json:
```json
{
    "body": "What exactly should be added to diagonal_matrix? I'd be happy to work on this ticket but it looks like the other patches in #3704 add doctests.",
    "created_at": "2018-05-26T14:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5110#issuecomment-39039",
    "user": "@black-stones"
}
```

What exactly should be added to diagonal_matrix? I'd be happy to work on this ticket but it looks like the other patches in #3704 add doctests.



---

archive/issue_comments_039040.json:
```json
{
    "body": "I think the idea is to use attachment:trac-3704-diagonal_matrix.patch:ticket:3704 to make a more generally applicable function.\n\nThat said, there are probably more important tickets to work on, notably reviewing many in symbolics ...",
    "created_at": "2018-05-30T17:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5110#issuecomment-39040",
    "user": "@kcrisman"
}
```

I think the idea is to use attachment:trac-3704-diagonal_matrix.patch:ticket:3704 to make a more generally applicable function.

That said, there are probably more important tickets to work on, notably reviewing many in symbolics ...



---

archive/issue_comments_039041.json:
```json
{
    "body": "I did see that patch, but looking at the source code for diagonal_matrix(), the differences seem to be\n\n1. Changing the parameters\n2. More comments and doctests\n3. Casting to Sequence\n\n1 could be a good fix since the current function uses \"arg0, arg1, arg2\" which is pretty bad, but in my opinion, 2 and 3 are not necessary (although if we do change 1 we will need to change 2).",
    "created_at": "2018-05-30T21:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5110#issuecomment-39041",
    "user": "@black-stones"
}
```

I did see that patch, but looking at the source code for diagonal_matrix(), the differences seem to be

1. Changing the parameters
2. More comments and doctests
3. Casting to Sequence

1 could be a good fix since the current function uses "arg0, arg1, arg2" which is pretty bad, but in my opinion, 2 and 3 are not necessary (although if we do change 1 we will need to change 2).



---

archive/issue_comments_039042.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2019-12-14T00:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5110#issuecomment-39042",
    "user": "@slel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039043.json:
```json
{
    "body": "This is probably solved by #10604 (please check).",
    "created_at": "2019-12-14T00:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5110#issuecomment-39043",
    "user": "@slel"
}
```

This is probably solved by #10604 (please check).



---

archive/issue_comments_039044.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2019-12-27T17:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5110#issuecomment-39044",
    "user": "@tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_039045.json:
```json
{
    "body": "I think so as well.",
    "created_at": "2019-12-27T17:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5110#issuecomment-39045",
    "user": "@tscrim"
}
```

I think so as well.



---

archive/issue_comments_039046.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2019-12-27T22:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5110#issuecomment-39046",
    "user": "@slel"
}
```

Resolution: duplicate
