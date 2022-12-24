# Issue 8414: lattice -> space in weyl_groups.py

archive/issues_008414.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  sage-combinat\n\nWeylGroups and WeylGroupElements have a method lattice() and also an attribute _lattice. At one time this pointed to the ambient lattice, but now it points to the ambient space.\n\nFor consistency perhaps the name of the method and attribute should therefore be changed to space(). The patch makes this change.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8414\n\n",
    "created_at": "2010-03-02T01:36:04Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "lattice -> space in weyl_groups.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8414",
    "user": "bump"
}
```
Assignee: AlexGhitza

CC:  sage-combinat

WeylGroups and WeylGroupElements have a method lattice() and also an attribute _lattice. At one time this pointed to the ambient lattice, but now it points to the ambient space.

For consistency perhaps the name of the method and attribute should therefore be changed to space(). The patch makes this change.

Issue created by migration from https://trac.sagemath.org/ticket/8414





---

archive/issue_comments_075385.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2010-03-02T01:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75385",
    "user": "bump"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_075386.json:
```json
{
    "body": "Changing assignee from AlexGhitza to bump.",
    "created_at": "2010-03-02T01:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75386",
    "user": "bump"
}
```

Changing assignee from AlexGhitza to bump.



---

archive/issue_comments_075387.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-10T12:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75387",
    "user": "bump"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075388.json:
```json
{
    "body": "Hi Dan!\n\nSorry for the late reply; I am just back from vacations.\n\nDepending on how the Weyl group is constructed, W.lattice() can actually be a lattice:\n\n\n```\nsage: WeylGroup(RootSystem([\"A\",3]).root_lattice())\nWeyl Group of type ['A', 3] (as a matrix group acting on the root lattice)\nsage: WeylGroup(RootSystem([\"A\",3]).root_lattice()).lattice()\nRoot lattice of the Root system of type ['A', 3]\n```\n\n\nIn fact, the name was meant as short hand for \"which realization of the root lattice the group is naturally acting upon\".\n\nThat being said, I agree that this name is not good. In particular, we probably will want to generalize this soon to handle Coxeter groups implemented as permutation groups (e.g. acting on the roots) instead of matrix groups. So the semantic of this method should probably be to return which ever natural space (or set) the group is naturally acting on. Its name should reflect that.\n\nAny good suggestions?\n\n- natural_action_space?\n- root_system_realization?\n- ...?\n\nAs for the reflections: this sounds like a useful feature, thanks! May I suggest an alternative implementation, namely to:\n\n- make reflections to be a family (still with the roots as keys) instead of a dictionary\n\n- Add an \"inverse\" feature to finite families (at least those without duplicates) returning the family with the keys and values exchanged.\n\nThen, you would do W.reflections().inverse_family() instead of W.reflections(keys=reflections). This would solve the problem at hand, be of general usefulness, and not clutter the Weyl group interface.\n\nThanks in advance!\n\nBest,\n           Nicolas",
    "created_at": "2010-03-10T16:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75388",
    "user": "nthiery"
}
```

Hi Dan!

Sorry for the late reply; I am just back from vacations.

Depending on how the Weyl group is constructed, W.lattice() can actually be a lattice:


```
sage: WeylGroup(RootSystem(["A",3]).root_lattice())
Weyl Group of type ['A', 3] (as a matrix group acting on the root lattice)
sage: WeylGroup(RootSystem(["A",3]).root_lattice()).lattice()
Root lattice of the Root system of type ['A', 3]
```


In fact, the name was meant as short hand for "which realization of the root lattice the group is naturally acting upon".

That being said, I agree that this name is not good. In particular, we probably will want to generalize this soon to handle Coxeter groups implemented as permutation groups (e.g. acting on the roots) instead of matrix groups. So the semantic of this method should probably be to return which ever natural space (or set) the group is naturally acting on. Its name should reflect that.

Any good suggestions?

- natural_action_space?
- root_system_realization?
- ...?

As for the reflections: this sounds like a useful feature, thanks! May I suggest an alternative implementation, namely to:

- make reflections to be a family (still with the roots as keys) instead of a dictionary

- Add an "inverse" feature to finite families (at least those without duplicates) returning the family with the keys and values exchanged.

Then, you would do W.reflections().inverse_family() instead of W.reflections(keys=reflections). This would solve the problem at hand, be of general usefulness, and not clutter the Weyl group interface.

Thanks in advance!

Best,
           Nicolas



---

archive/issue_comments_075389.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-10T16:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75389",
    "user": "nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075390.json:
```json
{
    "body": "\n```\nThat being said, I agree that this name is not good. In particular, we probably will want to generalize this soon to handle Coxeter groups implemented as permutation groups (e.g. acting on the roots) instead of matrix groups. So the semantic of this method should probably be to return which ever natural space (or set) the group is naturally acting on. Its name should reflect that.\n```\n\nIt seems to me that the need to implement roots for general Coxeter groups is a distinct issue. If the Coxeter group happens to be a Weyl group the roots are embedded in a lattice or vector space and that is a sufficiently important special case that it should be preserved.\n\n\n```\nAny good suggestions?\n\n    * natural_action_space?\n    * root_system_realization?\n    * ...?\n```\n\nTo me it would seem best to call it space. Then if the Weyl group is created in such a way that it is a lattice, it would be a misnomer, but calling a lattice a space seems less egregious than calling a space a lattice.\n\nAn alternative term would be *module*.\n\nI will revise the patch implementing the change for families if we can agree on this matter of terminology.\n\nDan",
    "created_at": "2010-03-11T13:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75390",
    "user": "bump"
}
```


```
That being said, I agree that this name is not good. In particular, we probably will want to generalize this soon to handle Coxeter groups implemented as permutation groups (e.g. acting on the roots) instead of matrix groups. So the semantic of this method should probably be to return which ever natural space (or set) the group is naturally acting on. Its name should reflect that.
```

It seems to me that the need to implement roots for general Coxeter groups is a distinct issue. If the Coxeter group happens to be a Weyl group the roots are embedded in a lattice or vector space and that is a sufficiently important special case that it should be preserved.


```
Any good suggestions?

    * natural_action_space?
    * root_system_realization?
    * ...?
