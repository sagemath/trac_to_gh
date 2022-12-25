# Issue 5166: Sage 3.3.a4: sage/symbolic/function.pyx doctest failure on OSX

archive/issues_005166.json:
```json
{
    "body": "Assignee: @burcin\n\n\n```\nsage -t -long \"devel/sage/sage/symbolic/function.pyx\"       \n**********************************************************************\nFile \"/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/symbolic/function.pyx\", line 377:\n    sage: f_list[8] # indices here depend on the GiNaC library\nExpected:\n    gamma\nGot nothing\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/symbolic/function.pyx\", line 379:\n    sage: f_list[12]\nExpected:\n    exp\nGot:\n    <function O at 0x8210170>\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/symbolic/function.pyx\", line 442:\n    sage: f_list[14]\nExpected:\n    sin\nGot:\n    <function log at 0xa2a8b30>\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/symbolic/function.pyx\", line 444:\n    sage: f_list[15]\nExpected:\n    cos\nGot:\n    sin\n**********************************************************************\n2 items had failures:\n   2 of   6 in __main__.example_6\n   2 of   6 in __main__.example_7\n***Test Failed*** 4 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5166\n\n",
    "created_at": "2009-02-03T17:32:50Z",
    "labels": [
        "component: calculus",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Sage 3.3.a4: sage/symbolic/function.pyx doctest failure on OSX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5166",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @burcin


```
sage -t -long "devel/sage/sage/symbolic/function.pyx"       
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/symbolic/function.pyx", line 377:
    sage: f_list[8] # indices here depend on the GiNaC library
Expected:
    gamma
Got nothing
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/symbolic/function.pyx", line 379:
    sage: f_list[12]
Expected:
    exp
Got:
    <function O at 0x8210170>
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/symbolic/function.pyx", line 442:
    sage: f_list[14]
Expected:
    sin
Got:
    <function log at 0xa2a8b30>
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/symbolic/function.pyx", line 444:
    sage: f_list[15]
Expected:
    cos
Got:
    sin
**********************************************************************
2 items had failures:
   2 of   6 in __main__.example_6
   2 of   6 in __main__.example_7
***Test Failed*** 4 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/5166





---

archive/issue_comments_039511.json:
```json
{
    "body": "Attachment [trac_5166-pynac_function_doctest_failure.patch](tarball://root/attachments/some-uuid/ticket5166/trac_5166-pynac_function_doctest_failure.patch) by @burcin created at 2009-02-04 08:50:50",
    "created_at": "2009-02-04T08:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5166#issuecomment-39511",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_5166-pynac_function_doctest_failure.patch](tarball://root/attachments/some-uuid/ticket5166/trac_5166-pynac_function_doctest_failure.patch) by @burcin created at 2009-02-04 08:50:50



---

archive/issue_comments_039512.json:
```json
{
    "body": "New doctests look good, and pass.  (Under Linux; I didn't try OSX.)\n\nPositive review.",
    "created_at": "2009-02-05T06:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5166#issuecomment-39512",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

New doctests look good, and pass.  (Under Linux; I didn't try OSX.)

Positive review.



---

archive/issue_comments_039513.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6. It also fixes the issue on OSX.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-05T10:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5166#issuecomment-39513",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha6. It also fixes the issue on OSX.

Cheers,

Michael



---

archive/issue_comments_039514.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-05T10:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5166#issuecomment-39514",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005416.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-05T10:37:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5166",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5166#event-5416"
}
```
