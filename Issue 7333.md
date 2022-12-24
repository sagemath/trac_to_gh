# Issue 7333: CBC spkg

archive/issues_007333.json:
```json
{
    "body": "Assignee: tbd\n\nSince the new version of sage.numerical.mip, which is now in the standard distribution of Sage, the old CBC spkg was not working anymore because of many changes in the structure of class MIP. This patch fixes this, by mainly changing some variables' names to the new ones, and Cythonizing part of the code when it was possible !\n\nThe spkg is available in two locations :\n* On sage.math at ~ncohen/cbc-2.3.p1.spkg\n* At http://www-sop.inria.fr/members/Nathann.Cohen/cbc-2.3.p1.spkg\n\nThank you for your help !!!!\n\nIssue created by migration from https://trac.sagemath.org/ticket/7333\n\n",
    "created_at": "2009-10-28T17:14:38Z",
    "labels": [
        "packages: optional",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "CBC spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7333",
    "user": "@nathanncohen"
}
```
Assignee: tbd

Since the new version of sage.numerical.mip, which is now in the standard distribution of Sage, the old CBC spkg was not working anymore because of many changes in the structure of class MIP. This patch fixes this, by mainly changing some variables' names to the new ones, and Cythonizing part of the code when it was possible !

The spkg is available in two locations :
* On sage.math at ~ncohen/cbc-2.3.p1.spkg
* At http://www-sop.inria.fr/members/Nathann.Cohen/cbc-2.3.p1.spkg

Thank you for your help !!!!

Issue created by migration from https://trac.sagemath.org/ticket/7333





---

archive/issue_comments_061323.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-28T17:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7333#issuecomment-61323",
    "user": "@nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061324.json:
```json
{
    "body": "I get a bunch of `--optional` doctest errors if only CBC but not GLPK is installed. Most of them are fine (they point out that I need GLPK), but this one isn't:\n\n\n```\n    sage: p.get_values(x[3]) # optional - requires Glpk or COIN-OR/CBC\nExpected:\n    2.0\nGot:\n    0.0\n```\n\n\nOther than that, it looks fine. I have been using it over the last week or so and cannot report any problems.",
    "created_at": "2009-12-08T13:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7333#issuecomment-61324",
    "user": "@malb"
}
```

I get a bunch of `--optional` doctest errors if only CBC but not GLPK is installed. Most of them are fine (they point out that I need GLPK), but this one isn't:


```
    sage: p.get_values(x[3]) # optional - requires Glpk or COIN-OR/CBC
Expected:
    2.0
Got:
    0.0
```


Other than that, it looks fine. I have been using it over the last week or so and cannot report any problems.



---

archive/issue_comments_061325.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-08T13:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7333#issuecomment-61325",
    "user": "@malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061326.json:
```json
{
    "body": "I should have got rid of this before... :p\n\nThis is just caused by the fact that the problem that is optimized is symmetric in the two variables x[3] and y. CBC returnd x[3] set to two, and Coin returns the other one to 2, both being good answers :p\n\nBut I thought this had been updated... Did you test it on the last alpha version ?",
    "created_at": "2009-12-08T14:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7333#issuecomment-61326",
    "user": "@nathanncohen"
}
```

I should have got rid of this before... :p

This is just caused by the fact that the problem that is optimized is symmetric in the two variables x[3] and y. CBC returnd x[3] set to two, and Coin returns the other one to 2, both being good answers :p

But I thought this had been updated... Did you test it on the last alpha version ?



---

archive/issue_comments_061327.json:
```json
{
    "body": "Yes, alpha1.",
    "created_at": "2009-12-08T14:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7333#issuecomment-61327",
    "user": "@malb"
}
```

Yes, alpha1.



---

archive/issue_comments_061328.json:
```json
{
    "body": "Sorry, then I did not check on the good file. I can not find any occurrence of p.get_values(x[3]) in mip.pyx. Could you tell me which file contains it please ? :-)\n\nI'll fix it immediately after !!!\n\nNathann",
    "created_at": "2009-12-08T14:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7333#issuecomment-61328",
    "user": "@nathanncohen"
}
```

Sorry, then I did not check on the good file. I can not find any occurrence of p.get_values(x[3]) in mip.pyx. Could you tell me which file contains it please ? :-)

I'll fix it immediately after !!!

Nathann



---

archive/issue_comments_061329.json:
```json
{
    "body": "Line 477:\n\n\n```\n        EXAMPLE::\n\n            sage: p = MixedIntegerLinearProgram()\n            sage: x = p.new_variable()\n            sage: y = p.new_variable(dim=2)\n            sage: p.set_objective(x[3] + y[2][9] + x[5])\n            sage: p.add_constraint(x[3] + y[2][9] + 2*x[5], max=2)\n            sage: p.solve() # optional - requires Glpk or COIN-OR/CBC\n            2.0\n            sage: #\n            sage: # Returns the optimal value of x[3]\n>>>         sage: p.get_values(x[3]) # optional - requires Glpk or COIN-OR/CBC\n            2.0\n```\n",
    "created_at": "2009-12-08T14:46:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7333#issuecomment-61329",
    "user": "@malb"
}
```

Line 477:


```
        EXAMPLE::

            sage: p = MixedIntegerLinearProgram()
            sage: x = p.new_variable()
            sage: y = p.new_variable(dim=2)
            sage: p.set_objective(x[3] + y[2][9] + x[5])
            sage: p.add_constraint(x[3] + y[2][9] + 2*x[5], max=2)
            sage: p.solve() # optional - requires Glpk or COIN-OR/CBC
            2.0
            sage: #
            sage: # Returns the optimal value of x[3]
>>>         sage: p.get_values(x[3]) # optional - requires Glpk or COIN-OR/CBC
            2.0
```




---

archive/issue_comments_061330.json:
```json
{
    "body": "Ah, I was talking about vanilla alpha1, while you are probably talking about #7561. Thus it might be fixed already since #7561 is in rc0.",
    "created_at": "2009-12-08T14:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7333#issuecomment-61330",
    "user": "@malb"
}
```

Ah, I was talking about vanilla alpha1, while you are probably talking about #7561. Thus it might be fixed already since #7561 is in rc0.



---

archive/issue_comments_061331.json:
```json
{
    "body": "Yes, sorry for the misunderstanding :-)",
    "created_at": "2009-12-08T14:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7333#issuecomment-61331",
    "user": "@nathanncohen"
}
```

Yes, sorry for the misunderstanding :-)



---

archive/issue_comments_061332.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-08T16:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7333#issuecomment-61332",
    "user": "@malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061333.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T16:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7333#issuecomment-61333",
    "user": "@malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061334.json:
```json
{
    "body": "Thank you ! :-)",
    "created_at": "2009-12-08T16:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7333#issuecomment-61334",
    "user": "@nathanncohen"
}
```

Thank you ! :-)



---

archive/issue_comments_061335.json:
```json
{
    "body": "Merged in with the optional packages.",
    "created_at": "2009-12-09T02:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7333#issuecomment-61335",
    "user": "@mwhansen"
}
```

Merged in with the optional packages.



---

archive/issue_comments_061336.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T02:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7333#issuecomment-61336",
    "user": "@mwhansen"
}
```

Resolution: fixed
