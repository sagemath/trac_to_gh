# Issue 3404: graph.automorphism_group returns permutations with the wrong number of elements.

archive/issues_003404.json:
```json
{
    "body": "Assignee: @rlmill\n\nBoth of the graphs below are the path graph on 3 vertices.  The problem is that the first labeling returns a permutation group of degree 2, when it should be of degree 3.\n\n\n```\nsage: g=Graph('Bo')\nsage: print g.automorphism_group().degree()\n2\nsage: h=Graph('Bg')\nsage: print h.automorphism_group().degree()\n3\nsage: g.is_isomorphic(h)\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3404\n\n",
    "created_at": "2008-06-12T18:09:14Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "graph.automorphism_group returns permutations with the wrong number of elements.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3404",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @rlmill

Both of the graphs below are the path graph on 3 vertices.  The problem is that the first labeling returns a permutation group of degree 2, when it should be of degree 3.


```
sage: g=Graph('Bo')
sage: print g.automorphism_group().degree()
2
sage: h=Graph('Bg')
sage: print h.automorphism_group().degree()
3
sage: g.is_isomorphic(h)
True
```


Issue created by migration from https://trac.sagemath.org/ticket/3404





---

archive/issue_comments_023831.json:
```json
{
    "body": "Unfortunately, since permutation groups are (currently) simply wrappers for GAP permutation groups, the object itself carries no notion of what it acts on, only a cycle representation of its generators.\n\n\n```\nsage: g=Graph('Bo')\nsage: G=g.automorphism_group()\nsage: G.degree?\nType:\t\tinstancemethod\nBase Class:\t<type 'instancemethod'>\nString Form:\t<bound method PermutationGroup_generic.degree of Permutation Group with generators [(1,2)]>\nNamespace:\tInteractive\nFile:\t\t/Users/rlmill/sage-3.0.2/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py\nDefinition:\tG.degree(self)\nDocstring:\n    \n            Synonym for largest_moved_point().\n    \n            EXAMPLES:\n                sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])\n                sage: G.degree()\n                5\n```\n \n\nHowever, you can do:\n\n```\nsage: g.automorphism_group(translation=True, orbits=True)\n(Permutation Group with generators [(1,2)], {0: 3, 1: 1, 2: 2}, [[0], [1, 2]])\n```\n\n\nThe second is telling you which vertex of the graph is thought of as which integer by the group (here GAP thinks of this as 3 fixed, 4 fixed, 5 fixed, ...) and the third are the actual orbits of all the vertices.\n\nThis is a problem in permutation groups, not graphs.",
    "created_at": "2008-06-12T19:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3404#issuecomment-23831",
    "user": "https://github.com/rlmill"
}
```

Unfortunately, since permutation groups are (currently) simply wrappers for GAP permutation groups, the object itself carries no notion of what it acts on, only a cycle representation of its generators.


```
sage: g=Graph('Bo')
sage: G=g.automorphism_group()
sage: G.degree?
Type:		instancemethod
Base Class:	<type 'instancemethod'>
String Form:	<bound method PermutationGroup_generic.degree of Permutation Group with generators [(1,2)]>
Namespace:	Interactive
File:		/Users/rlmill/sage-3.0.2/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py
Definition:	G.degree(self)
Docstring:
    
            Synonym for largest_moved_point().
    
            EXAMPLES:
                sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
                sage: G.degree()
                5
```
 

However, you can do:

```
sage: g.automorphism_group(translation=True, orbits=True)
(Permutation Group with generators [(1,2)], {0: 3, 1: 1, 2: 2}, [[0], [1, 2]])
```


The second is telling you which vertex of the graph is thought of as which integer by the group (here GAP thinks of this as 3 fixed, 4 fixed, 5 fixed, ...) and the third are the actual orbits of all the vertices.

This is a problem in permutation groups, not graphs.



---

archive/issue_comments_023832.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-12T19:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3404#issuecomment-23832",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023833.json:
```json
{
    "body": "Changing component from graph theory to basic arithmetic.",
    "created_at": "2008-06-12T19:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3404#issuecomment-23833",
    "user": "https://github.com/rlmill"
}
```

Changing component from graph theory to basic arithmetic.



---

archive/issue_comments_023834.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-04T22:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3404#issuecomment-23834",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_comments_023835.json:
```json
{
    "body": "This has been fixed.\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sage: g=Graph('Bo')\nsage: sage: print g.automorphism_group().degree()\n3\nsage: g.automorphism_group()\nPermutation Group with generators [(1,2)]\n```\n",
    "created_at": "2009-06-04T22:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3404",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3404#issuecomment-23835",
    "user": "https://github.com/mwhansen"
}
```

This has been fixed.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: g=Graph('Bo')
sage: sage: print g.automorphism_group().degree()
3
sage: g.automorphism_group()
Permutation Group with generators [(1,2)]
```

