# Issue 8589: New feature : Hopf algebra structure on group algebras

Issue created by migration from https://trac.sagemath.org/ticket/8589

Original creator: vferay

Original creation time: 2010-03-23 17:16:37

Assignee: sage-combinat

CC:  niles sage-combinat

This patch gives its Hopf algebra structure to the group algebra of `G` over `R` created in the following way


```
   sage: G.algebra(R)
```


Another feature is a method is_central on elements of the algebra (which works also for monoid algebras so is in the file sage.categories.monoids)


---

Comment by vferay created at 2010-03-23 17:35:21

Doing this, I have encountered and solved some problems:

* The generators of permutation groups were returned as a list and not as a family, which is the case for other types of groups. They are now returned as a family.

* The Hopf algebra structure didn't include counit. This has been corrected.

* There was a bug in module_morphism which didn't work when the codomain was the ring itself (because it is not considered as a module by sage). It has been corrected.


---

Comment by vferay created at 2010-03-23 17:35:21

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-04-02 16:20:33

Is line 919 in sage/categories/modules_with_basis.py a typo?

```
:meth:`rodulesWithBasis.HomCategory.ElementMethods.on_basis`. 
       ^
```

Also, at the start of sage/groups/perm_gps/permgroup.py, the line 

```
from sage.combinat.family import Family
```

might be changed to 

```
from sage.sets.family import Family
```

(since sage.combinat.family says "This is a backward compatibility stub. Use :mod:`sage.sets.family` instead").


---

Comment by vferay created at 2010-04-07 16:03:10

You're right! A new version of the patch has been uploaded

Thanks for these comments!

Valentin


---

Comment by hivert created at 2010-05-05 02:23:53

Replying to [comment:3 vferay]:
> You're right! A new version of the patch has been uploaded

The feature here depends on the Algebra functorial constructions #8881 which are not yet finished.


---

Comment by vferay created at 2010-05-05 09:06:42

Ok I wait until the Algebra functorial constructions are finished to finalize the patch


---

Comment by vferay created at 2010-05-05 09:06:42

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2010-06-09 15:32:42

Replying to [comment:5 vferay]:
> Ok I wait until the Algebra functorial constructions are finished to finalize the patch

#8881 was just merged in sage 4.4.4!


---

Comment by nthiery created at 2010-06-14 23:03:13

For the record with 4.4.3 and this patch applied,

```
sage: SymmetricGroup(3).algebra(QQ)
```

triggers an error about _basis_keys


---

Comment by niles created at 2010-10-10 20:15:44

Hello,

Is there any new progress on this?  

I'd like to help, but I think I have to start by understanding `Family`:  

Replying to [comment:1 vferay]:
> * The generators of permutation groups were returned as a list and not as a family, which is the case for other types of groups. They are now returned as a family.

`DihedralGroup` and `CyclicPermutationGroup` both return `gens` as lists, and polynomial/power series rings return `gens` as tuples . . . could someone tell me if there is an effort under way to convert all of these to `Family`, or what sorts of things do already return `gens` as a `Family`?

Are there other work issues for this patch (other than the bug with 4.4.3 reported by nthiery), or is it otherwise ready for review?

thanks,
Niles


---

Comment by vferay created at 2010-10-11 15:57:28

Hello,

   finishing this patch is on my todo list of the week.

>  could someone tell me if there is an effort under way to convert all of these to Family, or 
> what sorts of things do already return gens as a Family?
If we are only interested with groups, there is no interest to return things as a Family, but it is the natural structure when we work with algebra generators. So the change was to unify this but I confess that I don't remember for which function I wanted to do that.

more soon,

Valentin


---

Comment by nthiery created at 2010-10-12 16:18:51

Replying to [comment:9 vferay]:
> > could someone tell me if there is an effort under way to convert all of these to Family, or 
> > what sorts of things do already return gens as a Family?

> If we are only interested with groups, there is no interest to
> return things as a Family, but it is the natural structure when we
> work with algebra generators. So the change was to unify this but I
> confess that I don't remember for which function I wanted to do
> that.

The current convention is for algebra_generators,
semigroup_generators, and the like to return families.

There definitely is a plan for the long run (at least a wish from the
sage-combinat group :-)) to have .gens() return a family as well. But
this will require some serious coordination to maintain backward
compatibility, and I'd rather have it done in a separate patch.

Valentin: do you really need this feature right now?


---

Comment by vferay created at 2010-10-13 13:36:02

Hello,

> Valentin: do you really need this feature right now? 
It was needed in the function algebra_generators() which can be called on a group or semi-group algebra. But I changed this function such that it works in both cases.

I splitted the patch in 2 and keep just the part on group algebra and Hopf algebra (and not the part turning group generators into a family).

