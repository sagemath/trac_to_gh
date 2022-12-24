# Issue 8030: Strong generating system work only for transitive group

archive/issues_008030.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  sage-combinat\n\nMy fault from #6647\n\nThe method from Gap work only for transitive group.\n\n\n```\nsage: G = PermutationGroup([[(3,4)]])\nsage: G.strong_generating_system()\n[[()], [()], [()], [()]]\nsage: G.strong_generating_system(base_of_group=[3,1,2,4])\n[[(), (3,4)], [()], [()], [()]]\n```\n\n\nIf the first position is not moved by the permutation Group. Errors appears...\n\nIssue created by migration from https://trac.sagemath.org/ticket/8030\n\n",
    "created_at": "2010-01-21T19:37:01Z",
    "labels": [
        "group theory",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "Strong generating system work only for transitive group",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8030",
    "user": "nborie"
}
```
Assignee: joyner

CC:  sage-combinat

My fault from #6647

The method from Gap work only for transitive group.


```
sage: G = PermutationGroup([[(3,4)]])
sage: G.strong_generating_system()
[[()], [()], [()], [()]]
sage: G.strong_generating_system(base_of_group=[3,1,2,4])
[[(), (3,4)], [()], [()], [()]]
```


If the first position is not moved by the permutation Group. Errors appears...

Issue created by migration from https://trac.sagemath.org/ticket/8030





---

archive/issue_comments_070139.json:
```json
{
    "body": "I added a patch which solve the problem...\n\nI just changed the stabilizer method because the old version probably didn't point the right record of GAP for StabChain. The new stabilizer method is based form the Schreier's subgroup lemma.\n\nI ran some:\n\n```\nsage: G = SymmetricGroup(10)\nsage: H = PermutationGroup([G.random_element() for i in range(randrange(1,3,1))])\nsage: prod(map(lambda x : len(x), H.strong_generating_system()),1) == H.cardinality()\nTrue\n```\n\neverytimes, it was ok... For the speed, the method strong_generating_system is pretty slow! But I have no better idea and I still misunderstand records from GAP.",
    "created_at": "2010-01-23T20:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70139",
    "user": "nborie"
}
```

I added a patch which solve the problem...

I just changed the stabilizer method because the old version probably didn't point the right record of GAP for StabChain. The new stabilizer method is based form the Schreier's subgroup lemma.

I ran some:

```
sage: G = SymmetricGroup(10)
sage: H = PermutationGroup([G.random_element() for i in range(randrange(1,3,1))])
sage: prod(map(lambda x : len(x), H.strong_generating_system()),1) == H.cardinality()
True
```

everytimes, it was ok... For the speed, the method strong_generating_system is pretty slow! But I have no better idea and I still misunderstand records from GAP.



---

archive/issue_comments_070140.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-23T20:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70140",
    "user": "nborie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070141.json:
```json
{
    "body": "I uploaded a new version. There was also a mistake in the doc... That's an ugly bug...",
    "created_at": "2010-03-02T19:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70141",
    "user": "nborie"
}
```

I uploaded a new version. There was also a mistake in the doc... That's an ugly bug...



---

archive/issue_comments_070142.json:
```json
{
    "body": "I change the title hoping someone will pass to check that...",
    "created_at": "2010-04-16T16:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70142",
    "user": "nborie"
}
```

I change the title hoping someone will pass to check that...



---

archive/issue_comments_070143.json:
```json
{
    "body": "Hi Nicolas!\n\nThe tests are running.\n\nFor the record: I tried to compare the results in the new doctests\nwith GAP, and I get the following difference:\n\n\n```\ngap> G := Group([ (1,2) (3,4), (1,2,3,4,10) ]);\nGroup([ (1,2)(3,4), (1,2,3,4,10) ])\ngap> Stabilizer(G, 10);                        \nGroup([ (1,2)(3,4), (2,3,4) ])\n```\n\n\n\n```\nsage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4,10)]]) \nsage: G.stabilizer(10) \nPermutation Group with generators [(), (1,2)(3,4), (1,2,3), (1,2,4), (1,3,2), (1,3,4), (1,4,2)] \n```\n\n\nWell, in fact the results are equal:\n\n\n```\nsage: G2 = PermutationGroup( [ [(1,2),(3,4)], [(2,3,4)] ])\nsage: G.stabilizer(10) == G2\nTrue\n```\n\n\nbut GAP's result is nicer.",
    "created_at": "2010-04-18T16:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70143",
    "user": "@nthiery"
}
```

Hi Nicolas!

The tests are running.

For the record: I tried to compare the results in the new doctests
with GAP, and I get the following difference:


```
gap> G := Group([ (1,2) (3,4), (1,2,3,4,10) ]);
Group([ (1,2)(3,4), (1,2,3,4,10) ])
gap> Stabilizer(G, 10);                        
Group([ (1,2)(3,4), (2,3,4) ])
```



```
sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4,10)]]) 
sage: G.stabilizer(10) 
Permutation Group with generators [(), (1,2)(3,4), (1,2,3), (1,2,4), (1,3,2), (1,3,4), (1,4,2)] 
```


Well, in fact the results are equal:


```
sage: G2 = PermutationGroup( [ [(1,2),(3,4)], [(2,3,4)] ])
sage: G.stabilizer(10) == G2
True
```


but GAP's result is nicer.



---

archive/issue_comments_070144.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-19T08:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70144",
    "user": "nborie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070145.json:
```json
{
    "body": "Stay around, I am going to improve my \"horrible\" fix shortly...",
    "created_at": "2010-04-19T08:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70145",
    "user": "nborie"
}
```

Stay around, I am going to improve my "horrible" fix shortly...



---

archive/issue_comments_070146.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-19T09:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70146",
    "user": "nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070147.json:
```json
{
    "body": "Ok, now all the job is made in gap. The number of tests (including a random one) must help these methods to give right answer!\n\nAll tests passes including the optional one...",
    "created_at": "2010-04-19T09:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70147",
    "user": "nborie"
}
```

Ok, now all the job is made in gap. The number of tests (including a random one) must help these methods to give right answer!

All tests passes including the optional one...



---

archive/issue_comments_070148.json:
```json
{
    "body": "Attachment [trac_8030_stabilizer_bug-nb.patch](tarball://root/attachments/some-uuid/ticket8030/trac_8030_stabilizer_bug-nb.patch) by @nthiery created at 2010-05-18 21:30:58\n\nThe new implementation does the simplest thing: to just call GAP; and that fixes the problem at hand.The patch also adds a lots of doctests. All tests pass on 4.4.1. Positive review!",
    "created_at": "2010-05-18T21:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70148",
    "user": "@nthiery"
}
```

Attachment [trac_8030_stabilizer_bug-nb.patch](tarball://root/attachments/some-uuid/ticket8030/trac_8030_stabilizer_bug-nb.patch) by @nthiery created at 2010-05-18 21:30:58

The new implementation does the simplest thing: to just call GAP; and that fixes the problem at hand.The patch also adds a lots of doctests. All tests pass on 4.4.1. Positive review!



---

archive/issue_comments_070149.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-18T21:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70149",
    "user": "@nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070150.json:
```json
{
    "body": "Fix a trivial typo, and add hg header. Apply only this one.",
    "created_at": "2010-05-18T21:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70150",
    "user": "@nthiery"
}
```

Fix a trivial typo, and add hg header. Apply only this one.



---

archive/issue_comments_070151.json:
```json
{
    "body": "Attachment [trac_8030-stabilizer_bug-nb.patch](tarball://root/attachments/some-uuid/ticket8030/trac_8030-stabilizer_bug-nb.patch) by @rbeezer created at 2010-05-31 03:23:36\n\nStandalone doctring improvements, reviewer patch",
    "created_at": "2010-05-31T03:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70151",
    "user": "@rbeezer"
}
```

Attachment [trac_8030-stabilizer_bug-nb.patch](tarball://root/attachments/some-uuid/ticket8030/trac_8030-stabilizer_bug-nb.patch) by @rbeezer created at 2010-05-31 03:23:36

Standalone doctring improvements, reviewer patch



---

archive/issue_comments_070152.json:
```json
{
    "body": "Attachment [trac_8030-reviewer-doc-edit.patch](tarball://root/attachments/some-uuid/ticket8030/trac_8030-reviewer-doc-edit.patch) by @rbeezer created at 2010-05-31 03:30:06\n\nSomehow I thought this needed review, but obviously didn't look close enough.\n\nIn any event, I made some improvements to the docstring, which I just added.  I'm going to move them to a new ticket, so as to not mess this up.  Sorry for the confusion.\n\nRelease manager - you can remove trac_8030-reviewer-doc-edit.patch - it'll appear elsewhere with a new name.\n\nRob",
    "created_at": "2010-05-31T03:30:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70152",
    "user": "@rbeezer"
}
```

Attachment [trac_8030-reviewer-doc-edit.patch](tarball://root/attachments/some-uuid/ticket8030/trac_8030-reviewer-doc-edit.patch) by @rbeezer created at 2010-05-31 03:30:06

Somehow I thought this needed review, but obviously didn't look close enough.

In any event, I made some improvements to the docstring, which I just added.  I'm going to move them to a new ticket, so as to not mess this up.  Sorry for the confusion.

Release manager - you can remove trac_8030-reviewer-doc-edit.patch - it'll appear elsewhere with a new name.

Rob



---

archive/issue_comments_070153.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-03T04:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70153",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_070154.json:
```json
{
    "body": "It seems that [attachment:trac_8030-reviewer-doc-edit.patch] made it into 4.4.3.alpha2.  From building the PDF reference manual:\n\n```\n[2668] [2669] [2670] [2671] [2672] [2673] [2674] [2675] [2676] [2677]\n! Undefined control sequence.\nl.217693 ...als}(\\mathrm{pos}_{i+1})]_{1 \\leqslant\n                                                   i \\leqslant n}$\n? \n```\n\nI suppose #9102 is the place to fix this?",
    "created_at": "2010-06-03T09:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70154",
    "user": "@qed777"
}
```

It seems that [attachment:trac_8030-reviewer-doc-edit.patch] made it into 4.4.3.alpha2.  From building the PDF reference manual:

```
[2668] [2669] [2670] [2671] [2672] [2673] [2674] [2675] [2676] [2677]
! Undefined control sequence.
l.217693 ...als}(\mathrm{pos}_{i+1})]_{1 \leqslant
                                                   i \leqslant n}$
