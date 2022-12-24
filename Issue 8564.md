# Issue 8564: fix atan2() conversions between Sage and SymPy

archive/issues_008564.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nHi,\n\nplease apply the attached patch. The corresponding test is in sympy in sympy/test_external/test_sage.py. It'd be cool to execute that file automatically in sage doctests, not sure currently how to do it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8564\n\n",
    "created_at": "2010-03-20T02:29:43Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "fix atan2() conversions between Sage and SymPy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8564",
    "user": "certik"
}
```
Assignee: AlexGhitza

Hi,

please apply the attached patch. The corresponding test is in sympy in sympy/test_external/test_sage.py. It'd be cool to execute that file automatically in sage doctests, not sure currently how to do it.

Issue created by migration from https://trac.sagemath.org/ticket/8564





---

archive/issue_comments_077535.json:
```json
{
    "body": "Attachment [sympy1.patch](tarball://root/attachments/some-uuid/ticket8564/sympy1.patch) by burcin created at 2010-04-02 16:49:32\n\nondrej's patch with a header",
    "created_at": "2010-04-02T16:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77535",
    "user": "burcin"
}
```

Attachment [sympy1.patch](tarball://root/attachments/some-uuid/ticket8564/sympy1.patch) by burcin created at 2010-04-02 16:49:32

ondrej's patch with a header



---

archive/issue_comments_077536.json:
```json
{
    "body": "Attachment [trac_8564-doctests.patch](tarball://root/attachments/some-uuid/ticket8564/trac_8564-doctests.patch) by burcin created at 2010-04-02 16:49:53\n\ndoctest",
    "created_at": "2010-04-02T16:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77536",
    "user": "burcin"
}
```

Attachment [trac_8564-doctests.patch](tarball://root/attachments/some-uuid/ticket8564/trac_8564-doctests.patch) by burcin created at 2010-04-02 16:49:53

doctest



---

archive/issue_comments_077537.json:
```json
{
    "body": "Changing component from algebra to interfaces.",
    "created_at": "2010-04-02T16:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77537",
    "user": "burcin"
}
```

Changing component from algebra to interfaces.



---

archive/issue_comments_077538.json:
```json
{
    "body": "I uploaded two patches, \n* attachment:trac_8564-atan2_conversion.patch is Ondrej's fix including a header with a commit message \n* attachment:trac_8564-doctests.patch adds a doctest.\n\nI give a positive review to Ondrej's patch, if someone can review the doctest I added this will be ready to go.\n\nThe patches to be merged are (in this order):\n* attachment:trac_8564-atan2_conversion.patch\n* attachment:trac_8564-doctests.patch\n\nThe doctest patch depends on #8565.",
    "created_at": "2010-04-02T16:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77538",
    "user": "burcin"
}
```

I uploaded two patches, 
* attachment:trac_8564-atan2_conversion.patch is Ondrej's fix including a header with a commit message 
* attachment:trac_8564-doctests.patch adds a doctest.

I give a positive review to Ondrej's patch, if someone can review the doctest I added this will be ready to go.

The patches to be merged are (in this order):
* attachment:trac_8564-atan2_conversion.patch
* attachment:trac_8564-doctests.patch

The doctest patch depends on #8565.



---

archive/issue_comments_077539.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-02T16:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77539",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077540.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-10T01:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77540",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077541.json:
```json
{
    "body": "This seems fine, works well and tests the appropriate thing (i.e. not arctan2(2,3), but the symbolic thing).  Positive review to both.\n\nQuestion about the Sympy doctest file Ondrej mentions above - it doesn't have \n\n```\ncheck_expression(\"atan2(y,x)\", \"y x\")\n```\n\nor whatever would work, in test_functions or something like that.  Should it?",
    "created_at": "2010-06-10T01:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77541",
    "user": "kcrisman"
}
```

This seems fine, works well and tests the appropriate thing (i.e. not arctan2(2,3), but the symbolic thing).  Positive review to both.

Question about the Sympy doctest file Ondrej mentions above - it doesn't have 

```
check_expression("atan2(y,x)", "y x")
```

or whatever would work, in test_functions or something like that.  Should it?



---

archive/issue_comments_077542.json:
```json
{
    "body": "Thanks!\n\nBtw, the check_expression() for atan2 is in the latest git sympy, so I need to update the Sage package for it. There were some unrelated mpmath problems with it, that I have to solve first.\n\nOndrej",
    "created_at": "2010-06-10T02:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77542",
    "user": "certik"
}
```

Thanks!

Btw, the check_expression() for atan2 is in the latest git sympy, so I need to update the Sage package for it. There were some unrelated mpmath problems with it, that I have to solve first.

Ondrej



---

archive/issue_comments_077543.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T03:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77543",
    "user": "mpatel"
}
```

Resolution: fixed
