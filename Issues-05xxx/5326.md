# Issue 5326: support weighted term orderings

archive/issues_005326.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @johnperry-math\n\nJacob wrote on [sage-devel]:\n\n> From reading the documentation of the TermOrder command, it looks \n> like if I want to use a term order not defined in SAGE, I should \n> be able to make my term order a string that can be passed to \n> Singular.  This works for some term orderings, but not for those \n> that have commas in their definitions.  Judging from the code, I \n> think that SAGE sees the comma and assumes that I want a block \n> ordering (which I don't).\n\n\n> For example, if I want weighted reverse lex ordering with some\n> weights, I can do that in Singular:\n\n {{{\nring rr=0,(x,y),wp(2,3);\npoly f=x2+y3;\ndeg(f);\n9\npoly g = x<sup>3*y+y</sup>3;\nideal I = f,g;\nstd(I);\n_[1]=y3+x2\n_[2]=x3y-x2\n_[3]=x5+x2y2\n }}}\n\n> But not in SAGE:\n\n{{{\nsage: T = TermOrder(\"wp(2,3)\")\nTraceback (most recent call last):\n...\nTypeError: wp(2,3) is not a valid term ordering\n}}}\n\n```\nsage: R.<x,y> = PolynomialRing(QQ,2,T)\nsage: R._singular_()\n//   characteristic : 0\n//   number of vars : 2\n//        block   1 : ordering dp\n//                  : names    x y\n//        block   2 : ordering C\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5326\n\n",
    "closed_at": "2017-07-13T07:54:31Z",
    "created_at": "2009-02-21T02:07:21Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "support weighted term orderings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5326",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @johnperry-math

Jacob wrote on [sage-devel]:

> From reading the documentation of the TermOrder command, it looks 
> like if I want to use a term order not defined in SAGE, I should 
> be able to make my term order a string that can be passed to 
> Singular.  This works for some term orderings, but not for those 
> that have commas in their definitions.  Judging from the code, I 
> think that SAGE sees the comma and assumes that I want a block 
> ordering (which I don't).


> For example, if I want weighted reverse lex ordering with some
> weights, I can do that in Singular:

 {{{
ring rr=0,(x,y),wp(2,3);
poly f=x2+y3;
deg(f);
9
poly g = x<sup>3*y+y</sup>3;
ideal I = f,g;
std(I);
_[1]=y3+x2
_[2]=x3y-x2
_[3]=x5+x2y2
 }}}

> But not in SAGE:

{{{
sage: T = TermOrder("wp(2,3)")
Traceback (most recent call last):
...
TypeError: wp(2,3) is not a valid term ordering
}}}

```
sage: R.<x,y> = PolynomialRing(QQ,2,T)
sage: R._singular_()
//   characteristic : 0
//   number of vars : 2
//        block   1 : ordering dp
//                  : names    x y
//        block   2 : ordering C
```

Issue created by migration from https://trac.sagemath.org/ticket/5326





---

archive/issue_comments_040918.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2012-01-26T18:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5326#issuecomment-40918",
    "user": "https://github.com/johnperry-math"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_040919.json:
```json
{
    "body": "I believe this is a duplicate of #11316, in which case it has been fixed!",
    "created_at": "2012-01-26T18:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5326#issuecomment-40919",
    "user": "https://github.com/johnperry-math"
}
```

I believe this is a duplicate of #11316, in which case it has been fixed!



---

archive/issue_events_012406.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5326#event-12406"
}
```



---

archive/issue_events_012407.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5326#event-12407"
}
```



---

archive/issue_events_012408.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5326#event-12408"
}
```



---

archive/issue_events_012409.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5326#event-12409"
}
```



---

archive/issue_events_012410.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5326#event-12410"
}
```



---

archive/issue_events_012411.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5326#event-12411"
}
```



---

archive/issue_events_012412.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5326#event-12412"
}
```



---

archive/issue_comments_040920.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2017-04-06T10:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5326#issuecomment-40920",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_040921.json:
```json
{
    "body": "weighted term orders are implemented since long..",
    "created_at": "2017-04-06T10:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5326#issuecomment-40921",
    "user": "https://github.com/fchapoton"
}
```

weighted term orders are implemented since long..



---

archive/issue_events_012413.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2017-04-06T10:05:56Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5326#event-12413"
}
```



---

archive/issue_events_012414.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2017-04-06T10:05:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5326#event-12414"
}
```



---

archive/issue_comments_040922.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2017-04-06T10:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5326#issuecomment-40922",
    "user": "https://github.com/fchapoton"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_040923.json:
```json
{
    "body": "maybe not so clear..",
    "created_at": "2017-04-06T10:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5326#issuecomment-40923",
    "user": "https://github.com/fchapoton"
}
```

maybe not so clear..



---

archive/issue_comments_040924.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2017-06-02T13:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5326#issuecomment-40924",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_040925.json:
```json
{
    "body": "The correct syntax is \n\n```\nT =  TermOrder(\"wp\",(2,3))\n```",
    "created_at": "2017-06-02T13:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5326#issuecomment-40925",
    "user": "https://github.com/fchapoton"
}
```

The correct syntax is 

```
T =  TermOrder("wp",(2,3))
```



---

archive/issue_comments_040926.json:
```json
{
    "body": "Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).",
    "created_at": "2017-07-13T07:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5326#issuecomment-40926",
    "user": "https://github.com/embray"
}
```

Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).



---

archive/issue_events_012415.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2017-07-13T07:54:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5326#event-12415"
}
```



---

archive/issue_comments_040927.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-07-13T07:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5326#issuecomment-40927",
    "user": "https://github.com/embray"
}
```

Resolution: wontfix
