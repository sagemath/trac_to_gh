# Issue 6401: Typesettings of real() and imag() are broken

archive/issues_006401.json:
```json
{
    "body": "Typesetting of real() and imag() methods are broken due to missing parenthesis.\n\n\n```\nsage: latex(x.real())\n\\Rex\n```\n\n\"\\Rex\" is not a valid latex expression. It should be something\nlike \"\\Re\\left(x\\right)\".\n\nSimilar issues are present also for Symbolic functions\n\n```\nsage: f(x) = function('f',x)\nsage: latex( f(x).imag())\n\\Imf\\left(x\\right)\n```\n\nAgain it should be similar to \"\\Im\\left(f\\left(x\\right)\\right)\".\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6401\n\n",
    "created_at": "2009-06-25T11:09:12Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "Typesettings of real() and imag() are broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6401",
    "user": "https://github.com/golam-m-hossain"
}
```
Typesetting of real() and imag() methods are broken due to missing parenthesis.


```
sage: latex(x.real())
\Rex
```

"\Rex" is not a valid latex expression. It should be something
like "\Re\left(x\right)".

Similar issues are present also for Symbolic functions

```
sage: f(x) = function('f',x)
sage: latex( f(x).imag())
\Imf\left(x\right)
```

Again it should be similar to "\Im\left(f\left(x\right)\right)".


Issue created by migration from https://trac.sagemath.org/ticket/6401





---

archive/issue_comments_051310.json:
```json
{
    "body": "Attachment [trac_6401-real_imag_typesetting.patch](tarball://root/attachments/some-uuid/ticket6401/trac_6401-real_imag_typesetting.patch) by @burcin created at 2009-07-28 12:44:48\n\ndoctest fixes for typesetting changes in pynac",
    "created_at": "2009-07-28T12:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6401#issuecomment-51310",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6401-real_imag_typesetting.patch](tarball://root/attachments/some-uuid/ticket6401/trac_6401-real_imag_typesetting.patch) by @burcin created at 2009-07-28 12:44:48

doctest fixes for typesetting changes in pynac



---

archive/issue_comments_051311.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-28T12:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6401#issuecomment-51311",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_051312.json:
```json
{
    "body": "Set assignee to @burcin.",
    "created_at": "2009-07-28T12:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6401#issuecomment-51312",
    "user": "https://github.com/burcin"
}
```

Set assignee to @burcin.



---

archive/issue_comments_051313.json:
```json
{
    "body": "I have a fix for this in my local pynac tree. I will make a new package with a few more bugfixes available soon.",
    "created_at": "2009-07-28T12:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6401#issuecomment-51313",
    "user": "https://github.com/burcin"
}
```

I have a fix for this in my local pynac tree. I will make a new package with a few more bugfixes available soon.



---

archive/issue_comments_051314.json:
```json
{
    "body": "This now depends on the package linked from #6404.\n\nPlease follow the instructions on that ticket to apply & test.",
    "created_at": "2009-08-01T02:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6401#issuecomment-51314",
    "user": "https://github.com/burcin"
}
```

This now depends on the package linked from #6404.

Please follow the instructions on that ticket to apply & test.



---

archive/issue_comments_051315.json:
```json
{
    "body": "Hi Burcin,\n\nI am testing out the new pynac spkg. Seems alright to me so far. Out of curiosity: is there\nany reason to print the extra spaces around the the argument of real() and imag()?\n\n```\nsage: latex(real(x))\n\\Re \\left( x \\right)\n```\n\nGiven it differs a bit from your earlier convention for default typesetting of \nsymbolic function\n\n```\nsage: psi(x) = function('psi',x)\nsage: latex(psi(x))\n\\psi\\left(x\\right)\n```\n\n\nOtherwise, I am ready to give positive review as the output is valid latex expression in\nboth cases.",
    "created_at": "2009-08-02T15:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6401#issuecomment-51315",
    "user": "https://github.com/golam-m-hossain"
}
```

Hi Burcin,

I am testing out the new pynac spkg. Seems alright to me so far. Out of curiosity: is there
any reason to print the extra spaces around the the argument of real() and imag()?

```
sage: latex(real(x))
\Re \left( x \right)
```

Given it differs a bit from your earlier convention for default typesetting of 
symbolic function

```
sage: psi(x) = function('psi',x)
sage: latex(psi(x))
\psi\left(x\right)
```


Otherwise, I am ready to give positive review as the output is valid latex expression in
both cases.



---

archive/issue_comments_051316.json:
```json
{
    "body": "There is no specific reason I chose that format. We can change it in the future if we decide on a convention.",
    "created_at": "2009-08-02T15:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6401#issuecomment-51316",
    "user": "https://github.com/burcin"
}
```

There is no specific reason I chose that format. We can change it in the future if we decide on a convention.



---

archive/issue_comments_051317.json:
```json
{
    "body": "Note: I am giving partial positive review because I tested this patch against my stable sage-4.1. So if it applies cleanly on Sage-4.1.1.rc1 then that would be full positive from me.",
    "created_at": "2009-08-02T19:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6401#issuecomment-51317",
    "user": "https://github.com/golam-m-hossain"
}
```

Note: I am giving partial positive review because I tested this patch against my stable sage-4.1. So if it applies cleanly on Sage-4.1.1.rc1 then that would be full positive from me.



---

archive/issue_comments_051318.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-03T00:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6401#issuecomment-51318",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_051319.json:
```json
{
    "body": "I applied patches in the following order:\n1. the spkg `pynac-0.1.8.p2.spkg` at #6404\n2. `trac_6404-conjugate_typesetting.patch`\n3. `trac_6401-real_imag_typesetting.patch`\n4. `trac_6377-exp_infinity.patch`\n5. `trac_6243-fderivative_hash.patch`\nAll doctests pass in my merge tree. So I'm changing #6404, #6401, #6377 and #6243 to positive review as per Golam's request.",
    "created_at": "2009-08-03T00:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6401#issuecomment-51319",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I applied patches in the following order:
1. the spkg `pynac-0.1.8.p2.spkg` at #6404
2. `trac_6404-conjugate_typesetting.patch`
3. `trac_6401-real_imag_typesetting.patch`
4. `trac_6377-exp_infinity.patch`
5. `trac_6243-fderivative_hash.patch`
All doctests pass in my merge tree. So I'm changing #6404, #6401, #6377 and #6243 to positive review as per Golam's request.
