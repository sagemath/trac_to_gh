# Issue 7479: sage fails to integrate identity

archive/issues_007479.json:
```json
{
    "body": "Assignee: burcin\n\n32-bit Intel core duo, debian lenny, sage-4.2.1:\n\n\ngeorg`@`HILBERT:~$ sage\n----------------------------------------------------------------------\n| Sage Version 4.2.1, Release Date: 009-11-14                      |\n----------------------------------------------------------------------\nsage: f(x)=x\n| Type notebook() for the GUI, and license() for information.        |\nsage: integrate(f,x,0,1)\n\nsage0\n\nsage: integrate(f,x,0,1)\n\nsage7\n\nsage: integrate(f,x,0,1)\n\nsage12\n\nsage: integrate(f,x,0,1)\n\nsage17\n\nsage: integrate(f,x,0,1).n()\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/georg/<ipython console> in <module>()\n\n/mnt/data/georg/.system/bin/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:15863)()\n\n/mnt/data/georg/.system/bin/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.pyobject (sage/symbolic/expression.cpp:2701)()\n\nTypeError: self must be a numeric expression\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7479\n\n",
    "created_at": "2009-11-17T11:40:01Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "sage fails to integrate identity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7479",
    "user": "ggrafendorfer"
}
```
Assignee: burcin

32-bit Intel core duo, debian lenny, sage-4.2.1:


georg`@`HILBERT:~$ sage
----------------------------------------------------------------------
| Sage Version 4.2.1, Release Date: 009-11-14                      |
----------------------------------------------------------------------
sage: f(x)=x
| Type notebook() for the GUI, and license() for information.        |
sage: integrate(f,x,0,1)

sage0

sage: integrate(f,x,0,1)

sage7

sage: integrate(f,x,0,1)

sage12

sage: integrate(f,x,0,1)

sage17

sage: integrate(f,x,0,1).n()

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/georg/<ipython console> in <module>()

/mnt/data/georg/.system/bin/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:15863)()

/mnt/data/georg/.system/bin/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.pyobject (sage/symbolic/expression.cpp:2701)()

TypeError: self must be a numeric expression


Issue created by migration from https://trac.sagemath.org/ticket/7479





---

archive/issue_comments_063136.json:
```json
{
    "body": "Attachment [trac_7479.patch](tarball://root/attachments/some-uuid/ticket7479/trac_7479.patch) by mhansen created at 2009-11-17 12:19:06",
    "created_at": "2009-11-17T12:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7479#issuecomment-63136",
    "user": "mhansen"
}
```

Attachment [trac_7479.patch](tarball://root/attachments/some-uuid/ticket7479/trac_7479.patch) by mhansen created at 2009-11-17 12:19:06



---

archive/issue_comments_063137.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-17T12:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7479#issuecomment-63137",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063138.json:
```json
{
    "body": "Positive review except there is no doctest to indicate that one can now integrate f(x)=x!  It works:\n\n```\nsage: integrate(f,x,0,1)\n1/2\n```\n\nSo maybe this should be put in somewhere in sage/calculus/calculus.py in tests, or wherever you think is most appropriate.",
    "created_at": "2009-11-17T20:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7479#issuecomment-63138",
    "user": "kcrisman"
}
```

Positive review except there is no doctest to indicate that one can now integrate f(x)=x!  It works:

```
sage: integrate(f,x,0,1)
1/2
```

So maybe this should be put in somewhere in sage/calculus/calculus.py in tests, or wherever you think is most appropriate.



---

archive/issue_comments_063139.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-17T20:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7479#issuecomment-63139",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063140.json:
```json
{
    "body": "On the other hand, there is a doctest for the cause of the problem.",
    "created_at": "2009-11-18T04:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7479#issuecomment-63140",
    "user": "mhansen"
}
```

On the other hand, there is a doctest for the cause of the problem.



---

archive/issue_comments_063141.json:
```json
{
    "body": "Based on 4.2.1, apply only this patch",
    "created_at": "2009-11-18T14:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7479#issuecomment-63141",
    "user": "kcrisman"
}
```

Based on 4.2.1, apply only this patch



---

archive/issue_comments_063142.json:
```json
{
    "body": "Attachment [trac_7479-review.patch](tarball://root/attachments/some-uuid/ticket7479/trac_7479-review.patch) by kcrisman created at 2009-11-18 14:04:11\n\nI still feel safer putting it in there (for instance, if we switch to using Maxima as an ECL library this sort of thing could also break but for a different reason), so please apply this patch with the extra doctest.",
    "created_at": "2009-11-18T14:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7479#issuecomment-63142",
    "user": "kcrisman"
}
```

Attachment [trac_7479-review.patch](tarball://root/attachments/some-uuid/ticket7479/trac_7479-review.patch) by kcrisman created at 2009-11-18 14:04:11

I still feel safer putting it in there (for instance, if we switch to using Maxima as an ECL library this sort of thing could also break but for a different reason), so please apply this patch with the extra doctest.



---

archive/issue_comments_063143.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T10:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7479#issuecomment-63143",
    "user": "mhansen"
}
```

Resolution: fixed
