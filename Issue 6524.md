# Issue 6524: Ratio of two symbolic expressions involving derivative does not simplify

archive/issues_006524.json:
```json
{
    "body": "In new symbolics, ratio of two symbolic expressions involving derivative does not simplify\n\n\n```\nsage: f(x) = function('f', x)\nsage: g = f(x).diff(x)\nsage: h = f(x).diff(x)*sin(x)\nsage: h/g\nsin(x)*D[0](f)(x)/D[0](f)(x)\n```\n\n\n\nHowever, for some ordering it does simplify\n\n\n```\nsage: f(x) = function('f', x)\nsage: g = f(x).diff(x)\nsage: h = sin(x)*f(x).diff(x)\nsage: h/g\nsin(x)\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6524\n\n",
    "created_at": "2009-07-13T12:18:10Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Ratio of two symbolic expressions involving derivative does not simplify",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6524",
    "user": "gmhossain"
}
```
In new symbolics, ratio of two symbolic expressions involving derivative does not simplify


```
sage: f(x) = function('f', x)
sage: g = f(x).diff(x)
sage: h = f(x).diff(x)*sin(x)
sage: h/g
sin(x)*D[0](f)(x)/D[0](f)(x)
```



However, for some ordering it does simplify


```
sage: f(x) = function('f', x)
sage: g = f(x).diff(x)
sage: h = sin(x)*f(x).diff(x)
sage: h/g
sin(x)
```




Issue created by migration from https://trac.sagemath.org/ticket/6524





---

archive/issue_comments_053205.json:
```json
{
    "body": "Attachment [trac_6524-fderivative_compare.patch](tarball://root/attachments/some-uuid/ticket6524/trac_6524-fderivative_compare.patch) by burcin created at 2009-09-19 15:15:46",
    "created_at": "2009-09-19T15:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6524#issuecomment-53205",
    "user": "burcin"
}
```

Attachment [trac_6524-fderivative_compare.patch](tarball://root/attachments/some-uuid/ticket6524/trac_6524-fderivative_compare.patch) by burcin created at 2009-09-19 15:15:46



---

archive/issue_comments_053206.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-19T15:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6524#issuecomment-53206",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_053207.json:
```json
{
    "body": "This is fixed in my pynac tree, attachment:trac_6524-fderivative_compare.patch contains doctests for Sage.\n\nI will post a new pynac package and review instructions soon.",
    "created_at": "2009-09-19T15:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6524#issuecomment-53207",
    "user": "burcin"
}
```

This is fixed in my pynac tree, attachment:trac_6524-fderivative_compare.patch contains doctests for Sage.

I will post a new pynac package and review instructions soon.



---

archive/issue_comments_053208.json:
```json
{
    "body": "Set assignee to burcin.",
    "created_at": "2009-09-19T15:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6524#issuecomment-53208",
    "user": "burcin"
}
```

Set assignee to burcin.



---

archive/issue_comments_053209.json:
```json
{
    "body": "New pynac package available at #6993.",
    "created_at": "2009-09-22T19:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6524#issuecomment-53209",
    "user": "burcin"
}
```

New pynac package available at #6993.



---

archive/issue_comments_053210.json:
```json
{
    "body": "Looks like it's fixed.  Pending of course positive review of the Pynac package as a whole.",
    "created_at": "2009-09-23T02:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6524#issuecomment-53210",
    "user": "kcrisman"
}
```

Looks like it's fixed.  Pending of course positive review of the Pynac package as a whole.



---

archive/issue_comments_053211.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-25T22:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6524#issuecomment-53211",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053212.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6524#issuecomment-53212",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
