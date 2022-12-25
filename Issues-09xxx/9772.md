# Issue 9772: Abelian groups

archive/issues_009772.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @loefflerd @JohnCremona @williamstein @nthiery boothby @jasongrout @kcrisman @mwhansen justin alexghitza\n\nThis patch will implement abelian groups, both additive and multiplicative, finite and infinite, under a common abstract class, using machinery for quotients of modules over `ZZ`.  This will make subgroups, intersections of subgroups, isomorphism classes, and quotient groups possible.  Generators may be of any type, so long as they support the minimal operations required.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9773\n\n",
    "created_at": "2010-08-20T22:55:53Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Abelian groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9772",
    "user": "https://github.com/rbeezer"
}
```
Assignee: @aghitza

CC:  @loefflerd @JohnCremona @williamstein @nthiery boothby @jasongrout @kcrisman @mwhansen justin alexghitza

This patch will implement abelian groups, both additive and multiplicative, finite and infinite, under a common abstract class, using machinery for quotients of modules over `ZZ`.  This will make subgroups, intersections of subgroups, isomorphism classes, and quotient groups possible.  Generators may be of any type, so long as they support the minimal operations required.

Issue created by migration from https://trac.sagemath.org/ticket/9773





---

archive/issue_comments_095606.json:
```json
{
    "body": "Attachment [trac_9773-abelian-groups-draft-1.patch](tarball://root/attachments/some-uuid/ticket9773/trac_9773-abelian-groups-draft-1.patch) by @rbeezer created at 2010-08-20 23:14:32\n\nAAG is the class of additive abelian groups.  This is an infinite group with a subgroup and a quotient.  (Typically quotients lose the generators and are \"generic\" but not in this example.)\n\n```\nsage: A=AAG([3,4,0])\nsage: A.gens()\n((2, 3, 0), (0, 0, 1))\nsage: A.0.order()\n12\nsage: A.1.order()\n+Infinity\nsage: B=A.subgroup([A.1])\nsage: B\nInfinite additive abelian group isomorphic to Z with generator(s): (0, 0, 1)\nsage: C=A/B\nsage: C\nFinite additive abelian group isomorphic to Z_12 with generator(s): (2, 3, 0)\n```\n\nGUN is a constructor of Groups of Units Mod n.  It employs MAG, the class of multiplicative abelian groups.  This is an intersection of two subgroups, and then a Cayley table is free (in the category of multiplicative groups).\n\n```\nsage: G=GUN(72)\nsage: G.list()\n[1, 65, 49, 17, 25, 41, 55, 47, 31, 71, 7, 23, 37, 29, 13, 53, 61, 5, 19, 11, 67, 35, 43, 59]\nsage: G.subgroup([71,7])\nFinite multiplicative abelian group isomorphic to Z_2 + Z_6 with generator(s): 55, 65\nsage: K=G.subgroup([71,7])\nsage: K.list()\n[1, 65, 49, 17, 25, 41, 55, 47, 31, 71, 7, 23]\nsage: L=G.subgroup([13,7])\nsage: L\nFinite multiplicative abelian group isomorphic to Z_2 + Z_6 with generator(s): 55, 61\nsage: L.list()\n[1, 61, 49, 37, 25, 13, 55, 43, 31, 19, 7, 67]\nsage: M=K.intersection(L)\nsage: M.list()\n[1, 7, 49, 55, 25, 31]\nsage: M\nFinite multiplicative abelian group isomorphic to Z_6 with generator(s): 7\nsage: M.cayley_table()\n*  a b c d e f\n +------------\na| a b c d e f\nb| b c d e f a\nc| c d e f a b\nd| d e f a b c\ne| e f a b c d\nf| f a b c d e\n```\n\nThis is an example from the current additive abelian wrapper class.  It shows the generators keyword allowing arbitrary elements to form the group, so long as they know how to add.  GUN above is similar, but with multiplication.\n\n\n```\nsage: E = EllipticCurve('30a2')\nsage: pts = [E(4,-7,1), E(7/4, -11/8, 1), E(3, -2, 1)]\nsage: M=AAG([3,2,2], generators=pts)\nsage: M.list()\n[(0 : 1 : 0), (13 : -52 : 1), (4 : -7 : 1), (3 : -2 : 1), (4 : 2 : 1), (13 : 38 : 1), (7/4 : -11/8 : 1), (1 : -4 : 1), (-2 : -7 : 1), (-5 : 2 : 1), (-2 : 8 : 1), (1 : 2 : 1)]\nsage: M.gens()\n((7/4 : -11/8 : 1), (13 : -52 : 1))\nsage: N=M.subgroup([M.1])\nsage: N\nFinite additive abelian group isomorphic to Z_6 with generator(s): (13 : -52 : 1)\nsage: N.list()\n[(0 : 1 : 0), (13 : -52 : 1), (4 : -7 : 1), (3 : -2 : 1), (4 : 2 : 1), (13 : 38 : 1)]\n```\n\nThere is lots to do here still: different filenames, different class names, error-checking, doctests, comparisons, and so on.  But the code seems to be working.  I'm not 100% confident on the `__call__` method of the main abstract class and I don't know if I need some things to support coercion better.  Any advice or comments at this stage would be appreciated before I begin to clean this all up.",
    "created_at": "2010-08-20T23:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95606",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9773-abelian-groups-draft-1.patch](tarball://root/attachments/some-uuid/ticket9773/trac_9773-abelian-groups-draft-1.patch) by @rbeezer created at 2010-08-20 23:14:32

AAG is the class of additive abelian groups.  This is an infinite group with a subgroup and a quotient.  (Typically quotients lose the generators and are "generic" but not in this example.)

```
sage: A=AAG([3,4,0])
sage: A.gens()
((2, 3, 0), (0, 0, 1))
sage: A.0.order()
12
sage: A.1.order()
+Infinity
sage: B=A.subgroup([A.1])
sage: B
Infinite additive abelian group isomorphic to Z with generator(s): (0, 0, 1)
sage: C=A/B
sage: C
Finite additive abelian group isomorphic to Z_12 with generator(s): (2, 3, 0)
```

GUN is a constructor of Groups of Units Mod n.  It employs MAG, the class of multiplicative abelian groups.  This is an intersection of two subgroups, and then a Cayley table is free (in the category of multiplicative groups).

```
sage: G=GUN(72)
sage: G.list()
[1, 65, 49, 17, 25, 41, 55, 47, 31, 71, 7, 23, 37, 29, 13, 53, 61, 5, 19, 11, 67, 35, 43, 59]
sage: G.subgroup([71,7])
Finite multiplicative abelian group isomorphic to Z_2 + Z_6 with generator(s): 55, 65
sage: K=G.subgroup([71,7])
sage: K.list()
[1, 65, 49, 17, 25, 41, 55, 47, 31, 71, 7, 23]
sage: L=G.subgroup([13,7])
sage: L
Finite multiplicative abelian group isomorphic to Z_2 + Z_6 with generator(s): 55, 61
sage: L.list()
[1, 61, 49, 37, 25, 13, 55, 43, 31, 19, 7, 67]
sage: M=K.intersection(L)
sage: M.list()
[1, 7, 49, 55, 25, 31]
sage: M
Finite multiplicative abelian group isomorphic to Z_6 with generator(s): 7
sage: M.cayley_table()
*  a b c d e f
 +------------
a| a b c d e f
b| b c d e f a
c| c d e f a b
d| d e f a b c
e| e f a b c d
f| f a b c d e
```

This is an example from the current additive abelian wrapper class.  It shows the generators keyword allowing arbitrary elements to form the group, so long as they know how to add.  GUN above is similar, but with multiplication.


```
sage: E = EllipticCurve('30a2')
sage: pts = [E(4,-7,1), E(7/4, -11/8, 1), E(3, -2, 1)]
sage: M=AAG([3,2,2], generators=pts)
sage: M.list()
[(0 : 1 : 0), (13 : -52 : 1), (4 : -7 : 1), (3 : -2 : 1), (4 : 2 : 1), (13 : 38 : 1), (7/4 : -11/8 : 1), (1 : -4 : 1), (-2 : -7 : 1), (-5 : 2 : 1), (-2 : 8 : 1), (1 : 2 : 1)]
sage: M.gens()
((7/4 : -11/8 : 1), (13 : -52 : 1))
sage: N=M.subgroup([M.1])
sage: N
Finite additive abelian group isomorphic to Z_6 with generator(s): (13 : -52 : 1)
sage: N.list()
[(0 : 1 : 0), (13 : -52 : 1), (4 : -7 : 1), (3 : -2 : 1), (4 : 2 : 1), (13 : 38 : 1)]
```

There is lots to do here still: different filenames, different class names, error-checking, doctests, comparisons, and so on.  But the code seems to be working.  I'm not 100% confident on the `__call__` method of the main abstract class and I don't know if I need some things to support coercion better.  Any advice or comments at this stage would be appreciated before I begin to clean this all up.



---

archive/issue_comments_095607.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-08-20T23:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95607",
    "user": "https://github.com/rbeezer"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_095608.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-08-20T23:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95608",
    "user": "https://github.com/rbeezer"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_095609.json:
```json
{
    "body": "Will this interact at all with the class `CombinatorialFreeModule`?  I don't know what the long term plans are, or even if there are any, for connecting this with `FreeModule`, but the combinatorial version has some nice features.\n\nAlso, how do you define **R** or **Q** as additive abelian groups with this setup?",
    "created_at": "2010-08-21T00:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95609",
    "user": "https://github.com/jhpalmieri"
}
```

Will this interact at all with the class `CombinatorialFreeModule`?  I don't know what the long term plans are, or even if there are any, for connecting this with `FreeModule`, but the combinatorial version has some nice features.

Also, how do you define **R** or **Q** as additive abelian groups with this setup?



---

archive/issue_comments_095610.json:
```json
{
    "body": "Replying to [comment:2 jhpalmieri]:\n\nHi John,\n\nThanks for the good questions.  I began this when I tried to implement a multiplicative group in concert with the work at #6449.  So I really didn't even have groups like **R** and **Q** in mind.  Truth-in-advertising would suggest I sprinkle in some \"finitely generated\" qualifiers in class names and filenames.\n\nI've plugged this into the categories framework as groups, but hadn't thought about modules.  I'll go take a look at all that to see how this might fit in.  Maybe Nicolas Thiery will have some ideas as well.\n\nThanks again,\nRob",
    "created_at": "2010-08-21T01:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95610",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:2 jhpalmieri]:

Hi John,

Thanks for the good questions.  I began this when I tried to implement a multiplicative group in concert with the work at #6449.  So I really didn't even have groups like **R** and **Q** in mind.  Truth-in-advertising would suggest I sprinkle in some "finitely generated" qualifiers in class names and filenames.

I've plugged this into the categories framework as groups, but hadn't thought about modules.  I'll go take a look at all that to see how this might fit in.  Maybe Nicolas Thiery will have some ideas as well.

Thanks again,
Rob



---

archive/issue_comments_095611.json:
```json
{
    "body": "Replying to [comment:2 jhpalmieri]:\n> Will this interact at all with the class `CombinatorialFreeModule`?  I don't know what the long term plans are, or even if there are any, for connecting this with `FreeModule`, but the combinatorial version has some nice features.\n\n\nI looked at these two classes.  Generally they seem to require the same ring in each \"component\", whereas the FGP_Module class allows for diffferent rings in each component, such as in creating something like Z_3 x Z_4.  So I don't see an abvious way to leverage these, but maybe I'm missing something.\n\nRob",
    "created_at": "2010-08-23T07:01:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95611",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:2 jhpalmieri]:
> Will this interact at all with the class `CombinatorialFreeModule`?  I don't know what the long term plans are, or even if there are any, for connecting this with `FreeModule`, but the combinatorial version has some nice features.


I looked at these two classes.  Generally they seem to require the same ring in each "component", whereas the FGP_Module class allows for diffferent rings in each component, such as in creating something like Z_3 x Z_4.  So I don't see an abvious way to leverage these, but maybe I'm missing something.

Rob



---

archive/issue_comments_095612.json:
```json
{
    "body": "# To the release manager\n\nPlease close #9694 when this ticket is merged.",
    "created_at": "2010-08-23T09:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95612",
    "user": "https://github.com/qed777"
}
```

# To the release manager

Please close #9694 when this ticket is merged.



---

archive/issue_comments_095613.json:
```json
{
    "body": "Attachment [trac_9773-abelian-groups-draft-2.patch](tarball://root/attachments/some-uuid/ticket9773/trac_9773-abelian-groups-draft-2.patch) by @rbeezer created at 2010-09-02 04:18:10",
    "created_at": "2010-09-02T04:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95613",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9773-abelian-groups-draft-2.patch](tarball://root/attachments/some-uuid/ticket9773/trac_9773-abelian-groups-draft-2.patch) by @rbeezer created at 2010-09-02 04:18:10



---

archive/issue_comments_095614.json:
```json
{
    "body": "Code is stablizing in draft 2 patch, and I'm starting to write the doctests.  Still uncertain about `__call__` and now its interactions with `__contains__`.\n\nThere are liberal comments in the code and the `units_modn` module has a rather complete demo of functionality.",
    "created_at": "2010-09-02T04:23:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95614",
    "user": "https://github.com/rbeezer"
}
```

Code is stablizing in draft 2 patch, and I'm starting to write the doctests.  Still uncertain about `__call__` and now its interactions with `__contains__`.

There are liberal comments in the code and the `units_modn` module has a rather complete demo of functionality.



---

archive/issue_comments_095615.json:
```json
{
    "body": "Question: does this patch solve #10181?\n\nPaul Zimmermann",
    "created_at": "2010-10-28T09:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95615",
    "user": "https://github.com/zimmermann6"
}
```

Question: does this patch solve #10181?

Paul Zimmermann



---

archive/issue_comments_095616.json:
```json
{
    "body": "Replying to [comment:8 zimmerma]:\n> Question: does this patch solve #10181?\n\n\nWhile we're at it, how about #9940?",
    "created_at": "2010-10-28T19:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95616",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:8 zimmerma]:
> Question: does this patch solve #10181?


While we're at it, how about #9940?



---

archive/issue_comments_095617.json:
```json
{
    "body": "Replying to [comment:8 zimmerma]:\n> Question: does this patch solve #10181?\n\n\nShort answer:  this could speed up `subgroups()` by a factor of 8, if my experiments are right.  We won't beat Magma, but we won't be embarassed on really small examples.  This patch does not have a `subgroups()` method yet, but could be easy to add.\n\nFull details at #10181.  Thanks for asking.\n\nRob",
    "created_at": "2010-10-31T17:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95617",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:8 zimmerma]:
> Question: does this patch solve #10181?


Short answer:  this could speed up `subgroups()` by a factor of 8, if my experiments are right.  We won't beat Magma, but we won't be embarassed on really small examples.  This patch does not have a `subgroups()` method yet, but could be easy to add.

Full details at #10181.  Thanks for asking.

Rob



---

archive/issue_comments_095618.json:
```json
{
    "body": "Replying to [comment:9 jhpalmieri]:\n> While we're at it, how about #9940?\n\n\nThis patch has code that is in pretty good shape (IMHO).  It still needs doctests, plus things like an equality method.  So it could fix #9440 if the equality method is done right?",
    "created_at": "2010-10-31T17:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95618",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:9 jhpalmieri]:
> While we're at it, how about #9940?


This patch has code that is in pretty good shape (IMHO).  It still needs doctests, plus things like an equality method.  So it could fix #9440 if the equality method is done right?



---

archive/issue_comments_095619.json:
```json
{
    "body": "Justin - no documentation to speak of, but look at the derived classes to get a feel for how this might work.\n\nAny insights or ideas you might have would be helpful before I try to finish this off later this spring.\n\nRob",
    "created_at": "2011-03-23T20:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95619",
    "user": "https://github.com/rbeezer"
}
```

Justin - no documentation to speak of, but look at the derived classes to get a feel for how this might work.

Any insights or ideas you might have would be helpful before I try to finish this off later this spring.

Rob



---

archive/issue_comments_095620.json:
```json
{
    "body": "Attachment [trac_9773-abelian-groups-draft-3.patch](tarball://root/attachments/some-uuid/ticket9773/trac_9773-abelian-groups-draft-3.patch) by @rbeezer created at 2012-05-17 22:49:10\n\nDraft 3 patch is actually about a year old at time of posting (for safe-keeping).  Category code changed out from under me, so I had to start over last summer.  This applies on 5.0.rc0, builds, and simple testing of the abstract classes seems to be successful. \n\nNeeds documentation, some changes, and practical derived classes, like totally abstract cyclic groups, the multiplicative subgroup of units mod n, etc.  IIRC, there are examples of these in the previous drafts.  I fully intend to work on this over the summer.",
    "created_at": "2012-05-17T22:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95620",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9773-abelian-groups-draft-3.patch](tarball://root/attachments/some-uuid/ticket9773/trac_9773-abelian-groups-draft-3.patch) by @rbeezer created at 2012-05-17 22:49:10

Draft 3 patch is actually about a year old at time of posting (for safe-keeping).  Category code changed out from under me, so I had to start over last summer.  This applies on 5.0.rc0, builds, and simple testing of the abstract classes seems to be successful. 

Needs documentation, some changes, and practical derived classes, like totally abstract cyclic groups, the multiplicative subgroup of units mod n, etc.  IIRC, there are examples of these in the previous drafts.  I fully intend to work on this over the summer.



---

archive/issue_comments_095621.json:
```json
{
    "body": "I keep plugging away at this.  Some improvement by exploiting category code.  Totally reworked, so most of my comments above are obsolete.\n\nDraft 4 patch is very functional, with the following caveats that I cannot figure out.  Assistance greatly appreciated if you can provide advice or specific pointers.  There is quite a bit of functionality demonstrated in the module-level doctests.  Little or no error-checking yet.\n\n1.  `_element_constructor()` works fine with module elements, which is to be expected, since it is copied verbatim from there.  I cannot seem to make it accept reasonable elements of the parent of the generators for subsequent processing without totally breaking extensive doctests.\n2.  The multiplicative version does not pass the `TestSuite` framework.  Likely the implementation of multiplicative operators on top of an additive class (FGP modules) is to blame?\n\nI've tried to add copious comments to make it easier to navigate the code.  More specific problem areas are flagged with `*PROBLEM*`.",
    "created_at": "2012-07-16T03:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95621",
    "user": "https://github.com/rbeezer"
}
```

I keep plugging away at this.  Some improvement by exploiting category code.  Totally reworked, so most of my comments above are obsolete.

Draft 4 patch is very functional, with the following caveats that I cannot figure out.  Assistance greatly appreciated if you can provide advice or specific pointers.  There is quite a bit of functionality demonstrated in the module-level doctests.  Little or no error-checking yet.

1.  `_element_constructor()` works fine with module elements, which is to be expected, since it is copied verbatim from there.  I cannot seem to make it accept reasonable elements of the parent of the generators for subsequent processing without totally breaking extensive doctests.
2.  The multiplicative version does not pass the `TestSuite` framework.  Likely the implementation of multiplicative operators on top of an additive class (FGP modules) is to blame?

I've tried to add copious comments to make it easier to navigate the code.  More specific problem areas are flagged with `*PROBLEM*`.



---

archive/issue_comments_095622.json:
```json
{
    "body": "Attachment [trac_9773-abelian-groups-draft-4.patch](tarball://root/attachments/some-uuid/ticket9773/trac_9773-abelian-groups-draft-4.patch) by @rbeezer created at 2012-07-16 04:01:34",
    "created_at": "2012-07-16T04:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95622",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9773-abelian-groups-draft-4.patch](tarball://root/attachments/some-uuid/ticket9773/trac_9773-abelian-groups-draft-4.patch) by @rbeezer created at 2012-07-16 04:01:34



---

archive/issue_comments_095623.json:
```json
{
    "body": "Just replaced the patch.  Realized the `_user_to_optimized()` method needed to be in the parent class, not the element class.  Then had some partial success getting `_element_constructor()` to work, but it still fails on subgroups - `.smith_form_gens()` for FGP modules is the suspect.\n\nTest suite on the elliptic curve example was testing the wrong instance - as corrected one test fails, so it is commented out, but should be experimented with to determine root cause.",
    "created_at": "2012-07-16T04:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95623",
    "user": "https://github.com/rbeezer"
}
```

Just replaced the patch.  Realized the `_user_to_optimized()` method needed to be in the parent class, not the element class.  Then had some partial success getting `_element_constructor()` to work, but it still fails on subgroups - `.smith_form_gens()` for FGP modules is the suspect.

Test suite on the elliptic curve example was testing the wrong instance - as corrected one test fails, so it is commented out, but should be experimented with to determine root cause.



---

archive/issue_comments_095624.json:
```json
{
    "body": "Attachment [trac_9773-abelian-groups-draft-5.patch](tarball://root/attachments/some-uuid/ticket9773/trac_9773-abelian-groups-draft-5.patch) by @rbeezer created at 2012-07-31 02:58:56\n\ndraft-4 failed to include \"__init__.py\" in the patch - that has been corrected in draft-5.\n\nDavid Roe helped me rework the initialization of the module class, so now the test suite is not doing additive tests on the multiplicative classes.  And I also believe I understand the problems with the element constructor (again with David's help).  So I think I'm over the hump on this one now.\n\nLong list of tests at module level are all passing, except one test suite (which I think I understand and can correct).  A few other test suites commented-out, but I think they are correctable also.",
    "created_at": "2012-07-31T02:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95624",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9773-abelian-groups-draft-5.patch](tarball://root/attachments/some-uuid/ticket9773/trac_9773-abelian-groups-draft-5.patch) by @rbeezer created at 2012-07-31 02:58:56

draft-4 failed to include "__init__.py" in the patch - that has been corrected in draft-5.

David Roe helped me rework the initialization of the module class, so now the test suite is not doing additive tests on the multiplicative classes.  And I also believe I understand the problems with the element constructor (again with David's help).  So I think I'm over the hump on this one now.

Long list of tests at module level are all passing, except one test suite (which I think I understand and can correct).  A few other test suites commented-out, but I think they are correctable also.



---

archive/issue_comments_095625.json:
```json
{
    "body": "Attachment [trac_9773-abelian-groups-draft-6.patch](tarball://root/attachments/some-uuid/ticket9773/trac_9773-abelian-groups-draft-6.patch) by @rbeezer created at 2012-08-08 03:53:32",
    "created_at": "2012-08-08T03:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95625",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9773-abelian-groups-draft-6.patch](tarball://root/attachments/some-uuid/ticket9773/trac_9773-abelian-groups-draft-6.patch) by @rbeezer created at 2012-08-08 03:53:32



---

archive/issue_comments_095626.json:
```json
{
    "body": "draft-6 patch is darn close to functional.  Lots of doctests, all passing.  Lots of code pushed up to abstract class.  Much more to do on docstrings.\n\nOne **real** edit in `FGP_Module` code.  Remainder are stray print statements to be cleaned up.",
    "created_at": "2012-08-08T03:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95626",
    "user": "https://github.com/rbeezer"
}
```

draft-6 patch is darn close to functional.  Lots of doctests, all passing.  Lots of code pushed up to abstract class.  Much more to do on docstrings.

One **real** edit in `FGP_Module` code.  Remainder are stray print statements to be cleaned up.



---

archive/issue_comments_095627.json:
```json
{
    "body": "Hi Rob,\n\nJust a quick note to say that I've played with draft-6 a bit (mainly with the `UnitsModmGroup`), and I very much like it.  Thanks for all the work you've put into this (and the patience!).",
    "created_at": "2012-08-30T05:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95627",
    "user": "https://github.com/aghitza"
}
```

Hi Rob,

Just a quick note to say that I've played with draft-6 a bit (mainly with the `UnitsModmGroup`), and I very much like it.  Thanks for all the work you've put into this (and the patience!).



---

archive/issue_comments_095628.json:
```json
{
    "body": "Replying to [comment:18 AlexGhitza]:\n> Just a quick note to say that I've played with draft-6 a bit (mainly with the `UnitsModmGroup`), and I very much like it.  Thanks for all the work you've put into this (and the patience!).\n\n\nThanks very much, Alex, for the encouragement.  Still lots of docstrings to work on, but making (slow) progress, since classes started recently.  Soon.  ;-)",
    "created_at": "2012-08-30T21:20:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95628",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:18 AlexGhitza]:
> Just a quick note to say that I've played with draft-6 a bit (mainly with the `UnitsModmGroup`), and I very much like it.  Thanks for all the work you've put into this (and the patience!).


Thanks very much, Alex, for the encouragement.  Still lots of docstrings to work on, but making (slow) progress, since classes started recently.  Soon.  ;-)



---

archive/issue_comments_095629.json:
```json
{
    "body": "any progress on this? Which info is needed?\n\nPaul",
    "created_at": "2013-01-08T08:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95629",
    "user": "https://github.com/zimmermann6"
}
```

any progress on this? Which info is needed?

Paul



---

archive/issue_events_024495.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9772#event-24495"
}
```



---

archive/issue_comments_095630.json:
```json
{
    "body": "Update: v6 patch will compain about one hunk not applying - just ignore it, it is no longer needed.  \n\nOn 5.12: compiles and passes all tests.\n\nBasically I think the code is solid on this one, but it needs extensive work to fully document and doctest.  And then it would be a big effort to slowly integrate in.",
    "created_at": "2013-11-09T05:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95630",
    "user": "https://github.com/rbeezer"
}
```

Update: v6 patch will compain about one hunk not applying - just ignore it, it is no longer needed.  

On 5.12: compiles and passes all tests.

Basically I think the code is solid on this one, but it needs extensive work to fully document and doctest.  And then it would be a big effort to slowly integrate in.



---

archive/issue_events_024496.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9772#event-24496"
}
```



---

archive/issue_events_024497.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9772#event-24497"
}
```



---

archive/issue_events_024498.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9772#event-24498"
}
```



---

archive/issue_events_024499.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9772#event-24499"
}
```



---

archive/issue_events_024500.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9772#event-24500"
}
```



---

archive/issue_events_024501.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9772#event-24501"
}
```



