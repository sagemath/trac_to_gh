# Issue 1986: Numerical noise in fast evaluation code.

archive/issues_001986.json:
```json
{
    "body": "Assignee: failure\n\nTested on Fedora 7 and 8 32 bits:\n\n```\nsage -t  devel/sage-main/sage/ext/fast_eval.pyx             **********************************************************************\nFile \"fast_eval.pyx\", line 919:\n     sage: f(pi/4)\nExpected:\n     1.00000000000000...\nGot:\n     1.0\n**********************************************************************\nFile \"fast_eval.pyx\", line 1013:\n     sage: f(tanh(0.5))\nExpected:\n     0.5\nGot:\n     0.49999999999999994\n**********************************************************************\n2 items had failures:\n    1 of   3 in __main__.example_29\n    1 of   3 in __main__.example_38\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file .doctest_fast_eval.pyx\n          [2.0 s]\nexit code: 256\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n         sage -t  devel/sage-main/sage/ext/fast_eval.pyx\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1986\n\n",
    "created_at": "2008-01-30T18:16:24Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Numerical noise in fast evaluation code.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1986",
    "user": "jsp"
}
```
Assignee: failure

Tested on Fedora 7 and 8 32 bits:

```
sage -t  devel/sage-main/sage/ext/fast_eval.pyx             **********************************************************************
File "fast_eval.pyx", line 919:
     sage: f(pi/4)
Expected:
     1.00000000000000...
Got:
     1.0
**********************************************************************
File "fast_eval.pyx", line 1013:
     sage: f(tanh(0.5))
Expected:
     0.5
Got:
     0.49999999999999994
**********************************************************************
2 items had failures:
    1 of   3 in __main__.example_29
    1 of   3 in __main__.example_38
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_fast_eval.pyx
          [2.0 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


         sage -t  devel/sage-main/sage/ext/fast_eval.pyx
```



Issue created by migration from https://trac.sagemath.org/ticket/1986





---

archive/issue_comments_012861.json:
```json
{
    "body": "For the \n\n```\nExpected:\n     1.00000000000000...\nGot:\n     1.0\n```\n\nI thought the ... would take care of it. I'd be happy to make a patch, if someone could explain how the anti-numerical noise ... works in the doctests.",
    "created_at": "2008-01-31T07:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1986#issuecomment-12861",
    "user": "robertwb"
}
```

For the 

```
Expected:
     1.00000000000000...
Got:
     1.0
```

I thought the ... would take care of it. I'd be happy to make a patch, if someone could explain how the anti-numerical noise ... works in the doctests.



---

archive/issue_comments_012862.json:
```json
{
    "body": "Attachment [trac-1986.patch](tarball://root/attachments/some-uuid/ticket1986/trac-1986.patch) by was created at 2008-02-02 08:20:50",
    "created_at": "2008-02-02T08:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1986#issuecomment-12862",
    "user": "was"
}
```

Attachment [trac-1986.patch](tarball://root/attachments/some-uuid/ticket1986/trac-1986.patch) by was created at 2008-02-02 08:20:50



---

archive/issue_comments_012863.json:
```json
{
    "body": "The patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-02T08:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1986#issuecomment-12863",
    "user": "mabshoff"
}
```

The patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_012864.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-02T08:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1986#issuecomment-12864",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012865.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc5",
    "created_at": "2008-02-02T08:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1986#issuecomment-12865",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc5
