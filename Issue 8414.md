# Issue 8414: lattice -> space in weyl_groups.py

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2010-03-02 01:36:04

Assignee: AlexGhitza

CC:  sage-combinat

WeylGroups and WeylGroupElements have a method lattice() and also an attribute _lattice. At one time this pointed to the ambient lattice, but now it points to the ambient space.

For consistency perhaps the name of the method and attribute should therefore be changed to space(). The patch makes this change.


---

Comment by bump created at 2010-03-02 01:41:49

Changing component from algebra to combinatorics.


---

Comment by bump created at 2010-03-02 01:41:49

Changing assignee from AlexGhitza to bump.


---

Comment by bump created at 2010-03-10 12:13:34

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-03-10 16:22:55

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

Comment by nthiery created at 2010-03-10 16:22:55

Changing status from needs_review to needs_work.


---

Comment by bump created at 2010-03-11 13:16:16


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

Comment by bump created at 2010-03-11 17:48:17

Changing status from needs_work to needs_review.


---

Comment by bump created at 2010-03-11 17:48:17

I have revised the patch taking into account Nicolas' suggestion that  reflections be a family, and that finite families should have inverse  families as a method.

I did not revise the change lattice -> space pending further discussion of the matter. As I said in my last message, it seems that 
it might sometimes be a misnomer but still an improvement over calling the method "lattice".


---

Comment by hivert created at 2010-04-17 14:28:52

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2010-04-17 14:28:52

Hi Dan,

I had a quick look at your patch. It looks good but I'm not sure I'll find time to formally review it so if someone else wants to formally review it please go. I just want to mention a small problem which forbid it to go into sage: there is no examples or doctests for `inverse_family`. Moreover I think that `has_key`  probably deserve a negative (i.e. returning `False`) examples.

Sorry for not having the time to do it...

Florent


---

Comment by nthiery created at 2010-04-17 17:50:21

Replying to [comment:8 hivert]:
> Hi Dan,
> 
> I had a quick look at your patch. It looks good but I'm not sure I'll find time to formally review it so if someone else wants to formally review it please go. I just want to mention a small problem which forbid it to go into sage: there is no examples or doctests for `inverse_family`. Moreover I think that `has_key`  probably deserve a negative (i.e. returning `False`) examples.

I have fixed those yesterday in the Sage-Combinat queue; I'll try to finish the review tonight.

Cheers,


---

Comment by nthiery created at 2010-04-17 22:37:28

Changing keywords from "" to "Weyl groups".


---

Comment by nthiery created at 2010-04-17 22:37:28

Hi Dan!

All test pass, and the patch does what we had agreed upon. Thanks for handling this!

Please double check my reviewer patch, and if ok set a positive review on my behalf!


---

Comment by nthiery created at 2010-04-17 22:37:28

Changing status from needs_work to needs_review.


---

Comment by bump created at 2010-04-18 03:29:17

OK, I am setting positive review on the reviewer's patch.


---

Comment by bump created at 2010-04-18 03:29:17

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-18 05:16:52

Dan: please produce patch files using Mercurial, not using diff: they should have a header listing your email address and other information.  The "commit" message should also start with the trac ticket, also.  See [http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change](http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change) for more information.


---

Comment by bump created at 2010-04-18 17:48:59

Responding to jhpalmieri, I remade my patch to contain mercurial headers.

Nicolas' patch goes on top of mine. His patch headers contain some
non-ascii characters which I had to delete before merging his patch.


---

Attachment


---

Comment by nthiery created at 2010-04-18 18:11:21

Replying to [comment:13 bump]:
> Responding to jhpalmieri, I remade my patch to contain mercurial headers.

Please also include #8414: in front of the patch description!

> Nicolas' patch goes on top of mine. His patch headers contain some
> non-ascii characters which I had to delete before merging his patch.

Oops, mercurial now speaks French on my machine????

I just re=uploaded the patch after fixing it.


---

Comment by bump created at 2010-04-19 01:19:54

Rename lattice() method space() in WeylGroups. Add keys option to reflections()


---

Attachment

> Please also include #8414: in front of the patch description!

OK, I changed the patch description to begin #8414.


---

Comment by jhpalmieri created at 2010-04-19 05:22:06

Merged in 4.4.alpha1:
 - trac_8414_weyl_group_space.patch
 - trac_8414_weyl_group_space-review-nt.patch


---

Comment by jhpalmieri created at 2010-04-19 05:22:06

Resolution: fixed