```

To me it would seem best to call it space. Then if the Weyl group is created in such a way that it is a lattice, it would be a misnomer, but calling a lattice a space seems less egregious than calling a space a lattice.

An alternative term would be *module*.

I will revise the patch implementing the change for families if we can agree on this matter of terminology.

Dan



---

archive/issue_comments_075391.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-11T17:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75391",
    "user": "bump"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075392.json:
```json
{
    "body": "I have revised the patch taking into account Nicolas' suggestion that  reflections be a family, and that finite families should have inverse  families as a method.\n\nI did not revise the change lattice -> space pending further discussion of the matter. As I said in my last message, it seems that \nit might sometimes be a misnomer but still an improvement over calling the method \"lattice\".",
    "created_at": "2010-03-11T17:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75392",
    "user": "bump"
}
```

I have revised the patch taking into account Nicolas' suggestion that  reflections be a family, and that finite families should have inverse  families as a method.

I did not revise the change lattice -> space pending further discussion of the matter. As I said in my last message, it seems that 
it might sometimes be a misnomer but still an improvement over calling the method "lattice".



---

archive/issue_comments_075393.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-17T14:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75393",
    "user": "hivert"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075394.json:
```json
{
    "body": "Hi Dan,\n\nI had a quick look at your patch. It looks good but I'm not sure I'll find time to formally review it so if someone else wants to formally review it please go. I just want to mention a small problem which forbid it to go into sage: there is no examples or doctests for `inverse_family`. Moreover I think that `has_key`  probably deserve a negative (i.e. returning `False`) examples.\n\nSorry for not having the time to do it...\n\nFlorent",
    "created_at": "2010-04-17T14:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75394",
    "user": "hivert"
}
```

Hi Dan,

I had a quick look at your patch. It looks good but I'm not sure I'll find time to formally review it so if someone else wants to formally review it please go. I just want to mention a small problem which forbid it to go into sage: there is no examples or doctests for `inverse_family`. Moreover I think that `has_key`  probably deserve a negative (i.e. returning `False`) examples.

Sorry for not having the time to do it...

Florent



---

archive/issue_comments_075395.json:
```json
{
    "body": "Replying to [comment:8 hivert]:\n> Hi Dan,\n> \n> I had a quick look at your patch. It looks good but I'm not sure I'll find time to formally review it so if someone else wants to formally review it please go. I just want to mention a small problem which forbid it to go into sage: there is no examples or doctests for `inverse_family`. Moreover I think that `has_key`  probably deserve a negative (i.e. returning `False`) examples.\n\nI have fixed those yesterday in the Sage-Combinat queue; I'll try to finish the review tonight.\n\nCheers,",
    "created_at": "2010-04-17T17:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75395",
    "user": "nthiery"
}
```

Replying to [comment:8 hivert]:
> Hi Dan,
> 
> I had a quick look at your patch. It looks good but I'm not sure I'll find time to formally review it so if someone else wants to formally review it please go. I just want to mention a small problem which forbid it to go into sage: there is no examples or doctests for `inverse_family`. Moreover I think that `has_key`  probably deserve a negative (i.e. returning `False`) examples.

I have fixed those yesterday in the Sage-Combinat queue; I'll try to finish the review tonight.

Cheers,



---

archive/issue_comments_075396.json:
```json
{
    "body": "Changing keywords from \"\" to \"Weyl groups\".",
    "created_at": "2010-04-17T22:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75396",
    "user": "nthiery"
}
```

Changing keywords from "" to "Weyl groups".



---

archive/issue_comments_075397.json:
```json
{
    "body": "Hi Dan!\n\nAll test pass, and the patch does what we had agreed upon. Thanks for handling this!\n\nPlease double check my reviewer patch, and if ok set a positive review on my behalf!",
    "created_at": "2010-04-17T22:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75397",
    "user": "nthiery"
}
```

Hi Dan!

All test pass, and the patch does what we had agreed upon. Thanks for handling this!

Please double check my reviewer patch, and if ok set a positive review on my behalf!



---

archive/issue_comments_075398.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-17T22:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75398",
    "user": "nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075399.json:
```json
{
    "body": "OK, I am setting positive review on the reviewer's patch.",
    "created_at": "2010-04-18T03:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75399",
    "user": "bump"
}
```

OK, I am setting positive review on the reviewer's patch.



---

archive/issue_comments_075400.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-18T03:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75400",
    "user": "bump"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075401.json:
```json
{
    "body": "Dan: please produce patch files using Mercurial, not using diff: they should have a header listing your email address and other information.  The \"commit\" message should also start with the trac ticket, also.  See [http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change](http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change) for more information.",
    "created_at": "2010-04-18T05:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75401",
    "user": "jhpalmieri"
}
```

Dan: please produce patch files using Mercurial, not using diff: they should have a header listing your email address and other information.  The "commit" message should also start with the trac ticket, also.  See [http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change](http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change) for more information.



---

archive/issue_comments_075402.json:
```json
{
    "body": "Responding to jhpalmieri, I remade my patch to contain mercurial headers.\n\nNicolas' patch goes on top of mine. His patch headers contain some\nnon-ascii characters which I had to delete before merging his patch.",
    "created_at": "2010-04-18T17:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75402",
    "user": "bump"
}
```

Responding to jhpalmieri, I remade my patch to contain mercurial headers.

Nicolas' patch goes on top of mine. His patch headers contain some
non-ascii characters which I had to delete before merging his patch.



---

archive/issue_comments_075403.json:
```json
{
    "body": "Attachment [trac_8414_weyl_group_space-review-nt.patch](tarball://root/attachments/some-uuid/ticket8414/trac_8414_weyl_group_space-review-nt.patch) by nthiery created at 2010-04-18 18:09:08",
    "created_at": "2010-04-18T18:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75403",
    "user": "nthiery"
}
```

Attachment [trac_8414_weyl_group_space-review-nt.patch](tarball://root/attachments/some-uuid/ticket8414/trac_8414_weyl_group_space-review-nt.patch) by nthiery created at 2010-04-18 18:09:08



---

archive/issue_comments_075404.json:
```json
{
    "body": "Replying to [comment:13 bump]:\n> Responding to jhpalmieri, I remade my patch to contain mercurial headers.\n\nPlease also include #8414: in front of the patch description!\n\n> Nicolas' patch goes on top of mine. His patch headers contain some\n> non-ascii characters which I had to delete before merging his patch.\n\nOops, mercurial now speaks French on my machine????\n\nI just re=uploaded the patch after fixing it.",
    "created_at": "2010-04-18T18:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75404",
    "user": "nthiery"
}
```

Replying to [comment:13 bump]:
> Responding to jhpalmieri, I remade my patch to contain mercurial headers.

Please also include #8414: in front of the patch description!

> Nicolas' patch goes on top of mine. His patch headers contain some
> non-ascii characters which I had to delete before merging his patch.

Oops, mercurial now speaks French on my machine????

I just re=uploaded the patch after fixing it.



---

archive/issue_comments_075405.json:
```json
{
    "body": "Rename lattice() method space() in WeylGroups. Add keys option to reflections()",
    "created_at": "2010-04-19T01:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75405",
    "user": "bump"
}
```

Rename lattice() method space() in WeylGroups. Add keys option to reflections()



---

archive/issue_comments_075406.json:
```json
{
    "body": "Attachment [trac_8414_weyl_group_space.patch](tarball://root/attachments/some-uuid/ticket8414/trac_8414_weyl_group_space.patch) by bump created at 2010-04-19 01:21:22\n\n> Please also include #8414: in front of the patch description!\n\nOK, I changed the patch description to begin #8414.",
    "created_at": "2010-04-19T01:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75406",
    "user": "bump"
}
```

Attachment [trac_8414_weyl_group_space.patch](tarball://root/attachments/some-uuid/ticket8414/trac_8414_weyl_group_space.patch) by bump created at 2010-04-19 01:21:22

> Please also include #8414: in front of the patch description!

OK, I changed the patch description to begin #8414.



---

archive/issue_comments_075407.json:
```json
{
    "body": "Merged in 4.4.alpha1:\n- trac_8414_weyl_group_space.patch\n- trac_8414_weyl_group_space-review-nt.patch",
    "created_at": "2010-04-19T05:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75407",
    "user": "jhpalmieri"
}
```

Merged in 4.4.alpha1:
- trac_8414_weyl_group_space.patch
- trac_8414_weyl_group_space-review-nt.patch



---

archive/issue_comments_075408.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75408",
    "user": "jhpalmieri"
}
```

Resolution: fixed
