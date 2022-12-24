# Issue 2228: sage-2.10.2.alpha1 -- fractional ideal doctest failure -- output is equivalent

archive/issues_002228.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage -t  devel/sage-main/sage/rings/number_field/number_field_ideal.py**********************************************************************\nFile \"number_field_ideal.py\", line 203:\n    sage: I = K.factor_integer(17)[0][0]; I\nExpected:\n    Fractional ideal (100*a^2 - 730*a + 5329)\nGot:\n    Fractional ideal (-100*a^2 + 730*a - 5329)\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_8\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctes\n```\n\n\nThe output above is completely valid.  Just change the output.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2228\n\n",
    "created_at": "2008-02-20T07:02:49Z",
    "labels": [
        "number theory",
        "blocker",
        "bug"
    ],
    "title": "sage-2.10.2.alpha1 -- fractional ideal doctest failure -- output is equivalent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2228",
    "user": "was"
}
```
Assignee: was


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

archive/issue_comments_014759.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2008-02-20T13:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2228#issuecomment-14759",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_014760.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-20T13:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2228#issuecomment-14760",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014761.json:
```json
{
    "body": "Attachment [trac_2228_number_field_ideal_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket2228/trac_2228_number_field_ideal_doctest_fix.patch) by mabshoff created at 2008-02-20 13:46:21\n\nFix doctest as indicated by William",
    "created_at": "2008-02-20T13:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2228#issuecomment-14761",
    "user": "mabshoff"
}
```

Attachment [trac_2228_number_field_ideal_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket2228/trac_2228_number_field_ideal_doctest_fix.patch) by mabshoff created at 2008-02-20 13:46:21

Fix doctest as indicated by William



---

archive/issue_comments_014762.json:
```json
{
    "body": "looks good.",
    "created_at": "2008-02-20T14:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2228#issuecomment-14762",
    "user": "jason"
}
```

looks good.



---

archive/issue_comments_014763.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha2",
    "created_at": "2008-02-20T14:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2228#issuecomment-14763",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha2



---

archive/issue_comments_014764.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-20T14:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2228#issuecomment-14764",
    "user": "mabshoff"
}
```

Resolution: fixed
