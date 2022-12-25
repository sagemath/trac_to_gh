# Issue 6588: Root systems: categorification

archive/issues_006588.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat mshimo@math.vt.edu\n\nKeywords: root systems, categories\n\nReplace the abstract classes in RootSystems (like RootLatticeRealization) by categories.\n\nUse it to implement parabolic sub-rootsystems, and parabolic Weyl subgroups.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6588\n\n",
    "created_at": "2009-07-22T11:54:48Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "Root systems: categorification",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6588",
    "user": "https://github.com/nthiery"
}
```
Assignee: @mwhansen

CC:  sage-combinat mshimo@math.vt.edu

Keywords: root systems, categories

Replace the abstract classes in RootSystems (like RootLatticeRealization) by categories.

Use it to implement parabolic sub-rootsystems, and parabolic Weyl subgroups.

Issue created by migration from https://trac.sagemath.org/ticket/6588





---

archive/issue_comments_053773.json:
```json
{
    "body": "The updated patch adds many missing doctests, and improves coxeter diagrams. It's probably close to completion, up to fixing some potentially failing doctests.",
    "created_at": "2012-02-25T00:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53773",
    "user": "https://github.com/nthiery"
}
```

The updated patch adds many missing doctests, and improves coxeter diagrams. It's probably close to completion, up to fixing some potentially failing doctests.



---

archive/issue_comments_053774.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-02-25T00:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53774",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053775.json:
```json
{
    "body": "Beside, I commuted it up the Sage-Combinat queue. In principle, there should not be other dependencies than the listed ones.",
    "created_at": "2012-02-25T00:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53775",
    "user": "https://github.com/nthiery"
}
```

Beside, I commuted it up the Sage-Combinat queue. In principle, there should not be other dependencies than the listed ones.



---

archive/issue_comments_053776.json:
```json
{
    "body": "Replying to [comment:4 nthiery]:\n> The updated patch adds many missing doctests, and improves coxeter diagrams. It's probably close to completion, up to fixing some potentially failing doctests.\n\nThere are indeed a couple minor ones:\n\nhttp://sage.math.washington.edu/home/nthiery/trac_6588-categories-root_systems-nt.patch-testlog\n\nNote: that's with the following patches applied on 5.0.beta5:\n\n```\ntrac_12476-lattice_join_matrix_speedup-fh.patch\ntrac_9469-category-membership_without_arguments-nt.patch\ntrac_10603-union_enumset_elconstr_fix-fh.patch\ntrac_12528_free_module-optimize-nt.patch\ntrac_10817-generalized_associahedra-cs.patch\ntrac_10817-generalized_associahedra-review-nt.patch\ntrac_12078-see_also-fh.patch\ntrac_9128-intersphinx_python_database-fh.patch\ntrac_9128-sphinx_links_all-fh.patch\ntrac_12527-fraction_field-is_exact_optimization-nt.patch\ntrac_12510-nonzero_equal_consistency-fh.patch\ntrac_12536-linear_extensions-as.patch\ntrac_12518-enumerated_set_from_iterator-vd.patch\ntrac_11880.patch\ntrac_11880-graph_classes-review-nt.patch\ntrac_7980-multiple-realizations-nt.patch\ntrac_7980-multiple-realizations-review-nt.patch\ntrac_6588-categories-root_systems-nt.patch\n```\n\n\nOff for skiing :-)",
    "created_at": "2012-02-25T00:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53776",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:4 nthiery]:
> The updated patch adds many missing doctests, and improves coxeter diagrams. It's probably close to completion, up to fixing some potentially failing doctests.

There are indeed a couple minor ones:

http://sage.math.washington.edu/home/nthiery/trac_6588-categories-root_systems-nt.patch-testlog

Note: that's with the following patches applied on 5.0.beta5:

```
trac_12476-lattice_join_matrix_speedup-fh.patch
trac_9469-category-membership_without_arguments-nt.patch
trac_10603-union_enumset_elconstr_fix-fh.patch
trac_12528_free_module-optimize-nt.patch
trac_10817-generalized_associahedra-cs.patch
trac_10817-generalized_associahedra-review-nt.patch
trac_12078-see_also-fh.patch
trac_9128-intersphinx_python_database-fh.patch
trac_9128-sphinx_links_all-fh.patch
trac_12527-fraction_field-is_exact_optimization-nt.patch
trac_12510-nonzero_equal_consistency-fh.patch
trac_12536-linear_extensions-as.patch
trac_12518-enumerated_set_from_iterator-vd.patch
trac_11880.patch
trac_11880-graph_classes-review-nt.patch
trac_7980-multiple-realizations-nt.patch
trac_7980-multiple-realizations-review-nt.patch
trac_6588-categories-root_systems-nt.patch
```


Off for skiing :-)



---

archive/issue_comments_053777.json:
```json
{
    "body": "I fixed the doctests failures due to this patch. Most of them where due to the fact that affine weyl groups are iterable now, which gives a nicer an_element on any free module thereupon.\n\nThe other doctests failures showing up in the log are related to #12518 (or to the ISGCI patch, but that's because I did not upload the appropriate database on my test server).\n\nThe review can start!",
    "created_at": "2012-02-25T01:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53777",
    "user": "https://github.com/nthiery"
}
```

I fixed the doctests failures due to this patch. Most of them where due to the fact that affine weyl groups are iterable now, which gives a nicer an_element on any free module thereupon.

The other doctests failures showing up in the log are related to #12518 (or to the ISGCI patch, but that's because I did not upload the appropriate database on my test server).

The review can start!



---

archive/issue_comments_053778.json:
```json
{
    "body": "Patch updated after a bug report by Mark; see end of patch description",
    "created_at": "2012-03-05T21:40:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53778",
    "user": "https://github.com/nthiery"
}
```

Patch updated after a bug report by Mark; see end of patch description



---

archive/issue_comments_053779.json:
```json
{
    "body": "Upon popular demand, extended weight lattice/spaces are now implemented.",
    "created_at": "2012-03-08T13:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53779",
    "user": "https://github.com/nthiery"
}
```

Upon popular demand, extended weight lattice/spaces are now implemented.



---

archive/issue_comments_053780.json:
```json
{
    "body": "Hi Nicolas,\n\nImpressive patch! Thanks for working on this.\nHere are some first comments:\n\n- In /sage/categories/affine_weyl_groups.py there is a new import\nfrom sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets\nwhich is not used. Please either remove this line or add InfiniteEnumeratedSets\nin the class (which is probably preferable).\n\n- In /sage/categories/affine_weyl_groups.py please add a `TestSuite(s).run()` doctest.\n\n- I am not sure this is related to the patch, but there are some\nstrange methods in /sage/categories/coxeter_groups.py without doctests:\n\n        `@`abstract_method(optional = True)\n        def has_right_descent(self, i):\n            \"\"\"\n            Returns whether i is a right descent of self.\n\n#            EXAMPLES::\n#\n#                sage:\n            \"\"\"\n\n        def has_left_descent(self, i):\n            \"\"\"\n            Returns whether `i` is a left descent of self.\n\n            This default implementation uses that a left descent of\n            `w` is a right descent of `w^{-1}`.\n            \"\"\"\n            return (~self).has_right_descent(i)\n\nShould has_left_descent also be an abstract_method? Or is that implicit through\nhas_right_descent?\n\n- Why is the cateogry RootLatticeRealization in\n/sage/combinat/root_system/root_lattice_realization.py\nhere and not in categories (if it is a category as specified in the docstring)?\n\nThe same question holds for WeightLatticeRealizations(Category_over_base_ring)\nin /sage/combinat/root_system/weight_lattice_realization.py.\n\n- When using the extended weight lattice, the list of fundamental weights\ndoes not include `\\delta`. On the other hand it is possible to input\n`\\delta` into the method fundamental_weight. This seems a little inconsistent.\n\n\n```\n    sage: Q = RootSystem(['A', 3, 1]).weight_lattice(extended = True); Q\n    Extended weight lattice of the Root system of type ['A', 3, 1]\n    sage: Q.fundamental_weights()\n    Finite family {0: Lambda[0], 1: Lambda[1], 2: Lambda[2], 3: Lambda[3]}\n    sage: Q.fundamental_weight('delta')\n    delta\n```\n\n\nAlso, I posted a first reviewer's patch on sage-combinat with mostly just\ntrivial changes. Please fold it if you are satisfied.\n\nThanks!\n\nAnne",
    "created_at": "2012-03-09T20:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53780",
    "user": "https://github.com/anneschilling"
}
```

