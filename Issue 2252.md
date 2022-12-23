# Issue 2252: sage 2.10.2.rc0: rings/number_field/number_field_ideal.py failure

archive/issues_002252.json:
```json
{
    "body": "Assignee: craigcitro\n\n\n```\nsage -t -long devel/sage-main/sage/rings/number_field/number_field_ideal.py\n**********************************************************************\nFile \"number_field_ideal.py\", line 868:\n    sage: I.prime_factors()\nExpected:\n    [Fractional ideal (w)]\nGot:\n    [Fractional ideal (-w)]\n**********************************************************************\n1 items had failures:\n   1 of   3 in __main__.example_32\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_number_field_ideal.py\n         [6.6 s]\nexit code: 256\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2252\n\n",
    "created_at": "2008-02-21T19:33:49Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "sage 2.10.2.rc0: rings/number_field/number_field_ideal.py failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2252",
    "user": "mabshoff"
}
```
Assignee: craigcitro


```
sage -t -long devel/sage-main/sage/rings/number_field/number_field_ideal.py
**********************************************************************
File "number_field_ideal.py", line 868:
    sage: I.prime_factors()
Expected:
    [Fractional ideal (w)]
Got:
    [Fractional ideal (-w)]
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_32
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_number_field_ideal.py
         [6.6 s]
exit code: 256
```


Issue created by migration from https://trac.sagemath.org/ticket/2252





---

archive/issue_comments_014918.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-21T23:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2252#issuecomment-14918",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_014919.json:
```json
{
    "body": "The answer is still mathematically correct, and it's what sage is producing, so there's nothing \"wrong\" with it. However, there's something slightly unsavory (for me) about this -- tracing through the code, Pari doesn't seem to be producing the minus sign. I'm not sure where it's coming from.",
    "created_at": "2008-02-22T00:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2252#issuecomment-14919",
    "user": "craigcitro"
}
```

The answer is still mathematically correct, and it's what sage is producing, so there's nothing "wrong" with it. However, there's something slightly unsavory (for me) about this -- tracing through the code, Pari doesn't seem to be producing the minus sign. I'm not sure where it's coming from.



---

archive/issue_comments_014920.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-22T00:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2252#issuecomment-14920",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014921.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-22T00:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2252#issuecomment-14921",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014922.json:
```json
{
    "body": "Merged in Sage 2.10.2.rc0",
    "created_at": "2008-02-22T00:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2252#issuecomment-14922",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.rc0
