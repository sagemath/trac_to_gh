# Issue 7195: [with spkg, needs review] Cohomology rings of finite p-groups: new version

archive/issues_007195.json:
```json
{
    "body": "Assignee: @simon-king-jena\n\nCC:  david.green@uni-jena.de graham.ellis@nuigalway.ie @wdjoyner @jhpalmieri\n\nKeywords: cohomology ring group barcode\n\nHere is version 1.2 of our package for the computation of cohomology rings of finite p-groups.\n\n**__Authors__**\n- Simon King (Cython code, Singular code, some GAP code)\n- David Green (C-code, most GAP code)\n\n**__Installation__**\n\nCurrently, one installs the gap databases first and then retrieves our package from sage.math:\n\n```\nsage: install_package('database_gap')\nsage -i http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.2.spkg\n```\n\n\n**__News and Changes__**\n- Some bug fixes\n- Grammatical improvement in printing cocycles: not *c_8_12, a 8-Cochain in H<sup>*</sup>(foobar; GF(2))*, but *c_8_12: 8-Cocycle in H<sup>*</sup>(foobar; GF(2))*.\n- The web-accessible data base has a new location (thanks to William Stein for providing it!)\n- Bar Codes / Persistent Group Cohomology. The new stuff is documented at http://sage.math.washington.edu/home/SimonKing/Cohomology/barcode.html and http://sage.math.washington.edu/home/SimonKing/Cohomology/cohomology.html#pGroupCohomology.cohomology.COHO.bar_code\n\n**__Bar Codes__**\n\nThe notion of bar codes respectively of persistent group cohomology was introduced by Graham Ellis and Simon King. The idea is borrowed from applied mathematics. There, one wants to describe the geometric shape of point clouds.\n\nIn the point cloud setting, on the one hand one filters the data by \"importance\" (say, by a density threshold), on the other hand one thickens the points to some size, so that they overlap to some extend, and obtains geometric shapes that can be studied by homology methods. Changing threshold or point size, one obtains inclusions of geometric shapes, which gives rise to induced maps in homology. Not all homology generators \"survive\" being mapped, and new generators might show up. The idea is to focus on those homology generators that survive for the longest time (this is depicted by bar codes), which gives some idea of the geometric shape of the point cloud.\n\nFor a group G, we start with any normal series, e.g., the Upper Central Series. We obtain a chain of normal subgroups of increasing size, thus, inclusion maps, and we obtain a chain of factor groups of decreasing size, thus, quotient maps. These maps give rise to a chain of induced homomorphisms of cohomology rings, the cohomology of G being in the middle.\n\nIn any degree d, we may ask how many d-cocycles of the involved cohomology rings survive being mapped. If, say, a 2-dimensional subspace is mapped injectively by three consecutive induced maps and killed by the fourth map, then we would depict two bars of length 3. In the pictures below, the bars go from right to left, since we have CO-homology...\n\nOf course, if the normal series is characteristic then the bar code in each degree is a group invariant. The bar code in each degree can be encoded by an upper triangular integer matrix. So, these are very simple data, but still they contain much information about the group, as is shown below.\n\nThere is one advantage of cohomology over homology: We have the structure of a finitely presented ring, hence, we can capture all degrees at once, by Poincare series. This is also possible for bar codes. We thus obtain a 3d arrangement of bars, which is encoded by an upper triangular matrix of rational functions.\n\n**__Examples__**\n\nWe work here with groups of order 64, that are part of the cohomology data base shipped with the package.\n\n\n```\nsage: from pGroupCohomology import CohomologyRing\nsage: H158 = CohomologyRing(64,158)\nsage: H160 = CohomologyRing(64,160)\n```\n\n\nThe Poincare series, the a-invariants, the degrees of generators and of relations of the cohomology rings coincide:\n\n\n```\nsage: H158.poincare_series()\n(t^4 + t^3 + t^2 + t + 1)/(t^6 - 2*t^5 + 3*t^4 - 4*t^3 + 3*t^2 - 2*t + 1)\nsage: H160.poincare_series()\n(t^4 + t^3 + t^2 + t + 1)/(t^6 - 2*t^5 + 3*t^4 - 4*t^3 + 3*t^2 - 2*t + 1)\nsage: H158.gens()\n[1,\n c_4_4: 4-Cocycle in H^*(SmallGroup(64,158); GF(2)),\n c_4_5: 4-Cocycle in H^*(SmallGroup(64,158); GF(2)),\n a_1_0: 1-Cocycle in H^*(SmallGroup(64,158); GF(2)),\n a_1_1: 1-Cocycle in H^*(SmallGroup(64,158); GF(2)),\n a_1_2: 1-Cocycle in H^*(SmallGroup(64,158); GF(2)),\n a_3_2: 3-Cocycle in H^*(SmallGroup(64,158); GF(2)),\n a_3_3: 3-Cocycle in H^*(SmallGroup(64,158); GF(2))]\nsage: H160.gens()\n[1,\n c_4_4: 4-Cocycle in H^*(SmallGroup(64,160); GF(2)),\n c_4_5: 4-Cocycle in H^*(SmallGroup(64,160); GF(2)),\n a_1_0: 1-Cocycle in H^*(SmallGroup(64,160); GF(2)),\n a_1_1: 1-Cocycle in H^*(SmallGroup(64,160); GF(2)),\n a_1_2: 1-Cocycle in H^*(SmallGroup(64,160); GF(2)),\n a_3_2: 3-Cocycle in H^*(SmallGroup(64,160); GF(2)),\n a_3_3: 3-Cocycle in H^*(SmallGroup(64,160); GF(2))]\nsage: H158.set_ring()\nsage: [singular('deg(%s)'%r) for r in H158.rels()]\n[2, 2, 3, 3, 4, 4, 5, 6, 6, 6]\nsage: H160.set_ring()\nsage: [singular('deg(%s)'%r) for r in H160.rels()]\n[2, 2, 3, 3, 4, 4, 5, 6, 6, 6]\nsage: H158.a_invariants()\n[-Infinity, -Infinity, -2]\nsage: H160.a_invariants()\n[-Infinity, -Infinity, -2]\n```\n\n\nSo, the rings are \"almost\" the same.\n\nWe consider here the bar codes associated with the upper central series. It turns out that the non-trivial terms of the upper central series and the resulting factor groups are isomorphic:\n\n```\nsage: G158 = gap('SmallGroup(64,158)')\nsage: G160 = gap('SmallGroup(64,160)')\nsage: [(G.IdGroup(), (G158/G).IdGroup()) for G in G158.UpperCentralSeries()]\n[([ 64, 158 ], [ 1, 1 ]),\n ([ 16, 2 ], [ 4, 2 ]),\n ([ 4, 2 ], [ 16, 11 ]),\n ([ 1, 1 ], [ 64, 158 ])]\nsage: [(G.IdGroup(), (G160/G).IdGroup()) for G in G160.UpperCentralSeries()]\n[([ 64, 160 ], [ 1, 1 ]),\n ([ 16, 2 ], [ 4, 2 ]),\n ([ 4, 2 ], [ 16, 11 ]),\n ([ 1, 1 ], [ 64, 160 ])]\n```\n\n\nHence, there is no obvious way to tell the two groups apart by using the cohomology rings and the upper central series. However, even though the non-trivial parts of the series are isomorphic, the group homomorphisms in the series give rise to essentially different induced maps:\n\n```\nsage: B158 = H158.bar_code('UpperCentralSeries')\nsage: B160 = H160.bar_code('UpperCentralSeries')\nsage: B158 == B160\nFalse\n```\n\n\nHence, the bar codes can tell the two groups apart. In fact, this is already the case in degree 3:\n\n```\nsage: print B158[3]\n        *\n        *\n      *-*\n      *-*\n      *\n      *\n      *\n      *\n      *\n      *\n    *-*\n    *-*\n    *\n    *\n  *\n  *\n  *\n  *\n*\n*\n*\n*\nsage: print B160[3]\n        *\n        *\n      *-*\n      *\n      *\n      *\n      *\n      *\n      *\n      *\n    *-*-*\n    *-*\n    *\n  *-*\n  *\n  *\n  *\n*\n*\n*\n*\n```\n\n\nSo, the difference is that the cohomology of `SmallGroup(64,160)` has one 3-cocycle that comes from the last non-trivial factor group of the upper central series, while no such 3-cocycle exists for `SmallGroup(64,158)`.\n\nHere are the corresponding integer matrices, which provide a very handy way to distinguish the groups:\n\n```\nsage: B158[3].matrix()\n[ 4  0  0  0  0]\n[ 0  4  0  0  0]\n[ 0  0  4  2  0]\n[ 0  0  0 10  2]\n[ 0  0  0  0  4]\nsage: B160[3].matrix()\n[ 4  0  0  0  0]\n[ 0  4  1  0  0]\n[ 0  0  4  2  1]\n[ 0  0  0 10  2]\n[ 0  0  0  0  4]\n```\n\n\nHere is a smaller example, in which we show the Poincare series:\n\n```\nsage: H = CohomologyRing.user_db(8,3)\nsage: H.make()\nsage: B = H.bar_code('UpperCentralSeries')\nsage: B\nPersistence data for H^*(D8; GF(2)) associated with UpperCentralSeries\nsage: B.matrix()\n[       -1/(t - 1)      -1/(t^2 - 1)                 1]\n[                0 1/(t^2 - 2*t + 1)  (-t - 1)/(t - 1)]\n[                0                 0 1/(t^2 - 2*t + 1)]\n```\n\n\nThere are two ways to obtain the bar codes in a specific degree d: Either one computes the \"full\" persistence, using Poincare series computed by commutative algebra, and computes the data for degree d from it. Or, one *only* works in that degree and uses linear algebra. \n\nBoth methods yield the same result:\n\n```\nsage: B[5]\nBarcode of degree 5 for H^*(D8; GF(2)) associated with UpperCentralSeries\nsage: B[5] == H.bar_code('UpperCentralSeries', degree=5)\nTrue\n```\n\n\n**__Known Issues__**\n- Bar codes have a \"show\" method. On Intel Mac in 64 bit mode, graphics is broken, so, there will be one doc test error.\n- Intel Mac with the most recent XCode will not correctly compile the package in 32 bit mode. Older XCode should work.\n\nAs much as I understood, both is currently a general problem for Sage and not restricted to our package.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7195\n\n",
    "created_at": "2009-10-12T12:27:53Z",
    "labels": [
        "group theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "[with spkg, needs review] Cohomology rings of finite p-groups: new version",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7195",
    "user": "@simon-king-jena"
}
```
Assignee: @simon-king-jena

