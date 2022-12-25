# Issue 9557: fundamental domains for subgroups of PSL(2,ZZ)

archive/issues_009557.json:
```json
{
    "body": "Assignee: Vincent Delecroix\n\nKeywords: hyperbolic geometry, fundamental domains, Fuchsian groups\n\nGiven a discrete subgroup of PSL(2,R) there exists a fundamental domain of the action of this group on the hyperbolic plane. Knowing one fundamental domain for a group, gives you the fundamental domain for any subgroups. This module implement the passage from the fundamental domain of PSL(2,ZZ) to any subgroup of finite index\n\nThe way is work concerns only the second part as I have to improve the transition (subgroup of PSL(2,Z)) <-> (coset graph). The first line just build the coset graph associated to the congruence subgroup Gamma(3).\n\n```\nsage: g = sage.geometry.fundamental_domains.gamma_triangle_graph(3)\nsage: g\nTriangle graph (2,3,infinty) with 12 vertices\nsage: FundamentalDomain(g)\nFundamental domain of a subgroup of index 12\nsage: FundamentalDomain(g).show()\n```\n\nDependancy:\n #9439 on hyperbolic geometry\n\nIssue created by migration from https://trac.sagemath.org/ticket/9557\n\n",
    "created_at": "2010-07-20T17:53:35Z",
    "labels": [
        "component: geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.8",
    "title": "fundamental domains for subgroups of PSL(2,ZZ)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9557",
    "user": "https://github.com/videlec"
}
```
Assignee: Vincent Delecroix

Keywords: hyperbolic geometry, fundamental domains, Fuchsian groups

Given a discrete subgroup of PSL(2,R) there exists a fundamental domain of the action of this group on the hyperbolic plane. Knowing one fundamental domain for a group, gives you the fundamental domain for any subgroups. This module implement the passage from the fundamental domain of PSL(2,ZZ) to any subgroup of finite index

The way is work concerns only the second part as I have to improve the transition (subgroup of PSL(2,Z)) <-> (coset graph). The first line just build the coset graph associated to the congruence subgroup Gamma(3).

```
sage: g = sage.geometry.fundamental_domains.gamma_triangle_graph(3)
sage: g
Triangle graph (2,3,infinty) with 12 vertices
sage: FundamentalDomain(g)
Fundamental domain of a subgroup of index 12
sage: FundamentalDomain(g).show()
```

Dependancy:
 #9439 on hyperbolic geometry

Issue created by migration from https://trac.sagemath.org/ticket/9557





---

archive/issue_comments_091981.json:
```json
{
    "body": "Attachment [trac_9557-fundamental_domains.patch](tarball://root/attachments/some-uuid/ticket9557/trac_9557-fundamental_domains.patch) by @jdemeyer created at 2013-08-13 15:35:53",
    "created_at": "2013-08-13T15:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9557#issuecomment-91981",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [trac_9557-fundamental_domains.patch](tarball://root/attachments/some-uuid/ticket9557/trac_9557-fundamental_domains.patch) by @jdemeyer created at 2013-08-13 15:35:53



---

archive/issue_events_023785.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9557#event-23785"
}
```



---

archive/issue_events_023786.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9557#event-23786"
}
```



---

archive/issue_events_023787.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9557#event-23787"
}
```



---

archive/issue_events_023788.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9557#event-23788"
}
```



---

archive/issue_events_023789.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9557#event-23789"
}
```



---

archive/issue_events_023790.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9557#event-23790"
}
```



---

archive/issue_events_023791.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9557#event-23791"
}
```



---

archive/issue_events_023792.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-06-28T10:28:38Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9557#event-23792"
}
```



---

archive/issue_events_023793.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-06-28T10:28:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "milestone": "sage-6.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9557#event-23793"
}
```



---

archive/issue_comments_091982.json:
```json
{
    "body": "I just made a git branch and cleaned the code. May not be working anymore ?\n\n---\nNew commits:",
    "created_at": "2015-06-28T10:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9557#issuecomment-91982",
    "user": "https://github.com/fchapoton"
}
```

I just made a git branch and cleaned the code. May not be working anymore ?

---
New commits:



---

archive/issue_comments_091983.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-06-28T19:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9557#issuecomment-91983",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_091984.json:
```json
{
    "body": "This is a bit outdated. One now can do\n\n```\nsage: G = Gamma(2)\nsage: F = FareySymbol(G)\nsage: F.fundamental_domain()\n```",
    "created_at": "2015-06-28T19:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9557#issuecomment-91984",
    "user": "https://github.com/videlec"
}
```

This is a bit outdated. One now can do

```
sage: G = Gamma(2)
sage: F = FareySymbol(G)
sage: F.fundamental_domain()
```



---

archive/issue_comments_091985.json:
```json
{
    "body": "OK.. So maybe we can close this one as duplicate/invalid ?\n\nOr is there something useful still ?\n\n\nBy the way, for another ticket: there is still a big gap in the hyperbolic plot routines: there is no good hyperbolic polygon class, like for the hyperbolic geodesics. I would need that and #16679 would benefit also.",
    "created_at": "2015-06-28T20:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9557#issuecomment-91985",
    "user": "https://github.com/fchapoton"
}
```

OK.. So maybe we can close this one as duplicate/invalid ?

Or is there something useful still ?


By the way, for another ticket: there is still a big gap in the hyperbolic plot routines: there is no good hyperbolic polygon class, like for the hyperbolic geodesics. I would need that and #16679 would benefit also.



---

archive/issue_comments_091986.json:
```json
{
    "body": "`sage.plot.hyperbolic_polygon.hyperbolic_polygon`",
    "created_at": "2015-06-28T22:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9557#issuecomment-91986",
    "user": "https://github.com/videlec"
}
```

`sage.plot.hyperbolic_polygon.hyperbolic_polygon`



---

archive/issue_comments_091987.json:
```json
{
    "body": "Yes, but it only works for the upper half-plane model. And it is not integrated at all in the HyperbolicPlane setup. This is much needed in the Poincar\u00e9 disk model, in fact.",
    "created_at": "2015-06-29T06:32:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9557#issuecomment-91987",
    "user": "https://github.com/fchapoton"
}
```

Yes, but it only works for the upper half-plane model. And it is not integrated at all in the HyperbolicPlane setup. This is much needed in the Poincaré disk model, in fact.
