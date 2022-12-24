# Issue 9630: Python ints should have a conversion to Maxima

archive/issues_009630.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  mjo\n\nI don't know how this might be done, but \n\n```\nfor n in range(1,10): \n    sum(k, k, 1, n) \n```\n\ndoesn't work, while \n\n```\nfor n in [1..10]:\n    sum(k,k,1,n)\n```\n\ndoes.  We need to fix\n\n```\nint(3)._maxima_()\nAttributeError: 'int' object has no attribute '_maxima_'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9630\n\n",
    "created_at": "2010-07-29T01:36:07Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Python ints should have a conversion to Maxima",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9630",
    "user": "kcrisman"
}
```
Assignee: burcin

CC:  mjo

I don't know how this might be done, but 

```
for n in range(1,10): 
    sum(k, k, 1, n) 
```

doesn't work, while 

```
for n in [1..10]:
    sum(k,k,1,n)
```

does.  We need to fix

```
int(3)._maxima_()
AttributeError: 'int' object has no attribute '_maxima_'
```


Issue created by migration from https://trac.sagemath.org/ticket/9630





---

archive/issue_comments_093315.json:
```json
{
    "body": "the particular error that arises here is raised in sage/calculus/calculus.pyc line 501:\n\n```\nsum  = \"'sum(%s, %s, %s, %s)\" % tuple([repr(expr._maxima_()) for expr in (expression, v, a, b)])\n```\n\nOne could fix this one by first coercing a,b into SR. As an example:\n\n```\nsage: SR(int(1))._maxima_()\n1\n```\n\nThis code looks rather convoluted to me anyway: Convert to maxima, take string representative, paste together and then simplify? Shouldn't the whole sum first be turned into a pynac sum expression, the whole thing converted to maxima, simplified, and then cast back?\n\n```\nsage: var(\"x,a,b\")                       # this is just because I don't know\nsage: SUM=sum(sin(x^2),x,a,b).operator() # where this is defined\nsage: SR(SUM(x,x,1,int(10))._maxima_().simplify_sum())\n55\n```\n",
    "created_at": "2010-07-29T06:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9630#issuecomment-93315",
    "user": "nbruin"
}
```

the particular error that arises here is raised in sage/calculus/calculus.pyc line 501:

```
sum  = "'sum(%s, %s, %s, %s)" % tuple([repr(expr._maxima_()) for expr in (expression, v, a, b)])
```

One could fix this one by first coercing a,b into SR. As an example:

```
sage: SR(int(1))._maxima_()
1
```

This code looks rather convoluted to me anyway: Convert to maxima, take string representative, paste together and then simplify? Shouldn't the whole sum first be turned into a pynac sum expression, the whole thing converted to maxima, simplified, and then cast back?

```
sage: var("x,a,b")                       # this is just because I don't know
sage: SUM=sum(sin(x^2),x,a,b).operator() # where this is defined
sage: SR(SUM(x,x,1,int(10))._maxima_().simplify_sum())
55
```




---

archive/issue_comments_093316.json:
```json
{
    "body": "Sure, if Pynac sum expressions had been known to exist (or how to use them) when this code went in.  There was also some weird bug that this originally took care of that had to do with held expressions in Maxima, if I recall correctly, though that had ceased to be an issue.\n\nThis just goes to show that we need some sort of Pynac tutorial so that more people can be effective on this!",
    "created_at": "2010-07-29T13:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9630#issuecomment-93316",
    "user": "kcrisman"
}
```

Sure, if Pynac sum expressions had been known to exist (or how to use them) when this code went in.  There was also some weird bug that this originally took care of that had to do with held expressions in Maxima, if I recall correctly, though that had ceased to be an issue.

This just goes to show that we need some sort of Pynac tutorial so that more people can be effective on this!



---

archive/issue_comments_093317.json:
```json
{
    "body": "I don't think it's possible to monkey-patch methods onto int, but the symbolic sum issue has been fixed and I have a patch with a doctest (needs review!) at #9393.",
    "created_at": "2012-01-16T05:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9630#issuecomment-93317",
    "user": "mjo"
}
```

I don't think it's possible to monkey-patch methods onto int, but the symbolic sum issue has been fixed and I have a patch with a doctest (needs review!) at #9393.



---

archive/issue_comments_093318.json:
```json
{
    "body": "This is a duplicate of #9393. There is a patch with a doctest attached to that ticket.",
    "created_at": "2012-01-16T09:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9630#issuecomment-93318",
    "user": "burcin"
}
```

This is a duplicate of #9393. There is a patch with a doctest attached to that ticket.



---

archive/issue_comments_093319.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-16T09:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9630#issuecomment-93319",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093320.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-16T09:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9630#issuecomment-93320",
    "user": "burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093321.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-01-16T10:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9630#issuecomment-93321",
    "user": "jdemeyer"
}
```

Resolution: duplicate