CC:  david.green@uni-jena.de graham.ellis@nuigalway.ie @wdjoyner @jhpalmieri

Keywords: cohomology ring group barcode

Here is version 1.2 of our package for the computation of cohomology rings of finite p-groups.

**__Authors__**
- Simon King (Cython code, Singular code, some GAP code)
- David Green (C-code, most GAP code)

**__Installation__**

Currently, one installs the gap databases first and then retrieves our package from sage.math:

```
sage: install_package('database_gap')
sage -i http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.2.spkg
```


**__News and Changes__**
- Some bug fixes
- Grammatical improvement in printing cocycles: not *c_8_12, a 8-Cochain in H<sup>*</sup>(foobar; GF(2))*, but *c_8_12: 8-Cocycle in H<sup>*</sup>(foobar; GF(2))*.
- The web-accessible data base has a new location (thanks to William Stein for providing it!)
- Bar Codes / Persistent Group Cohomology. The new stuff is documented at http://sage.math.washington.edu/home/SimonKing/Cohomology/barcode.html and http://sage.math.washington.edu/home/SimonKing/Cohomology/cohomology.html#pGroupCohomology.cohomology.COHO.bar_code

**__Bar Codes__**

The notion of bar codes respectively of persistent group cohomology was introduced by Graham Ellis and Simon King. The idea is borrowed from applied mathematics. There, one wants to describe the geometric shape of point clouds.

