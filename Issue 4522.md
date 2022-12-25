# Issue 4522: [with patch, needs review] polynomial interface improvements

archive/issues_004522.json:
```json
{
    "body": "Assignee: @burcin\n\nAttached patch makes the following changes to improve the user interface of the polynomial classes:\n\n* Remove .name() method, since .variable_name() already provides same functionality.\n* make the .degree() function of univariate polynomials accept one argument,\n  the generator, to be consistent with the .degree() of multivariate\n  polynomials.\n* Add an .is_monomial() method to univariate polynomials.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4522\n\n",
    "created_at": "2008-11-14T09:17:02Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch, needs review] polynomial interface improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4522",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

Attached patch makes the following changes to improve the user interface of the polynomial classes:

* Remove .name() method, since .variable_name() already provides same functionality.
* make the .degree() function of univariate polynomials accept one argument,
  the generator, to be consistent with the .degree() of multivariate
  polynomials.
* Add an .is_monomial() method to univariate polynomials.


Issue created by migration from https://trac.sagemath.org/ticket/4522





---

archive/issue_comments_033497.json:
```json
{
    "body": "One more change I forgot to specify above:\n* make the .polynomial() function of univariate polynomials behave the same way as that of multivariate polynomials. (I.e., return a univariate polynomial with a coefficient ring in the rest of the generators of the same parent, which simply means returning self in this case.)",
    "created_at": "2008-11-14T09:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4522#issuecomment-33497",
    "user": "https://github.com/burcin"
}
```

One more change I forgot to specify above:
* make the .polynomial() function of univariate polynomials behave the same way as that of multivariate polynomials. (I.e., return a univariate polynomial with a coefficient ring in the rest of the generators of the same parent, which simply means returning self in this case.)



---

archive/issue_comments_033498.json:
```json
{
    "body": "REFEREE REPORT:\n\nThis looks very good. Positive review *subject* to you posting an additional patch that puts the name method back in and has a deprecation warning with a doctest of this.  We'll delete that in a few months.",
    "created_at": "2008-11-28T03:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4522#issuecomment-33498",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

This looks very good. Positive review *subject* to you posting an additional patch that puts the name method back in and has a deprecation warning with a doctest of this.  We'll delete that in a few months.



---

archive/issue_comments_033499.json:
```json
{
    "body": "Oh yes, by the way, I doctested all of the rings directory after this patch and it works 100%.",
    "created_at": "2008-11-28T03:59:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4522#issuecomment-33499",
    "user": "https://github.com/williamstein"
}
```

Oh yes, by the way, I doctested all of the rings directory after this patch and it works 100%.



---

archive/issue_comments_033500.json:
```json
{
    "body": "Attachment [trac_4522-polynomial_interface.patch](tarball://root/attachments/some-uuid/ticket4522/trac_4522-polynomial_interface.patch) by @burcin created at 2008-11-28 12:41:51\n\nmake the interface of polynomials more consistent",
    "created_at": "2008-11-28T12:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4522#issuecomment-33500",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_4522-polynomial_interface.patch](tarball://root/attachments/some-uuid/ticket4522/trac_4522-polynomial_interface.patch) by @burcin created at 2008-11-28 12:41:51

make the interface of polynomials more consistent



---

archive/issue_comments_033501.json:
```json
{
    "body": "New version of the patch with the deprecation warning, and doctests for it.\n\nI'm marking this positivie review, since William didn't state that he wanted to see the patch again. :)",
    "created_at": "2008-11-28T12:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4522#issuecomment-33501",
    "user": "https://github.com/burcin"
}
```

New version of the patch with the deprecation warning, and doctests for it.

I'm marking this positivie review, since William didn't state that he wanted to see the patch again. :)



---

archive/issue_comments_033502.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc0",
    "created_at": "2008-11-28T20:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4522#issuecomment-33502",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.rc0



---

archive/issue_comments_033503.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-28T20:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4522#issuecomment-33503",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010285.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-28T20:51:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4522",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4522#event-10285"
}
```