Hi Nicolas,

Impressive patch! Thanks for working on this.
Here are some first comments:

- In /sage/categories/affine_weyl_groups.py there is a new import
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets
which is not used. Please either remove this line or add InfiniteEnumeratedSets
in the class (which is probably preferable).

- In /sage/categories/affine_weyl_groups.py please add a `TestSuite(s).run()` doctest.

- I am not sure this is related to the patch, but there are some
strange methods in /sage/categories/coxeter_groups.py without doctests:

        `@`abstract_method(optional = True)
        def has_right_descent(self, i):
            """
            Returns whether i is a right descent of self.

#            EXAMPLES::
#
#                sage:
            """

        def has_left_descent(self, i):
            """
            Returns whether `i` is a left descent of self.

            This default implementation uses that a left descent of
            `w` is a right descent of `w^{-1}`.
            """
            return (~self).has_right_descent(i)

Should has_left_descent also be an abstract_method? Or is that implicit through
has_right_descent?

- Why is the cateogry RootLatticeRealization in
/sage/combinat/root_system/root_lattice_realization.py
here and not in categories (if it is a category as specified in the docstring)?

The same question holds for WeightLatticeRealizations(Category_over_base_ring)
in /sage/combinat/root_system/weight_lattice_realization.py.

- When using the extended weight lattice, the list of fundamental weights
does not include `\delta`. On the other hand it is possible to input
`\delta` into the method fundamental_weight. This seems a little inconsistent.


```
    sage: Q = RootSystem(['A', 3, 1]).weight_lattice(extended = True); Q
    Extended weight lattice of the Root system of type ['A', 3, 1]
    sage: Q.fundamental_weights()
    Finite family {0: Lambda[0], 1: Lambda[1], 2: Lambda[2], 3: Lambda[3]}
    sage: Q.fundamental_weight('delta')
    delta
```


Also, I posted a first reviewer's patch on sage-combinat with mostly just
trivial changes. Please fold it if you are satisfied.

Thanks!

Anne



---

archive/issue_comments_053781.json:
```json
{
    "body": "Thanks much Anne for your detailed review!\n\nReplying to [comment:10 aschilling]:\n> - In /sage/categories/affine_weyl_groups.py there is a new import\n> from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets\n> which is not used. Please either remove this line or add InfiniteEnumeratedSets\n> in the class (which is probably preferable).\n\nGood point. Done!\n\n> - In /sage/categories/affine_weyl_groups.py please add a `TestSuite(s).run()` doctest.\n\nDone.\n\n> - I am not sure this is related to the patch, but there are some\n> strange methods in /sage/categories/coxeter_groups.py without doctests:\n\nCoxeterGroups is now 100% doctested.\n\n> Should has_left_descent also be an abstract_method? Or is that implicit through\n> has_right_descent?\n\nThere is a default implementation for this method, so it's not abstract. Indeed, it would be nice to track such dependencies in the documentation; but we don't have the infrastructure for that.\n\n> - Why is the cateogry RootLatticeRealization in\n> /sage/combinat/root_system/root_lattice_realization.py\n> here and not in categories (if it is a category as specified in the docstring)?\n> \n> The same question holds for WeightLatticeRealizations(Category_over_base_ring)\n> in /sage/combinat/root_system/weight_lattice_realization.py.\n> \n> - When using the extended weight lattice, the list of fundamental weights\n> does not include `\\delta`. On the other hand it is possible to input\n> `\\delta` into the method fundamental_weight. This seems a little\n> inconsistent.\n> \n> {{{\n>     sage: Q = RootSystem(['A', 3, 1]).weight_lattice(extended = True); Q\n>     Extended weight lattice of the Root system of type ['A', 3, 1]\n>     sage: Q.fundamental_weights()\n>     Finite family {0: Lambda[0], 1: Lambda[1], 2: Lambda[2], 3: Lambda[3]}\n>     sage: Q.fundamental_weight('delta')\n>     delta\n> }}}\n> \n\nMore on those after lunch!\n\n> Also, I posted a first reviewer's patch on sage-combinat with mostly just\n> trivial changes. Please fold it if you are satisfied.\n\nFolded in! There is a new reviewer's patch on the patch server.\n\nCheers,\n           Nicolas",
    "created_at": "2012-03-10T12:04:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53781",
    "user": "https://github.com/nthiery"
}
```

Thanks much Anne for your detailed review!

Replying to [comment:10 aschilling]:
> - In /sage/categories/affine_weyl_groups.py there is a new import
> from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets
> which is not used. Please either remove this line or add InfiniteEnumeratedSets
> in the class (which is probably preferable).

Good point. Done!

> - In /sage/categories/affine_weyl_groups.py please add a `TestSuite(s).run()` doctest.

Done.

> - I am not sure this is related to the patch, but there are some
> strange methods in /sage/categories/coxeter_groups.py without doctests:

CoxeterGroups is now 100% doctested.

> Should has_left_descent also be an abstract_method? Or is that implicit through
> has_right_descent?

There is a default implementation for this method, so it's not abstract. Indeed, it would be nice to track such dependencies in the documentation; but we don't have the infrastructure for that.

> - Why is the cateogry RootLatticeRealization in
> /sage/combinat/root_system/root_lattice_realization.py
> here and not in categories (if it is a category as specified in the docstring)?
> 
> The same question holds for WeightLatticeRealizations(Category_over_base_ring)
> in /sage/combinat/root_system/weight_lattice_realization.py.
> 
> - When using the extended weight lattice, the list of fundamental weights
> does not include `\delta`. On the other hand it is possible to input
> `\delta` into the method fundamental_weight. This seems a little
> inconsistent.
> 
> {{{
>     sage: Q = RootSystem(['A', 3, 1]).weight_lattice(extended = True); Q
>     Extended weight lattice of the Root system of type ['A', 3, 1]
>     sage: Q.fundamental_weights()
>     Finite family {0: Lambda[0], 1: Lambda[1], 2: Lambda[2], 3: Lambda[3]}
>     sage: Q.fundamental_weight('delta')
>     delta
> }}}
> 

More on those after lunch!

> Also, I posted a first reviewer's patch on sage-combinat with mostly just
> trivial changes. Please fold it if you are satisfied.

Folded in! There is a new reviewer's patch on the patch server.

Cheers,
           Nicolas



---

