# Issue 9907: maxima sum returns hypergeometric function

archive/issues_009907.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @eviatarbach\n\nThe parsing of Maxima's output is not good enough to handle this:\n\n\n```\nvar('n')\nsum(((2*I)^n/(n^3+1)*(1/4)^n), n, 0, infinity)\n```\n\ngives an exception\n\n```\nTypeError: unable to make sense of Maxima expression 'f[4,3]([1,1,-(sqrt(3)*I+1)/2,(sqrt(3)*I-1)/2],[2,-(sqrt(3)*I-1)/2,(sqrt(3)*I+1)/2],I/2)' in Sage\n```\n\nwhich is - i think - a f_43 hypergeometric function.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9908\n\n",
    "created_at": "2010-09-14T10:31:28Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "maxima sum returns hypergeometric function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9907",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: @burcin

CC:  @eviatarbach

The parsing of Maxima's output is not good enough to handle this:


```
var('n')
sum(((2*I)^n/(n^3+1)*(1/4)^n), n, 0, infinity)
```

gives an exception

```
TypeError: unable to make sense of Maxima expression 'f[4,3]([1,1,-(sqrt(3)*I+1)/2,(sqrt(3)*I-1)/2],[2,-(sqrt(3)*I-1)/2,(sqrt(3)*I+1)/2],I/2)' in Sage
```

which is - i think - a f_43 hypergeometric function.

Issue created by migration from https://trac.sagemath.org/ticket/9908





---

archive/issue_comments_098380.json:
```json
{
    "body": "one additional example by omologos on irc:\n\n```\nvar('x n')\nf=(-1)^n/((2*n+1)*factorial(2n+1))\nsum(f,n,0,oo)\n```\n\nbut i get this error:\n\n```\nTypeError: unable to make sense of Maxima expression 'f[1,2]([1/2],[3/2,3/2],-1/4)' in Sage\n```\n",
    "created_at": "2010-09-18T11:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9907#issuecomment-98380",
    "user": "https://github.com/haraldschilly"
}
```

one additional example by omologos on irc:

```
var('x n')
f=(-1)^n/((2*n+1)*factorial(2n+1))
sum(f,n,0,oo)
```

but i get this error:

```
TypeError: unable to make sense of Maxima expression 'f[1,2]([1/2],[3/2,3/2],-1/4)' in Sage
```




---

archive/issue_comments_098381.json:
```json
{
    "body": "This should be \n\n```\nvar('x n')\nf=(-1)^n/((2*n+1)*factorial(2*n+1))\nsum(f,n,0,oo)\n```\n\nIf I'm not mistaken, this might be related to #2516, in the sense that we should be parsing hypergeometric functions correctly and that would be part of that ticket.",
    "created_at": "2011-02-17T01:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9907#issuecomment-98381",
    "user": "https://github.com/kcrisman"
}
```

This should be 

```
var('x n')
f=(-1)^n/((2*n+1)*factorial(2*n+1))
sum(f,n,0,oo)
```

If I'm not mistaken, this might be related to #2516, in the sense that we should be parsing hypergeometric functions correctly and that would be part of that ticket.



---

archive/issue_comments_098382.json:
```json
{
    "body": "This also causes a similar problem in #4102:\n\n\n```\nsage: f = bessel_J(2, x)\nsage: f.integrate(x)\nTraceback (most recent call last):\n...\nTypeError: cannot coerce arguments: no canonical coercion from <type 'list'> to Symbolic Ring\n```\n\n\nIn that case, Maxima is returning `hypergeometric([3/2],[5/2,3],-x^2/4)`.",
    "created_at": "2013-06-17T21:01:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9907#issuecomment-98382",
    "user": "https://github.com/eviatarbach"
}
```

This also causes a similar problem in #4102:


```
sage: f = bessel_J(2, x)
sage: f.integrate(x)
Traceback (most recent call last):
...
TypeError: cannot coerce arguments: no canonical coercion from <type 'list'> to Symbolic Ring
```


In that case, Maxima is returning `hypergeometric([3/2],[5/2,3],-x^2/4)`.



---

archive/issue_comments_098383.json:
```json
{
    "body": "See also http://ask.sagemath.org/question/3091 for another example.",
    "created_at": "2013-10-17T01:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9907#issuecomment-98383",
    "user": "https://github.com/kcrisman"
}
```

See also http://ask.sagemath.org/question/3091 for another example.



---

