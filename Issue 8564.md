# Issue 8564: fix atan2() conversions between Sage and SymPy

archive/issues_008564.json:
```json
{
    "body": "Assignee: @aghitza\n\nHi,\n\nplease apply the attached patch. The corresponding test is in sympy in sympy/test_external/test_sage.py. It'd be cool to execute that file automatically in sage doctests, not sure currently how to do it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8564\n\n",
    "closed_at": "2010-07-21T03:31:39Z",
    "created_at": "2010-03-20T02:29:43Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "fix atan2() conversions between Sage and SymPy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8564",
    "user": "https://github.com/certik"
}
```
Assignee: @aghitza

Hi,

please apply the attached patch. The corresponding test is in sympy in sympy/test_external/test_sage.py. It'd be cool to execute that file automatically in sage doctests, not sure currently how to do it.

Issue created by migration from https://trac.sagemath.org/ticket/8564





---

archive/issue_comments_077407.json:
```json
{
    "body": "Attachment [sympy1.patch](tarball://root/attachments/some-uuid/ticket8564/sympy1.patch) by @burcin created at 2010-04-02 16:49:32\n\nondrej's patch with a header",
    "created_at": "2010-04-02T16:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77407",
    "user": "https://github.com/burcin"
}
```

Attachment [sympy1.patch](tarball://root/attachments/some-uuid/ticket8564/sympy1.patch) by @burcin created at 2010-04-02 16:49:32

ondrej's patch with a header



---

archive/issue_comments_077408.json:
```json
{
    "body": "Attachment [trac_8564-doctests.patch](tarball://root/attachments/some-uuid/ticket8564/trac_8564-doctests.patch) by @burcin created at 2010-04-02 16:49:53\n\ndoctest",
    "created_at": "2010-04-02T16:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77408",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8564-doctests.patch](tarball://root/attachments/some-uuid/ticket8564/trac_8564-doctests.patch) by @burcin created at 2010-04-02 16:49:53

doctest



---

archive/issue_events_020661.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2010-04-02T16:54:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "milestone": "sage-4.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8564#event-20661"
}
```



---

archive/issue_comments_077409.json:
```json
{
    "body": "Changing component from algebra to interfaces.",
    "created_at": "2010-04-02T16:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77409",
    "user": "https://github.com/burcin"
}
```

Changing component from algebra to interfaces.



---

archive/issue_comments_077410.json:
```json
{
    "body": "I uploaded two patches, \n* attachment:trac_8564-atan2_conversion.patch is Ondrej's fix including a header with a commit message \n* attachment:trac_8564-doctests.patch adds a doctest.\n\nI give a positive review to Ondrej's patch, if someone can review the doctest I added this will be ready to go.\n\nThe patches to be merged are (in this order):\n* attachment:trac_8564-atan2_conversion.patch\n* attachment:trac_8564-doctests.patch\n\nThe doctest patch depends on #8565.",
    "created_at": "2010-04-02T16:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77410",
    "user": "https://github.com/burcin"
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

archive/issue_comments_077411.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-02T16:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77411",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077412.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-10T01:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77412",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077413.json:
```json
{
    "body": "This seems fine, works well and tests the appropriate thing (i.e. not arctan2(2,3), but the symbolic thing).  Positive review to both.\n\nQuestion about the Sympy doctest file Ondrej mentions above - it doesn't have \n\n```\ncheck_expression(\"atan2(y,x)\", \"y x\")\n```\nor whatever would work, in test_functions or something like that.  Should it?",
    "created_at": "2010-06-10T01:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77413",
    "user": "https://github.com/kcrisman"
}
```

This seems fine, works well and tests the appropriate thing (i.e. not arctan2(2,3), but the symbolic thing).  Positive review to both.

Question about the Sympy doctest file Ondrej mentions above - it doesn't have 

```
check_expression("atan2(y,x)", "y x")
```
or whatever would work, in test_functions or something like that.  Should it?



---

archive/issue_comments_077414.json:
```json
{
    "body": "Thanks!\n\nBtw, the check_expression() for atan2 is in the latest git sympy, so I need to update the Sage package for it. There were some unrelated mpmath problems with it, that I have to solve first.\n\nOndrej",
    "created_at": "2010-06-10T02:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77414",
    "user": "https://github.com/certik"
}
```

Thanks!

Btw, the check_expression() for atan2 is in the latest git sympy, so I need to update the Sage package for it. There were some unrelated mpmath problems with it, that I have to solve first.

Ondrej



---

archive/issue_events_020662.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-21T03:31:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8564#event-20662"
}
```



---

archive/issue_comments_077415.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T03:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8564#issuecomment-77415",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