---

archive/issue_comments_095631.json:
```json
{
    "body": "Hey Rob, what's the status here?  If one (say, me) were to have a student who knows some algebra and is a solid programmer, could they finish up what is remaining?  Could be really useful stuff.",
    "created_at": "2015-02-12T15:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95631",
    "user": "https://github.com/kcrisman"
}
```

Hey Rob, what's the status here?  If one (say, me) were to have a student who knows some algebra and is a solid programmer, could they finish up what is remaining?  Could be really useful stuff.



---

archive/issue_comments_095632.json:
```json
{
    "body": "Replying to [comment:26 kcrisman]:\n> Hey Rob, what's the status here?  If one (say, me) were to have a student who knows some algebra and is a solid programmer, could they finish up what is remaining?  Could be really useful stuff.\n\n\nI am also interested in this. I am a student as well with algebra coursework under my belt. If there is still a need for this and you would like to work together, I am down.",
    "created_at": "2015-02-19T03:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9772#issuecomment-95632",
    "user": "https://trac.sagemath.org/admin/accounts/users/mcognetta"
}
```

Replying to [comment:26 kcrisman]:
> Hey Rob, what's the status here?  If one (say, me) were to have a student who knows some algebra and is a solid programmer, could they finish up what is remaining?  Could be really useful stuff.


I am also interested in this. I am a student as well with algebra coursework under my belt. If there is still a need for this and you would like to work together, I am down.