In the point cloud setting, on the one hand one filters the data by "importance" (say, by a density threshold), on the other hand one thickens the points to some size, so that they overlap to some extend, and obtains geometric shapes that can be studied by homology methods. Changing threshold or point size, one obtains inclusions of geometric shapes, which gives rise to induced maps in homology. Not all homology generators "survive" being mapped, and new generators might show up. The idea is to focus on those homology generators that survive for the longest time (this is depicted by bar codes), which gives some idea of the geometric shape of the point cloud.

For a group G, we start with any normal series, e.g., the Upper Central Series. We obtain a chain of normal subgroups of increasing size, thus, inclusion maps, and we obtain a chain of factor groups of decreasing size, thus, quotient maps. These maps give rise to a chain of induced homomorphisms of cohomology rings, the cohomology of G being in the middle.

In any degree d, we may ask how many d-cocycles of the involved cohomology rings survive being mapped. If, say, a 2-dimensional subspace is mapped injectively by three consecutive induced maps and killed by the fourth map, then we would depict two bars of length 3. In the pictures below, the bars go from right to left, since we have CO-homology...

Of course, if the normal series is characteristic then the bar code in each degree is a group invariant. The bar code in each degree can be encoded by an upper triangular integer matrix. So, these are very simple data, but still they contain much information about the group, as is shown below.