archive/issue_comments_053782.json:
```json
{
    "body": "> - Why is the cateogry RootLatticeRealization in\n> /sage/combinat/root_system/root_lattice_realization.py\n> here and not in categories (if it is a category as specified in the docstring)?\n> \n> The same question holds for WeightLatticeRealizations(Category_over_base_ring)\n> in /sage/combinat/root_system/weight_lattice_realization.py.\n\nYeah, we had a similar discussion for the crystal categories and the\ncategories for Symmetric Functions and friends. And there is a non\ntrivial borderline to set.\n\nOn one hand, we have general categories (like Groups, Algebras, ...)\nwhich are likely to get used in several Sage modules.  Also, they name\na well-known area of mathematics; so it's natural to import them by\ndefault in the interpreter, if not just as an entry point.\n\nOn the other hand we have categories that are rather specific to a\nSage module, if not just implementation details. So it's good to keep\nthem in this module, in particular to be as close as close as possible\nfrom the other sources of that module.\n\nCoxeterGroups clearly fits the first case (most mathematicians have\nheard of them; this category is used by WeylGroup (in\nsage.combinat.root_system) and by SymmetricGroup (in sage.groups).\n\nThe categories for symmetric functions are basically implementation\ndetails and fits in the second case. Anyway, SymmetricFunctions is\nalready a good entry point.\n\nCrystals are only implemented in sage.combinat.crystals (so far). But\nthis names an area of mathematics. So this fits a bit more the first\ncase.\n\nRootLatticeRealizations and WeightLatticeRealizations seem rather\nspecific. So this fits a bit more the second case.\n\n> - When using the extended weight lattice, the list of fundamental weights\n> does not include `\\delta`. On the other hand it is possible to input\n> `\\delta` into the method fundamental_weight. This seems a little\n> inconsistent.\n\nYeah, this abuse is documented in \"fundamental_weight\". Basically, we\nneed a function that describes the embedding of the basis elements of\nthe (extended) weight lattice. That's almost what fundamental_weight\ndoes, and I did not have a good alternative name. So I abused\nfundamental_weight to do just a bit more that its natural job.\nAnyway, we currently only have a single implementation of\nWeightLatticeRealizations in the affine case, so it's very localized,\nand easy to change in the future if we come up with a good name\n(unless you have one!).\n\nLet me know if you are ok with the above and with my reviewer's patch.\nIf yes, I'll fold the patches, reindent properly\nroot_lattice_realization.py and weight_lattice_realization.py, and add\na 's' at the end of those files (I haven't done those yet to keep the\ndiff meaningful). Then, the patch will be good to go.\n\nFor the record, all tests pass on Sage 5.0 beta6, with the following\npatches applied:\n\n```\ntrac_10817-generalized_associahedra-cs.patch\ntrac_12645-fix_rst_markup-sk.patch\ntrac_9128-intersphinx_python_database-fh.patch\ntrac_9128-sphinx_links_all-fh.patch\ntrac_9128-MANIFEST-fh.patch\ntrac_12527-fraction_field-is_exact_optimization-nt.patch\ntrac_12510-nonzero_equal_consistency-fh.patch\ntrac_12536-linear_extensions-as.patch\nelement_compare_consistency-fh.patch\ntrac_11880-isgci-all_in_one-nc.patch\ntrac_11880-isgci-more-review-nt.patch\ntrac_7980-multiple-realizations-nt.patch\ntrac_7980-multiple-realizations-review-nt.patch\ntrac_6588-categories-root_systems-nt.patch\ntrac_6588-categories-root_systems-review-nt.patch\n```\n\n\nCheers,\n                        Nicolas",
    "created_at": "2012-03-11T09:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53782",
    "user": "https://github.com/nthiery"
}
```

> - Why is the cateogry RootLatticeRealization in
> /sage/combinat/root_system/root_lattice_realization.py
> here and not in categories (if it is a category as specified in the docstring)?
> 
> The same question holds for WeightLatticeRealizations(Category_over_base_ring)
> in /sage/combinat/root_system/weight_lattice_realization.py.

Yeah, we had a similar discussion for the crystal categories and the
categories for Symmetric Functions and friends. And there is a non
trivial borderline to set.

On one hand, we have general categories (like Groups, Algebras, ...)
which are likely to get used in several Sage modules.  Also, they name
a well-known area of mathematics; so it's natural to import them by
default in the interpreter, if not just as an entry point.

On the other hand we have categories that are rather specific to a
Sage module, if not just implementation details. So it's good to keep
them in this module, in particular to be as close as close as possible
from the other sources of that module.

CoxeterGroups clearly fits the first case (most mathematicians have
heard of them; this category is used by WeylGroup (in
sage.combinat.root_system) and by SymmetricGroup (in sage.groups).

The categories for symmetric functions are basically implementation
details and fits in the second case. Anyway, SymmetricFunctions is
already a good entry point.

Crystals are only implemented in sage.combinat.crystals (so far). But
this names an area of mathematics. So this fits a bit more the first
case.

RootLatticeRealizations and WeightLatticeRealizations seem rather
specific. So this fits a bit more the second case.

> - When using the extended weight lattice, the list of fundamental weights
> does not include `\delta`. On the other hand it is possible to input
> `\delta` into the method fundamental_weight. This seems a little
> inconsistent.

Yeah, this abuse is documented in "fundamental_weight". Basically, we
need a function that describes the embedding of the basis elements of
the (extended) weight lattice. That's almost what fundamental_weight
does, and I did not have a good alternative name. So I abused
fundamental_weight to do just a bit more that its natural job.
Anyway, we currently only have a single implementation of
WeightLatticeRealizations in the affine case, so it's very localized,
and easy to change in the future if we come up with a good name
(unless you have one!).

Let me know if you are ok with the above and with my reviewer's patch.
If yes, I'll fold the patches, reindent properly
root_lattice_realization.py and weight_lattice_realization.py, and add
a 's' at the end of those files (I haven't done those yet to keep the
diff meaningful). Then, the patch will be good to go.

For the record, all tests pass on Sage 5.0 beta6, with the following
patches applied:

```
trac_10817-generalized_associahedra-cs.patch
trac_12645-fix_rst_markup-sk.patch
trac_9128-intersphinx_python_database-fh.patch
trac_9128-sphinx_links_all-fh.patch
trac_9128-MANIFEST-fh.patch
trac_12527-fraction_field-is_exact_optimization-nt.patch
trac_12510-nonzero_equal_consistency-fh.patch
trac_12536-linear_extensions-as.patch
element_compare_consistency-fh.patch
trac_11880-isgci-all_in_one-nc.patch
trac_11880-isgci-more-review-nt.patch
trac_7980-multiple-realizations-nt.patch
trac_7980-multiple-realizations-review-nt.patch
trac_6588-categories-root_systems-nt.patch
trac_6588-categories-root_systems-review-nt.patch
```


Cheers,
                        Nicolas



---

archive/issue_comments_053783.json:
```json
{
    "body": "Fails doctests on Sage 5.0.beta7:\n\n```\nsage -t -long devel/sage-main/sage/combinat/root_system/weight_space.py\n**********************************************************************\nFile \"/storage/masiao/sage-5.0.beta7/devel/sage-main/sage/combinat/root_system/weight_space.py\", line 126:\n    sage: Q.null_root(0)[index]\nException raised:\n    Traceback (most recent call last):\n      File \"/storage/masiao/sage-5.0.beta7/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/storage/masiao/sage-5.0.beta7/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/storage/masiao/sage-5.0.beta7/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[17]>\", line 1, in <module>\n        Q.null_root(Integer(0))[index]###line 126:\n    sage: Q.null_root(0)[index]\n    TypeError: __call__() takes exactly 0 positional arguments (1 given)\n**********************************************************************\n```\n\n(The patchbot found this, but I also reproduced it by hand)",
    "created_at": "2012-03-11T10:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53783",
    "user": "https://github.com/loefflerd"
}
```

Fails doctests on Sage 5.0.beta7:

```
sage -t -long devel/sage-main/sage/combinat/root_system/weight_space.py
**********************************************************************
File "/storage/masiao/sage-5.0.beta7/devel/sage-main/sage/combinat/root_system/weight_space.py", line 126:
    sage: Q.null_root(0)[index]
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-5.0.beta7/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-5.0.beta7/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-5.0.beta7/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[17]>", line 1, in <module>
        Q.null_root(Integer(0))[index]###line 126:
    sage: Q.null_root(0)[index]
    TypeError: __call__() takes exactly 0 positional arguments (1 given)
**********************************************************************
```

(The patchbot found this, but I also reproduced it by hand)



---

archive/issue_comments_053784.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-11T10:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53784",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_053785.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-11T10:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53785",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053786.json:
```json
{
    "body": "Replying to [comment:13 davidloeffler]:\n> Fails doctests on Sage 5.0.beta7:\n> {{{\n> sage -t -long devel/sage-main/sage/combinat/root_system/weight_space.py\n> **********************************************************************\n> File \"/storage/masiao/sage-5.0.beta7/devel/sage-main/sage/combinat/root_system/weight_space.py\", line 126:\n>     sage: Q.null_root(0)[index]\n> Exception raised:\n>     Traceback (most recent call last):\n>       File \"/storage/masiao/sage-5.0.beta7/local/bin/ncadoctest.py\", line 1231, in run_one_test\n>         self.run_one_example(test, example, filename, compileflags)\n>       File \"/storage/masiao/sage-5.0.beta7/local/bin/sagedoctest.py\", line 38, in run_one_example\n>         OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n>       File \"/storage/masiao/sage-5.0.beta7/local/bin/ncadoctest.py\", line 1172, in run_one_example\n>         compileflags, 1) in test.globs\n>       File \"<doctest __main__.example_1[17]>\", line 1, in <module>\n>         Q.null_root(Integer(0))[index]###line 126:\n>     sage: Q.null_root(0)[index]\n>     TypeError: __call__() takes exactly 0 positional arguments (1 given)\n> **********************************************************************\n> }}}\n> (The patchbot found this, but I also reproduced it by hand)\n\nSorry, already fixed on the Sage-Combinat queue where the review is occuring. I'll delete the patch here for the moment so that others don't waste time reviewing an outdated version.\n\nThanks though for the report!",
    "created_at": "2012-03-11T10:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53786",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:13 davidloeffler]:
> Fails doctests on Sage 5.0.beta7:
> {{{
> sage -t -long devel/sage-main/sage/combinat/root_system/weight_space.py
> **********************************************************************
> File "/storage/masiao/sage-5.0.beta7/devel/sage-main/sage/combinat/root_system/weight_space.py", line 126:
>     sage: Q.null_root(0)[index]
> Exception raised:
>     Traceback (most recent call last):
>       File "/storage/masiao/sage-5.0.beta7/local/bin/ncadoctest.py", line 1231, in run_one_test
>         self.run_one_example(test, example, filename, compileflags)
>       File "/storage/masiao/sage-5.0.beta7/local/bin/sagedoctest.py", line 38, in run_one_example
>         OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
>       File "/storage/masiao/sage-5.0.beta7/local/bin/ncadoctest.py", line 1172, in run_one_example
>         compileflags, 1) in test.globs
>       File "<doctest __main__.example_1[17]>", line 1, in <module>
>         Q.null_root(Integer(0))[index]###line 126:
>     sage: Q.null_root(0)[index]
>     TypeError: __call__() takes exactly 0 positional arguments (1 given)
> **********************************************************************
> }}}
> (The patchbot found this, but I also reproduced it by hand)

Sorry, already fixed on the Sage-Combinat queue where the review is occuring. I'll delete the patch here for the moment so that others don't waste time reviewing an outdated version.

Thanks though for the report!



---

archive/issue_comments_053787.json:
```json
{
    "body": "Replying to [comment:12 nthiery]:\n\n>  Thanks much Anne for your detailed review!\n\nYou are welcome. I hope you will return the favor for trac_12536-linear_extensions-as.patch!\n\n> > - Why is the cateogry RootLatticeRealization in\n> > /sage/combinat/root_system/root_lattice_realization.py\n> > here and not in categories (if it is a category as specified in the docstring)?\n> > \n> > The same question holds for WeightLatticeRealizations(Category_over_base_ring)\n> > in /sage/combinat/root_system/weight_lattice_realization.py.\n> \n> Yeah, we had a similar discussion for the crystal categories and the\n> categories for Symmetric Functions and friends. And there is a non\n> trivial borderline to set.\n> \n> On one hand, we have general categories (like Groups, Algebras, ...)\n> which are likely to get used in several Sage modules.  Also, they name\n> a well-known area of mathematics; so it's natural to import them by\n> default in the interpreter, if not just as an entry point.\n> \n> On the other hand we have categories that are rather specific to a\n> Sage module, if not just implementation details. So it's good to keep\n> them in this module, in particular to be as close as close as possible\n> from the other sources of that module.\n> \n> CoxeterGroups clearly fits the first case (most mathematicians have\n> heard of them; this category is used by WeylGroup (in\n> sage.combinat.root_system) and by SymmetricGroup (in sage.groups).\n> \n> The categories for symmetric functions are basically implementation\n> details and fits in the second case. Anyway, SymmetricFunctions is\n> already a good entry point.\n> \n> Crystals are only implemented in sage.combinat.crystals (so far). But\n> this names an area of mathematics. So this fits a bit more the first\n> case.\n\nNo, there is a lot of crystal code in /sage/categories: crystals, finite_crystals, highest_weight_crystals, ....\n\n> > - When using the extended weight lattice, the list of fundamental weights\n> > does not include `\\delta`. On the other hand it is possible to input\n> > `\\delta` into the method fundamental_weight. This seems a little\n> > inconsistent.\n> \n> Yeah, this abuse is documented in \"fundamental_weight\". Basically, we\n> need a function that describes the embedding of the basis elements of\n> the (extended) weight lattice. That's almost what fundamental_weight\n> does, and I did not have a good alternative name. So I abused\n> fundamental_weight to do just a bit more that its natural job.\n> Anyway, we currently only have a single implementation of\n> WeightLatticeRealizations in the affine case, so it's very localized,\n> and easy to change in the future if we come up with a good name\n> (unless you have one!).\n\nWhy can't fundamental_weights when \"extended\" is set also include `delta`? This would at least fit with the notational abuse of fundamental_weight.\n\n> Let me know if you are ok with the above and with my reviewer's patch.\n> If yes, I'll fold the patches, reindent properly\n> root_lattice_realization.py and weight_lattice_realization.py, and add\n> a 's' at the end of those files (I haven't done those yet to keep the\n> diff meaningful). Then, the patch will be good to go.\n\nI also wrote another very small reviewer's patch that you can fold in.\n\n> For the record, all tests pass on Sage 5.0 beta6, with the following\n> patches applied:\n> {{{\n> trac_10817-generalized_associahedra-cs.patch\n> trac_12645-fix_rst_markup-sk.patch\n> trac_9128-intersphinx_python_database-fh.patch\n> trac_9128-sphinx_links_all-fh.patch\n> trac_9128-MANIFEST-fh.patch\n> trac_12527-fraction_field-is_exact_optimization-nt.patch\n> trac_12510-nonzero_equal_consistency-fh.patch\n> trac_12536-linear_extensions-as.patch\n> element_compare_consistency-fh.patch\n> trac_11880-isgci-all_in_one-nc.patch\n> trac_11880-isgci-more-review-nt.patch\n> trac_7980-multiple-realizations-nt.patch\n> trac_7980-multiple-realizations-review-nt.patch\n> trac_6588-categories-root_systems-nt.patch\n> trac_6588-categories-root_systems-review-nt.patch\n> }}}\n\nThat's good!\n\nCheers,\n\nAnne",
    "created_at": "2012-03-12T04:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53787",
    "user": "https://github.com/anneschilling"
}
```

Replying to [comment:12 nthiery]:

>  Thanks much Anne for your detailed review!

You are welcome. I hope you will return the favor for trac_12536-linear_extensions-as.patch!

