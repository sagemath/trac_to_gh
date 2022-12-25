# Issue 2228: sage-2.10.2.alpha1 -- fractional ideal doctest failure -- output is equivalent

archive/issues_002228.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage -t  devel/sage-main/sage/rings/number_field/number_field_ideal.py**********************************************************************\nFile \"number_field_ideal.py\", line 203:\n    sage: I = K.factor_integer(17)[0][0]; I\nExpected:\n    Fractional ideal (100*a^2 - 730*a + 5329)\nGot:\n    Fractional ideal (-100*a^2 + 730*a - 5329)\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_8\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctes\n```\n\n\nThe output above is completely valid.  Just change the output.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2228\n\n",
    "created_at": "2008-02-20T07:02:49Z",
    "labels": [
        "component: number theory",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "sage-2.10.2.alpha1 -- fractional ideal doctest failure -- output is equivalent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2228",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage -t  devel/sage-main/sage/rings/number_field/number_field_ideal.py**********************************************************************
File "number_field_ideal.py", line 203:
    sage: I = K.factor_integer(17)[0][0]; I
Expected:
    Fractional ideal (100*a^2 - 730*a + 5329)
Got:
    Fractional ideal (-100*a^2 + 730*a - 5329)
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_8
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctes
```


The output above is completely valid.  Just change the output.

Issue created by migration from https://trac.sagemath.org/ticket/2228





---

archive/issue_comments_014728.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-02-20T13:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2228#issuecomment-14728",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_014729.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-20T13:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2228#issuecomment-14729",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014730.json:
```json
{
    "body": "Attachment [trac_2228_number_field_ideal_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket2228/trac_2228_number_field_ideal_doctest_fix.patch) by mabshoff created at 2008-02-20 13:46:21\n\nFix doctest as indicated by William",
    "created_at": "2008-02-20T13:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2228#issuecomment-14730",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2228_number_field_ideal_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket2228/trac_2228_number_field_ideal_doctest_fix.patch) by mabshoff created at 2008-02-20 13:46:21

Fix doctest as indicated by William



---

archive/issue_comments_014731.json:
```json
{
    "body": "looks good.",
    "created_at": "2008-02-20T14:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2228#issuecomment-14731",
    "user": "https://github.com/jasongrout"
}
```

looks good.



---

archive/issue_comments_014732.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha2",
    "created_at": "2008-02-20T14:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2228#issuecomment-14732",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha2



---

archive/issue_comments_014733.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-20T14:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2228#issuecomment-14733",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