There is one advantage of cohomology over homology: We have the structure of a finitely presented ring, hence, we can capture all degrees at once, by Poincare series. This is also possible for bar codes. We thus obtain a 3d arrangement of bars, which is encoded by an upper triangular matrix of rational functions.

**__Examples__**

We work here with groups of order 64, that are part of the cohomology data base shipped with the package.


```
sage: from pGroupCohomology import CohomologyRing
sage: H158 = CohomologyRing(64,158)
sage: H160 = CohomologyRing(64,160)
```


The Poincare series, the a-invariants, the degrees of generators and of relations of the cohomology rings coincide:


```
sage: H158.poincare_series()
(t^4 + t^3 + t^2 + t + 1)/(t^6 - 2*t^5 + 3*t^4 - 4*t^3 + 3*t^2 - 2*t + 1)
sage: H160.poincare_series()
(t^4 + t^3 + t^2 + t + 1)/(t^6 - 2*t^5 + 3*t^4 - 4*t^3 + 3*t^2 - 2*t + 1)
sage: H158.gens()
[1,
 c_4_4: 4-Cocycle in H^*(SmallGroup(64,158); GF(2)),
 c_4_5: 4-Cocycle in H^*(SmallGroup(64,158); GF(2)),
 a_1_0: 1-Cocycle in H^*(SmallGroup(64,158); GF(2)),
 a_1_1: 1-Cocycle in H^*(SmallGroup(64,158); GF(2)),
 a_1_2: 1-Cocycle in H^*(SmallGroup(64,158); GF(2)),
 a_3_2: 3-Cocycle in H^*(SmallGroup(64,158); GF(2)),
 a_3_3: 3-Cocycle in H^*(SmallGroup(64,158); GF(2))]
sage: H160.gens()
[1,
 c_4_4: 4-Cocycle in H^*(SmallGroup(64,160); GF(2)),
 c_4_5: 4-Cocycle in H^*(SmallGroup(64,160); GF(2)),
 a_1_0: 1-Cocycle in H^*(SmallGroup(64,160); GF(2)),
 a_1_1: 1-Cocycle in H^*(SmallGroup(64,160); GF(2)),
 a_1_2: 1-Cocycle in H^*(SmallGroup(64,160); GF(2)),
 a_3_2: 3-Cocycle in H^*(SmallGroup(64,160); GF(2)),
 a_3_3: 3-Cocycle in H^*(SmallGroup(64,160); GF(2))]
sage: H158.set_ring()
sage: [singular('deg(%s)'%r) for r in H158.rels()]
[2, 2, 3, 3, 4, 4, 5, 6, 6, 6]
sage: H160.set_ring()
sage: [singular('deg(%s)'%r) for r in H160.rels()]
[2, 2, 3, 3, 4, 4, 5, 6, 6, 6]
sage: H158.a_invariants()
[-Infinity, -Infinity, -2]
sage: H160.a_invariants()
[-Infinity, -Infinity, -2]
```


So, the rings are "almost" the same.

We consider here the bar codes associated with the upper central series. It turns out that the non-trivial terms of the upper central series and the resulting factor groups are isomorphic:

```
sage: G158 = gap('SmallGroup(64,158)')
sage: G160 = gap('SmallGroup(64,160)')
sage: [(G.IdGroup(), (G158/G).IdGroup()) for G in G158.UpperCentralSeries()]
[([ 64, 158 ], [ 1, 1 ]),
 ([ 16, 2 ], [ 4, 2 ]),
 ([ 4, 2 ], [ 16, 11 ]),
 ([ 1, 1 ], [ 64, 158 ])]
sage: [(G.IdGroup(), (G160/G).IdGroup()) for G in G160.UpperCentralSeries()]
[([ 64, 160 ], [ 1, 1 ]),
 ([ 16, 2 ], [ 4, 2 ]),
 ([ 4, 2 ], [ 16, 11 ]),
 ([ 1, 1 ], [ 64, 160 ])]
```


Hence, there is no obvious way to tell the two groups apart by using the cohomology rings and the upper central series. However, even though the non-trivial parts of the series are isomorphic, the group homomorphisms in the series give rise to essentially different induced maps:

```
sage: B158 = H158.bar_code('UpperCentralSeries')
sage: B160 = H160.bar_code('UpperCentralSeries')
sage: B158 == B160
False
```


Hence, the bar codes can tell the two groups apart. In fact, this is already the case in degree 3:

```
sage: print B158[3]
        *
        *
      *-*
      *-*
      *
      *
      *
      *
      *
      *
    *-*
    *-*
    *
    *
  *
  *
  *
  *
*
*
*
*
sage: print B160[3]
        *
        *
      *-*
      *
      *
      *
      *
      *
      *
      *
    *-*-*
    *-*
    *
  *-*
  *
  *
  *
*
*
*
*
```


So, the difference is that the cohomology of `SmallGroup(64,160)` has one 3-cocycle that comes from the last non-trivial factor group of the upper central series, while no such 3-cocycle exists for `SmallGroup(64,158)`.

Here are the corresponding integer matrices, which provide a very handy way to distinguish the groups:

```
sage: B158[3].matrix()
[ 4  0  0  0  0]
[ 0  4  0  0  0]
[ 0  0  4  2  0]
[ 0  0  0 10  2]
[ 0  0  0  0  4]
sage: B160[3].matrix()
[ 4  0  0  0  0]
[ 0  4  1  0  0]
[ 0  0  4  2  1]
[ 0  0  0 10  2]
[ 0  0  0  0  4]
```


Here is a smaller example, in which we show the Poincare series:

```
sage: H = CohomologyRing.user_db(8,3)
sage: H.make()
sage: B = H.bar_code('UpperCentralSeries')
sage: B
Persistence data for H^*(D8; GF(2)) associated with UpperCentralSeries
sage: B.matrix()
[       -1/(t - 1)      -1/(t^2 - 1)                 1]
[                0 1/(t^2 - 2*t + 1)  (-t - 1)/(t - 1)]
[                0                 0 1/(t^2 - 2*t + 1)]
```


There are two ways to obtain the bar codes in a specific degree d: Either one computes the "full" persistence, using Poincare series computed by commutative algebra, and computes the data for degree d from it. Or, one *only* works in that degree and uses linear algebra. 

Both methods yield the same result:

```
sage: B[5]
Barcode of degree 5 for H^*(D8; GF(2)) associated with UpperCentralSeries
sage: B[5] == H.bar_code('UpperCentralSeries', degree=5)
True
```


**__Known Issues__**
- Bar codes have a "show" method. On Intel Mac in 64 bit mode, graphics is broken, so, there will be one doc test error.
- Intel Mac with the most recent XCode will not correctly compile the package in 32 bit mode. Older XCode should work.

As much as I understood, both is currently a general problem for Sage and not restricted to our package.

Issue created by migration from https://trac.sagemath.org/ticket/7195





---

archive/issue_comments_059678.json:
```json
{
    "body": "I modified the description, since a while ago David Green mentioned off list that the description gives the wrong impression that he is co-author for the new parts of the spkg. So, I changed it accordingly.\n\nFrom my point of view, David Green is certainly co-author for the SPKG, and addressed as such in the documentation: His code is in it since the very beginning. However, I still did not get the exact meaning of \"Author of a ticket\". Is it just myself (since I wrote the new parts, which this ticket is about) or is it David Green and I (since we are the authors of the SPKG)? Please help!",
    "created_at": "2009-10-31T12:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7195#issuecomment-59678",
    "user": "@simon-king-jena"
}
```

I modified the description, since a while ago David Green mentioned off list that the description gives the wrong impression that he is co-author for the new parts of the spkg. So, I changed it accordingly.

From my point of view, David Green is certainly co-author for the SPKG, and addressed as such in the documentation: His code is in it since the very beginning. However, I still did not get the exact meaning of "Author of a ticket". Is it just myself (since I wrote the new parts, which this ticket is about) or is it David Green and I (since we are the authors of the SPKG)? Please help!



---

archive/issue_comments_059679.json:
```json
{
    "body": "I sent some suggestions for the next version of this spkg (due out soon) to the author \"off-list\".",
    "created_at": "2009-12-16T22:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7195#issuecomment-59679",
    "user": "@wdjoyner"
}
```

I sent some suggestions for the next version of this spkg (due out soon) to the author "off-list".



---

archive/issue_comments_059680.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-16T22:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7195#issuecomment-59680",
    "user": "@wdjoyner"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059681.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-16T22:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7195#issuecomment-59681",
    "user": "@wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059682.json:
```json
{
    "body": "This compiles fine and passes sage -testall.",
    "created_at": "2009-12-16T22:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7195#issuecomment-59682",
    "user": "@wdjoyner"
}
```

This compiles fine and passes sage -testall.



---

archive/issue_comments_059683.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-20T07:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7195#issuecomment-59683",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_059684.json:
```json
{
    "body": "unique name",
    "created_at": "2017-07-19T08:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7195#issuecomment-59684",
    "user": "@fchapoton"
}
```

unique name
