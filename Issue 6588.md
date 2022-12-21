# Issue 6588: Root systems: categorification

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-07-22 11:54:48

Assignee: mhansen

CC:  sage-combinat mshimo@math.vt.edu

Keywords: root systems, categories

Replace the abstract classes in RootSystems (like RootLatticeRealization) by categories.

Use it to implement parabolic sub-rootsystems, and parabolic Weyl subgroups.


---

Comment by nthiery created at 2012-02-25 00:43:30

The updated patch adds many missing doctests, and improves coxeter diagrams. It's probably close to completion, up to fixing some potentially failing doctests.


---

Comment by nthiery created at 2012-02-25 00:43:30

Changing status from new to needs_review.


---

Comment by nthiery created at 2012-02-25 00:50:57

Beside, I commuted it up the Sage-Combinat queue. In principle, there should not be other dependencies than the listed ones.


---

Comment by nthiery created at 2012-02-25 00:55:06

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

Comment by nthiery created at 2012-02-25 01:18:00

I fixed the doctests failures due to this patch. Most of them where due to the fact that affine weyl groups are iterable now, which gives a nicer an_element on any free module thereupon.

The other doctests failures showing up in the log are related to #12518 (or to the ISGCI patch, but that's because I did not upload the appropriate database on my test server).

The review can start!


---

Comment by nthiery created at 2012-03-05 21:40:53

Patch updated after a bug report by Mark; see end of patch description


---

Comment by nthiery created at 2012-03-08 13:09:31

Upon popular demand, extended weight lattice/spaces are now implemented.


---

Comment by aschilling created at 2012-03-09 20:07:48

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

Comment by nthiery created at 2012-03-10 12:04:44

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

Comment by nthiery created at 2012-03-11 09:44:56

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

Comment by davidloeffler created at 2012-03-11 10:37:25

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

Comment by davidloeffler created at 2012-03-11 10:37:25

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2012-03-11 10:43:26

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2012-03-11 10:43:26

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

Comment by aschilling created at 2012-03-12 04:38:38

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

Comment by nthiery created at 2012-03-12 08:12:55

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

Comment by aschilling created at 2012-03-12 14:26:13

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

Attachment

This contains the user-readable diff. Do not apply!


---

Comment by nthiery created at 2012-03-12 22:34:24

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

Comment by aschilling created at 2012-03-13 13:42:06

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

Comment by aschilling created at 2012-03-13 13:42:06

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2012-03-13 13:53:10

Good morning Anne!

Replying to [comment:22 aschilling]:
> Ok, thanks! Unless I hear otherwise from Mark, I'll set a positive review.

Yippee!

A bunch of patches went into 5.0.beta8 this morning. Maybe this one will follow :-)

I am working on the review of #12536.

Cheers,
                             Nicolas


---

Comment by jdemeyer created at 2012-03-15 20:07:28

Let's not anthropomorphize the PatchBot :-)


---

Comment by aschilling created at 2012-03-16 06:01:01

Hi Nicolas,

When working on a review for #12667, I noticed some documentation problems with this patch in root_lattice_realizations. I wrote a review patch on the sage-combinat queue. If you are happy, please fold, repost here and reset the positive review.

Best,

Anne


---

Comment by aschilling created at 2012-03-16 06:01:45

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2012-03-16 08:28:50

Changing status from needs_work to positive_review.


---

Comment by nthiery created at 2012-03-16 08:32:20

Replying to [comment:25 aschilling]:
> When working on a review for #12667, I noticed some documentation problems with this patch in root_lattice_realizations. I wrote a review patch on the sage-combinat queue. If you are happy, please fold, repost here and reset the positive review.

Good catches. Thanks! Folded.

I allowed myself to further add the weight lattice realizations file to the reference manual, and to replace {\vee} by \vee. I also set back \mathbb{N} to \NN, since \NN will be added very soon to the standard Sage macros.


---

Comment by nthiery created at 2012-03-16 09:59:37

