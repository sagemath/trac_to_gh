# Issue 8414: lattice -> domain in weyl_groups.py

archive/issues_008414.json:
```json
{
    "body": "Assignee: @dwbump\n\nCC:  sage-combinat\n\nKeywords: Weyl groups\n\nWeylGroups and WeylGroupElements have a method lattice() and also an attribute _lattice. At one time this pointed to the ambient lattice, but now it points to the ambient space.\n\nAfter some discussion here:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/ad0c77557e78313f/9cfd6f09bcd1de2f?#9cfd6f09bcd1de2f\n\nit has been decided that the method and attribute should be called `domain`.\n\nThe patch also makes reflections of the Weyl group a\nfamily and adds methods `inverse_family` and `has_key` to\nthe method family, per Nicolas' suggestion.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8414\n\n",
    "closed_at": "2010-04-19T05:22:06Z",
    "created_at": "2010-03-02T01:36:04Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "lattice -> domain in weyl_groups.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8414",
    "user": "https://github.com/dwbump"
}
```
Assignee: @dwbump

CC:  sage-combinat

Keywords: Weyl groups

WeylGroups and WeylGroupElements have a method lattice() and also an attribute _lattice. At one time this pointed to the ambient lattice, but now it points to the ambient space.

After some discussion here:

http://groups.google.com/group/sage-devel/browse_thread/thread/ad0c77557e78313f/9cfd6f09bcd1de2f?#9cfd6f09bcd1de2f

it has been decided that the method and attribute should be called `domain`.

The patch also makes reflections of the Weyl group a
family and adds methods `inverse_family` and `has_key` to
the method family, per Nicolas' suggestion.

Issue created by migration from https://trac.sagemath.org/ticket/8414





---

archive/issue_comments_075261.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2010-03-02T01:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75261",
    "user": "https://github.com/dwbump"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_075262.json:
```json
{
    "body": "Changing assignee from @aghitza to @dwbump.",
    "created_at": "2010-03-02T01:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75262",
    "user": "https://github.com/dwbump"
}
```

Changing assignee from @aghitza to @dwbump.



---

archive/issue_comments_075263.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-10T12:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75263",
    "user": "https://github.com/dwbump"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075264.json:
