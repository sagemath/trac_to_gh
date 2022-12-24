# Issue 1003: [with patch] GF(2^n) elements powering overflow

archive/issues_001003.json:
```json
{
    "body": "Assignee: @malb\n\nCarl Witty reported:\n\n```\nOn my 32-bit linux box, I had an additional failure:\n **********************************************************************\nFile \"finite_field_element.py\", line 18:\n    sage: c = a^e\nException raised:\n    Traceback (most recent call last):\n      File \"/home/cwitty/sage/local/lib/python2.5/doctest.py\", line\n1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[9]>\", line 1, in <module>\n        c = a**e###line 18:\n    sage: c = a^e\n      File \"finite_field_ntl_gf2e.pyx\", line 925, in\nfinite_field_ntl_gf2e.FiniteField_ntl_gf2eElement.__pow__\n        GF2E_power(r.x, (<FiniteField_ntl_gf2eElement>self).x, exp)\n    OverflowError: long int too large to convert to int\n**********************************************************************\n```\n\n\nThe attached patch should fix that issue.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1003\n\n",
    "created_at": "2007-10-26T09:23:15Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.10",
    "title": "[with patch] GF(2^n) elements powering overflow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1003",
    "user": "@malb"
}
```
Assignee: @malb

Carl Witty reported:

```
On my 32-bit linux box, I had an additional failure:
 **********************************************************************
File "finite_field_element.py", line 18:
    sage: c = a^e
Exception raised:
    Traceback (most recent call last):
      File "/home/cwitty/sage/local/lib/python2.5/doctest.py", line
1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[9]>", line 1, in <module>
        c = a**e###line 18:
    sage: c = a^e
      File "finite_field_ntl_gf2e.pyx", line 925, in
finite_field_ntl_gf2e.FiniteField_ntl_gf2eElement.__pow__
        GF2E_power(r.x, (<FiniteField_ntl_gf2eElement>self).x, exp)
    OverflowError: long int too large to convert to int
**********************************************************************
```


The attached patch should fix that issue.

Issue created by migration from https://trac.sagemath.org/ticket/1003





---

archive/issue_comments_006111.json:
```json
{
    "body": "Attachment [1003.patch](tarball://root/attachments/some-uuid/ticket1003/1003.patch) by @malb created at 2007-10-26 09:27:03",
    "created_at": "2007-10-26T09:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1003#issuecomment-6111",
    "user": "@malb"
}
```

Attachment [1003.patch](tarball://root/attachments/some-uuid/ticket1003/1003.patch) by @malb created at 2007-10-26 09:27:03



---

archive/issue_comments_006112.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T04:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1003#issuecomment-6112",
    "user": "cwitty"
}
```

Resolution: fixed
