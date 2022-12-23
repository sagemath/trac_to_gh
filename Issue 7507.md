# Issue 7507: can't forget some assumptions

archive/issues_007507.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  kcrisman robert.marik\n\nKeywords: maxima, assume\n\nReported by Mike Witt on sage-support:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: n=var('n')\nsage: assumptions()\n[]\nsage: foo=sin((-1)*n*pi)\nsage: foo.simplify()\n-sin(pi*n)\nsage: assume(n, 'odd')\nsage: assumptions()\n[n is odd]\nsage: foo=sin((-1)*n*pi)\nsage: foo.simplify()\n0\nsage: forget(n, 'odd')\nsage: assumptions()\n[]\nsage: foo=sin((-1)*n*pi)\nsage: foo.simplify()\n0\n```\n\n| Sage Version 4.2, Release Date: 2009-10-24                         |\n| Type notebook() for the GUI, and license() for information.        |\nRobert Dodier's comments:\n\n\n```\nI'm guessing that Sage punts to Maxima for this stuff.\nFor better or worse (mostly worse) there are different ways\nto declare & undeclare stuff in Maxima.\nFor the \"odd\" declaration, it's declare(n, odd) and remove(n, odd).\nI guess assume(n, 'odd') was translated to declare(n, odd) but\nforget(n, 'odd') was not translated to remove(n, odd).\nI don't know much about Sage so I could be way off here.\n```\n\n\nHere is the thread:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/9db67c2df781966b\n\nIssue created by migration from https://trac.sagemath.org/ticket/7507\n\n",
    "created_at": "2009-11-21T12:21:56Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "can't forget some assumptions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7507",
    "user": "burcin"
}
```
Assignee: burcin

CC:  kcrisman robert.marik

Keywords: maxima, assume

Reported by Mike Witt on sage-support:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: n=var('n')
sage: assumptions()
[]
sage: foo=sin((-1)*n*pi)
sage: foo.simplify()
-sin(pi*n)
sage: assume(n, 'odd')
sage: assumptions()
[n is odd]
sage: foo=sin((-1)*n*pi)
sage: foo.simplify()
0
sage: forget(n, 'odd')
sage: assumptions()
[]
sage: foo=sin((-1)*n*pi)
sage: foo.simplify()
0
```

| Sage Version 4.2, Release Date: 2009-10-24                         |
| Type notebook() for the GUI, and license() for information.        |
Robert Dodier's comments:


```
I'm guessing that Sage punts to Maxima for this stuff.
For better or worse (mostly worse) there are different ways
to declare & undeclare stuff in Maxima.
For the "odd" declaration, it's declare(n, odd) and remove(n, odd).
I guess assume(n, 'odd') was translated to declare(n, odd) but
forget(n, 'odd') was not translated to remove(n, odd).
I don't know much about Sage so I could be way off here.
```


Here is the thread:

http://groups.google.com/group/sage-support/browse_thread/thread/9db67c2df781966b

Issue created by migration from https://trac.sagemath.org/ticket/7507





---

archive/issue_comments_063515.json:
```json
{
    "body": "Okay, this is closed related to #1163 and #7315.  Should not be hard to fix, and might help in making GenericDeclarations better in any case.",
    "created_at": "2009-11-21T14:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7507#issuecomment-63515",
    "user": "kcrisman"
}
```

Okay, this is closed related to #1163 and #7315.  Should not be hard to fix, and might help in making GenericDeclarations better in any case.



---

archive/issue_comments_063516.json:
```json
{
    "body": "Replying to [comment:1 kcrisman]:\n> Okay, this is closed related to #1163 and #7315.  Should not be hard to fix, and might help in making GenericDeclarations better in any case.\n\nSorry, I meant *closely* related.",
    "created_at": "2010-01-08T16:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7507#issuecomment-63516",
    "user": "kcrisman"
}
```

Replying to [comment:1 kcrisman]:
> Okay, this is closed related to #1163 and #7315.  Should not be hard to fix, and might help in making GenericDeclarations better in any case.

Sorry, I meant *closely* related.



---

archive/issue_comments_063517.json:
```json
{
    "body": "Attachment\n\nThis seems to be fixed in the meanwhile. attachment:trac_7507-forget_assumptions.patch adds a doctest.",
    "created_at": "2011-05-08T20:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7507#issuecomment-63517",
    "user": "burcin"
}
```

Attachment

This seems to be fixed in the meanwhile. attachment:trac_7507-forget_assumptions.patch adds a doctest.



---

archive/issue_comments_063518.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-08T20:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7507#issuecomment-63518",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063519.json:
```json
{
    "body": "Yes, this was fixed as part of #1163, as it turns out.\n\n```\n\n    for x in preprocess_assumptions(args):\n        if isinstance(x, (tuple, list)):\n            forget(*x)\n```\n\nused to have\n\n```\n\n    for x in preprocess_assumptions(args):\n        if isinstance(x, (tuple, list)):\n            assume(*x)\n```\n\nbefore that patch.",
    "created_at": "2011-05-11T18:58:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7507#issuecomment-63519",
    "user": "kcrisman"
}
```

Yes, this was fixed as part of #1163, as it turns out.

```

    for x in preprocess_assumptions(args):
        if isinstance(x, (tuple, list)):
            forget(*x)
```

used to have

```

    for x in preprocess_assumptions(args):
        if isinstance(x, (tuple, list)):
            assume(*x)
```

before that patch.



---

archive/issue_comments_063520.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-11T19:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7507#issuecomment-63520",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063521.json:
```json
{
    "body": "Nice catch to close this; tests pass.",
    "created_at": "2011-05-11T19:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7507#issuecomment-63521",
    "user": "kcrisman"
}
```

Nice catch to close this; tests pass.



---

archive/issue_comments_063522.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-25T12:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7507#issuecomment-63522",
    "user": "jdemeyer"
}
```

Resolution: fixed
