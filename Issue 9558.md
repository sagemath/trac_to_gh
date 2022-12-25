# Issue 9558: Make `is_symmetric` method for polynomials or where else useful

archive/issues_009558.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  sage-combinat\n\nThis is a little vague - should it also be for SR, not just polynomial rings?  But it seems like a reasonable request on sage-support:\n\n```\nHi, \nI would like to know if there are any function that says if a \npolynomial is or not symmetric (like: 'is_symmetric'), so Mathematica \nhave this kind of function. \nhttp://en.wikipedia.org/wiki/Symmetric_polynomial \nThanks! \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9558\n\n",
    "created_at": "2010-07-21T01:22:52Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Make `is_symmetric` method for polynomials or where else useful",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9558",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @aghitza

CC:  sage-combinat

This is a little vague - should it also be for SR, not just polynomial rings?  But it seems like a reasonable request on sage-support:

```
Hi, 
I would like to know if there are any function that says if a 
polynomial is or not symmetric (like: 'is_symmetric'), so Mathematica 
have this kind of function. 
http://en.wikipedia.org/wiki/Symmetric_polynomial 
Thanks! 
```

Issue created by migration from https://trac.sagemath.org/ticket/9558





---

archive/issue_comments_091988.json:
```json
{
    "body": "Changing assignee from @aghitza to sage-combinat.",
    "created_at": "2010-07-30T15:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9558#issuecomment-91988",
    "user": "https://github.com/jbandlow"
}
```

Changing assignee from @aghitza to sage-combinat.



---

archive/issue_comments_091989.json:
```json
{
    "body": "The following works (at least in sage-4.4.4):\n\n```\nsage: R.<x,y,z> = QQ[]\nsage: SF = SymmetricFunctions(QQ)\nsage: SF.from_polynomial(x^2 + y^2 + z^2)\nm[2]\nsage: SF.from_polynomial(x^2 + y^2)\n...\nValueError: x^2 + y^2 is not a symmetric polynomial\n```\n\nIf someone wants to make a top level function like that suggested in the initial post, a design discussion should probably happen on sage.devel or sage.combinat.devel first.  \n\nI'm changing the component to combinatorics since that's where tickets related to symmetric functions usually live.",
    "created_at": "2010-07-30T15:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9558#issuecomment-91989",
    "user": "https://github.com/jbandlow"
}
```

The following works (at least in sage-4.4.4):

```
sage: R.<x,y,z> = QQ[]
sage: SF = SymmetricFunctions(QQ)
sage: SF.from_polynomial(x^2 + y^2 + z^2)
m[2]
sage: SF.from_polynomial(x^2 + y^2)
...
ValueError: x^2 + y^2 is not a symmetric polynomial
```

If someone wants to make a top level function like that suggested in the initial post, a design discussion should probably happen on sage.devel or sage.combinat.devel first.  

I'm changing the component to combinatorics since that's where tickets related to symmetric functions usually live.



---

archive/issue_comments_091990.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2010-07-30T15:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9558#issuecomment-91990",
    "user": "https://github.com/jbandlow"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_events_023794.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9558",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9558#event-23794"
}
```



---

archive/issue_events_023795.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9558",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9558#event-23795"
}
```



---

archive/issue_events_023796.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9558",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9558#event-23796"
}
```



---

archive/issue_events_023797.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9558",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9558#event-23797"
}
```



---

archive/issue_events_023798.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9558",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9558#event-23798"
}
```



---

archive/issue_events_023799.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9558",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9558#event-23799"
}
```



---

archive/issue_events_023800.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9558",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9558#event-23800"
}
```
