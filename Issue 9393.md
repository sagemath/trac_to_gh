# Issue 9393: symbolic sum cannot handle python ints

archive/issues_009393.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  whuss @orlitzky\n\nReported by Tobias Katz on sage-support:\n\n\n```\nsage: sum(x, x, 1r, 5r)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n.../<ipython console> in <module>()\n.../local/lib/python2.6/site-packages/sage/misc/functional.pyc in symbolic_sum(expression, *args, **kwds)\n    657     \"\"\"\n    658     if hasattr(expression, 'sum'):\n--> 659         return expression.sum(*args, **kwds)\n    660     elif len(args) <= 1:\n    661         return sum(expression, *args)\n\n.../local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.sum (sage/symbolic/expression.cpp:28895)()\n\n.../local/lib/python2.6/site-packages/sage/calculus/calculus.pyc in symbolic_sum(expression, v, a, b, algorithm)\n    482 \n    483     if algorithm == 'maxima':\n--> 484         sum  = \"'sum(%s, %s, %s, %s)\" % tuple([repr(expr._maxima_()) for expr in (expression, v, a, b)])\n    485         try:\n    486             result = maxima.simplify_sum(sum)\n\nAttributeError: 'int' object has no attribute '_maxima_'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9393\n\n",
    "created_at": "2010-06-30T11:52:27Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "symbolic sum cannot handle python ints",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9393",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

CC:  whuss @orlitzky

Reported by Tobias Katz on sage-support:


```
sage: sum(x, x, 1r, 5r)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
.../<ipython console> in <module>()
.../local/lib/python2.6/site-packages/sage/misc/functional.pyc in symbolic_sum(expression, *args, **kwds)
    657     """
    658     if hasattr(expression, 'sum'):
--> 659         return expression.sum(*args, **kwds)
    660     elif len(args) <= 1:
    661         return sum(expression, *args)

.../local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.sum (sage/symbolic/expression.cpp:28895)()

.../local/lib/python2.6/site-packages/sage/calculus/calculus.pyc in symbolic_sum(expression, v, a, b, algorithm)
    482 
    483     if algorithm == 'maxima':
--> 484         sum  = "'sum(%s, %s, %s, %s)" % tuple([repr(expr._maxima_()) for expr in (expression, v, a, b)])
    485         try:
    486             result = maxima.simplify_sum(sum)

AttributeError: 'int' object has no attribute '_maxima_'
```


Issue created by migration from https://trac.sagemath.org/ticket/9393





---

archive/issue_comments_089286.json:
```json
{
    "body": "Add a doctest for the fix.",
    "created_at": "2012-01-09T04:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9393#issuecomment-89286",
    "user": "https://github.com/orlitzky"
}
```

Add a doctest for the fix.



---

archive/issue_comments_089287.json:
```json
{
    "body": "Attachment [sage-trac_9393.patch](tarball://root/attachments/some-uuid/ticket9393/sage-trac_9393.patch) by @orlitzky created at 2012-01-09 04:28:53\n\nThis is fixed, so I've added a doctest for it.",
    "created_at": "2012-01-09T04:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9393#issuecomment-89287",
    "user": "https://github.com/orlitzky"
}
```

Attachment [sage-trac_9393.patch](tarball://root/attachments/some-uuid/ticket9393/sage-trac_9393.patch) by @orlitzky created at 2012-01-09 04:28:53

This is fixed, so I've added a doctest for it.



---

archive/issue_comments_089288.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-09T04:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9393#issuecomment-89288",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089289.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-16T09:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9393#issuecomment-89289",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089290.json:
```json
{
    "body": "Looks good to me.\n\nThanks for looking into this.",
    "created_at": "2012-01-16T09:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9393#issuecomment-89290",
    "user": "https://github.com/burcin"
}
```

Looks good to me.

Thanks for looking into this.



---

archive/issue_events_009550.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-01-18T08:13:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9393",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9393#event-9550"
}
```



---

archive/issue_comments_089291.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-01-18T08:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9393#issuecomment-89291",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
