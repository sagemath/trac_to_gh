# Issue 9421: desolve mixes user parameters and integration constants

archive/issues_009421.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  robert.marik kcrisman\n\nConsider\n\n```\nsage: var('t')\nsage: x=function('x',t)\nsage: var('c')\nsage: desolve(diff(x,t)+2*x==t^2-2*t+c,x,ivar=t).expand()\nc*e^(-2*t) + 1/2*t^2 + 1/2*c - 3/2*t + 3/4\n```\n\nHere the first occurrence of `c` is an integration constant,\nwhereas the second one is the parameter in the ODE:\n\n```\nsage: var('d')\nsage: desolve(diff(x,t)+2*x==t^2-2*t+d,x,ivar=t).expand()\nc*e^(-2*t) + 1/2*t^2 + 1/2*d - 3/2*t + 3/4\n```\n\nIn case the ODE contains `c`, desolve should choose another\nname for the integration constant.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9421\n\n",
    "created_at": "2010-07-03T13:56:02Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "desolve mixes user parameters and integration constants",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9421",
    "user": "zimmerma"
}
```
Assignee: burcin

CC:  robert.marik kcrisman

Consider

```
sage: var('t')
sage: x=function('x',t)
sage: var('c')
sage: desolve(diff(x,t)+2*x==t^2-2*t+c,x,ivar=t).expand()
c*e^(-2*t) + 1/2*t^2 + 1/2*c - 3/2*t + 3/4
```

Here the first occurrence of `c` is an integration constant,
whereas the second one is the parameter in the ODE:

```
sage: var('d')
sage: desolve(diff(x,t)+2*x==t^2-2*t+d,x,ivar=t).expand()
c*e^(-2*t) + 1/2*t^2 + 1/2*d - 3/2*t + 3/4
```

In case the ODE contains `c`, desolve should choose another
name for the integration constant.

Issue created by migration from https://trac.sagemath.org/ticket/9421





---

archive/issue_comments_089854.json:
```json
{
    "body": "This is a part of more general problem which has been reported in #6882.",
    "created_at": "2010-07-04T15:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9421#issuecomment-89854",
    "user": "robert.marik"
}
```

This is a part of more general problem which has been reported in #6882.



---

archive/issue_comments_089855.json:
```json
{
    "body": "Attachment [trac_9421.patch](tarball://root/attachments/some-uuid/ticket9421/trac_9421.patch) by zimmerma created at 2013-08-25 13:25:17",
    "created_at": "2013-08-25T13:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9421#issuecomment-89855",
    "user": "zimmerma"
}
```

Attachment [trac_9421.patch](tarball://root/attachments/some-uuid/ticket9421/trac_9421.patch) by zimmerma created at 2013-08-25 13:25:17



---

archive/issue_comments_089856.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-25T13:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9421#issuecomment-89856",
    "user": "zimmerma"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089857.json:
```json
{
    "body": "waiting for the general problem to be solved, the attached patch prints a warning if the given equation contains the variable `c`.\n\nPaul",
    "created_at": "2013-08-25T13:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9421#issuecomment-89857",
    "user": "zimmerma"
}
```

waiting for the general problem to be solved, the attached patch prints a warning if the given equation contains the variable `c`.

Paul



---

archive/issue_comments_089858.json:
```json
{
    "body": "I will OK this if you have a look at #8734 in turn, please 8)  See also #16007",
    "created_at": "2014-03-25T10:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9421#issuecomment-89858",
    "user": "rws"
}
```

I will OK this if you have a look at #8734 in turn, please 8)  See also #16007



---

archive/issue_comments_089859.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-25T10:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9421#issuecomment-89859",
    "user": "rws"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089860.json:
```json
{
    "body": "thus should we have a dependency on #8734?\n\nPaul",
    "created_at": "2014-03-25T21:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9421#issuecomment-89860",
    "user": "zimmerma"
}
```

thus should we have a dependency on #8734?

Paul



---

archive/issue_comments_089861.json:
```json
{
    "body": "Replying to [comment:7 zimmerma]:\n> thus should we have a dependency on #8734?\n\nThen everything waits for that review, which could take forever. But I want the warning now.",
    "created_at": "2014-03-26T04:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9421#issuecomment-89861",
    "user": "rws"
}
```

Replying to [comment:7 zimmerma]:
> thus should we have a dependency on #8734?

Then everything waits for that review, which could take forever. But I want the warning now.



---

archive/issue_comments_089862.json:
```json
{
    "body": "You might want to consider this one too:\n\n```\nsage: desolve(diff(f(x),x,x)-f(x),f(x))\nk2*e^(-x) + k1*e^x\n```\n\nWe can recognize the variables as distinct before they are converted from maxima:\n\n```\nsage: function('f',x)\nf(x)\nsage: var('c')\nc\nsage: V=diff(f(x),x)-f(x)+c\nsage: v=maxima_calculus(V)\nsage: v.ode2(f(x),x)\n'f(x)=(c*%e^-x+%c)*%e^x\nsage: v.ode2(f(x),x).ecl()\n<ECL: ((MEQUAL SIMP) ((%F SIMP) $X)\n ((MTIMES SIMP)\n  ((MPLUS SIMP) $%C\n   ((MTIMES SIMP) $C ((MEXPT SIMP) $%E ((MTIMES SIMP) -1 $X))))\n  ((MEXPT SIMP) $%E $X)))>\n```\n\nso perhaps the right solution is to warn when sage's \"forget the %\" causes a name collision (with the righter solution being: making sage's \"forget the %\" more intelligent, so that collisions can be avoided)",
    "created_at": "2014-03-26T05:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9421#issuecomment-89862",
    "user": "nbruin"
}
```

You might want to consider this one too:

```
sage: desolve(diff(f(x),x,x)-f(x),f(x))
k2*e^(-x) + k1*e^x
```

We can recognize the variables as distinct before they are converted from maxima:

```
sage: function('f',x)
f(x)
sage: var('c')
c
sage: V=diff(f(x),x)-f(x)+c
sage: v=maxima_calculus(V)
sage: v.ode2(f(x),x)
'f(x)=(c*%e^-x+%c)*%e^x
sage: v.ode2(f(x),x).ecl()
<ECL: ((MEQUAL SIMP) ((%F SIMP) $X)
 ((MTIMES SIMP)
  ((MPLUS SIMP) $%C
   ((MTIMES SIMP) $C ((MEXPT SIMP) $%E ((MTIMES SIMP) -1 $X))))
  ((MEXPT SIMP) $%E $X)))>