archive/issue_comments_098384.json:
```json
{
    "body": "Changing keywords from \"\" to \"hypergeometric\".",
    "created_at": "2014-03-06T17:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9907#issuecomment-98384",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "hypergeometric".



---

archive/issue_comments_098385.json:
```json
{
    "body": "And see [this sage-support thread](https://groups.google.com/forum/#!topic/sage-support/IgC78rcdO7c) for possibly another example.",
    "created_at": "2014-04-24T01:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9907#issuecomment-98385",
    "user": "https://github.com/kcrisman"
}
```

And see [this sage-support thread](https://groups.google.com/forum/#!topic/sage-support/IgC78rcdO7c) for possibly another example.



---

archive/issue_comments_098386.json:
```json
{
    "body": "#2516 has all the examples above in it, with the exception of the ones mentioned in the comments.\n* One would want to be able to do\n\n```\nb=var('b')\nintegral(1/(x^b+1),x)\n```\n\n  without using W|A; apparently `1/(a^b+1)` would yield `2F1(1,1/a,1+1/a,-a^x)`.\n* Apparently \n\n```\nsum(x^(3*k)/factorial(2*k),k,0,oo)\n```\n\n  would also be doable with hypergeometrics.",
    "created_at": "2014-07-08T15:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9907#issuecomment-98386",
    "user": "https://github.com/kcrisman"
}
```

#2516 has all the examples above in it, with the exception of the ones mentioned in the comments.
* One would want to be able to do

```
b=var('b')
integral(1/(x^b+1),x)
```

  without using W|A; apparently `1/(a^b+1)` would yield `2F1(1,1/a,1+1/a,-a^x)`.
* Apparently 

```
sum(x^(3*k)/factorial(2*k),k,0,oo)
```

  would also be doable with hypergeometrics.



---

archive/issue_comments_098387.json:
```json
{
    "body": "Replying to [comment:11 kcrisman]:\n> #2516 has all the examples above in it, with the exception of the ones mentioned in the comments.\nWhat I get with #2516 is\n\n```\nsage: integral(1/(x^b+1),x)\nintegrate(1/(x^b + 1), x)\nsage: sum(x^(3*k)/factorial(2*k),k,0,oo)\nsqrt(pi)*x^(3/4)*sqrt(1/(pi*x^(3/2)))*cosh(x^(3/2))\n```\n",
    "created_at": "2014-07-08T15:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9907#issuecomment-98387",
    "user": "https://github.com/rwst"
}
```

Replying to [comment:11 kcrisman]:
> #2516 has all the examples above in it, with the exception of the ones mentioned in the comments.
What I get with #2516 is

```
sage: integral(1/(x^b+1),x)
integrate(1/(x^b + 1), x)
sage: sum(x^(3*k)/factorial(2*k),k,0,oo)
sqrt(pi)*x^(3/4)*sqrt(1/(pi*x^(3/2)))*cosh(x^(3/2))
```




---

archive/issue_comments_098388.json:
```json
{
    "body": "> What I get with #2516 is\n> {{{\n> sage: integral(1/(x^b+1),x)\n> integrate(1/(x^b + 1), x)\n> }}}\nNot really worth keeping open, as even Maxima does this.\n> {{{\n> sage: sum(x^(3*k)/factorial(2*k),k,0,oo)\n> sqrt(pi)*x<sup>(3/4)*sqrt(1/(pi*x</sup>(3/2)))*cosh(x^(3/2))\n> }}}\nInterestingly, this works in vanilla Sage as well.  Maybe there weren't any hg functions to begin with there.  I assume it was fixed with #16224 - earlier it gave yet another (wrong) answer.\n\nSo I nominate to close this ticket.",
    "created_at": "2014-07-08T16:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9907#issuecomment-98388",
    "user": "https://github.com/kcrisman"
}
```

> What I get with #2516 is
> {{{
> sage: integral(1/(x^b+1),x)
> integrate(1/(x^b + 1), x)
> }}}
Not really worth keeping open, as even Maxima does this.
> {{{
> sage: sum(x^(3*k)/factorial(2*k),k,0,oo)
> sqrt(pi)*x<sup>(3/4)*sqrt(1/(pi*x</sup>(3/2)))*cosh(x^(3/2))
> }}}
Interestingly, this works in vanilla Sage as well.  Maybe there weren't any hg functions to begin with there.  I assume it was fixed with #16224 - earlier it gave yet another (wrong) answer.

So I nominate to close this ticket.



---

archive/issue_comments_098389.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-07-08T16:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9907#issuecomment-98389",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098390.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-07-08T16:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9907#issuecomment-98390",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098391.json:
```json
{
    "body": "> > {{{\n> > sage: sum(x^(3*k)/factorial(2*k),k,0,oo)\n> > sqrt(pi)*x<sup>(3/4)*sqrt(1/(pi*x</sup>(3/2)))*cosh(x^(3/2))\n> > }}}\n> Interestingly, this works in vanilla Sage as well.  Maybe there weren't any hg functions to begin with there.  I assume it was fixed with #16224 - earlier it gave yet another (wrong) answer.\nEven more interestingly, this is not as simple as just `cosh(x^(3/2))` (which is correct) but I'm not going to repurpose this one for that.",
    "created_at": "2014-07-08T16:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9907#issuecomment-98391",
    "user": "https://github.com/kcrisman"
}
```

> > {{{
> > sage: sum(x^(3*k)/factorial(2*k),k,0,oo)
> > sqrt(pi)*x<sup>(3/4)*sqrt(1/(pi*x</sup>(3/2)))*cosh(x^(3/2))
> > }}}
> Interestingly, this works in vanilla Sage as well.  Maybe there weren't any hg functions to begin with there.  I assume it was fixed with #16224 - earlier it gave yet another (wrong) answer.
Even more interestingly, this is not as simple as just `cosh(x^(3/2))` (which is correct) but I'm not going to repurpose this one for that.



---

archive/issue_comments_098392.json:
```json
{
    "body": "Practically a duplicate of #2516",
    "created_at": "2014-07-08T16:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9907#issuecomment-98392",
    "user": "https://github.com/rwst"
}
```

Practically a duplicate of #2516



---

archive/issue_comments_098393.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-07-08T22:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9907#issuecomment-98393",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate



---

archive/issue_events_010034.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-07-08T22:53:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9907",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9907#event-10034"
}
```