While I was at it, I added all the other missing files in root_system.rst (type_*, ...), and fixed the documentation typos revealled by the compilation. Florent reviewed them. New patch posted.


---

Comment by jdemeyer created at 2012-03-16 10:06:30

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-03-16 10:06:48

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2012-03-16 10:06:48

I guess the last patch still needs review?


---

Comment by nthiery created at 2012-03-16 10:25:22

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2012-03-16 10:25:22

No, I had uploaded the wrong file. The new one is the one that has been checked by Florent.

Now it's a very final positive review. Sorry Jeroen for the mess; I hope you were not in the process of applying / testing it!


---

Comment by aschilling created at 2012-03-16 14:56:05

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

Comment by nthiery created at 2012-03-16 15:08:52

Hi Anne:

Replying to [comment:34 aschilling]:
> I am not sure why you replaced \mathcal{N} by \NN since this currently gives a latex error when compiling the documentation:

As I said: ``I also set back \mathbb{N} to \NN, since \NN will be added very soon to the standard Sage macros''

There are lots of other failures like this in the documentation; it's best to progressively get rid of them, but here it's just temporary, so that's good enough. Let's not waste time on having to update this later.

Cheers,
                           Nicolas


---

Comment by aschilling created at 2012-03-16 15:16:00

Hi Nicolas,

Well, one of my patches recently did not get merged until all these failures were rectified. So I thought it was compulsory for all documentation to work.

Best,

Anne


---

Comment by nthiery created at 2012-03-16 15:40:15

Replying to [comment:36 aschilling]:
> Well, one of my patches recently did not get merged until all these failures were rectified. So I thought it was compulsory for all documentation to work.

There is at least one other \NN in th sources. Anyway, let's not waste even more time discussing it. Here is the diff with the patch I am about to upload(sorry Jeroen):

```
-+                with the coroots are all in `\NN`, which is not
++                with the coroots are all non negative integers, which is not
```


I left the positive review; feel free to change.


---

Comment by jdemeyer created at 2012-03-18 11:08:24

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-03-18 11:08:24

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

Comment by nthiery created at 2012-03-18 17:53:33

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2012-03-18 17:53:33

Thanks Jeroen for the report. This should be fixed with the upcoming patch. The diff is:

```diff
diff --git a/sage/combinat/root_system/dynkin_diagram.py b/sage/combinat/root_system/dynkin_diagram.py
--- a/sage/combinat/root_system/dynkin_diagram.py
+++ b/sage/combinat/root_system/dynkin_diagram.py
`@``@` -165,8 +165,8 `@``@` class DynkinDiagram_class(DiGraph, Carta
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

Comment by jdemeyer created at 2012-03-19 16:08:19

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

Comment by jdemeyer created at 2012-03-19 16:08:19

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2012-03-19 20:39:10

Ok, it was in root_lattice_realizations. At this occasion, Anne and myself spotted a couple more doc typos. I am about to upload an updated patch. See :attachment:latest_change.patch for the changes since last version.


---

Attachment


---

Comment by aschilling created at 2012-03-19 21:34:18

Changing status from needs_work to positive_review.


---

Comment by hivert created at 2012-03-21 18:25:03

> There is at least one other \NN in th sources. Anyway, let's not waste even more time discussing it. Here is the diff with the patch I am about to upload(sorry Jeroen):

I finished my patch on \NN: this is #12717


---

Attachment

Apply this one (identical to the other, but renames and reindents two files; thus unreadable)


---

Comment by jdemeyer created at 2012-03-23 13:11:36

Rebased the last patch to sage-5.0.beta9 (there was some trivial fuzz).


---

Comment by jdemeyer created at 2012-03-23 15:18:56

Resolution: fixed


---

Comment by nthiery created at 2012-03-23 16:00:06

Yippee! Thanks all for your help getting this in!


---

Comment by jdemeyer created at 2012-04-02 15:22:30

The examples for `__cmp__` in `sage/combinat/root_system/type_dual.py` are bad.  #12793 fixes them, *please review*.
