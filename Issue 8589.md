# Issue 8589: New feature : Hopf algebra structure on group algebras

archive/issues_008589.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  @nilesjohnson sage-combinat\n\nThis patch gives its Hopf algebra structure to the group algebra of `G` over `R` created in the following way\n\n\n```\n   sage: G.algebra(R)\n```\n\n\nAnother feature is a method is_central on elements of the algebra (which works also for monoid algebras so is in the file sage.categories.monoids)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8589\n\n",
    "created_at": "2010-03-23T17:16:37Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "New feature : Hopf algebra structure on group algebras",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8589",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```
Assignee: sage-combinat

CC:  @nilesjohnson sage-combinat

This patch gives its Hopf algebra structure to the group algebra of `G` over `R` created in the following way


```
   sage: G.algebra(R)
```


Another feature is a method is_central on elements of the algebra (which works also for monoid algebras so is in the file sage.categories.monoids)

Issue created by migration from https://trac.sagemath.org/ticket/8589





---

archive/issue_comments_077655.json:
```json
{
    "body": "Doing this, I have encountered and solved some problems:\n\n* The generators of permutation groups were returned as a list and not as a family, which is the case for other types of groups. They are now returned as a family.\n\n* The Hopf algebra structure didn't include counit. This has been corrected.\n\n* There was a bug in module_morphism which didn't work when the codomain was the ring itself (because it is not considered as a module by sage). It has been corrected.",
    "created_at": "2010-03-23T17:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77655",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Doing this, I have encountered and solved some problems:

* The generators of permutation groups were returned as a list and not as a family, which is the case for other types of groups. They are now returned as a family.

* The Hopf algebra structure didn't include counit. This has been corrected.

* There was a bug in module_morphism which didn't work when the codomain was the ring itself (because it is not considered as a module by sage). It has been corrected.



---

archive/issue_comments_077656.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-23T17:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77656",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077657.json:
```json
{
    "body": "Is line 919 in sage/categories/modules_with_basis.py a typo?\n\n```\n:meth:`rodulesWithBasis.HomCategory.ElementMethods.on_basis`. \n       ^\n```\n\nAlso, at the start of sage/groups/perm_gps/permgroup.py, the line \n\n```\nfrom sage.combinat.family import Family\n```\n\nmight be changed to \n\n```\nfrom sage.sets.family import Family\n```\n\n(since sage.combinat.family says \"This is a backward compatibility stub. Use :mod:`sage.sets.family` instead\").",
    "created_at": "2010-04-02T16:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77657",
    "user": "https://github.com/jhpalmieri"
}
```

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

archive/issue_comments_077658.json:
```json
{
    "body": "You're right! A new version of the patch has been uploaded\n\nThanks for these comments!\n\nValentin",
    "created_at": "2010-04-07T16:03:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77658",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

You're right! A new version of the patch has been uploaded

Thanks for these comments!

Valentin



---

archive/issue_comments_077659.json:
```json
{
    "body": "Replying to [comment:3 vferay]:\n> You're right! A new version of the patch has been uploaded\n\nThe feature here depends on the Algebra functorial constructions #8881 which are not yet finished.",
    "created_at": "2010-05-05T02:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77659",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:3 vferay]:
> You're right! A new version of the patch has been uploaded

The feature here depends on the Algebra functorial constructions #8881 which are not yet finished.



---

archive/issue_comments_077660.json:
```json
{
    "body": "Ok I wait until the Algebra functorial constructions are finished to finalize the patch",
    "created_at": "2010-05-05T09:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77660",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Ok I wait until the Algebra functorial constructions are finished to finalize the patch



---

archive/issue_comments_077661.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-05T09:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77661",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077662.json:
```json
{
    "body": "Replying to [comment:5 vferay]:\n> Ok I wait until the Algebra functorial constructions are finished to finalize the patch\n\n#8881 was just merged in sage 4.4.4!",
    "created_at": "2010-06-09T15:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77662",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:5 vferay]:
> Ok I wait until the Algebra functorial constructions are finished to finalize the patch

#8881 was just merged in sage 4.4.4!



---

archive/issue_comments_077663.json:
```json
{
    "body": "For the record with 4.4.3 and this patch applied,\n\n```\nsage: SymmetricGroup(3).algebra(QQ)\n```\n\ntriggers an error about _basis_keys",
    "created_at": "2010-06-14T23:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77663",
    "user": "https://github.com/nthiery"
}
```

For the record with 4.4.3 and this patch applied,

```
sage: SymmetricGroup(3).algebra(QQ)
```

triggers an error about _basis_keys



---

archive/issue_comments_077664.json:
```json
{
    "body": "Hello,\n\nIs there any new progress on this?  \n\nI'd like to help, but I think I have to start by understanding `Family`:  \n\nReplying to [comment:1 vferay]:\n> * The generators of permutation groups were returned as a list and not as a family, which is the case for other types of groups. They are now returned as a family.\n\n`DihedralGroup` and `CyclicPermutationGroup` both return `gens` as lists, and polynomial/power series rings return `gens` as tuples . . . could someone tell me if there is an effort under way to convert all of these to `Family`, or what sorts of things do already return `gens` as a `Family`?\n\nAre there other work issues for this patch (other than the bug with 4.4.3 reported by nthiery), or is it otherwise ready for review?\n\nthanks,\nNiles",
    "created_at": "2010-10-10T20:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77664",
    "user": "https://github.com/nilesjohnson"
}
```

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

archive/issue_comments_077665.json:
```json
{
    "body": "Hello,\n\n   finishing this patch is on my todo list of the week.\n\n>  could someone tell me if there is an effort under way to convert all of these to Family, or \n> what sorts of things do already return gens as a Family?\nIf we are only interested with groups, there is no interest to return things as a Family, but it is the natural structure when we work with algebra generators. So the change was to unify this but I confess that I don't remember for which function I wanted to do that.\n\nmore soon,\n\nValentin",
    "created_at": "2010-10-11T15:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77665",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Hello,

   finishing this patch is on my todo list of the week.

>  could someone tell me if there is an effort under way to convert all of these to Family, or 
> what sorts of things do already return gens as a Family?
If we are only interested with groups, there is no interest to return things as a Family, but it is the natural structure when we work with algebra generators. So the change was to unify this but I confess that I don't remember for which function I wanted to do that.

more soon,

Valentin



---

archive/issue_comments_077666.json:
```json
{
    "body": "Replying to [comment:9 vferay]:\n> > could someone tell me if there is an effort under way to convert all of these to Family, or \n> > what sorts of things do already return gens as a Family?\n\n> If we are only interested with groups, there is no interest to\n> return things as a Family, but it is the natural structure when we\n> work with algebra generators. So the change was to unify this but I\n> confess that I don't remember for which function I wanted to do\n> that.\n\nThe current convention is for algebra_generators,\nsemigroup_generators, and the like to return families.\n\nThere definitely is a plan for the long run (at least a wish from the\nsage-combinat group :-)) to have .gens() return a family as well. But\nthis will require some serious coordination to maintain backward\ncompatibility, and I'd rather have it done in a separate patch.\n\nValentin: do you really need this feature right now?",
    "created_at": "2010-10-12T16:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77666",
    "user": "https://github.com/nthiery"
}
```

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

archive/issue_comments_077667.json:
```json
{
    "body": "Hello,\n\n> Valentin: do you really need this feature right now? \nIt was needed in the function algebra_generators() which can be called on a group or semi-group algebra. But I changed this function such that it works in both cases.\n\nI splitted the patch in 2 and keep just the part on group algebra and Hopf algebra (and not the part turning group generators into a family).\n\nEverything seems to work now (I have one error in the test of hopf_algebra_with_basis.py :\n\"... still using old coercion framework) when the patch is applied in the sage-combinat queue. But it seems to depend on other patches (because import it when no other patches are applied lead to a lot of mistakes. Nicolas, do you know which ones and what I should do.\n\nI attach the new version of the patch",
    "created_at": "2010-10-13T13:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77667",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Hello,

> Valentin: do you really need this feature right now? 
It was needed in the function algebra_generators() which can be called on a group or semi-group algebra. But I changed this function such that it works in both cases.

I splitted the patch in 2 and keep just the part on group algebra and Hopf algebra (and not the part turning group generators into a family).

Everything seems to work now (I have one error in the test of hopf_algebra_with_basis.py :
"... still using old coercion framework) when the patch is applied in the sage-combinat queue. But it seems to depend on other patches (because import it when no other patches are applied lead to a lot of mistakes. Nicolas, do you know which ones and what I should do.

I attach the new version of the patch



---

archive/issue_comments_077668.json:
```json
{
    "body": "Replying to [comment:11 vferay]:\n> It was needed in the function algebra_generators() which can be\n> called on a group or semi-group algebra. But I changed this function\n> such that it works in both cases.\n\nThanks. Do you mind fixing instead semigroup_generators?\n\n> I splitted the patch in 2 and keep just the part on group algebra\n> and Hopf algebra (and not the part turning group generators into a\n> family).\n\nThanks.\n\n> Everything seems to work now (I have one error in the test of\n> hopf_algebra_with_basis.py : \"... still using old coercion\n> framework) when the patch is applied in the sage-combinat queue. But\n> it seems to depend on other patches (because import it when no other\n> patches are applied lead to a lot of mistakes. Nicolas, do you know\n> which ones and what I should do.\n\nAfter investigation, your patch depends on:\n\n- trac_9648_modulemorphism_codomain_extension-cs.patch # Needs review\n- free_module_basis_key_initialisation-nb.patch\n\n#9648 just needs a last pass of proofreading + rerunning the tests\nwith the latest Sage. Do you volunteer for the former?\n\nI just created #10127 for the second. We should be able to finalize it\nsoon with Nicolas B.\n\nWith those patches applied, I only get two trivial errors in sage/categories:\n\n\n```\nsage -t  \"devel/sage-combinat/sage/categories/groups.py\"    \n**********************************************************************\nFile \"/opt/sage-4.5.2/devel/sage-combinat/sage/categories/groups.py\", line 69:\n    sage: A.group_generators()\nExpected:\n    [(2,3,4), (1,2,3)]\nGot:\n    [(1,2,3), (2,3,4)]\nsage -t  \"devel/sage-combinat/sage/categories/algebra_functor.py\"\n**********************************************************************\nFile \"/opt/sage-4.5.2/devel/sage-combinat/sage/categories/algebra_functor.py\", line 37:\n    sage: Groups().Algebras(QQ) # todo: update once there will be a category for group algebras\nExpected:\n    Category of monoid algebras over Rational Field\nGot:\n    Category of group algebras over Rational Field\n```\n\n\nCheers,\n\t\t\tNicolas",
    "created_at": "2010-10-13T14:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77668",
    "user": "https://github.com/nthiery"
}
```

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

archive/issue_comments_077669.json:
```json
{
    "body": "Hi\n\n> Thanks. Do you mind fixing instead semigroup_generators? \nYou mean that you want semigroup_generators to return a list. I assume that this will need to change a few things in all the semigroup file. Another solution is also to overload the algebra_generators function for group algebras.\n\n> #9648 just needs a last pass of proofreading + rerunning the tests with the latest Sage. Do you > volunteer for the former? \nok I will try to do that.\n\n> With those patches applied, I only get two trivial errors in sage/categories: \nthe first one does not appear on my computer (?). I corrected the second one.\n\nValentin",
    "created_at": "2010-10-14T10:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77669",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Hi

> Thanks. Do you mind fixing instead semigroup_generators? 
You mean that you want semigroup_generators to return a list. I assume that this will need to change a few things in all the semigroup file. Another solution is also to overload the algebra_generators function for group algebras.

> #9648 just needs a last pass of proofreading + rerunning the tests with the latest Sage. Do you > volunteer for the former? 
ok I will try to do that.

> With those patches applied, I only get two trivial errors in sage/categories: 
the first one does not appear on my computer (?). I corrected the second one.

Valentin



---

archive/issue_comments_077670.json:
```json
{
    "body": "Replying to [comment:13 vferay]:\n> > Thanks. Do you mind fixing instead semigroup_generators? \n> You mean that you want semigroup_generators to return a list. I assume that this will need to change a few things in all the semigroup file. Another solution is also to overload the algebra_generators function for group algebras.\n\nOops, I investigated this too quickly. The culprit is actually Groups.ParentMethods.group_generators which returns self.gens() directly, instead of making the result first into a family.\n\n> > #9648 just needs a last pass of proofreading + rerunning the tests with the latest Sage. > > Do you volunteer for the former? \n> ok I will try to do that.\n\nThanks!\n\n> > With those patches applied, I only get two trivial errors in sage/categories: \n> the first one does not appear on my computer (?). \n\nHmm. Which patches did you have applied when you tried? Which version of Sage?\n\n> I corrected the second one.\n\nThanks!",
    "created_at": "2010-10-14T12:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77670",
    "user": "https://github.com/nthiery"
}
```

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

archive/issue_comments_077671.json:
```json
{
    "body": "Replying to nthiery:\n\n> Oops, I investigated this too quickly. The culprit is actually\n> Groups.ParentMethods?.group_generators which returns self.gens() directly, instead of making the > result first into a family. \nok I have changed this function and every test pass...\n\nI think the patch is ready now, I am waiting that the other patches are included in sage to set it as need_review .\n\n\n> > > With those patches applied, I only get two trivial errors in sage/categories:\n> > the first one does not appear on my computer (?).\n> Hmm. Which patches did you have applied when you tried? Which version of Sage? \nversion 4.5.3, patches up to this one were applied. But now, I find the same result as you do (except that now, it has been transformed into a family)...\n\nValentin",
    "created_at": "2010-10-14T13:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77671",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

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

archive/issue_comments_077672.json:
```json
{
    "body": "All test pass on 4.5.3, with the following patches applied:\n\n```\ntrac_9648_modulemorphism_codomain_extension-cs.patch # Needs review\ntrac_10127_free_module_basis_key_initialisation-nb.patch # Under review\ntrac_8589_feature_group_algebras_vf.patch  #-4_5    # Under review\ntrac_8589_feature_group_algebras-reviewer-nt.patch\n```\n\n\nGenerally speaking, the patch is good to go, up to missing documentation and tests for Coalgebras.ElementMethods.counit. Valentin, please fold in my reviewer's patch, add doc and test, check that the documentation compiles smoothly, and upload here. \n\nThen you can set a positive review on my behalf. Thanks for your work on that!\n\nNiles: feel free to make a last check up!",
    "created_at": "2010-10-15T13:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77672",
    "user": "https://github.com/nthiery"
}
```

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

archive/issue_comments_077673.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-10-18T13:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77673",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_077674.json:
```json
{
    "body": "> Valentin, please fold in my reviewer's patch, add doc and test, check that the documentation\n> compiles smoothly, and upload here.\n\nDone!",
    "created_at": "2010-10-18T13:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77674",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

> Valentin, please fold in my reviewer's patch, add doc and test, check that the documentation
> compiles smoothly, and upload here.

Done!



---

archive/issue_comments_077675.json:
```json
{
    "body": "Attachment [trac_8589_feature_group_algebras_vf.2.patch](tarball://root/attachments/some-uuid/ticket8589/trac_8589_feature_group_algebras_vf.2.patch) by vferay created at 2010-10-18 13:21:04",
    "created_at": "2010-10-18T13:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77675",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Attachment [trac_8589_feature_group_algebras_vf.2.patch](tarball://root/attachments/some-uuid/ticket8589/trac_8589_feature_group_algebras_vf.2.patch) by vferay created at 2010-10-18 13:21:04



---

archive/issue_comments_077676.json:
```json
{
    "body": "Attachment [trac_8589_feature_group_algebras_vf.patch](tarball://root/attachments/some-uuid/ticket8589/trac_8589_feature_group_algebras_vf.patch) by @jdemeyer created at 2010-10-23 11:58:11\n\nWhich of the patches should be applied?",
    "created_at": "2010-10-23T11:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77676",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [trac_8589_feature_group_algebras_vf.patch](tarball://root/attachments/some-uuid/ticket8589/trac_8589_feature_group_algebras_vf.patch) by @jdemeyer created at 2010-10-23 11:58:11

Which of the patches should be applied?



---

archive/issue_comments_077677.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2010-10-23T11:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77677",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_077678.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-10-26T08:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77678",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_077679.json:
```json
{
    "body": "The two files are the same. I did wrong manipulation. Sorry for that",
    "created_at": "2010-10-26T08:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77679",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

The two files are the same. I did wrong manipulation. Sorry for that



---

archive/issue_comments_077680.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-26T08:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77680",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077681.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-01T10:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77681",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_077682.json:
```json
{
    "body": "name with accent",
    "created_at": "2017-07-19T08:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8589#issuecomment-77682",
    "user": "https://github.com/fchapoton"
}
```

name with accent