> > - Why is the cateogry RootLatticeRealization in
> > /sage/combinat/root_system/root_lattice_realization.py
> > here and not in categories (if it is a category as specified in the docstring)?
> > 
> > The same question holds for WeightLatticeRealizations(Category_over_base_ring)
> > in /sage/combinat/root_system/weight_lattice_realization.py.
> 
> Yeah, we had a similar discussion for the crystal categories and the
> categories for Symmetric Functions and friends. And there is a non
> trivial borderline to set.
> 
> On one hand, we have general categories (like Groups, Algebras, ...)
> which are likely to get used in several Sage modules.  Also, they name
> a well-known area of mathematics; so it's natural to import them by
> default in the interpreter, if not just as an entry point.
> 
> On the other hand we have categories that are rather specific to a
> Sage module, if not just implementation details. So it's good to keep
> them in this module, in particular to be as close as close as possible
> from the other sources of that module.
> 
> CoxeterGroups clearly fits the first case (most mathematicians have
> heard of them; this category is used by WeylGroup (in
> sage.combinat.root_system) and by SymmetricGroup (in sage.groups).
> 
> The categories for symmetric functions are basically implementation
> details and fits in the second case. Anyway, SymmetricFunctions is
> already a good entry point.
> 
> Crystals are only implemented in sage.combinat.crystals (so far). But
> this names an area of mathematics. So this fits a bit more the first
> case.

No, there is a lot of crystal code in /sage/categories: crystals, finite_crystals, highest_weight_crystals, ....

> > - When using the extended weight lattice, the list of fundamental weights
> > does not include `\delta`. On the other hand it is possible to input
> > `\delta` into the method fundamental_weight. This seems a little
> > inconsistent.
> 
> Yeah, this abuse is documented in "fundamental_weight". Basically, we
> need a function that describes the embedding of the basis elements of
> the (extended) weight lattice. That's almost what fundamental_weight
> does, and I did not have a good alternative name. So I abused
> fundamental_weight to do just a bit more that its natural job.
> Anyway, we currently only have a single implementation of
> WeightLatticeRealizations in the affine case, so it's very localized,
> and easy to change in the future if we come up with a good name
> (unless you have one!).

Why can't fundamental_weights when "extended" is set also include `delta`? This would at least fit with the notational abuse of fundamental_weight.

> Let me know if you are ok with the above and with my reviewer's patch.
> If yes, I'll fold the patches, reindent properly
> root_lattice_realization.py and weight_lattice_realization.py, and add
> a 's' at the end of those files (I haven't done those yet to keep the
> diff meaningful). Then, the patch will be good to go.

I also wrote another very small reviewer's patch that you can fold in.

> For the record, all tests pass on Sage 5.0 beta6, with the following
> patches applied:
> {{{
> trac_10817-generalized_associahedra-cs.patch
> trac_12645-fix_rst_markup-sk.patch
> trac_9128-intersphinx_python_database-fh.patch
> trac_9128-sphinx_links_all-fh.patch
> trac_9128-MANIFEST-fh.patch
> trac_12527-fraction_field-is_exact_optimization-nt.patch
> trac_12510-nonzero_equal_consistency-fh.patch
> trac_12536-linear_extensions-as.patch
> element_compare_consistency-fh.patch
> trac_11880-isgci-all_in_one-nc.patch
> trac_11880-isgci-more-review-nt.patch
> trac_7980-multiple-realizations-nt.patch
> trac_7980-multiple-realizations-review-nt.patch
> trac_6588-categories-root_systems-nt.patch
> trac_6588-categories-root_systems-review-nt.patch
> }}}

That's good!

Cheers,

Anne



---

archive/issue_comments_053788.json:
```json
{
    "body": "Replying to [comment:16 aschilling]:\n> You are welcome. I hope you will return the favor for trac_12536-linear_extensions-as.patch!\n\nI sure will, soon!\n\n> > Crystals are only implemented in sage.combinat.crystals (so far). But\n> > this names an area of mathematics. So this fits a bit more the first\n> > case.\n> \n> No, there is a lot of crystal code in /sage/categories: crystals, finite_crystals, highest_weight_crystals, ....\n\nI meant: the crystals themselves (CrystalOfLetter, KR, ...) are all in\nimplemented in sage.combinat.crystals.\n\n> Why can't fundamental_weights when \"extended\" is set also include\n> `delta`? This would at least fit with the notational abuse of\n> fundamental_weight.\n\nBecause we want to do things like:\n\n    sage: x in self.fundamental_weights()\n    \n    sage: all(L.some_property() for L in self.fundamental_weights())\n\nSo adding delta would change the semantic of fundamental_weights.\nWhereas the current abuse of fundamental_weight can't break any code.\n\n> I also wrote another very small reviewer's patch that you can fold in.\n\nI don't see it on the queue; did you push?\n\nThanks!\n                     Nicolas",
    "created_at": "2012-03-12T08:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53788",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:16 aschilling]:
> You are welcome. I hope you will return the favor for trac_12536-linear_extensions-as.patch!

I sure will, soon!

> > Crystals are only implemented in sage.combinat.crystals (so far). But
> > this names an area of mathematics. So this fits a bit more the first
> > case.
> 
> No, there is a lot of crystal code in /sage/categories: crystals, finite_crystals, highest_weight_crystals, ....

I meant: the crystals themselves (CrystalOfLetter, KR, ...) are all in
implemented in sage.combinat.crystals.

> Why can't fundamental_weights when "extended" is set also include
> `delta`? This would at least fit with the notational abuse of
> fundamental_weight.

Because we want to do things like:

    sage: x in self.fundamental_weights()
    
    sage: all(L.some_property() for L in self.fundamental_weights())

So adding delta would change the semantic of fundamental_weights.
Whereas the current abuse of fundamental_weight can't break any code.

> I also wrote another very small reviewer's patch that you can fold in.

I don't see it on the queue; did you push?

Thanks!
                     Nicolas



---

archive/issue_comments_053789.json:
```json
{
    "body": "Replying to [comment:17 nthiery]:\n> Replying to [comment:16 aschilling]:\n> > You are welcome. I hope you will return the favor for trac_12536-linear_extensions-as.patch!\n> \n> I sure will, soon!\n\nThanks.\n\n> > > Crystals are only implemented in sage.combinat.crystals (so far). But\n> > > this names an area of mathematics. So this fits a bit more the first\n> > > case.\n> > \n> > No, there is a lot of crystal code in /sage/categories: crystals, finite_crystals, highest_weight_crystals, ....\n> \n> I meant: the crystals themselves (CrystalOfLetter, KR, ...) are all in\n> implemented in sage.combinat.crystals.\n\nBut these are not categories, they are classes. In your case, a cateogory is in\n/sage/combinat/root_systems/\n\n> > Why can't fundamental_weights when \"extended\" is set also include\n> > `delta`? This would at least fit with the notational abuse of\n> > fundamental_weight.\n> \n> Because we want to do things like:\n> \n>     sage: x in self.fundamental_weights()\n>     \n>     sage: all(L.some_property() for L in self.fundamental_weights())\n> \n> So adding delta would change the semantic of fundamental_weights.\n> Whereas the current abuse of fundamental_weight can't break any code.\n\nHow about self.fundamental_weights(extended = True) with default extended = False?\n\n> > I also wrote another very small reviewer's patch that you can fold in.\n> \n> I don't see it on the queue; did you push?\n\nSorry, I forgot to push. It should be there now.\n\nBest,\n\nAnne",
    "created_at": "2012-03-12T14:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53789",
    "user": "https://github.com/anneschilling"
}
```

Replying to [comment:17 nthiery]:
> Replying to [comment:16 aschilling]:
> > You are welcome. I hope you will return the favor for trac_12536-linear_extensions-as.patch!
> 
> I sure will, soon!

Thanks.

> > > Crystals are only implemented in sage.combinat.crystals (so far). But
> > > this names an area of mathematics. So this fits a bit more the first
> > > case.
> > 
> > No, there is a lot of crystal code in /sage/categories: crystals, finite_crystals, highest_weight_crystals, ....
> 
> I meant: the crystals themselves (CrystalOfLetter, KR, ...) are all in
> implemented in sage.combinat.crystals.

But these are not categories, they are classes. In your case, a cateogory is in
/sage/combinat/root_systems/

> > Why can't fundamental_weights when "extended" is set also include
> > `delta`? This would at least fit with the notational abuse of
> > fundamental_weight.
> 
> Because we want to do things like:
> 
>     sage: x in self.fundamental_weights()
>     
>     sage: all(L.some_property() for L in self.fundamental_weights())
> 
> So adding delta would change the semantic of fundamental_weights.
> Whereas the current abuse of fundamental_weight can't break any code.

How about self.fundamental_weights(extended = True) with default extended = False?

> > I also wrote another very small reviewer's patch that you can fold in.
> 
> I don't see it on the queue; did you push?

Sorry, I forgot to push. It should be there now.

Best,

Anne



---

archive/issue_comments_053790.json:
```json
{
    "body": "Attachment [trac_6588-categories-root_systems-nt-before-reindentation.patch](tarball://root/attachments/some-uuid/ticket6588/trac_6588-categories-root_systems-nt-before-reindentation.patch) by @nthiery created at 2012-03-12 22:15:36\n\nThis contains the user-readable diff. Do not apply!",
    "created_at": "2012-03-12T22:15:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53790",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_6588-categories-root_systems-nt-before-reindentation.patch](tarball://root/attachments/some-uuid/ticket6588/trac_6588-categories-root_systems-nt-before-reindentation.patch) by @nthiery created at 2012-03-12 22:15:36

This contains the user-readable diff. Do not apply!



---

archive/issue_comments_053791.json:
```json
{
    "body": "Replying to [comment:18 aschilling]:\n> But these are not categories, they are classes. In your case, a cateogory is in\n> /sage/combinat/root_systems/\n\nYes: unlike for crystals, and like for symmetric functions (well for\nNCSF actually; the categorification of symmetric functions is yet to\nbe done), I want to keep the categories close to the classes. As I\nsaid, it's borderline, but it feels better to me this way.\n\n> How about self.fundamental_weights(extended = True) with default extended = False?\n\nWell, since it's an abuse, and one that we might want to get rid of,\nI'd rather not abuse yet another function. Unless you have a natural\nuse case for this notation? (for the extended weight lattice, that's\njust self.basis()).\n\n> Sorry, I forgot to push.\n\nGiven how many times I played that gag to you, I am not going\nto throw the first rock :-)\n\n> It should be there now.\n\nYes, thanks! I have folded together all patches and posted them\nhere. I also did the reindentation and renaming *_lattice_realization\n-> *_lattice_realizations. On my side, the patch is good to go.\n\nCheers,\n                        Nicolas",
    "created_at": "2012-03-12T22:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53791",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:18 aschilling]:
> But these are not categories, they are classes. In your case, a cateogory is in
> /sage/combinat/root_systems/

Yes: unlike for crystals, and like for symmetric functions (well for
NCSF actually; the categorification of symmetric functions is yet to
be done), I want to keep the categories close to the classes. As I
said, it's borderline, but it feels better to me this way.

> How about self.fundamental_weights(extended = True) with default extended = False?

Well, since it's an abuse, and one that we might want to get rid of,
I'd rather not abuse yet another function. Unless you have a natural
use case for this notation? (for the extended weight lattice, that's
just self.basis()).

> Sorry, I forgot to push.

Given how many times I played that gag to you, I am not going
to throw the first rock :-)

> It should be there now.

Yes, thanks! I have folded together all patches and posted them
here. I also did the reindentation and renaming *_lattice_realization
-> *_lattice_realizations. On my side, the patch is good to go.

Cheers,
                        Nicolas



---

archive/issue_comments_053792.json:
```json
{
    "body": "> > How about self.fundamental_weights(extended = True) with default extended = False?\n> \n> Well, since it's an abuse, and one that we might want to get rid of,\n> I'd rather not abuse yet another function. Unless you have a natural\n> use case for this notation? (for the extended weight lattice, that's\n> just self.basis()).\n\nOk, since this is in self.basis() I am satisfied.\n\n> Yes, thanks! I have folded together all patches and posted them\n> here. I also did the reindentation and renaming *_lattice_realization\n> -> *_lattice_realizations. On my side, the patch is good to go.\n\nOk, thanks! Unless I hear otherwise from Mark, I'll set a positive review.\n\nCheers,\n\nAnne",
    "created_at": "2012-03-13T13:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53792",
    "user": "https://github.com/anneschilling"
}
```

> > How about self.fundamental_weights(extended = True) with default extended = False?
> 
> Well, since it's an abuse, and one that we might want to get rid of,
> I'd rather not abuse yet another function. Unless you have a natural
> use case for this notation? (for the extended weight lattice, that's
> just self.basis()).

Ok, since this is in self.basis() I am satisfied.

> Yes, thanks! I have folded together all patches and posted them
> here. I also did the reindentation and renaming *_lattice_realization
> -> *_lattice_realizations. On my side, the patch is good to go.

Ok, thanks! Unless I hear otherwise from Mark, I'll set a positive review.

Cheers,

Anne



---

archive/issue_comments_053793.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-13T13:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53793",
    "user": "https://github.com/anneschilling"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053794.json:
```json
{
    "body": "Good morning Anne!\n\nReplying to [comment:22 aschilling]:\n> Ok, thanks! Unless I hear otherwise from Mark, I'll set a positive review.\n\nYippee!\n\nA bunch of patches went into 5.0.beta8 this morning. Maybe this one will follow :-)\n\nI am working on the review of #12536.\n\nCheers,\n                             Nicolas",
    "created_at": "2012-03-13T13:53:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53794",
    "user": "https://github.com/nthiery"
}
```

Good morning Anne!

Replying to [comment:22 aschilling]:
> Ok, thanks! Unless I hear otherwise from Mark, I'll set a positive review.

Yippee!

A bunch of patches went into 5.0.beta8 this morning. Maybe this one will follow :-)

I am working on the review of #12536.

Cheers,
                             Nicolas



---

archive/issue_comments_053795.json:
```json
{
    "body": "Let's not anthropomorphize the PatchBot :-)",
    "created_at": "2012-03-15T20:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53795",
    "user": "https://github.com/jdemeyer"
}
```

Let's not anthropomorphize the PatchBot :-)



---

archive/issue_comments_053796.json:
```json
{
    "body": "Hi Nicolas,\n\nWhen working on a review for #12667, I noticed some documentation problems with this patch in root_lattice_realizations. I wrote a review patch on the sage-combinat queue. If you are happy, please fold, repost here and reset the positive review.\n\nBest,\n\nAnne",
    "created_at": "2012-03-16T06:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53796",
    "user": "https://github.com/anneschilling"
}
```

Hi Nicolas,

When working on a review for #12667, I noticed some documentation problems with this patch in root_lattice_realizations. I wrote a review patch on the sage-combinat queue. If you are happy, please fold, repost here and reset the positive review.

Best,

Anne



---

archive/issue_comments_053797.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-03-16T06:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53797",
    "user": "https://github.com/anneschilling"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_053798.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-03-16T08:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53798",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_053799.json:
```json
{
    "body": "Replying to [comment:25 aschilling]:\n> When working on a review for #12667, I noticed some documentation problems with this patch in root_lattice_realizations. I wrote a review patch on the sage-combinat queue. If you are happy, please fold, repost here and reset the positive review.\n\nGood catches. Thanks! Folded.\n\nI allowed myself to further add the weight lattice realizations file to the reference manual, and to replace {\\vee} by \\vee. I also set back \\mathbb{N} to \\NN, since \\NN will be added very soon to the standard Sage macros.",
    "created_at": "2012-03-16T08:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53799",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:25 aschilling]:
> When working on a review for #12667, I noticed some documentation problems with this patch in root_lattice_realizations. I wrote a review patch on the sage-combinat queue. If you are happy, please fold, repost here and reset the positive review.

Good catches. Thanks! Folded.

I allowed myself to further add the weight lattice realizations file to the reference manual, and to replace {\vee} by \vee. I also set back \mathbb{N} to \NN, since \NN will be added very soon to the standard Sage macros.



---

archive/issue_comments_053800.json:
```json
{
    "body": "While I was at it, I added all the other missing files in root_system.rst (type_*, ...), and fixed the documentation typos revealled by the compilation. Florent reviewed them. New patch posted.",
    "created_at": "2012-03-16T09:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53800",
    "user": "https://github.com/nthiery"
}
```

While I was at it, I added all the other missing files in root_system.rst (type_*, ...), and fixed the documentation typos revealled by the compilation. Florent reviewed them. New patch posted.



---

archive/issue_comments_053801.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-03-16T10:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53801",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_053802.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-16T10:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53802",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053803.json:
```json
{
    "body": "I guess the last patch still needs review?",
    "created_at": "2012-03-16T10:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53803",
    "user": "https://github.com/jdemeyer"
}
```

I guess the last patch still needs review?



---

archive/issue_comments_053804.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-16T10:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53804",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053805.json:
```json
{
    "body": "No, I had uploaded the wrong file. The new one is the one that has been checked by Florent.\n\nNow it's a very final positive review. Sorry Jeroen for the mess; I hope you were not in the process of applying / testing it!",
    "created_at": "2012-03-16T10:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53805",
    "user": "https://github.com/nthiery"
}
```

No, I had uploaded the wrong file. The new one is the one that has been checked by Florent.

Now it's a very final positive review. Sorry Jeroen for the mess; I hope you were not in the process of applying / testing it!



---

archive/issue_comments_053806.json:
```json
{
    "body": "I am not sure why you replaced \\mathcal{N} by \\NN since this currently gives a latex error when compiling the documentation:\n\npreparing documents... done\nWARNING: display latex u'\\\\NN': latex exited with error:lattice_realizations                                                                        \n[stderr]\n\n[stdout]\nThis is pdfTeXk, Version 3.1415926-1.40.9 (Web2C 7.5.7)\n %&-line parsing enabled.\nentering extended mode\n(./math.tex\nLaTeX2e <2005/12/01>\nBabel <v3.8l> and hyphenation patterns for english, usenglishmax, dumylang, noh\nyphenation, german-x-2008-06-18, ngerman-x-2008-06-18, ancientgreek, ibycus, ar\nabic, basque, bulgarian, catalan, pinyin, coptic, croatian, czech, danish, dutc\nh, esperanto, estonian, farsi, finnish, french, galician, german, ngerman, mono\ngreek, greek, hungarian, icelandic, indonesian, interlingua, irish, italian, la\ntin, lithuanian, mongolian, mongolian2a, bokmal, nynorsk, polish, portuguese, r\nomanian, russian, sanskrit, serbian, slovak, slovenian, spanish, swedish, turki\nsh, ukenglish, ukrainian, uppersorbian, welsh, loaded.\n(/usr/local/texlive/2008/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2005/09/16 v1.4f Standard LaTeX document class\n(/usr/local/texlive/2008/texmf-dist/tex/latex/base/size12.clo))\n(/usr/local/texlive/2008/texmf-dist/tex/latex/base/inputenc.sty\n(/usr/local/texlive/2008/texmf-dist/tex/latex/base/utf8.def\n(/usr/local/texlive/2008/texmf-dist/tex/latex/base/t1enc.dfu)\n(/usr/local/texlive/2008/texmf-dist/tex/latex/base/ot1enc.dfu)\n(/usr/local/texlive/2008/texmf-dist/tex/latex/base/omsenc.dfu)))\n(/usr/local/texlive/2008/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/local/texlive/2008/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/local/texlive/2008/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/local/texlive/2008/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/local/texlive/2008/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/local/texlive/2008/texmf-dist/tex/latex/amscls/amsthm.sty)\n(/usr/local/texlive/2008/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/local/texlive/2008/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/local/texlive/2008/texmf-dist/tex/latex/tools/bm.sty) (./math.aux)\n(/usr/local/texlive/2008/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/local/texlive/2008/texmf-dist/tex/latex/amsfonts/umsb.fd)\n! Undefined control sequence.\n<recently read> \\NN \n                    \nl.29 $\\NN\n         $\n[1] (./math.aux) )\n(see the transcript file for additional information)\nOutput written on math.dvi (1 page, 152 bytes).\nTranscript written on math.log.\n\nIs it allowed to leave such a failure?\n\nThanks,\n\nAnne",
    "created_at": "2012-03-16T14:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53806",
    "user": "https://github.com/anneschilling"
}
```

I am not sure why you replaced \mathcal{N} by \NN since this currently gives a latex error when compiling the documentation:

preparing documents... done
WARNING: display latex u'\\NN': latex exited with error:lattice_realizations                                                                        
[stderr]

[stdout]
This is pdfTeXk, Version 3.1415926-1.40.9 (Web2C 7.5.7)
 %&-line parsing enabled.
entering extended mode
(./math.tex
LaTeX2e <2005/12/01>
Babel <v3.8l> and hyphenation patterns for english, usenglishmax, dumylang, noh
yphenation, german-x-2008-06-18, ngerman-x-2008-06-18, ancientgreek, ibycus, ar
abic, basque, bulgarian, catalan, pinyin, coptic, croatian, czech, danish, dutc
h, esperanto, estonian, farsi, finnish, french, galician, german, ngerman, mono
greek, greek, hungarian, icelandic, indonesian, interlingua, irish, italian, la
tin, lithuanian, mongolian, mongolian2a, bokmal, nynorsk, polish, portuguese, r
omanian, russian, sanskrit, serbian, slovak, slovenian, spanish, swedish, turki
sh, ukenglish, ukrainian, uppersorbian, welsh, loaded.
(/usr/local/texlive/2008/texmf-dist/tex/latex/base/article.cls
Document Class: article 2005/09/16 v1.4f Standard LaTeX document class
(/usr/local/texlive/2008/texmf-dist/tex/latex/base/size12.clo))
(/usr/local/texlive/2008/texmf-dist/tex/latex/base/inputenc.sty
(/usr/local/texlive/2008/texmf-dist/tex/latex/base/utf8.def
(/usr/local/texlive/2008/texmf-dist/tex/latex/base/t1enc.dfu)
(/usr/local/texlive/2008/texmf-dist/tex/latex/base/ot1enc.dfu)
(/usr/local/texlive/2008/texmf-dist/tex/latex/base/omsenc.dfu)))
(/usr/local/texlive/2008/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/local/texlive/2008/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/local/texlive/2008/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/local/texlive/2008/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/local/texlive/2008/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/local/texlive/2008/texmf-dist/tex/latex/amscls/amsthm.sty)
(/usr/local/texlive/2008/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/local/texlive/2008/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/local/texlive/2008/texmf-dist/tex/latex/tools/bm.sty) (./math.aux)
(/usr/local/texlive/2008/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/local/texlive/2008/texmf-dist/tex/latex/amsfonts/umsb.fd)
! Undefined control sequence.
<recently read> \NN 
                    
l.29 $\NN
         $
[1] (./math.aux) )
(see the transcript file for additional information)
Output written on math.dvi (1 page, 152 bytes).
Transcript written on math.log.

Is it allowed to leave such a failure?

Thanks,

Anne



---

archive/issue_comments_053807.json:
```json
{
    "body": "Hi Anne:\n\nReplying to [comment:34 aschilling]:\n> I am not sure why you replaced \\mathcal{N} by \\NN since this currently gives a latex error when compiling the documentation:\n\nAs I said: ``I also set back \\mathbb{N} to \\NN, since \\NN will be added very soon to the standard Sage macros''\n\nThere are lots of other failures like this in the documentation; it's best to progressively get rid of them, but here it's just temporary, so that's good enough. Let's not waste time on having to update this later.\n\nCheers,\n                           Nicolas",
    "created_at": "2012-03-16T15:08:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53807",
    "user": "https://github.com/nthiery"
}
```

Hi Anne:

Replying to [comment:34 aschilling]:
> I am not sure why you replaced \mathcal{N} by \NN since this currently gives a latex error when compiling the documentation:

As I said: ``I also set back \mathbb{N} to \NN, since \NN will be added very soon to the standard Sage macros''

There are lots of other failures like this in the documentation; it's best to progressively get rid of them, but here it's just temporary, so that's good enough. Let's not waste time on having to update this later.

Cheers,
                           Nicolas



---

archive/issue_comments_053808.json:
```json
{
    "body": "Hi Nicolas,\n\nWell, one of my patches recently did not get merged until all these failures were rectified. So I thought it was compulsory for all documentation to work.\n\nBest,\n\nAnne",
    "created_at": "2012-03-16T15:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53808",
    "user": "https://github.com/anneschilling"
}
```

Hi Nicolas,

Well, one of my patches recently did not get merged until all these failures were rectified. So I thought it was compulsory for all documentation to work.

Best,

Anne



---

archive/issue_comments_053809.json:
```json
{
    "body": "Replying to [comment:36 aschilling]:\n> Well, one of my patches recently did not get merged until all these failures were rectified. So I thought it was compulsory for all documentation to work.\n\nThere is at least one other \\NN in th sources. Anyway, let's not waste even more time discussing it. Here is the diff with the patch I am about to upload(sorry Jeroen):\n\n```\n-+                with the coroots are all in `\\NN`, which is not\n++                with the coroots are all non negative integers, which is not\n```\n\n\nI left the positive review; feel free to change.",
    "created_at": "2012-03-16T15:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53809",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:36 aschilling]:
> Well, one of my patches recently did not get merged until all these failures were rectified. So I thought it was compulsory for all documentation to work.

There is at least one other \NN in th sources. Anyway, let's not waste even more time discussing it. Here is the diff with the patch I am about to upload(sorry Jeroen):

```
-+                with the coroots are all in `\NN`, which is not
++                with the coroots are all non negative integers, which is not
```


I left the positive review; feel free to change.



---

archive/issue_comments_053810.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-03-18T11:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53810",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_053811.json:
```json
{
    "body": "This obviously fails on 32-bit systems:\n\n```\nsage -t  \"devel/sage/sage/combinat/root_system/dynkin_diagram.py\"\n**********************************************************************\nFile \"/export/home/buildbot/sage-5.0.beta9/devel/sage/sage/combinat/root_system/dynkin_diagram.py\", line 167:\n    sage: hash(CartanType(['A',3]).dynkin_diagram()) # indirect doctest\nExpected:\n    286820813001824631\nGot:\n    -2127980169\n**********************************************************************\n```\n",
    "created_at": "2012-03-18T11:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53811",
    "user": "https://github.com/jdemeyer"
}
```

This obviously fails on 32-bit systems:

```
sage -t  "devel/sage/sage/combinat/root_system/dynkin_diagram.py"
**********************************************************************
File "/export/home/buildbot/sage-5.0.beta9/devel/sage/sage/combinat/root_system/dynkin_diagram.py", line 167:
    sage: hash(CartanType(['A',3]).dynkin_diagram()) # indirect doctest
Expected:
    286820813001824631
Got:
    -2127980169
**********************************************************************
```




---

archive/issue_comments_053812.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-18T17:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53812",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053813.json:
```json
{
    "body": "Thanks Jeroen for the report. This should be fixed with the upcoming patch. The diff is:\n\n```diff\ndiff --git a/sage/combinat/root_system/dynkin_diagram.py b/sage/combinat/root_system/dynkin_diagram.py\n--- a/sage/combinat/root_system/dynkin_diagram.py\n+++ b/sage/combinat/root_system/dynkin_diagram.py\n@@ -165,8 +165,8 @@ class DynkinDiagram_class(DiGraph, Carta\n         EXAMPLES::\n \n             sage: hash(CartanType(['A',3]).dynkin_diagram()) # indirect doctest\n-            286820813001824631\n-\n+            286820813001824631     # 64-bit\n+            -2127980169            # 32-bit\n         \"\"\"\n         # Should assert for immutability!\n\n```\n",
    "created_at": "2012-03-18T17:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53813",
    "user": "https://github.com/nthiery"
}
```

Thanks Jeroen for the report. This should be fixed with the upcoming patch. The diff is:

```diff
diff --git a/sage/combinat/root_system/dynkin_diagram.py b/sage/combinat/root_system/dynkin_diagram.py
--- a/sage/combinat/root_system/dynkin_diagram.py
+++ b/sage/combinat/root_system/dynkin_diagram.py
@@ -165,8 +165,8 @@ class DynkinDiagram_class(DiGraph, Carta
         EXAMPLES::
 
             sage: hash(CartanType(['A',3]).dynkin_diagram()) # indirect doctest
-            286820813001824631
-
+            286820813001824631     # 64-bit
+            -2127980169            # 32-bit
         """
         # Should assert for immutability!

```




---

archive/issue_comments_053814.json:
```json
{
    "body": "There is a problem with the documentation.  Doing \"make doc\" after applying this patch gives:\n\n```\nreading sources... [ 92%] sage/combinat/root_system/weight_lattice_realizations\nreading sources... [ 95%] sage/combinat/root_system/weight_space\nreading sources... [ 97%] sage/combinat/root_system/weyl_group\nreading sources... [100%] sage/structure/parent\n\n<autodoc>:0: ERROR: Inconsistent literal block quoting.\nlooking for now-outdated files... none found\npickling environment... done\nchecking consistency... done\npreparing documents... done\nwriting output... [  2%] categories\nwriting output... [  4%] combinat/algebra\nwriting output... [  6%] combinat/index\nwriting output... [  8%] combinat/root_systems\nwriting output... [ 10%] index\n```\n\nUnfortunately, there is no indication which file caused the problem.",
    "created_at": "2012-03-19T16:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53814",
    "user": "https://github.com/jdemeyer"
}
```

There is a problem with the documentation.  Doing "make doc" after applying this patch gives:

```
reading sources... [ 92%] sage/combinat/root_system/weight_lattice_realizations
reading sources... [ 95%] sage/combinat/root_system/weight_space
reading sources... [ 97%] sage/combinat/root_system/weyl_group
reading sources... [100%] sage/structure/parent

<autodoc>:0: ERROR: Inconsistent literal block quoting.
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [  2%] categories
writing output... [  4%] combinat/algebra
writing output... [  6%] combinat/index
writing output... [  8%] combinat/root_systems
writing output... [ 10%] index
```

Unfortunately, there is no indication which file caused the problem.



---

archive/issue_comments_053815.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-19T16:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53815",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_053816.json:
```json
{
    "body": "Ok, it was in root_lattice_realizations. At this occasion, Anne and myself spotted a couple more doc typos. I am about to upload an updated patch. See :attachment:latest_change.patch for the changes since last version.",
    "created_at": "2012-03-19T20:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53816",
    "user": "https://github.com/nthiery"
}
```

Ok, it was in root_lattice_realizations. At this occasion, Anne and myself spotted a couple more doc typos. I am about to upload an updated patch. See :attachment:latest_change.patch for the changes since last version.



---

archive/issue_comments_053817.json:
```json
{
    "body": "Attachment [latest_change.patch](tarball://root/attachments/some-uuid/ticket6588/latest_change.patch) by @nthiery created at 2012-03-19 20:41:58",
    "created_at": "2012-03-19T20:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53817",
    "user": "https://github.com/nthiery"
}
```

Attachment [latest_change.patch](tarball://root/attachments/some-uuid/ticket6588/latest_change.patch) by @nthiery created at 2012-03-19 20:41:58



---

archive/issue_comments_053818.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-03-19T21:34:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53818",
    "user": "https://github.com/anneschilling"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_053819.json:
```json
{
    "body": "> There is at least one other \\NN in th sources. Anyway, let's not waste even more time discussing it. Here is the diff with the patch I am about to upload(sorry Jeroen):\n\nI finished my patch on \\NN: this is #12717",
    "created_at": "2012-03-21T18:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53819",
    "user": "https://github.com/hivert"
}
```

> There is at least one other \NN in th sources. Anyway, let's not waste even more time discussing it. Here is the diff with the patch I am about to upload(sorry Jeroen):

I finished my patch on \NN: this is #12717



---

archive/issue_comments_053820.json:
```json
{
    "body": "Attachment [trac_6588-categories-root_systems-nt.patch](tarball://root/attachments/some-uuid/ticket6588/trac_6588-categories-root_systems-nt.patch) by @jdemeyer created at 2012-03-23 13:11:06\n\nApply this one (identical to the other, but renames and reindents two files; thus unreadable)",
    "created_at": "2012-03-23T13:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53820",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [trac_6588-categories-root_systems-nt.patch](tarball://root/attachments/some-uuid/ticket6588/trac_6588-categories-root_systems-nt.patch) by @jdemeyer created at 2012-03-23 13:11:06

Apply this one (identical to the other, but renames and reindents two files; thus unreadable)



---

archive/issue_comments_053821.json:
```json
{
    "body": "Rebased the last patch to sage-5.0.beta9 (there was some trivial fuzz).",
    "created_at": "2012-03-23T13:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53821",
    "user": "https://github.com/jdemeyer"
}
```

Rebased the last patch to sage-5.0.beta9 (there was some trivial fuzz).



---

archive/issue_comments_053822.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-23T15:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53822",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_015530.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-03-23T15:18:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6588#event-15530"
}
```



---

archive/issue_comments_053823.json:
```json
{
    "body": "Yippee! Thanks all for your help getting this in!",
    "created_at": "2012-03-23T16:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53823",
    "user": "https://github.com/nthiery"
}
```

Yippee! Thanks all for your help getting this in!



---

archive/issue_comments_053824.json:
```json
{
    "body": "The examples for `__cmp__` in `sage/combinat/root_system/type_dual.py` are bad.  #12793 fixes them, **please review**.",
    "created_at": "2012-04-02T15:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6588#issuecomment-53824",
    "user": "https://github.com/jdemeyer"
}
```

The examples for `__cmp__` in `sage/combinat/root_system/type_dual.py` are bad.  #12793 fixes them, **please review**.