Everything seems to work now (I have one error in the test of hopf_algebra_with_basis.py :
"... still using old coercion framework) when the patch is applied in the sage-combinat queue. But it seems to depend on other patches (because import it when no other patches are applied lead to a lot of mistakes. Nicolas, do you know which ones and what I should do.

I attach the new version of the patch


---

Comment by nthiery created at 2010-10-13 14:19:08

Replying to [comment:11 vferay]:
> It was needed in the function algebra_generators() which can be
> called on a group or semi-group algebra. But I changed this function
> such that it works in both cases.

Thanks. Do you mind fixing instead semigroup_generators?

> I splitted the patch in 2 and keep just the part on group algebra
> and Hopf algebra (and not the part turning group generators into a
> family).

Thanks.

> Everything seems to work now (I have one error in the test of
> hopf_algebra_with_basis.py : "... still using old coercion
> framework) when the patch is applied in the sage-combinat queue. But
> it seems to depend on other patches (because import it when no other
> patches are applied lead to a lot of mistakes. Nicolas, do you know
> which ones and what I should do.

After investigation, your patch depends on:

 - trac_9648_modulemorphism_codomain_extension-cs.patch # Needs review
 - free_module_basis_key_initialisation-nb.patch

#9648 just needs a last pass of proofreading + rerunning the tests
with the latest Sage. Do you volunteer for the former?

I just created #10127 for the second. We should be able to finalize it
soon with Nicolas B.

With those patches applied, I only get two trivial errors in sage/categories:


```
sage -t  "devel/sage-combinat/sage/categories/groups.py"    
**********************************************************************
File "/opt/sage-4.5.2/devel/sage-combinat/sage/categories/groups.py", line 69:
    sage: A.group_generators()
Expected:
    [(2,3,4), (1,2,3)]
Got:
    [(1,2,3), (2,3,4)]
sage -t  "devel/sage-combinat/sage/categories/algebra_functor.py"
**********************************************************************
File "/opt/sage-4.5.2/devel/sage-combinat/sage/categories/algebra_functor.py", line 37:
    sage: Groups().Algebras(QQ) # todo: update once there will be a category for group algebras
Expected:
    Category of monoid algebras over Rational Field
Got:
    Category of group algebras over Rational Field
```


Cheers,
			Nicolas


---

Comment by vferay created at 2010-10-14 10:09:20

Hi

> Thanks. Do you mind fixing instead semigroup_generators? 
You mean that you want semigroup_generators to return a list. I assume that this will need to change a few things in all the semigroup file. Another solution is also to overload the algebra_generators function for group algebras.

> #9648 just needs a last pass of proofreading + rerunning the tests with the latest Sage. Do you > volunteer for the former? 
ok I will try to do that.

> With those patches applied, I only get two trivial errors in sage/categories: 
the first one does not appear on my computer (?). I corrected the second one.

Valentin


---

Comment by nthiery created at 2010-10-14 12:57:10

Replying to [comment:13 vferay]:
> > Thanks. Do you mind fixing instead semigroup_generators? 
> You mean that you want semigroup_generators to return a list. I assume that this will need to change a few things in all the semigroup file. Another solution is also to overload the algebra_generators function for group algebras.

Oops, I investigated this too quickly. The culprit is actually Groups.ParentMethods.group_generators which returns self.gens() directly, instead of making the result first into a family.

> > #9648 just needs a last pass of proofreading + rerunning the tests with the latest Sage. > > Do you volunteer for the former? 
> ok I will try to do that.

Thanks!

> > With those patches applied, I only get two trivial errors in sage/categories: 
> the first one does not appear on my computer (?). 

Hmm. Which patches did you have applied when you tried? Which version of Sage?

> I corrected the second one.

Thanks!


---

Comment by vferay created at 2010-10-14 13:28:57

Replying to nthiery:

> Oops, I investigated this too quickly. The culprit is actually
> Groups.ParentMethods?.group_generators which returns self.gens() directly, instead of making the > result first into a family. 
ok I have changed this function and every test pass...

I think the patch is ready now, I am waiting that the other patches are included in sage to set it as need_review .


> > > With those patches applied, I only get two trivial errors in sage/categories:
> > the first one does not appear on my computer (?).
> Hmm. Which patches did you have applied when you tried? Which version of Sage? 
version 4.5.3, patches up to this one were applied. But now, I find the same result as you do (except that now, it has been transformed into a family)...

Valentin


---

Comment by nthiery created at 2010-10-15 13:56:12

All test pass on 4.5.3, with the following patches applied:

```
trac_9648_modulemorphism_codomain_extension-cs.patch # Needs review
trac_10127_free_module_basis_key_initialisation-nb.patch # Under review
trac_8589_feature_group_algebras_vf.patch  #-4_5    # Under review
trac_8589_feature_group_algebras-reviewer-nt.patch
```


Generally speaking, the patch is good to go, up to missing documentation and tests for Coalgebras.ElementMethods.counit. Valentin, please fold in my reviewer's patch, add doc and test, check that the documentation compiles smoothly, and upload here. 

Then you can set a positive review on my behalf. Thanks for your work on that!

Niles: feel free to make a last check up!


---

Comment by vferay created at 2010-10-18 13:20:28

Changing status from needs_work to positive_review.


---

Comment by vferay created at 2010-10-18 13:20:28

> Valentin, please fold in my reviewer's patch, add doc and test, check that the documentation
> compiles smoothly, and upload here.

Done!


---

Attachment


---

Attachment

Which of the patches should be applied?


---

Comment by jdemeyer created at 2010-10-23 11:58:11

Changing status from positive_review to needs_info.


---

Comment by vferay created at 2010-10-26 08:16:11

Changing status from needs_info to needs_review.


---

Comment by vferay created at 2010-10-26 08:16:11

The two files are the same. I did wrong manipulation. Sorry for that


---

Comment by vferay created at 2010-10-26 08:16:20

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-01 10:06:12

Resolution: fixed


---

Comment by chapoton created at 2017-07-19 08:25:27

name with accent
