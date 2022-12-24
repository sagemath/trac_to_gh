# Issue 6877: Boolean function for crypto, small bugfixes and improvement

archive/issues_006877.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  malb\n\nNot even in sage, but already a bug fix...\n\nThe bug comes from the different ordering for enumerating finite fields depending on the implementation (givaro or ntl in this case).\n\nThe improvements are:\n\n- an option to output the truth table in hexadecimal\n- the computation of the algebraic normal form\n\nIssue created by migration from https://trac.sagemath.org/ticket/6877\n\n",
    "created_at": "2009-09-03T12:21:59Z",
    "labels": [
        "cryptography",
        "major",
        "bug"
    ],
    "title": "Boolean function for crypto, small bugfixes and improvement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6877",
    "user": "ylchapuy"
}
```
Assignee: somebody

CC:  malb

Not even in sage, but already a bug fix...

The bug comes from the different ordering for enumerating finite fields depending on the implementation (givaro or ntl in this case).

The improvements are:

- an option to output the truth table in hexadecimal
- the computation of the algebraic normal form

Issue created by migration from https://trac.sagemath.org/ticket/6877





---

archive/issue_comments_056770.json:
```json
{
    "body": "Attachment [trac_6877_Boolean_function_bugfix.patch](tarball://root/attachments/some-uuid/ticket6877/trac_6877_Boolean_function_bugfix.patch) by ylchapuy created at 2009-09-03 12:24:31",
    "created_at": "2009-09-03T12:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6877#issuecomment-56770",
    "user": "ylchapuy"
}
```

Attachment [trac_6877_Boolean_function_bugfix.patch](tarball://root/attachments/some-uuid/ticket6877/trac_6877_Boolean_function_bugfix.patch) by ylchapuy created at 2009-09-03 12:24:31



---

archive/issue_comments_056771.json:
```json
{
    "body": "you need to apply #6514 (both patches) first",
    "created_at": "2009-09-03T12:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6877#issuecomment-56771",
    "user": "ylchapuy"
}
```

you need to apply #6514 (both patches) first



---

archive/issue_comments_056772.json:
```json
{
    "body": "**Review**\n* patch looks good\n* applies cleanly against 4.1.1 + #6514\n* doctests pass on sage.math",
    "created_at": "2009-09-03T14:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6877#issuecomment-56772",
    "user": "malb"
}
```

**Review**
* patch looks good
* applies cleanly against 4.1.1 + #6514
* doctests pass on sage.math



---

archive/issue_comments_056773.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-03T21:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6877#issuecomment-56773",
    "user": "mvngu"
}
```

Resolution: fixed
