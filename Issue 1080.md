# Issue 1080: inconsistent doctest failure in sage/misc/sage_eval.py

archive/issues_001080.json:
```json
{
    "body": "Assignee: cwitty\n\nOn one of my machines (64-bit x86 Debian testing), doctesting sage/misc/sage_eval.py sometimes fails with:\n\n```\n**********************************************************************\nFile \"sage_eval.py\", line 92:\n    sage: ff = gap.eval('x:=IndeterminatesOfPolynomialRing(R);; f:=x^2+1;'); ff\nExpected:\n    'x^2+1'\nGot:\n    '1'\n**********************************************************************\nFile \"sage_eval.py\", line 94:\n    sage: sage_eval(ff, locals={'x':x})\nExpected:\n    x^2 + 1\nGot:\n    1\n**********************************************************************\nFile \"sage_eval.py\", line 96:\n    sage: eval(ff)\nExpected:\n    Traceback (most recent call last):\n    ...\n    RuntimeError: Use ** for exponentiation, not '^', which means xor\n    in Python, and has the wrong precedence.\nGot:\n    1\n**********************************************************************\n1 items had failures:\n   3 of  27 in __main__.example_1\n```\n\n\n(This fails about half the times I run it.)\n\nIt looks like some sort of timing issue.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1080\n\n",
    "created_at": "2007-11-03T17:14:28Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "inconsistent doctest failure in sage/misc/sage_eval.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1080",
    "user": "cwitty"
}
```
Assignee: cwitty

On one of my machines (64-bit x86 Debian testing), doctesting sage/misc/sage_eval.py sometimes fails with:

```
**********************************************************************
File "sage_eval.py", line 92:
    sage: ff = gap.eval('x:=IndeterminatesOfPolynomialRing(R);; f:=x^2+1;'); ff
Expected:
    'x^2+1'
Got:
    '1'
**********************************************************************
File "sage_eval.py", line 94:
    sage: sage_eval(ff, locals={'x':x})
Expected:
    x^2 + 1
Got:
    1
**********************************************************************
File "sage_eval.py", line 96:
    sage: eval(ff)
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: Use ** for exponentiation, not '^', which means xor
    in Python, and has the wrong precedence.
Got:
    1
**********************************************************************
1 items had failures:
   3 of  27 in __main__.example_1
```


(This fails about half the times I run it.)

It looks like some sort of timing issue.

Issue created by migration from https://trac.sagemath.org/ticket/1080





---

archive/issue_comments_006535.json:
```json
{
    "body": "Attachment [1080.patch](tarball://root/attachments/some-uuid/ticket1080/1080.patch) by cwitty created at 2007-11-03 18:42:05\n\nFound it.  Gap sends garbage collection information that starts with an '`@`', followed by one of these characters '123456!\"#$%&', and then terminated by a plus sign.  The code was sometimes grabbing too much data, including part of the real Gap output.",
    "created_at": "2007-11-03T18:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1080#issuecomment-6535",
    "user": "cwitty"
}
```

Attachment [1080.patch](tarball://root/attachments/some-uuid/ticket1080/1080.patch) by cwitty created at 2007-11-03 18:42:05

Found it.  Gap sends garbage collection information that starts with an '`@`', followed by one of these characters '123456!"#$%&', and then terminated by a plus sign.  The code was sometimes grabbing too much data, including part of the real Gap output.



---

archive/issue_comments_006536.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T18:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1080#issuecomment-6536",
    "user": "@williamstein"
}
```

Resolution: fixed
