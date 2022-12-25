# Issue 7508: hash collisions for derivatives of symbolic functions - act 3

archive/issues_007508.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: pynac\n\nReported by Alex Raichev on sage-support:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: X= var('x,y,z')\nsage: f= function('f',*X); f\nf(x, y, z)\nsage: d= {}\nsage: for l in [1..2]:\n....:     for s in UnorderedTuples(X,l):\n....:         print diff(f,s)\n....:         d[diff(f,s)]= 69\n....:\nD[0](f)(x, y, z)\nD[1](f)(x, y, z)\nD[2](f)(x, y, z)\nD[0, 0](f)(x, y, z)\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call\nlast)\n...\n/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/\nexpression_conversions.py in derivative(self, ex, operator)\n    344             NotImplementedError: derivative\n    345         \"\"\"\n--> 346         raise NotImplementedError, \"derivative\"  \n    347\n    348     def arithmetic(self, ex, operator):\n| Sage Version 4.2.1, Release Date: 2009-11-14                       |\n| Type notebook() for the GUI, and license() for information.        |\nNotImplementedError: derivative\n```\n\n\nThis is another form of the problem I couldn't fix in #6243 and #6851.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7508\n\n",
    "created_at": "2009-11-21T12:56:52Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "hash collisions for derivatives of symbolic functions - act 3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7508",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

Keywords: pynac

Reported by Alex Raichev on sage-support:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: X= var('x,y,z')
sage: f= function('f',*X); f
f(x, y, z)
sage: d= {}
sage: for l in [1..2]:
....:     for s in UnorderedTuples(X,l):
....:         print diff(f,s)
....:         d[diff(f,s)]= 69
....:
D[0](f)(x, y, z)
D[1](f)(x, y, z)
D[2](f)(x, y, z)
D[0, 0](f)(x, y, z)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call
last)
...
/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/
expression_conversions.py in derivative(self, ex, operator)
    344             NotImplementedError: derivative
    345         """
--> 346         raise NotImplementedError, "derivative"  
    347
    348     def arithmetic(self, ex, operator):
| Sage Version 4.2.1, Release Date: 2009-11-14                       |
| Type notebook() for the GUI, and license() for information.        |
NotImplementedError: derivative
```


This is another form of the problem I couldn't fix in #6243 and #6851.

Issue created by migration from https://trac.sagemath.org/ticket/7508





---

archive/issue_comments_063407.json:
```json
{
    "body": "add doctests",
    "created_at": "2009-11-22T17:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7508#issuecomment-63407",
    "user": "https://github.com/burcin"
}
```

add doctests



---

archive/issue_comments_063408.json:
```json
{
    "body": "Attachment [trac_7508-fderivative_hash_collision_doctest.patch](tarball://root/attachments/some-uuid/ticket7508/trac_7508-fderivative_hash_collision_doctest.patch) by @burcin created at 2009-11-22 17:24:32\n\nThis is fixed (hopefully, for good) in the new pynac package here:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.spkg\n\nattachment:trac_7508-fderivative_hash_collision_doctest.patch adds doctests for the fix.\n\nNote that the new pynac version also contains fixes for #7264 and #7406. Tests should be run with the patches from those tickets also applied in this order:\n\n* #7508 (this ticket)\n* #7264\n* #7406\n\nThis ticket now depends on #7490.",
    "created_at": "2009-11-22T17:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7508#issuecomment-63408",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7508-fderivative_hash_collision_doctest.patch](tarball://root/attachments/some-uuid/ticket7508/trac_7508-fderivative_hash_collision_doctest.patch) by @burcin created at 2009-11-22 17:24:32

This is fixed (hopefully, for good) in the new pynac package here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.spkg

attachment:trac_7508-fderivative_hash_collision_doctest.patch adds doctests for the fix.

Note that the new pynac version also contains fixes for #7264 and #7406. Tests should be run with the patches from those tickets also applied in this order:

* #7508 (this ticket)
* #7264
* #7406

This ticket now depends on #7490.



---

archive/issue_comments_063409.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-22T17:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7508#issuecomment-63409",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063410.json:
```json
{
    "body": "Positive review.",
    "created_at": "2009-12-05T13:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7508#issuecomment-63410",
    "user": "https://github.com/kcrisman"
}
```

Positive review.



---

archive/issue_comments_063411.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-05T13:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7508#issuecomment-63411",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063412.json:
```json
{
    "body": "I should point out that #7264 has a problem, so the spkg should not be merged until that is resolved.",
    "created_at": "2009-12-05T13:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7508#issuecomment-63412",
    "user": "https://github.com/kcrisman"
}
```

I should point out that #7264 has a problem, so the spkg should not be merged until that is resolved.



---

archive/issue_comments_063413.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-10T14:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7508#issuecomment-63413",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007736.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-10T14:22:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7508",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7508#event-7736"
}
```