```

so perhaps the right solution is to warn when sage's "forget the %" causes a name collision (with the righter solution being: making sage's "forget the %" more intelligent, so that collisions can be avoided)



---

archive/issue_comments_089863.json:
```json
{
    "body": "With #16007 the output is now\n\n```\nsage: sage: x=function('x',t)\nsage: sage: var('c')\nc\nsage: sage: desolve(diff(x,t)+2*x==t^2-2*t+c,x,ivar=t).expand()\n1/2*t^2 + _C*e^(-2*t) + 1/2*c - 3/2*t + 3/4\n\nsage: desolve(diff(f(x),x,x)-f(x),f(x))\n_K2*e^(-x) + _K1*e^x\n```\n\nAs that's a simple and fine solution instead of a warning or an extended patch I would be glad if someone could review that one-liner.",
    "created_at": "2014-03-26T16:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9421#issuecomment-89863",
    "user": "rws"
}
```

With #16007 the output is now

```
sage: sage: x=function('x',t)
sage: sage: var('c')
c
sage: sage: desolve(diff(x,t)+2*x==t^2-2*t+c,x,ivar=t).expand()
1/2*t^2 + _C*e^(-2*t) + 1/2*c - 3/2*t + 3/4

sage: desolve(diff(f(x),x,x)-f(x),f(x))
_K2*e^(-x) + _K1*e^x
```

As that's a simple and fine solution instead of a warning or an extended patch I would be glad if someone could review that one-liner.



---

archive/issue_comments_089864.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-03-31T15:03:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9421#issuecomment-89864",
    "user": "vbraun"
}
```

Resolution: duplicate
