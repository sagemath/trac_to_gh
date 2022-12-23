# Issue 8942: failing calculation with limit

archive/issues_008942.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  jason mvngu mhansen\n\nKeywords: limit\n\nIn all three calculations below, the first result is false, whereas in a previous version of Sage, he returned Und what is the correct answer.\n\n\n```\nsage:f(x) = (cos(pi/4-x) - tan(x)) / (1 - sin(pi/4+x))\nsage:limit(f(x), x = pi/4) \n+Infinity\nsage: limit(f(x), x = pi/4, dir='plus')            \n-Infinity\nsage: limit(f(x), x = pi/4, dir='minus')           \n+Infinity\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8942\n\n",
    "created_at": "2010-05-10T09:32:39Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "title": "failing calculation with limit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8942",
    "user": "casamayou"
}
```
Assignee: burcin

CC:  jason mvngu mhansen

Keywords: limit

In all three calculations below, the first result is false, whereas in a previous version of Sage, he returned Und what is the correct answer.


```
sage:f(x) = (cos(pi/4-x) - tan(x)) / (1 - sin(pi/4+x))
sage:limit(f(x), x = pi/4) 
+Infinity
sage: limit(f(x), x = pi/4, dir='plus')            
-Infinity
sage: limit(f(x), x = pi/4, dir='minus')           
+Infinity
```


Issue created by migration from https://trac.sagemath.org/ticket/8942





---

archive/issue_comments_082331.json:
```json
{
    "body": "This was fixed when we improved our recognition of Maxima's unsigned infinity.\n\n```\nsage: sage: limit(f(x), x = pi/4, dir='minus')           \n+Infinity\nsage: sage: limit(f(x), x = pi/4, dir='plus')            \n-Infinity\nsage: sage:limit(f(x), x = pi/4) \nInfinity\n```\n\nSo I guess this can be closed?  Or should we whip up a patch to document this...?",
    "created_at": "2010-05-26T20:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8942#issuecomment-82331",
    "user": "kcrisman"
}
```

This was fixed when we improved our recognition of Maxima's unsigned infinity.

```
sage: sage: limit(f(x), x = pi/4, dir='minus')           
+Infinity
sage: sage: limit(f(x), x = pi/4, dir='plus')            
-Infinity
sage: sage:limit(f(x), x = pi/4) 
Infinity
```

So I guess this can be closed?  Or should we whip up a patch to document this...?



---

archive/issue_comments_082332.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-27T15:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8942#issuecomment-82332",
    "user": "casamayou"
}
```

Resolution: fixed



---

archive/issue_comments_082333.json:
```json
{
    "body": "Replying to [comment:1 kcrisman]:\n> This was fixed when we improved our recognition of Maxima's unsigned infinity.\n> {{{\n> sage: sage: limit(f(x), x = pi/4, dir='minus')           \n> +Infinity\n> sage: sage: limit(f(x), x = pi/4, dir='plus')            \n> -Infinity\n> sage: sage:limit(f(x), x = pi/4) \n> Infinity\n> }}}\n> So I guess this can be closed?  Or should we whip up a patch to document this...?\n\nThis can be closed. Thanks a lot !",
    "created_at": "2010-05-27T15:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8942#issuecomment-82333",
    "user": "casamayou"
}
```

Replying to [comment:1 kcrisman]:
> This was fixed when we improved our recognition of Maxima's unsigned infinity.
> {{{
> sage: sage: limit(f(x), x = pi/4, dir='minus')           
> +Infinity
> sage: sage: limit(f(x), x = pi/4, dir='plus')            
> -Infinity
> sage: sage:limit(f(x), x = pi/4) 
> Infinity
> }}}
> So I guess this can be closed?  Or should we whip up a patch to document this...?

This can be closed. Thanks a lot !



---

archive/issue_comments_082334.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-05-27T15:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8942#issuecomment-82334",
    "user": "kcrisman"
}
```

Changing status from closed to new.



---

archive/issue_comments_082335.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-05-27T15:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8942#issuecomment-82335",
    "user": "kcrisman"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_082336.json:
```json
{
    "body": "Thanks.  One thing to point out is [http://www.sagemath.org/doc/developer/trac.html#closing-tickets](http://www.sagemath.org/doc/developer/trac.html#closing-tickets), so that in theory only the release manager should close a ticket.  For instance, we might want to document this somewhere (which is what I was really asking about).  \n\nI will now violate that same web page by re-opening it; since it hasn't actually been merged (nothing to merge) hopefully that is ok, Minh or Mike :)",
    "created_at": "2010-05-27T15:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8942#issuecomment-82336",
    "user": "kcrisman"
}
```

Thanks.  One thing to point out is [http://www.sagemath.org/doc/developer/trac.html#closing-tickets](http://www.sagemath.org/doc/developer/trac.html#closing-tickets), so that in theory only the release manager should close a ticket.  For instance, we might want to document this somewhere (which is what I was really asking about).  

I will now violate that same web page by re-opening it; since it hasn't actually been merged (nothing to merge) hopefully that is ok, Minh or Mike :)



---

archive/issue_comments_082337.json:
```json
{
    "body": "Attachment\n\nBased on 4.4.2",
    "created_at": "2010-05-27T16:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8942#issuecomment-82337",
    "user": "kcrisman"
}
```

Attachment

Based on 4.4.2



---

archive/issue_comments_082338.json:
```json
{
    "body": "If we want more documentation that we have fixed this, here it is.  Ready for review.",
    "created_at": "2010-05-27T16:05:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8942#issuecomment-82338",
    "user": "kcrisman"
}
```

If we want more documentation that we have fixed this, here it is.  Ready for review.



---

archive/issue_comments_082339.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-27T16:05:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8942#issuecomment-82339",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082340.json:
```json
{
    "body": "positive review (I've checked that all doctests still pass).\n\nA small comment: maybe the documentation could say more explicitly that the output `Infinity`\nindicates a complex infinity, whereas `+Infinity` means plus infinity.\n\nBy the way, there is a problem since Sage parses `Infinity` as `+Infinity`:\n\n```\nsage: Infinity\n+Infinity\nsage: Infinity == +Infinity\nTrue\nsage: a=limit(1/x, x=0)\nsage: a == +Infinity\nTrue\n```\n\nbut this could be in a different ticket.",
    "created_at": "2010-07-12T12:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8942#issuecomment-82340",
    "user": "zimmerma"
}
```

positive review (I've checked that all doctests still pass).

A small comment: maybe the documentation could say more explicitly that the output `Infinity`
indicates a complex infinity, whereas `+Infinity` means plus infinity.

By the way, there is a problem since Sage parses `Infinity` as `+Infinity`:

```
sage: Infinity
+Infinity
sage: Infinity == +Infinity
True
sage: a=limit(1/x, x=0)
sage: a == +Infinity
True
```

but this could be in a different ticket.



---

archive/issue_comments_082341.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-12T12:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8942#issuecomment-82341",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082342.json:
```json
{
    "body": "> but this could be in a different ticket. \n\nsee #9480",
    "created_at": "2010-07-12T12:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8942#issuecomment-82342",
    "user": "zimmerma"
}
```

> but this could be in a different ticket. 

see #9480



---

archive/issue_comments_082343.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T10:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8942#issuecomment-82343",
    "user": "mpatel"
}
```

Resolution: fixed
