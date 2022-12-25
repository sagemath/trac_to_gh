# Issue 8949: symbolic functions dont work with numpy.int32

archive/issues_008949.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @jasongrout\n\n\n```\nsage: import numpy\nsage: a = numpy.array([1,2])\nsage: type(a[0])\n<type 'numpy.int32'>\nsage: f(x) = x^2\nsage: f(a[0])\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n./sage-4.4.2/<ipython console> in <module>()\n\n./sage-4.4.2/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__call__ (sage/symbolic/expression.cpp:15476)()\n\n./sage-4.4.2/local/lib/python2.6/site-packages/sage/symbolic/callable.pyc in _call_element_(self, _the_element, *args, **kwds)\n    454         d = dict(zip(map(repr, self.arguments()), args))\n    455         d.update(kwds)\n--> 456         return SR(_the_element.substitute(**d))\n    457\n    458\n\n./sage-4.4.2/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.substitute (sage/symbolic/expression.cpp:14850)()\n\n./sage-4.4.2/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.coerce_in (sage/symbolic/expression.cpp:10193)()\n\n./sage-4.4.2/local/lib/python2.6/site-packages/sage/structure/parent_old.so in sage.structure.parent_old.Parent._coerce_ (sage/structure/parent_old.c:3288)()\n\n./sage-4.4.2/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.coerce (sage/structure/parent.c:6970)()\n\nTypeError: no canonical coercion from <type 'numpy.int32'> to Callable function ring with arguments (x,)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8949\n\n",
    "created_at": "2010-05-11T08:18:24Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "symbolic functions dont work with numpy.int32",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8949",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```
Assignee: @burcin

CC:  @jasongrout


```
sage: import numpy
sage: a = numpy.array([1,2])
sage: type(a[0])
<type 'numpy.int32'>
sage: f(x) = x^2
sage: f(a[0])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
./sage-4.4.2/<ipython console> in <module>()

./sage-4.4.2/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__call__ (sage/symbolic/expression.cpp:15476)()

./sage-4.4.2/local/lib/python2.6/site-packages/sage/symbolic/callable.pyc in _call_element_(self, _the_element, *args, **kwds)
    454         d = dict(zip(map(repr, self.arguments()), args))
    455         d.update(kwds)
--> 456         return SR(_the_element.substitute(**d))
    457
    458

./sage-4.4.2/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.substitute (sage/symbolic/expression.cpp:14850)()

./sage-4.4.2/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.coerce_in (sage/symbolic/expression.cpp:10193)()

./sage-4.4.2/local/lib/python2.6/site-packages/sage/structure/parent_old.so in sage.structure.parent_old.Parent._coerce_ (sage/structure/parent_old.c:3288)()

./sage-4.4.2/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.coerce (sage/structure/parent.c:6970)()

TypeError: no canonical coercion from <type 'numpy.int32'> to Callable function ring with arguments (x,)
```



Issue created by migration from https://trac.sagemath.org/ticket/8949





---

archive/issue_comments_082259.json:
```json
{
    "body": "I think #8824 may have the solution for this.",
    "created_at": "2010-05-11T20:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8949#issuecomment-82259",
    "user": "https://github.com/jasongrout"
}
```

I think #8824 may have the solution for this.



---

archive/issue_comments_082260.json:
```json
{
    "body": "[computer pictures](http://like-search.info/)",
    "created_at": "2010-05-26T08:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8949#issuecomment-82260",
    "user": "https://trac.sagemath.org/admin/accounts/users/bascorp2"
}
```

[computer pictures](http://like-search.info/)



---

archive/issue_comments_082261.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-03-28T12:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8949#issuecomment-82261",
    "user": "https://github.com/videlec"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082262.json:
```json
{
    "body": "Hello,\n\nI propose to close this as duplicates because of #18076. With the branch applied\n\n```\nsage: import numpy\nsage: cos(numpy.float('12'))\n0.8438539587324921\n```\n\nThough it is not perfect since the result is a Python float and not a numpy float.\n\nVincent",
    "created_at": "2015-03-28T12:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8949#issuecomment-82262",
    "user": "https://github.com/videlec"
}
```

Hello,

I propose to close this as duplicates because of #18076. With the branch applied

```
sage: import numpy
sage: cos(numpy.float('12'))
0.8438539587324921
```

Though it is not perfect since the result is a Python float and not a numpy float.

Vincent



---

archive/issue_comments_082263.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-23T10:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8949#issuecomment-82263",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082264.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2015-04-23T14:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8949#issuecomment-82264",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate



---

archive/issue_events_009102.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-04-23T14:51:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8949",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8949#event-9102"
}
```
