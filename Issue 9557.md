# Issue 9557: fundamental domains for subgroups of PSL(2,ZZ)

archive/issues_009557.json:
```json
{
    "body": "Assignee: Vincent Delecroix\n\nKeywords: hyperbolic geometry, fundamental domains, Fuchsian groups\n\nGiven a discrete subgroup of PSL(2,R) there exists a fundamental domain of the action of this group on the hyperbolic plane. Knowing one fundamental domain for a group, gives you the fundamental domain for any subgroups. This module implement the passage from the fundamental domain of PSL(2,ZZ) to any subgroup of finite index\n\nThe way is work concerns only the second part as I have to improve the transition (subgroup of PSL(2,Z)) <-> (coset graph). The first line just build the coset graph associated to the congruence subgroup Gamma(3).\n\n```\nsage: g = sage.geometry.fundamental_domains.gamma_triangle_graph(3)\nsage: g\nTriangle graph (2,3,infinty) with 12 vertices\nsage: FundamentalDomain(g)\nFundamental domain of a subgroup of index 12\nsage: FundamentalDomain(g).show()\n```\n\n\nDependancy:\n #9439 on hyperbolic geometry\n\nIssue created by migration from https://trac.sagemath.org/ticket/9557\n\n",
    "created_at": "2010-07-20T17:53:35Z",
    "labels": [
        "geometry",
        "major",
        "enhancement"
    ],
    "title": "fundamental domains for subgroups of PSL(2,ZZ)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9557",
    "user": "vdelecroix"
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

archive/issue_comments_092135.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-08-13T15:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9557#issuecomment-92135",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_092136.json:
```json
{
    "body": "I just made a git branch and cleaned the code. May not be working anymore ?\n----\nNew commits:",
    "created_at": "2015-06-28T10:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9557#issuecomment-92136",
    "user": "chapoton"
}
```

I just made a git branch and cleaned the code. May not be working anymore ?
----
New commits:



---

archive/issue_comments_092137.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-06-28T19:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9557#issuecomment-92137",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_092138.json:
```json
{
    "body": "This is a bit outdated. One now can do\n\n```\nsage: G = Gamma(2)\nsage: F = FareySymbol(G)\nsage: F.fundamental_domain()\n```\n",
    "created_at": "2015-06-28T19:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9557#issuecomment-92138",
    "user": "vdelecroix"
}
```

This is a bit outdated. One now can do

```
sage: G = Gamma(2)
sage: F = FareySymbol(G)
sage: F.fundamental_domain()
```




---

archive/issue_comments_092139.json:
```json
{
    "body": "OK.. So maybe we can close this one as duplicate/invalid ?\n\nOr is there something useful still ?\n\n\nBy the way, for another ticket: there is still a big gap in the hyperbolic plot routines: there is no good hyperbolic polygon class, like for the hyperbolic geodesics. I would need that and #16679 would benefit also.",
    "created_at": "2015-06-28T20:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9557#issuecomment-92139",
    "user": "chapoton"
}
```

OK.. So maybe we can close this one as duplicate/invalid ?

Or is there something useful still ?


By the way, for another ticket: there is still a big gap in the hyperbolic plot routines: there is no good hyperbolic polygon class, like for the hyperbolic geodesics. I would need that and #16679 would benefit also.



---

archive/issue_comments_092140.json:
```json
{
    "body": "`sage.plot.hyperbolic_polygon.hyperbolic_polygon`",
    "created_at": "2015-06-28T22:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9557#issuecomment-92140",
    "user": "vdelecroix"
}
```

`sage.plot.hyperbolic_polygon.hyperbolic_polygon`



---

archive/issue_comments_092141.json:
```json
{
    "body": "Yes, but it only works for the upper half-plane model. And it is not integrated at all in the HyperbolicPlane setup. This is much needed in the Poincar\u00e9 disk model, in fact.",
    "created_at": "2015-06-29T06:32:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9557#issuecomment-92141",
    "user": "chapoton"
}
```

Yes, but it only works for the upper half-plane model. And it is not integrated at all in the HyperbolicPlane setup. This is much needed in the Poincaré disk model, in fact.