```json
{
    "body": "Hi Dan!\n\nSorry for the late reply; I am just back from vacations.\n\nDepending on how the Weyl group is constructed, W.lattice() can actually be a lattice:\n\n```\nsage: WeylGroup(RootSystem([\"A\",3]).root_lattice())\nWeyl Group of type ['A', 3] (as a matrix group acting on the root lattice)\nsage: WeylGroup(RootSystem([\"A\",3]).root_lattice()).lattice()\nRoot lattice of the Root system of type ['A', 3]\n```\n\nIn fact, the name was meant as short hand for \"which realization of the root lattice the group is naturally acting upon\".\n\nThat being said, I agree that this name is not good. In particular, we probably will want to generalize this soon to handle Coxeter groups implemented as permutation groups (e.g. acting on the roots) instead of matrix groups. So the semantic of this method should probably be to return which ever natural space (or set) the group is naturally acting on. Its name should reflect that.\n\nAny good suggestions?\n\n- natural_action_space?\n- root_system_realization?\n- ...?\n\nAs for the reflections: this sounds like a useful feature, thanks! May I suggest an alternative implementation, namely to:\n\n- make reflections to be a family (still with the roots as keys) instead of a dictionary\n\n- Add an \"inverse\" feature to finite families (at least those without duplicates) returning the family with the keys and values exchanged.\n\nThen, you would do W.reflections().inverse_family() instead of W.reflections(keys=reflections). This would solve the problem at hand, be of general usefulness, and not clutter the Weyl group interface.\n\nThanks in advance!\n\nBest,\n           Nicolas",
    "created_at": "2010-03-10T16:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75264",
    "user": "https://github.com/nthiery"
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

archive/issue_comments_075265.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-10T16:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75265",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075266.json:
```json
{
    "body": "```\nThat being said, I agree that this name is not good. In particular, we probably will want to generalize this soon to handle Coxeter groups implemented as permutation groups (e.g. acting on the roots) instead of matrix groups. So the semantic of this method should probably be to return which ever natural space (or set) the group is naturally acting on. Its name should reflect that.\n```\nIt seems to me that the need to implement roots for general Coxeter groups is a distinct issue. If the Coxeter group happens to be a Weyl group the roots are embedded in a lattice or vector space and that is a sufficiently important special case that it should be preserved.\n\n```\nAny good suggestions?\n\n    * natural_action_space?\n    * root_system_realization?\n    * ...?\n```\nTo me it would seem best to call it space. Then if the Weyl group is created in such a way that it is a lattice, it would be a misnomer, but calling a lattice a space seems less egregious than calling a space a lattice.\n\nAn alternative term would be *module*.\n\nI will revise the patch implementing the change for families if we can agree on this matter of terminology.\n\nDan",
    "created_at": "2010-03-11T13:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75266",
    "user": "https://github.com/dwbump"
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

archive/issue_comments_075267.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-11T17:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75267",
    "user": "https://github.com/dwbump"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075268.json:
```json
{
    "body": "I have revised the patch taking into account Nicolas' suggestion that  reflections be a family, and that finite families should have inverse  families as a method.\n\nI did not revise the change lattice -> space pending further discussion of the matter. As I said in my last message, it seems that \nit might sometimes be a misnomer but still an improvement over calling the method \"lattice\".",
    "created_at": "2010-03-11T17:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75268",
    "user": "https://github.com/dwbump"
}
```

I have revised the patch taking into account Nicolas' suggestion that  reflections be a family, and that finite families should have inverse  families as a method.

I did not revise the change lattice -> space pending further discussion of the matter. As I said in my last message, it seems that 
it might sometimes be a misnomer but still an improvement over calling the method "lattice".



---

archive/issue_comments_075269.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-17T14:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75269",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075270.json:
```json
{
    "body": "Hi Dan,\n\nI had a quick look at your patch. It looks good but I'm not sure I'll find time to formally review it so if someone else wants to formally review it please go. I just want to mention a small problem which forbid it to go into sage: there is no examples or doctests for `inverse_family`. Moreover I think that `has_key`  probably deserve a negative (i.e. returning `False`) examples.\n\nSorry for not having the time to do it...\n\nFlorent",
    "created_at": "2010-04-17T14:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75270",
    "user": "https://github.com/hivert"
}
```

Hi Dan,

I had a quick look at your patch. It looks good but I'm not sure I'll find time to formally review it so if someone else wants to formally review it please go. I just want to mention a small problem which forbid it to go into sage: there is no examples or doctests for `inverse_family`. Moreover I think that `has_key`  probably deserve a negative (i.e. returning `False`) examples.

Sorry for not having the time to do it...

Florent



---

archive/issue_comments_075271.json:
```json
{
    "body": "Replying to [comment:8 hivert]:\n> Hi Dan,\n> \n> I had a quick look at your patch. It looks good but I'm not sure I'll find time to formally review it so if someone else wants to formally review it please go. I just want to mention a small problem which forbid it to go into sage: there is no examples or doctests for `inverse_family`. Moreover I think that `has_key`  probably deserve a negative (i.e. returning `False`) examples.\n\n\nI have fixed those yesterday in the Sage-Combinat queue; I'll try to finish the review tonight.\n\nCheers,",
    "created_at": "2010-04-17T17:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75271",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:8 hivert]:
> Hi Dan,
> 
> I had a quick look at your patch. It looks good but I'm not sure I'll find time to formally review it so if someone else wants to formally review it please go. I just want to mention a small problem which forbid it to go into sage: there is no examples or doctests for `inverse_family`. Moreover I think that `has_key`  probably deserve a negative (i.e. returning `False`) examples.


I have fixed those yesterday in the Sage-Combinat queue; I'll try to finish the review tonight.

Cheers,



---

archive/issue_comments_075272.json:
```json
{
    "body": "Changing keywords from \"\" to \"Weyl groups\".",
    "created_at": "2010-04-17T22:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75272",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "" to "Weyl groups".



---

archive/issue_comments_075273.json:
```json
{
    "body": "Hi Dan!\n\nAll test pass, and the patch does what we had agreed upon. Thanks for handling this!\n\nPlease double check my reviewer patch, and if ok set a positive review on my behalf!",
    "created_at": "2010-04-17T22:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75273",
    "user": "https://github.com/nthiery"
}
```

Hi Dan!

All test pass, and the patch does what we had agreed upon. Thanks for handling this!

Please double check my reviewer patch, and if ok set a positive review on my behalf!



---

archive/issue_comments_075274.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-17T22:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75274",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075275.json:
```json
{
    "body": "OK, I am setting positive review on the reviewer's patch.",
    "created_at": "2010-04-18T03:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75275",
    "user": "https://github.com/dwbump"
}
```

OK, I am setting positive review on the reviewer's patch.



---

archive/issue_comments_075276.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-18T03:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75276",
    "user": "https://github.com/dwbump"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075277.json:
```json
{
    "body": "Dan: please produce patch files using Mercurial, not using diff: they should have a header listing your email address and other information.  The \"commit\" message should also start with the trac ticket, also.  See [http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change](http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change) for more information.",
    "created_at": "2010-04-18T05:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75277",
    "user": "https://github.com/jhpalmieri"
}
```

Dan: please produce patch files using Mercurial, not using diff: they should have a header listing your email address and other information.  The "commit" message should also start with the trac ticket, also.  See [http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change](http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change) for more information.



---

archive/issue_comments_075278.json:
```json
{
    "body": "Responding to jhpalmieri, I remade my patch to contain mercurial headers.\n\nNicolas' patch goes on top of mine. His patch headers contain some\nnon-ascii characters which I had to delete before merging his patch.",
    "created_at": "2010-04-18T17:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75278",
    "user": "https://github.com/dwbump"
}
```

Responding to jhpalmieri, I remade my patch to contain mercurial headers.

Nicolas' patch goes on top of mine. His patch headers contain some
non-ascii characters which I had to delete before merging his patch.



---

archive/issue_comments_075279.json:
```json
{
    "body": "Attachment [trac_8414_weyl_group_space-review-nt.patch](tarball://root/attachments/some-uuid/ticket8414/trac_8414_weyl_group_space-review-nt.patch) by @nthiery created at 2010-04-18 18:09:08",
    "created_at": "2010-04-18T18:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75279",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_8414_weyl_group_space-review-nt.patch](tarball://root/attachments/some-uuid/ticket8414/trac_8414_weyl_group_space-review-nt.patch) by @nthiery created at 2010-04-18 18:09:08



---

archive/issue_comments_075280.json:
```json
{
    "body": "Replying to [comment:13 bump]:\n> Responding to jhpalmieri, I remade my patch to contain mercurial headers.\n\n\nPlease also include #8414: in front of the patch description!\n\n> Nicolas' patch goes on top of mine. His patch headers contain some\n> non-ascii characters which I had to delete before merging his patch.\n\n\nOops, mercurial now speaks French on my machine????\n\nI just re=uploaded the patch after fixing it.",
    "created_at": "2010-04-18T18:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75280",
    "user": "https://github.com/nthiery"
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

archive/issue_comments_075281.json:
```json
{
    "body": "Rename lattice() method space() in WeylGroups. Add keys option to reflections()",
    "created_at": "2010-04-19T01:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75281",
    "user": "https://github.com/dwbump"
}
```

Rename lattice() method space() in WeylGroups. Add keys option to reflections()



---

archive/issue_comments_075282.json:
```json
{
    "body": "Attachment [trac_8414_weyl_group_space.patch](tarball://root/attachments/some-uuid/ticket8414/trac_8414_weyl_group_space.patch) by @dwbump created at 2010-04-19 01:21:22\n\n> Please also include #8414: in front of the patch description!\n\n\nOK, I changed the patch description to begin #8414.",
    "created_at": "2010-04-19T01:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75282",
    "user": "https://github.com/dwbump"
}
```

Attachment [trac_8414_weyl_group_space.patch](tarball://root/attachments/some-uuid/ticket8414/trac_8414_weyl_group_space.patch) by @dwbump created at 2010-04-19 01:21:22

> Please also include #8414: in front of the patch description!


OK, I changed the patch description to begin #8414.



---

archive/issue_comments_075283.json:
```json
{
    "body": "Merged in 4.4.alpha1:\n- trac_8414_weyl_group_space.patch\n- trac_8414_weyl_group_space-review-nt.patch",
    "created_at": "2010-04-19T05:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75283",
    "user": "https://github.com/jhpalmieri"
}
```

Merged in 4.4.alpha1:
- trac_8414_weyl_group_space.patch
- trac_8414_weyl_group_space-review-nt.patch



---

archive/issue_comments_075284.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8414#issuecomment-75284",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_020164.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-19T05:22:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8414",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8414#event-20164"
}
```
