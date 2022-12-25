# Issue 6404: Typeseting for conjugate() of symbolic function is inadequate

archive/issues_006404.json:
```json
{
    "body": "In current Sage (4.0.2), while typesetting conjugate() of\nan symbolic expression, latex symbol \"\\bar\" is used\n\n```\nsage: latex(x.conjugate())\n\\bar{x}\n```\n\n\nThe problem with \"\\bar\" is that it is of fixed width and not scalable. For example, this is inadequate for symbolic functions\n\n\n```\nsage: x,y=var('x,y')\nsage: f = function('psi',x,y)\nsage: latex(f.conjugate())\n\\bar{\\psi\\left(x, y\\right)\n```\n\n\nA better solution is to use \"\\overline\" instead of \"\\bar\".\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6404\n\n",
    "created_at": "2009-06-25T14:22:31Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "Typeseting for conjugate() of symbolic function is inadequate",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6404",
    "user": "https://github.com/golam-m-hossain"
}
```
In current Sage (4.0.2), while typesetting conjugate() of
an symbolic expression, latex symbol "\bar" is used

```
sage: latex(x.conjugate())
\bar{x}
```


The problem with "\bar" is that it is of fixed width and not scalable. For example, this is inadequate for symbolic functions


```
sage: x,y=var('x,y')
sage: f = function('psi',x,y)
sage: latex(f.conjugate())
\bar{\psi\left(x, y\right)
```


A better solution is to use "\overline" instead of "\bar".


Issue created by migration from https://trac.sagemath.org/ticket/6404





---

archive/issue_comments_051334.json:
```json
{
    "body": "Attachment [trac_6404-conjugate_typesetting.patch](tarball://root/attachments/some-uuid/ticket6404/trac_6404-conjugate_typesetting.patch) by @burcin created at 2009-07-28 12:10:22\n\ndoctest fixes for conjugate typesetting change",
    "created_at": "2009-07-28T12:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6404#issuecomment-51334",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6404-conjugate_typesetting.patch](tarball://root/attachments/some-uuid/ticket6404/trac_6404-conjugate_typesetting.patch) by @burcin created at 2009-07-28 12:10:22

doctest fixes for conjugate typesetting change



---

archive/issue_comments_051335.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-28T12:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6404#issuecomment-51335",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_051336.json:
```json
{
    "body": "I have a fix for this in my local pynac tree. I'll make a new pynac package available soon, with some other bug fixes.",
    "created_at": "2009-07-28T12:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6404#issuecomment-51336",
    "user": "https://github.com/burcin"
}
```

I have a fix for this in my local pynac tree. I'll make a new pynac package available soon, with some other bug fixes.



---

archive/issue_comments_051337.json:
```json
{
    "body": "Set assignee to @burcin.",
    "created_at": "2009-07-28T12:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6404#issuecomment-51337",
    "user": "https://github.com/burcin"
}
```

Set assignee to @burcin.



---

archive/issue_comments_051338.json:
```json
{
    "body": "New pynac package is available here:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.p2.spkg\n\nBesides this issue, it includes fixes for #6401, #6243 and #6377. Please apply the patches from those issues too before doctesting.",
    "created_at": "2009-08-01T02:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6404#issuecomment-51338",
    "user": "https://github.com/burcin"
}
```

New pynac package is available here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.p2.spkg

Besides this issue, it includes fixes for #6401, #6243 and #6377. Please apply the patches from those issues too before doctesting.



---

archive/issue_comments_051339.json:
```json
{
    "body": "Looks OK to me.\n\nNote: I am giving partial positive review because I tested this patch against my stable sage-4.1. So if it applies cleanly on Sage-4.1.1.rc1 then that would be full positive from me.",
    "created_at": "2009-08-02T19:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6404#issuecomment-51339",
    "user": "https://github.com/golam-m-hossain"
}
```

Looks OK to me.

Note: I am giving partial positive review because I tested this patch against my stable sage-4.1. So if it applies cleanly on Sage-4.1.1.rc1 then that would be full positive from me.



---

archive/issue_comments_051340.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-03T00:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6404#issuecomment-51340",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_051341.json:
```json
{
    "body": "I applied patches in the following order:\n1. the spkg `pynac-0.1.8.p2.spkg`\n2. `trac_6404-conjugate_typesetting.patch`\n3. `trac_6401-real_imag_typesetting.patch`\n4. `trac_6377-exp_infinity.patch`\n5. `trac_6243-fderivative_hash.patch`\nAll doctests pass in my merge tree. So I'm changing #6404, #6401, #6377 and #6243 to positive review as per Golam's request.",
    "created_at": "2009-08-03T00:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6404#issuecomment-51341",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I applied patches in the following order:
1. the spkg `pynac-0.1.8.p2.spkg`
2. `trac_6404-conjugate_typesetting.patch`
3. `trac_6401-real_imag_typesetting.patch`
4. `trac_6377-exp_infinity.patch`
5. `trac_6243-fderivative_hash.patch`
All doctests pass in my merge tree. So I'm changing #6404, #6401, #6377 and #6243 to positive review as per Golam's request.
