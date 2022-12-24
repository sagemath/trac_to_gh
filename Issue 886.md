# Issue 886: 2.8.7-alpha0: doctest failure in rings/integer_mod.pyx (expecting wrong type)

archive/issues_000886.json:
```json
{
    "body": "Assignee: failure\n\nA trivial doctest failure.  On sage.math:\n\n```\nFile \"integer_mod.pyx\", line 460:\n    sage: type(a.polynomial())\nExpected:\n    <class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_dense_mod_p'>\nGot:\n    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/886\n\n",
    "created_at": "2007-10-13T20:25:31Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "2.8.7-alpha0: doctest failure in rings/integer_mod.pyx (expecting wrong type)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/886",
    "user": "cwitty"
}
```
Assignee: failure

A trivial doctest failure.  On sage.math:

```
File "integer_mod.pyx", line 460:
    sage: type(a.polynomial())
Expected:
    <class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_dense_mod_p'>
Got:
    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>
```


Issue created by migration from https://trac.sagemath.org/ticket/886





---

archive/issue_comments_005472.json:
```json
{
    "body": "Attachment [6932.patch](tarball://root/attachments/some-uuid/ticket886/6932.patch) by cwitty created at 2007-10-13 22:52:00\n\nThe obvious fix.",
    "created_at": "2007-10-13T22:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/886#issuecomment-5472",
    "user": "cwitty"
}
```

Attachment [6932.patch](tarball://root/attachments/some-uuid/ticket886/6932.patch) by cwitty created at 2007-10-13 22:52:00

The obvious fix.



---

archive/issue_comments_005473.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-14T22:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/886#issuecomment-5473",
    "user": "@williamstein"
}
```

Resolution: fixed
