# Issue 9557: fundamental domains for subgroups of PSL(2,ZZ)

Issue created by migration from https://trac.sagemath.org/ticket/9557

Original creator: vdelecroix

Original creation time: 2010-07-20 17:53:35

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


---

Attachment


---

Comment by chapoton created at 2015-06-28 10:28:38

I just made a git branch and cleaned the code. May not be working anymore ?
----
New commits:


---

Comment by git created at 2015-06-28 19:00:48

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2015-06-28 19:06:43

This is a bit outdated. One now can do

```
sage: G = Gamma(2)
sage: F = FareySymbol(G)
sage: F.fundamental_domain()
```



---

Comment by chapoton created at 2015-06-28 20:16:21

OK.. So maybe we can close this one as duplicate/invalid ?

Or is there something useful still ?


By the way, for another ticket: there is still a big gap in the hyperbolic plot routines: there is no good hyperbolic polygon class, like for the hyperbolic geodesics. I would need that and #16679 would benefit also.


---

Comment by vdelecroix created at 2015-06-28 22:22:25

`sage.plot.hyperbolic_polygon.hyperbolic_polygon`


---

Comment by chapoton created at 2015-06-29 06:32:48

Yes, but it only works for the upper half-plane model. And it is not integrated at all in the HyperbolicPlane setup. This is much needed in the Poincaré disk model, in fact.
