# Issue 6099: morphisms of simplicial complexes and the associated chain complex morphisms

Issue created by migration from Trac.

Original creator: bantieau

Original creation time: 2009-05-21 03:37:46

Assignee: bantieau

CC:  jhpalmieri

Add functionality to sage to create morphisms between simplicial complexes, and to associate to these morphisms the chain complex maps on the homological and cohomological chain complexes.


---

Attachment

This patch implements the chain complex morphisms part of this trac ticket.


---

Attachment

This patch implements the chain complex morphisms part of this trac ticket.


---

Comment by bantieau created at 2009-06-01 23:15:19

Ignore 12335.patch. I would take it off, but I do not know how.


---

Attachment


---

Attachment

tweak to be compatibe with #6141, which changes facets to facets().


---

Comment by jhpalmieri created at 2009-06-17 18:19:24

It's great that you're working on this.  It looks very good, but there are a few issues:

 - in the docstring for effective_vertices, you might mention that it returns a Simplex.  The docstring could start "The set of vertices belonging to some face, as a simplex", and you could also put in a doctest like

```
sage: type(S.effective_vertices())
<class 'sage.homology.simplicial_complex.Simplex'>
```


 - I had a few doctest failures which I think are fixed in #6309 (two extra periods), but they should be fixed here.

 - Is it a good idea to have `domain` and `codomain` methods for morphisms?  I can imagine someone wanting to use the domain of the fiber product, for example, but they won't see the `_domain` attribute on tab completion.

 - You don't have 100% documentation and doctest coverage.  Type 'sage -coverage ...insert_path_here.../sage/homology' to get a summary.  When you do this, note that messages like
 {{{
 Possibly wrong (function name doesn't occur in doctests):
	 * _repr_(self):
 }}}
 can be avoided if you add "# indirect doctest", like this:
 {{{
            sage: x = i.associated_chain_complex_morphism()
            sage: x # indirect doctest
 }}}

 - Should "product" be renamed "fiber_product" so it's less ambiguous?

 - I wonder if `ChainComplexMorphism` should inherit from `ModuleElement` rather than `SageObject`.  Then you would define a method `_mul_` (rather than `__mul__`), and similarly for `_add_`, and you could also define `_lmul_` and `_rmul_` to deal with scalar multiplication.  Check the Sage reference manual, the "Coercion" section.  (This section is newly added to the reference manual, as of Sage 4.0.1 or 4.0.2, I think.)

 - I'm attaching a small patch which adds the new files to the reference manual.  (This involves editing one file, doc/en/reference/homology.rst, and also because of the way reST works, I had to change 
 {{{ 
 - D. Benjamin Antieau <d.ben.antieau`@`gmail.com> (2009.06)
 }}}
 to 
 {{{
 - \D. Benjamin Antieau <d.ben.antieau`@`gmail.com> (2009.06)
 }}}
 (The "D." at essentially the beginning of the line seemed to tell Sphinx that this was part of a numbered list, starting with number 4.)  Feel free to incorporate my changes and produce one single patch which does everything here.


---

Attachment


---

Comment by bantieau created at 2009-11-06 21:18:57

Hopefully final merged patch.


---

Attachment

OK. I've uploaded a patch that includes all of the patches above, and also includes all of your recommendations, except for inheriting from ModuleElement. Perhaps that can be another ticket, if someone wants that. Coverage and doctest are %100.


---

Comment by bantieau created at 2009-11-06 21:20:28

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2009-11-10 22:59:13

This is almost done.  I'm attaching a patch making a few changes.  First, in homology.rst, it should say `sage/homology/chain_complex_homspace` (it has "homset" instead of "homspace").  Also, I think that in category_types.py, the entry for chain complexes should say:

```
    ChainComplexes         : [RingModules, AbelianGroups, Sets],\
```

Also, I've changed the `__mul__` method for maps of chain complexes so that when the right-hand factor is a ring element, it gets multiplied on the right, not the left (in case we ever work over noncommutative rings).  I've also added an `__rmul__` method for multiplying on the left by a ring element.  I changed the string representation for chain complexes so it doesn't have a period at the end, so that your string representations for chain maps look better.

Finally, the only major problem: my patch fixes an issue with converting maps of simplicial complexes to maps of chain complexes:

```
sage: X = SimplicialComplex(1, [This is the Trac macro *0,1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#0,1-macro)); X
Simplicial complex with vertex set (0, 1) and facets {(0, 1)}
sage: H = Hom(X, X)
sage: f = H({0:1, 1:0})
sage: f.associated_chain_complex_morphism()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/palmieri/.sage/temp/jpalmieri538.local/84693/_Users_palmieri__sage_init_sage_0.py in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/homology/simplicial_complex_morphism.pyc in associated_chain_complex_morphism(self, base_ring, augmented, cochain)
    322             return ChainComplexMorphism(matrices,\
    323                     self._domain.chain_complex(base_ring=base_ring,augmented=augmented,cochain=cochain),\
--> 324                     self._codomain.chain_complex(base_ring=base_ring,augmented=augmented,cochain=cochain))
    325         else:
    326             return ChainComplexMorphism(matrices,\

/Applications/sage/local/lib/python2.6/site-packages/sage/homology/chain_complex_morphism.pyc in __init__(self, matrices, C, D)
    132                 if (i+1) in C.differential().keys() and (i+1) in D.differential().keys():
    133                     if not matrices[i]*C.differential()[i+1]==D.differential()[i+1]*matrices[i+1]:
--> 134                         raise ValueError, "Matrices must define a chain complex morphism."
    135                 elif (i+1) in C.differential().keys():
    136                     if not matrices[i]*C.differential()[i+1].is_zero():

ValueError: Matrices must define a chain complex morphism.
```

The issue is orientation: in the line

```
                    mval[X_faces.index(i)+(Y_faces.index(y)*num_faces_X)] = 1
```

in `associated_chain_complex_morphism`, the right side should be 1 or -1, depending on the orientation of y.

I'm giving your patch a positive review.  If you're happy with my new patch, change the ticket to "positive review".


---

Attachment

apply on top of 6099-merged.patch


---

Comment by bantieau created at 2009-11-14 22:49:42

Changing status from needs_review to positive_review.


---

Comment by bantieau created at 2009-11-14 22:49:42

Release manager: apply only 6099-merged.patch and trac_6099-part2.patch.


---

Comment by mhansen created at 2009-11-17 06:18:08

Resolution: fixed


---

Comment by mhansen created at 2009-11-17 14:56:30

Resolution changed from fixed to 


---

Comment by mhansen created at 2009-11-17 14:56:30

I had to back this out for now due to conflicts with the category code.  I'll look at readding this once those patches are merged.


---

Comment by mhansen created at 2009-11-17 14:56:30

Changing status from closed to new.


---

Comment by nthiery created at 2009-11-17 15:10:13

Replying to [comment:8 mhansen]:
> I had to back this out for now due to conflicts with the category code.  I'll look at readding this once those patches are merged.

    Hi Benjamin,

Sorry for the conflict. Rebasing the patch should be fairly easy. I suspect that the change to category_types can simply be discarded. As for the change in homset.py: I have removed this ugly run time type checking there. Instead, Hom(X, Y) looks for a method X._Hom_, and calls it if it exists. This _Hom_ method could typically be implemented in ChainComplexes.ParentMethods to achieve the current effect.

Good luck, and feel free to bug me.


---

Comment by jhpalmieri created at 2009-11-17 18:09:57

Replying to [comment:9 nthiery]:

> Sorry for the conflict. Rebasing the patch should be fairly easy. I suspect that the change to category_types can simply be discarded. 

Okay, that's easy enough.

>As for the change in homset.py: I have removed this ugly run time type checking there. Instead, Hom(X, Y) looks for a method X._Hom_, and calls it if it exists. This _Hom_ method could typically be implemented in ChainComplexes.ParentMethods to achieve the current effect.

I'm not sure what `ChainComplexes.ParentMethods` means, but we can just define, within the class `ChainComplex`, a method `_Hom_(self, other)`, right?


---

Comment by jhpalmieri created at 2009-11-17 20:24:42

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2009-11-17 20:24:42

Here's a rebased version.  This makes no changes to category_types.py or to categories/homset.py, instead implementing `_Hom_` methods for simplicial complexes and chain complexes.  With Sage 4.2.1, it applies cleanly and passes all tests.  If it still causes problems when merged, we'll probably have to wait until 4.3.alpha0 is released and work from there.


---

Comment by jhpalmieri created at 2009-11-17 20:25:53

I guess the only parts that need review are the two new `_Hom_` methods, one in chain_complex.py and one in simplicial_complex.py.  And then there is the issue of whether it plays well with the new category stuff...


---

Comment by nthiery created at 2009-11-17 20:34:35

Replying to [comment:10 jhpalmieri]:
> >As for the change in homset.py: I have removed this ugly run time type checking there. Instead, Hom(X, Y) looks for a method X._Hom_, and calls it if it exists. This _Hom_ method could typically be implemented in ChainComplexes.ParentMethods to achieve the current effect.
> 
> I'm not sure what `ChainComplexes.ParentMethods` means, but we can just define, within the class `ChainComplex`, a method `_Hom_(self, other)`, right?

Indeed.

`ChainComplexes.ParentMethods` is the class in the `ChainComplexes` category containing the generic code that applies to all parents in this category. That could be useful later on if there is more than one implementation of such parents. No rush for now.


---

Comment by nthiery created at 2009-11-17 20:40:29

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2009-11-17 20:40:29

Replying to [comment:12 jhpalmieri]:
> I guess the only parts that need review are the two new `_Hom_` methods, one in chain_complex.py and one in simplicial_complex.py.  

I just looked at those, and this sounds good. I am setting the positive review back. Thanks!

> And then there is the issue of whether it plays well with the new category stuff...

At first sight, it should work smoothly.

For the record: in the new category code, when a category is passed as optional argument, it's done as `category=...` rather than `cat=...`. I just checked, and this should not be an issue for _Hom_. You may want to change this for consistency though, now or later.


---

Comment by jhpalmieri created at 2009-11-17 20:44:06

I'll put up a new patch in just a minute.  (I was just imitating the code in rings/number_field/number_field.py and structure/parent.pyx, two places where I found pre-existing `_Hom_` methods.)


---

Comment by nthiery created at 2009-11-17 23:28:49

Replying to [comment:15 jhpalmieri]:
> I'll put up a new patch in just a minute.

Thanks!

> (I was just imitating the code in rings/number_field/number_field.py and structure/parent.pyx, two places where I found pre-existing `_Hom_` methods.)

Yup, you had no chance to guess otherwise. This part is seriously missing documentation.


---

Comment by jhpalmieri created at 2009-11-24 19:46:51

rebased version of patch. apply only this file.


---

Comment by mhansen created at 2009-11-29 04:55:49

Resolution: fixed


---

Attachment
