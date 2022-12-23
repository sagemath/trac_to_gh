# Issue 6858: [with patch, needs review] Cayley graph connecting set

archive/issues_006858.json:
```json
{
    "body": "Assignee: rlm\n\nReported by Chris Godsil.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6858\n\n",
    "created_at": "2009-09-02T01:11:38Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Cayley graph connecting set",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6858",
    "user": "rlm"
}
```
Assignee: rlm

Reported by Chris Godsil.

Issue created by migration from https://trac.sagemath.org/ticket/6858





---

archive/issue_comments_056555.json:
```json
{
    "body": "Hmmm.. I may have done something wrong, but here is what I tried \n\n\n```\nsage: g=PermutationGroup([(i+1,j+1) for i in range(5) for j in range(5) if j!=i])\nsage: (1,2) in g\nTrue\nsage: (2,3) in g\nTrue\nsage: g.cayley_graph(connecting_set=[(1,2),(2,3)])\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/user/ncohen/home/.sage/temp/rebelote.inria.fr/4013/_user_ncohen_home__sage_init_sage_0.py in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/groups/group.so in sage.groups.group.FiniteGroup.cayley_graph (sage/groups/group.c:2157)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.MonoidElement.__mul__ (sage/structure/element.c:8537)()\n\nTypeError: unsupported operand parent(s) for '*': 'Permutation Group with generators [(4,5), (3,4), (3,5), (2,3), (2,4), (2,5), (1,2), (1,3), (1,4), (1,5)]' and '<type 'tuple'>'\n\n```\n\n\nEven though it's apparent I know very few about groups in Sage as I had to build S_n by enumerating generators ( I guess there is a command to do that with only the cardinal ? ) ^^;",
    "created_at": "2009-09-05T08:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6858#issuecomment-56555",
    "user": "ncohen"
}
```

Hmmm.. I may have done something wrong, but here is what I tried 


```
sage: g=PermutationGroup([(i+1,j+1) for i in range(5) for j in range(5) if j!=i])
sage: (1,2) in g
True
sage: (2,3) in g
True
sage: g.cayley_graph(connecting_set=[(1,2),(2,3)])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/user/ncohen/home/.sage/temp/rebelote.inria.fr/4013/_user_ncohen_home__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/groups/group.so in sage.groups.group.FiniteGroup.cayley_graph (sage/groups/group.c:2157)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.MonoidElement.__mul__ (sage/structure/element.c:8537)()

TypeError: unsupported operand parent(s) for '*': 'Permutation Group with generators [(4,5), (3,4), (3,5), (2,3), (2,4), (2,5), (1,2), (1,3), (1,4), (1,5)]' and '<type 'tuple'>'

```


Even though it's apparent I know very few about groups in Sage as I had to build S_n by enumerating generators ( I guess there is a command to do that with only the cardinal ? ) ^^;



---

archive/issue_comments_056556.json:
```json
{
    "body": "Attachment\n\nOK, this new patch should do the trick.",
    "created_at": "2009-09-09T03:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6858#issuecomment-56556",
    "user": "rlm"
}
```

Attachment

OK, this new patch should do the trick.



---

archive/issue_comments_056557.json:
```json
{
    "body": "Applies fine, documented,does its job.... Positive review ! ;-)\n\nWhen testing the patch, I tried ( among others ) :\n\n```\nsage: len(g.cayley_graph(connecting_set=[(1,2)]).connected_components())\n60\nsage: len(g.cayley_graph(connecting_set=[(1,2),(2,3)]).connected_components())\n20\nsage: len(g.cayley_graph(connecting_set=[(1,2),(2,3),(3,4)]).connected_components())\n5\n```\n\n\nIf you think it useful, it could also be included in the examples contained in the docstring, even though there are already two and it may not be necessary at all :-)\n\nNathann",
    "created_at": "2009-09-11T14:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6858#issuecomment-56557",
    "user": "ncohen"
}
```

Applies fine, documented,does its job.... Positive review ! ;-)

When testing the patch, I tried ( among others ) :

```
sage: len(g.cayley_graph(connecting_set=[(1,2)]).connected_components())
60
sage: len(g.cayley_graph(connecting_set=[(1,2),(2,3)]).connected_components())
20
sage: len(g.cayley_graph(connecting_set=[(1,2),(2,3),(3,4)]).connected_components())
5
```


If you think it useful, it could also be included in the examples contained in the docstring, even though there are already two and it may not be necessary at all :-)

Nathann



---

archive/issue_comments_056558.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-11T17:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6858#issuecomment-56558",
    "user": "mvngu"
}
```

Resolution: fixed