? 
```

I suppose #9102 is the place to fix this?



---

archive/issue_comments_070155.json:
```json
{
    "body": "Replying to [comment:10 mpatel]:\n> It seems that [attachment:trac_8030-reviewer-doc-edit.patch] made it into 4.4.3.alpha2.  From building the PDF reference manual:\n> {{{\n> [2668] [2669] [2670] [2671] [2672] [2673] [2674] [2675] [2676] [2677]\n> ! Undefined control sequence.\n> l.217693 ...als}(\\mathrm{pos}_{i+1})]_{1 \\leqslant\n>                                                    i \\leqslant n}$\n> ? \n> }}}\n> I suppose #9102 is the place to fix this?\n\nHi Misha,\n\nThat was a new macro to me, and worked fine in the HTML version of the docs.  Looks like it is part of the AMS packages.  I'll work on a patch as part of #9102, but long-term, does the PDF version need  amsmath or amssymb  packages to be included?  I can investigate later, but have a busy day today, so I'll get a quick fix up first.\n\nRob",
    "created_at": "2010-06-03T15:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70155",
    "user": "@rbeezer"
}
```

Replying to [comment:10 mpatel]:
> It seems that [attachment:trac_8030-reviewer-doc-edit.patch] made it into 4.4.3.alpha2.  From building the PDF reference manual:
> {{{
> [2668] [2669] [2670] [2671] [2672] [2673] [2674] [2675] [2676] [2677]
> ! Undefined control sequence.
> l.217693 ...als}(\mathrm{pos}_{i+1})]_{1 \leqslant
>                                                    i \leqslant n}$
> ? 
> }}}
> I suppose #9102 is the place to fix this?

Hi Misha,

That was a new macro to me, and worked fine in the HTML version of the docs.  Looks like it is part of the AMS packages.  I'll work on a patch as part of #9102, but long-term, does the PDF version need  amsmath or amssymb  packages to be included?  I can investigate later, but have a busy day today, so I'll get a quick fix up first.

Rob
