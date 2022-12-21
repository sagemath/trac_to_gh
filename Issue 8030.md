# Issue 8030: Strong generating system work only for transitive group

Issue created by migration from Trac.

Original creator: nborie

Original creation time: 2010-01-21 19:37:01

Assignee: joyner

CC:  sage-combinat

My fault from #6647

The method from Gap work only for transitive group.


```
sage: G = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (3,4))](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: G.strong_generating_system()
[[()], [()], [()], [()]]
sage: G.strong_generating_system(base_of_group=[3,1,2,4])
[[(), (3,4)], [()], [()], [()]]
```


If the first position is not moved by the permutation Group. Errors appears...


---

Comment by nborie created at 2010-01-23 20:23:33

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

Comment by nborie created at 2010-01-23 20:23:33

Changing status from new to needs_review.


---

Comment by nborie created at 2010-03-02 19:03:39

I uploaded a new version. There was also a mistake in the doc... That's an ugly bug...


---

Comment by nborie created at 2010-04-16 16:26:25

I change the title hoping someone will pass to check that...


---

Comment by nthiery created at 2010-04-18 16:15:49

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

Comment by nborie created at 2010-04-19 08:53:07

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2010-04-19 08:53:07

Stay around, I am going to improve my "horrible" fix shortly...


---

Comment by nborie created at 2010-04-19 09:25:52

Changing status from needs_work to needs_review.


---

Comment by nborie created at 2010-04-19 09:25:52

Ok, now all the job is made in gap. The number of tests (including a random one) must help these methods to give right answer!

All tests passes including the optional one...


---

Attachment

The new implementation does the simplest thing: to just call GAP; and that fixes the problem at hand.The patch also adds a lots of doctests. All tests pass on 4.4.1. Positive review!


---

Comment by nthiery created at 2010-05-18 21:30:58

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-05-18 21:40:22

Fix a trivial typo, and add hg header. Apply only this one.


---

Attachment

Standalone doctring improvements, reviewer patch


---

Attachment

Somehow I thought this needed review, but obviously didn't look close enough.

In any event, I made some improvements to the docstring, which I just added.  I'm going to move them to a new ticket, so as to not mess this up.  Sorry for the confusion.

Release manager - you can remove trac_8030-reviewer-doc-edit.patch - it'll appear elsewhere with a new name.

Rob


---

Comment by was created at 2010-06-03 04:18:44

Resolution: fixed


---

Comment by mpatel created at 2010-06-03 09:14:37

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

Comment by rbeezer created at 2010-06-03 15:10:29

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
