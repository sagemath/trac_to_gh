# Issue 8030: Strong generating system work only for transitive group

archive/issues_008030.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  sage-combinat\n\nMy fault from #6647\n\nThe method from Gap work only for transitive group.\n\n```\nsage: G = PermutationGroup([[(3,4)]])\nsage: G.strong_generating_system()\n[[()], [()], [()], [()]]\nsage: G.strong_generating_system(base_of_group=[3,1,2,4])\n[[(), (3,4)], [()], [()], [()]]\n```\n\nIf the first position is not moved by the permutation Group. Errors appears...\n\nIssue created by migration from https://trac.sagemath.org/ticket/8030\n\n",
    "created_at": "2010-01-21T19:37:01Z",
    "labels": [
        "component: group theory",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "Strong generating system work only for transitive group",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8030",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
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

archive/issue_comments_070018.json:
```json
{
    "body": "I added a patch which solve the problem...\n\nI just changed the stabilizer method because the old version probably didn't point the right record of GAP for StabChain. The new stabilizer method is based form the Schreier's subgroup lemma.\n\nI ran some:\n\n```\nsage: G = SymmetricGroup(10)\nsage: H = PermutationGroup([G.random_element() for i in range(randrange(1,3,1))])\nsage: prod(map(lambda x : len(x), H.strong_generating_system()),1) == H.cardinality()\nTrue\n```\neverytimes, it was ok... For the speed, the method strong_generating_system is pretty slow! But I have no better idea and I still misunderstand records from GAP.",
    "created_at": "2010-01-23T20:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70018",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
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

archive/issue_comments_070019.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-23T20:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70019",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from new to needs_review.



---

archive/issue_events_019237.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/nborie",
    "created_at": "2010-01-23T20:23:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "milestone": "sage-4.3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8030#event-19237"
}
```



---

archive/issue_comments_070020.json:
```json
{
    "body": "I uploaded a new version. There was also a mistake in the doc... That's an ugly bug...",
    "created_at": "2010-03-02T19:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70020",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

I uploaded a new version. There was also a mistake in the doc... That's an ugly bug...



---

archive/issue_comments_070021.json:
```json
{
    "body": "I change the title hoping someone will pass to check that...",
    "created_at": "2010-04-16T16:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70021",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

I change the title hoping someone will pass to check that...



---

archive/issue_comments_070022.json:
```json
{
    "body": "Hi Nicolas!\n\nThe tests are running.\n\nFor the record: I tried to compare the results in the new doctests\nwith GAP, and I get the following difference:\n\n```\ngap> G := Group([ (1,2) (3,4), (1,2,3,4,10) ]);\nGroup([ (1,2)(3,4), (1,2,3,4,10) ])\ngap> Stabilizer(G, 10);                        \nGroup([ (1,2)(3,4), (2,3,4) ])\n```\n\n```\nsage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4,10)]]) \nsage: G.stabilizer(10) \nPermutation Group with generators [(), (1,2)(3,4), (1,2,3), (1,2,4), (1,3,2), (1,3,4), (1,4,2)] \n```\n\nWell, in fact the results are equal:\n\n```\nsage: G2 = PermutationGroup( [ [(1,2),(3,4)], [(2,3,4)] ])\nsage: G.stabilizer(10) == G2\nTrue\n```\n\nbut GAP's result is nicer.",
    "created_at": "2010-04-18T16:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70022",
    "user": "https://github.com/nthiery"
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

archive/issue_comments_070023.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-19T08:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70023",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070024.json:
```json
{
    "body": "Stay around, I am going to improve my \"horrible\" fix shortly...",
    "created_at": "2010-04-19T08:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70024",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Stay around, I am going to improve my "horrible" fix shortly...



---

archive/issue_comments_070025.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-19T09:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70025",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070026.json:
```json
{
    "body": "Ok, now all the job is made in gap. The number of tests (including a random one) must help these methods to give right answer!\n\nAll tests passes including the optional one...",
    "created_at": "2010-04-19T09:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70026",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Ok, now all the job is made in gap. The number of tests (including a random one) must help these methods to give right answer!

All tests passes including the optional one...



---

archive/issue_comments_070027.json:
```json
{
    "body": "Attachment [trac_8030_stabilizer_bug-nb.patch](tarball://root/attachments/some-uuid/ticket8030/trac_8030_stabilizer_bug-nb.patch) by @nthiery created at 2010-05-18 21:30:58\n\nThe new implementation does the simplest thing: to just call GAP; and that fixes the problem at hand.The patch also adds a lots of doctests. All tests pass on 4.4.1. Positive review!",
    "created_at": "2010-05-18T21:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70027",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_8030_stabilizer_bug-nb.patch](tarball://root/attachments/some-uuid/ticket8030/trac_8030_stabilizer_bug-nb.patch) by @nthiery created at 2010-05-18 21:30:58

The new implementation does the simplest thing: to just call GAP; and that fixes the problem at hand.The patch also adds a lots of doctests. All tests pass on 4.4.1. Positive review!



---

archive/issue_comments_070028.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-18T21:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70028",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070029.json:
```json
{
    "body": "Fix a trivial typo, and add hg header. Apply only this one.",
    "created_at": "2010-05-18T21:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70029",
    "user": "https://github.com/nthiery"
}
```

Fix a trivial typo, and add hg header. Apply only this one.



---

archive/issue_comments_070030.json:
```json
{
    "body": "Attachment [trac_8030-stabilizer_bug-nb.patch](tarball://root/attachments/some-uuid/ticket8030/trac_8030-stabilizer_bug-nb.patch) by @rbeezer created at 2010-05-31 03:23:36\n\nStandalone doctring improvements, reviewer patch",
    "created_at": "2010-05-31T03:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70030",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_8030-stabilizer_bug-nb.patch](tarball://root/attachments/some-uuid/ticket8030/trac_8030-stabilizer_bug-nb.patch) by @rbeezer created at 2010-05-31 03:23:36

Standalone doctring improvements, reviewer patch



---

archive/issue_comments_070031.json:
```json
{
    "body": "Attachment [trac_8030-reviewer-doc-edit.patch](tarball://root/attachments/some-uuid/ticket8030/trac_8030-reviewer-doc-edit.patch) by @rbeezer created at 2010-05-31 03:30:06\n\nSomehow I thought this needed review, but obviously didn't look close enough.\n\nIn any event, I made some improvements to the docstring, which I just added.  I'm going to move them to a new ticket, so as to not mess this up.  Sorry for the confusion.\n\nRelease manager - you can remove trac_8030-reviewer-doc-edit.patch - it'll appear elsewhere with a new name.\n\nRob",
    "created_at": "2010-05-31T03:30:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70031",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_8030-reviewer-doc-edit.patch](tarball://root/attachments/some-uuid/ticket8030/trac_8030-reviewer-doc-edit.patch) by @rbeezer created at 2010-05-31 03:30:06

Somehow I thought this needed review, but obviously didn't look close enough.

In any event, I made some improvements to the docstring, which I just added.  I'm going to move them to a new ticket, so as to not mess this up.  Sorry for the confusion.

Release manager - you can remove trac_8030-reviewer-doc-edit.patch - it'll appear elsewhere with a new name.

Rob



---

archive/issue_events_019238.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-06-03T04:18:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8030#event-19238"
}
```



---

archive/issue_comments_070032.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-03T04:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70032",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_070033.json:
```json
{
    "body": "It seems that [attachment:trac_8030-reviewer-doc-edit.patch] made it into 4.4.3.alpha2.  From building the PDF reference manual:\n\n```\n[2668] [2669] [2670] [2671] [2672] [2673] [2674] [2675] [2676] [2677]\n! Undefined control sequence.\nl.217693 ...als}(\\mathrm{pos}_{i+1})]_{1 \\leqslant\n                                                   i \\leqslant n}$\n? \n```\nI suppose #9102 is the place to fix this?",
    "created_at": "2010-06-03T09:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70033",
    "user": "https://github.com/qed777"
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

archive/issue_comments_070034.json:
```json
{
    "body": "Replying to [comment:10 mpatel]:\n> It seems that [attachment:trac_8030-reviewer-doc-edit.patch] made it into 4.4.3.alpha2.  From building the PDF reference manual:\n> \n> ```\n> [2668] [2669] [2670] [2671] [2672] [2673] [2674] [2675] [2676] [2677]\n> ! Undefined control sequence.\n> l.217693 ...als}(\\mathrm{pos}_{i+1})]_{1 \\leqslant\n>                                                    i \\leqslant n}$\n> ? \n> ```\n> I suppose #9102 is the place to fix this?\n\n\nHi Misha,\n\nThat was a new macro to me, and worked fine in the HTML version of the docs.  Looks like it is part of the AMS packages.  I'll work on a patch as part of #9102, but long-term, does the PDF version need  amsmath or amssymb  packages to be included?  I can investigate later, but have a busy day today, so I'll get a quick fix up first.\n\nRob",
    "created_at": "2010-06-03T15:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8030",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8030#issuecomment-70034",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:10 mpatel]:
> It seems that [attachment:trac_8030-reviewer-doc-edit.patch] made it into 4.4.3.alpha2.  From building the PDF reference manual:
> 
> ```
> [2668] [2669] [2670] [2671] [2672] [2673] [2674] [2675] [2676] [2677]
> ! Undefined control sequence.
> l.217693 ...als}(\mathrm{pos}_{i+1})]_{1 \leqslant
>                                                    i \leqslant n}$
> ? 
> ```
> I suppose #9102 is the place to fix this?


Hi Misha,

That was a new macro to me, and worked fine in the HTML version of the docs.  Looks like it is part of the AMS packages.  I'll work on a patch as part of #9102, but long-term, does the PDF version need  amsmath or amssymb  packages to be included?  I can investigate later, but have a busy day today, so I'll get a quick fix up first.

Rob
