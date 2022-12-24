# Issue 4071: Fix issues in the lisp interface

archive/issues_004071.json:
```json
{
    "body": "Assignee: was\n\n\n```\nFile \"/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py\", line 5:\n    sage: lisp.eval('(* 4 5)')\nExpected:\n    '20'\nGot:\n    '(* 4 5)\\r\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\n20'\n**********************************************************************\nFile \"/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py\", line 22:\n    sage: lisp.eval('(+ %s %s)'%(a.name(), b.name()))\nExpected:\n    '8'\nGot:\n    '(+ sage0 sage1)\\r\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\n8'\n**********************************************************************\nFile \"/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py\", line 27:\n    sage: lisp.eval('(defun factorial (n) (if (= n 1) 1 (* n (factorial (- n 1)))))')\nExpected:\n    'FACTORIAL'\nGot:\n    '(defun factorial (n)\\x08\\x08\\x08\\x1b[C\\x1b[C\\x1b[C (if (= n 1)\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C 1 (* n (factorial (- n 1)\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C)\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C)\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C)\\r\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C)\\r\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\nFACTORIAL'\n**********************************************************************\nFile \"/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py\", line 112:\n    sage: lisp.eval('(+ 2 2)')\nExpected:\n    '4'\nGot:\n    '(+ 2 2)\\r\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\x1b[C\\n4'\n**********************************************************************\nFile \"/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py\", line 390:\n    sage: one == one\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py\", line 394:\n    sage: one < two\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py\", line 400:\n    sage: two == 2\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py\", line 420:\n    sage: lisp(0).bool()\nExpected:\n    False\nGot:\n    True\n**********************************************************************\n4 items had failures:\n   3 of  17 in __main__.example_0\n   1 of   3 in __main__.example_2\n   3 of   9 in __main__.example_23\n   1 of   5 in __main__.example_24\n***Test Failed*** 8 failures.\nFor whitespace errors, see the file /Users/mhansen/sage-3.1.2.rc0/tmp/.doctest_lisp.py\n         [7.4 s]\nexit code: 1024\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4071\n\n",
    "created_at": "2008-09-07T18:09:06Z",
    "labels": [
        "interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Fix issues in the lisp interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4071",
    "user": "mhansen"
}
```
Assignee: was


```
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 5:
    sage: lisp.eval('(* 4 5)')
Expected:
    '20'
Got:
    '(* 4 5)\r\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\n20'
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 22:
    sage: lisp.eval('(+ %s %s)'%(a.name(), b.name()))
Expected:
    '8'
Got:
    '(+ sage0 sage1)\r\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\n8'
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 27:
    sage: lisp.eval('(defun factorial (n) (if (= n 1) 1 (* n (factorial (- n 1)))))')
Expected:
    'FACTORIAL'
Got:
    '(defun factorial (n)\x08\x08\x08\x1b[C\x1b[C\x1b[C (if (= n 1)\x08\x08\x08\x08\x08\x08\x08\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C 1 (* n (factorial (- n 1)\x08\x08\x08\x08\x08\x08\x08\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C)\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C)\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C)\r\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C)\r\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\nFACTORIAL'
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 112:
    sage: lisp.eval('(+ 2 2)')
Expected:
    '4'
Got:
    '(+ 2 2)\r\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\n4'
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 390:
    sage: one == one
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 394:
    sage: one < two
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 400:
    sage: two == 2
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 420:
    sage: lisp(0).bool()
Expected:
    False
Got:
    True
**********************************************************************
4 items had failures:
   3 of  17 in __main__.example_0
   1 of   3 in __main__.example_2
   3 of   9 in __main__.example_23
   1 of   5 in __main__.example_24
***Test Failed*** 8 failures.
For whitespace errors, see the file /Users/mhansen/sage-3.1.2.rc0/tmp/.doctest_lisp.py
         [7.4 s]
exit code: 1024
```


Issue created by migration from https://trac.sagemath.org/ticket/4071





---

archive/issue_comments_029380.json:
```json
{
    "body": "Attachment [trac_4071.patch](tarball://root/attachments/some-uuid/ticket4071/trac_4071.patch) by mhansen created at 2008-09-07 18:10:28",
    "created_at": "2008-09-07T18:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4071#issuecomment-29380",
    "user": "mhansen"
}
```

Attachment [trac_4071.patch](tarball://root/attachments/some-uuid/ticket4071/trac_4071.patch) by mhansen created at 2008-09-07 18:10:28



---

archive/issue_comments_029381.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-07T18:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4071#issuecomment-29381",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029382.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2008-09-07T18:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4071#issuecomment-29382",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_029383.json:
```json
{
    "body": "Patch looks good to me and fixes the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-07T18:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4071#issuecomment-29383",
    "user": "mabshoff"
}
```

Patch looks good to me and fixes the issue.

Cheers,

Michael



---

archive/issue_comments_029384.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-07T23:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4071#issuecomment-29384",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029385.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-07T23:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4071#issuecomment-29385",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc1
