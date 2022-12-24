# Issue 6244: conjugate() in sage-4.0 is broken

archive/issues_006244.json:
```json
{
    "body": "CC:  @ncalexan\n\nKeywords: conjugate, pynac\n\n1) pynac  .conjugate() method returns wrong answer:\n\n\n```\nf(x) = function('f',x)\nf(x).conjugate()\n\nf(conjugate(x))\n```\n\n\nAbove is certainly not true. For example: f(x) = I + x implies\nf(x).conjugate() = -I + conjugate(x) which is not equal to\nf(conjugate(x))\n\n\n2)  view() causes SIGSEGV crash\n\n\n```\nf(x) = function('f',x)\ng(x) = f(x).conjugate()\nview( g(x) )\nboom!!\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6244\n\n",
    "created_at": "2009-06-08T01:40:44Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "conjugate() in sage-4.0 is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6244",
    "user": "@golam-m-hossain"
}
```
CC:  @ncalexan

Keywords: conjugate, pynac

1) pynac  .conjugate() method returns wrong answer:


```
f(x) = function('f',x)
f(x).conjugate()

f(conjugate(x))
```


Above is certainly not true. For example: f(x) = I + x implies
f(x).conjugate() = -I + conjugate(x) which is not equal to
f(conjugate(x))


2)  view() causes SIGSEGV crash


```
f(x) = function('f',x)
g(x) = f(x).conjugate()
view( g(x) )
boom!!
```



Issue created by migration from https://trac.sagemath.org/ticket/6244





---

archive/issue_comments_049864.json:
```json
{
    "body": "I have a fix for (1) above, don't know about (2) yet. Same issue effects `.real_part()`, `.imag_part()`, etc. functions.",
    "created_at": "2009-06-13T22:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6244#issuecomment-49864",
    "user": "@burcin"
}
```

I have a fix for (1) above, don't know about (2) yet. Same issue effects `.real_part()`, `.imag_part()`, etc. functions.



---

archive/issue_comments_049865.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-13T22:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6244#issuecomment-49865",
    "user": "@burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049866.json:
```json
{
    "body": "Set assignee to @burcin.",
    "created_at": "2009-06-13T22:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6244#issuecomment-49866",
    "user": "@burcin"
}
```

Set assignee to @burcin.



---

archive/issue_comments_049867.json:
```json
{
    "body": "Attachment [trac_6244-conjugate.patch](tarball://root/attachments/some-uuid/ticket6244/trac_6244-conjugate.patch) by @burcin created at 2009-06-14 20:52:43",
    "created_at": "2009-06-14T20:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6244#issuecomment-49867",
    "user": "@burcin"
}
```

Attachment [trac_6244-conjugate.patch](tarball://root/attachments/some-uuid/ticket6244/trac_6244-conjugate.patch) by @burcin created at 2009-06-14 20:52:43



---

archive/issue_comments_049868.json:
```json
{
    "body": "This is fixed in the new pynac package here:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.p0.spkg\n\nSince the package also contains fixes for #6256 and #6211, the doctests should be run with those patches applied.\n\nBesides adding doctests for the fix, the patch cleans up symbolic functions and adds correct conversions for asin, asinh, acos, acosh, and atan.\n\n\nNick, can you review this?",
    "created_at": "2009-06-14T21:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6244#issuecomment-49868",
    "user": "@burcin"
}
```

This is fixed in the new pynac package here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.p0.spkg

Since the package also contains fixes for #6256 and #6211, the doctests should be run with those patches applied.

Besides adding doctests for the fix, the patch cleans up symbolic functions and adds correct conversions for asin, asinh, acos, acosh, and atan.


Nick, can you review this?



---

archive/issue_comments_049869.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-14T21:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6244#issuecomment-49869",
    "user": "@ncalexan"
}
```

Resolution: fixed



---

archive/issue_comments_049870.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2009-06-14T21:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6244#issuecomment-49870",
    "user": "@ncalexan"
}
```

Fine by me.
