# Issue 2564: Sage 2.10.4.rc0: fix numerical noise doctest failure in numerical/optimize.py

archive/issues_002564.json:
```json
{
    "body": "Assignee: mabshoff\n\nAlex Ghitza reported:\n\n```\nsage -t  devel/sage-main/sage/numerical/optimize.py\n**********************************************************************\nFile \"optimize.py\", line 309:\n~    sage: minimize_constrained(f, [[None,None],[4,10]],[5,5])\nExpected:\n~    (4.854..., 4.854...)\nGot:\n~    (4.83976831157, 4.83976831157)\n**********************************************************************\n1 items had failures:\n~   1 of  11 in __main__.example_6\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_optimize.py\n~         [2.3 s]\nexit code: 256 \n```\n\n\nPatch coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2564\n\n",
    "created_at": "2008-03-17T03:35:40Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "Sage 2.10.4.rc0: fix numerical noise doctest failure in numerical/optimize.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2564",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Alex Ghitza reported:

```
sage -t  devel/sage-main/sage/numerical/optimize.py
**********************************************************************
File "optimize.py", line 309:
~    sage: minimize_constrained(f, [[None,None],[4,10]],[5,5])
Expected:
~    (4.854..., 4.854...)
Got:
~    (4.83976831157, 4.83976831157)
**********************************************************************
1 items had failures:
~   1 of  11 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_optimize.py
~         [2.3 s]
exit code: 256 
```


Patch coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2564





---

archive/issue_comments_017478.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-17T03:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2564#issuecomment-17478",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017479.json:
```json
{
    "body": "Attachment [trac_2564.patch](tarball://root/attachments/some-uuid/ticket2564/trac_2564.patch) by @rlmill created at 2008-03-17 03:44:40",
    "created_at": "2008-03-17T03:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2564#issuecomment-17479",
    "user": "@rlmill"
}
```

Attachment [trac_2564.patch](tarball://root/attachments/some-uuid/ticket2564/trac_2564.patch) by @rlmill created at 2008-03-17 03:44:40



---

archive/issue_comments_017480.json:
```json
{
    "body": "For the record: I am not happy that we have to dial down the precision for this computation so much. So if anybody can come up with a numerically more stable example it would be great.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-17T03:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2564#issuecomment-17480",
    "user": "mabshoff"
}
```

For the record: I am not happy that we have to dial down the precision for this computation so much. So if anybody can come up with a numerically more stable example it would be great.

Cheers,

Michael



---

archive/issue_comments_017481.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-17T03:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2564#issuecomment-17481",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017482.json:
```json
{
    "body": "Merged in Sage 2.10.4.final",
    "created_at": "2008-03-17T03:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2564#issuecomment-17482",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.final
