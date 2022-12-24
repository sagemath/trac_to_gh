# Issue 6099: morphisms of simplicial complexes and the associated chain complex morphisms

archive/issues_006099.json:
```json
{
    "body": "Assignee: bantieau\n\nCC:  jhpalmieri\n\nAdd functionality to sage to create morphisms between simplicial complexes, and to associate to these morphisms the chain complex maps on the homological and cohomological chain complexes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6099\n\n",
    "created_at": "2009-05-21T03:37:46Z",
    "labels": [
        "algebraic topology",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "morphisms of simplicial complexes and the associated chain complex morphisms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6099",
    "user": "bantieau"
}
```
Assignee: bantieau

CC:  jhpalmieri

Add functionality to sage to create morphisms between simplicial complexes, and to associate to these morphisms the chain complex maps on the homological and cohomological chain complexes.

Issue created by migration from https://trac.sagemath.org/ticket/6099





---

archive/issue_comments_048634.json:
```json
{
    "body": "Attachment [12335.patch](tarball://root/attachments/some-uuid/ticket6099/12335.patch) by bantieau created at 2009-06-01 23:10:24\n\nThis patch implements the chain complex morphisms part of this trac ticket.",
    "created_at": "2009-06-01T23:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48634",
    "user": "bantieau"
}
```

Attachment [12335.patch](tarball://root/attachments/some-uuid/ticket6099/12335.patch) by bantieau created at 2009-06-01 23:10:24

This patch implements the chain complex morphisms part of this trac ticket.



---

archive/issue_comments_048635.json:
```json
{
    "body": "Attachment [6099-1.patch](tarball://root/attachments/some-uuid/ticket6099/6099-1.patch) by bantieau created at 2009-06-01 23:14:34\n\nThis patch implements the chain complex morphisms part of this trac ticket.",
    "created_at": "2009-06-01T23:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48635",
    "user": "bantieau"
}
```

Attachment [6099-1.patch](tarball://root/attachments/some-uuid/ticket6099/6099-1.patch) by bantieau created at 2009-06-01 23:14:34

This patch implements the chain complex morphisms part of this trac ticket.



---

archive/issue_comments_048636.json:
```json
{
    "body": "Ignore 12335.patch. I would take it off, but I do not know how.",
    "created_at": "2009-06-01T23:15:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48636",
    "user": "bantieau"
}
```

Ignore 12335.patch. I would take it off, but I do not know how.



---

archive/issue_comments_048637.json:
```json
{
    "body": "Attachment [6099-2.patch](tarball://root/attachments/some-uuid/ticket6099/6099-2.patch) by bantieau created at 2009-06-16 06:21:12",
    "created_at": "2009-06-16T06:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48637",
    "user": "bantieau"
}
```

Attachment [6099-2.patch](tarball://root/attachments/some-uuid/ticket6099/6099-2.patch) by bantieau created at 2009-06-16 06:21:12



---

archive/issue_comments_048638.json:
```json
{
    "body": "Attachment [6099-3.patch](tarball://root/attachments/some-uuid/ticket6099/6099-3.patch) by bantieau created at 2009-06-17 00:50:46\n\ntweak to be compatibe with #6141, which changes facets to facets().",
    "created_at": "2009-06-17T00:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48638",
    "user": "bantieau"
}
```

Attachment [6099-3.patch](tarball://root/attachments/some-uuid/ticket6099/6099-3.patch) by bantieau created at 2009-06-17 00:50:46

tweak to be compatibe with #6141, which changes facets to facets().



---

archive/issue_comments_048639.json:
```json
{
    "body": "It's great that you're working on this.  It looks very good, but there are a few issues:\n\n- in the docstring for effective_vertices, you might mention that it returns a Simplex.  The docstring could start \"The set of vertices belonging to some face, as a simplex\", and you could also put in a doctest like\n\n```\nsage: type(S.effective_vertices())\n<class 'sage.homology.simplicial_complex.Simplex'>\n```\n\n\n- I had a few doctest failures which I think are fixed in #6309 (two extra periods), but they should be fixed here.\n\n- Is it a good idea to have `domain` and `codomain` methods for morphisms?  I can imagine someone wanting to use the domain of the fiber product, for example, but they won't see the `_domain` attribute on tab completion.\n\n- You don't have 100% documentation and doctest coverage.  Type 'sage -coverage ...insert_path_here.../sage/homology' to get a summary.  When you do this, note that messages like\n {{{\n Possibly wrong (function name doesn't occur in doctests):\n* _repr_(self):\n }}}\n can be avoided if you add \"# indirect doctest\", like this:\n {{{\n            sage: x = i.associated_chain_complex_morphism()\n            sage: x # indirect doctest\n }}}\n\n- Should \"product\" be renamed \"fiber_product\" so it's less ambiguous?\n\n- I wonder if `ChainComplexMorphism` should inherit from `ModuleElement` rather than `SageObject`.  Then you would define a method `_mul_` (rather than `__mul__`), and similarly for `_add_`, and you could also define `_lmul_` and `_rmul_` to deal with scalar multiplication.  Check the Sage reference manual, the \"Coercion\" section.  (This section is newly added to the reference manual, as of Sage 4.0.1 or 4.0.2, I think.)\n\n- I'm attaching a small patch which adds the new files to the reference manual.  (This involves editing one file, doc/en/reference/homology.rst, and also because of the way reST works, I had to change \n {{{ \n- D. Benjamin Antieau <d.ben.antieau`@`gmail.com> (2009.06)\n }}}\n to \n {{{\n- \\D. Benjamin Antieau <d.ben.antieau`@`gmail.com> (2009.06)\n }}}\n (The \"D.\" at essentially the beginning of the line seemed to tell Sphinx that this was part of a numbered list, starting with number 4.)  Feel free to incorporate my changes and produce one single patch which does everything here.",
    "created_at": "2009-06-17T18:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48639",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_048640.json:
```json
{
    "body": "Attachment [ref_6099.patch](tarball://root/attachments/some-uuid/ticket6099/ref_6099.patch) by jhpalmieri created at 2009-06-17 18:19:40",
    "created_at": "2009-06-17T18:19:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48640",
    "user": "jhpalmieri"
}
```

Attachment [ref_6099.patch](tarball://root/attachments/some-uuid/ticket6099/ref_6099.patch) by jhpalmieri created at 2009-06-17 18:19:40



---

archive/issue_comments_048641.json:
```json
{
    "body": "Hopefully final merged patch.",
    "created_at": "2009-11-06T21:18:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48641",
    "user": "bantieau"
}
```

Hopefully final merged patch.



---

archive/issue_comments_048642.json:
```json
{
    "body": "Attachment [6099-merged.patch](tarball://root/attachments/some-uuid/ticket6099/6099-merged.patch) by bantieau created at 2009-11-06 21:20:28\n\nOK. I've uploaded a patch that includes all of the patches above, and also includes all of your recommendations, except for inheriting from ModuleElement. Perhaps that can be another ticket, if someone wants that. Coverage and doctest are %100.",
    "created_at": "2009-11-06T21:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48642",
    "user": "bantieau"
}
```

Attachment [6099-merged.patch](tarball://root/attachments/some-uuid/ticket6099/6099-merged.patch) by bantieau created at 2009-11-06 21:20:28

OK. I've uploaded a patch that includes all of the patches above, and also includes all of your recommendations, except for inheriting from ModuleElement. Perhaps that can be another ticket, if someone wants that. Coverage and doctest are %100.



---

archive/issue_comments_048643.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-06T21:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48643",
    "user": "bantieau"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_048644.json:
```json
{
    "body": "This is almost done.  I'm attaching a patch making a few changes.  First, in homology.rst, it should say `sage/homology/chain_complex_homspace` (it has \"homset\" instead of \"homspace\").  Also, I think that in category_types.py, the entry for chain complexes should say:\n\n```\n    ChainComplexes         : [RingModules, AbelianGroups, Sets],\\\n```\n\nAlso, I've changed the `__mul__` method for maps of chain complexes so that when the right-hand factor is a ring element, it gets multiplied on the right, not the left (in case we ever work over noncommutative rings).  I've also added an `__rmul__` method for multiplying on the left by a ring element.  I changed the string representation for chain complexes so it doesn't have a period at the end, so that your string representations for chain maps look better.\n\nFinally, the only major problem: my patch fixes an issue with converting maps of simplicial complexes to maps of chain complexes:\n\n```\nsage: X = SimplicialComplex(1, [[0,1]]); X\nSimplicial complex with vertex set (0, 1) and facets {(0, 1)}\nsage: H = Hom(X, X)\nsage: f = H({0:1, 1:0})\nsage: f.associated_chain_complex_morphism()\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/Users/palmieri/.sage/temp/jpalmieri538.local/84693/_Users_palmieri__sage_init_sage_0.py in <module>()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/homology/simplicial_complex_morphism.pyc in associated_chain_complex_morphism(self, base_ring, augmented, cochain)\n    322             return ChainComplexMorphism(matrices,\\\n    323                     self._domain.chain_complex(base_ring=base_ring,augmented=augmented,cochain=cochain),\\\n--> 324                     self._codomain.chain_complex(base_ring=base_ring,augmented=augmented,cochain=cochain))\n    325         else:\n    326             return ChainComplexMorphism(matrices,\\\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/homology/chain_complex_morphism.pyc in __init__(self, matrices, C, D)\n    132                 if (i+1) in C.differential().keys() and (i+1) in D.differential().keys():\n    133                     if not matrices[i]*C.differential()[i+1]==D.differential()[i+1]*matrices[i+1]:\n--> 134                         raise ValueError, \"Matrices must define a chain complex morphism.\"\n    135                 elif (i+1) in C.differential().keys():\n    136                     if not matrices[i]*C.differential()[i+1].is_zero():\n\nValueError: Matrices must define a chain complex morphism.\n```\n\nThe issue is orientation: in the line\n\n```\n                    mval[X_faces.index(i)+(Y_faces.index(y)*num_faces_X)] = 1\n```\n\nin `associated_chain_complex_morphism`, the right side should be 1 or -1, depending on the orientation of y.\n\nI'm giving your patch a positive review.  If you're happy with my new patch, change the ticket to \"positive review\".",
    "created_at": "2009-11-10T22:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48644",
    "user": "jhpalmieri"
}
```

This is almost done.  I'm attaching a patch making a few changes.  First, in homology.rst, it should say `sage/homology/chain_complex_homspace` (it has "homset" instead of "homspace").  Also, I think that in category_types.py, the entry for chain complexes should say:

```
    ChainComplexes         : [RingModules, AbelianGroups, Sets],\
```

Also, I've changed the `__mul__` method for maps of chain complexes so that when the right-hand factor is a ring element, it gets multiplied on the right, not the left (in case we ever work over noncommutative rings).  I've also added an `__rmul__` method for multiplying on the left by a ring element.  I changed the string representation for chain complexes so it doesn't have a period at the end, so that your string representations for chain maps look better.

Finally, the only major problem: my patch fixes an issue with converting maps of simplicial complexes to maps of chain complexes:

```
sage: X = SimplicialComplex(1, [[0,1]]); X
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

archive/issue_comments_048645.json:
```json
{
    "body": "Attachment [trac_6099-part2.patch](tarball://root/attachments/some-uuid/ticket6099/trac_6099-part2.patch) by jhpalmieri created at 2009-11-10 23:38:12\n\napply on top of 6099-merged.patch",
    "created_at": "2009-11-10T23:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48645",
    "user": "jhpalmieri"
}
```

Attachment [trac_6099-part2.patch](tarball://root/attachments/some-uuid/ticket6099/trac_6099-part2.patch) by jhpalmieri created at 2009-11-10 23:38:12

apply on top of 6099-merged.patch



---

archive/issue_comments_048646.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-14T22:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48646",
    "user": "bantieau"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_048647.json:
```json
{
    "body": "Release manager: apply only 6099-merged.patch and trac_6099-part2.patch.",
    "created_at": "2009-11-14T22:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48647",
    "user": "bantieau"
}
```

Release manager: apply only 6099-merged.patch and trac_6099-part2.patch.



---

archive/issue_comments_048648.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T06:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48648",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_048649.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-11-17T14:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48649",
    "user": "mhansen"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_048650.json:
```json
{
    "body": "I had to back this out for now due to conflicts with the category code.  I'll look at readding this once those patches are merged.",
    "created_at": "2009-11-17T14:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48650",
    "user": "mhansen"
}
```

I had to back this out for now due to conflicts with the category code.  I'll look at readding this once those patches are merged.



---

archive/issue_comments_048651.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2009-11-17T14:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48651",
    "user": "mhansen"
}
```

Changing status from closed to new.



---

archive/issue_comments_048652.json:
```json
{
    "body": "Replying to [comment:8 mhansen]:\n> I had to back this out for now due to conflicts with the category code.  I'll look at readding this once those patches are merged.\n\n    Hi Benjamin,\n\nSorry for the conflict. Rebasing the patch should be fairly easy. I suspect that the change to category_types can simply be discarded. As for the change in homset.py: I have removed this ugly run time type checking there. Instead, Hom(X, Y) looks for a method X._Hom_, and calls it if it exists. This _Hom_ method could typically be implemented in ChainComplexes.ParentMethods to achieve the current effect.\n\nGood luck, and feel free to bug me.",
    "created_at": "2009-11-17T15:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48652",
    "user": "nthiery"
}
```

Replying to [comment:8 mhansen]:
> I had to back this out for now due to conflicts with the category code.  I'll look at readding this once those patches are merged.

    Hi Benjamin,

Sorry for the conflict. Rebasing the patch should be fairly easy. I suspect that the change to category_types can simply be discarded. As for the change in homset.py: I have removed this ugly run time type checking there. Instead, Hom(X, Y) looks for a method X._Hom_, and calls it if it exists. This _Hom_ method could typically be implemented in ChainComplexes.ParentMethods to achieve the current effect.

Good luck, and feel free to bug me.



---

archive/issue_comments_048653.json:
```json
{
    "body": "Replying to [comment:9 nthiery]:\n\n> Sorry for the conflict. Rebasing the patch should be fairly easy. I suspect that the change to category_types can simply be discarded. \n\nOkay, that's easy enough.\n\n>As for the change in homset.py: I have removed this ugly run time type checking there. Instead, Hom(X, Y) looks for a method X._Hom_, and calls it if it exists. This _Hom_ method could typically be implemented in ChainComplexes.ParentMethods to achieve the current effect.\n\nI'm not sure what `ChainComplexes.ParentMethods` means, but we can just define, within the class `ChainComplex`, a method `_Hom_(self, other)`, right?",
    "created_at": "2009-11-17T18:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48653",
    "user": "jhpalmieri"
}
```

Replying to [comment:9 nthiery]:

> Sorry for the conflict. Rebasing the patch should be fairly easy. I suspect that the change to category_types can simply be discarded. 

Okay, that's easy enough.

>As for the change in homset.py: I have removed this ugly run time type checking there. Instead, Hom(X, Y) looks for a method X._Hom_, and calls it if it exists. This _Hom_ method could typically be implemented in ChainComplexes.ParentMethods to achieve the current effect.

I'm not sure what `ChainComplexes.ParentMethods` means, but we can just define, within the class `ChainComplex`, a method `_Hom_(self, other)`, right?



---

archive/issue_comments_048654.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-17T20:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48654",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_048655.json:
```json
{
    "body": "Here's a rebased version.  This makes no changes to category_types.py or to categories/homset.py, instead implementing `_Hom_` methods for simplicial complexes and chain complexes.  With Sage 4.2.1, it applies cleanly and passes all tests.  If it still causes problems when merged, we'll probably have to wait until 4.3.alpha0 is released and work from there.",
    "created_at": "2009-11-17T20:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48655",
    "user": "jhpalmieri"
}
```

Here's a rebased version.  This makes no changes to category_types.py or to categories/homset.py, instead implementing `_Hom_` methods for simplicial complexes and chain complexes.  With Sage 4.2.1, it applies cleanly and passes all tests.  If it still causes problems when merged, we'll probably have to wait until 4.3.alpha0 is released and work from there.



---

archive/issue_comments_048656.json:
```json
{
    "body": "I guess the only parts that need review are the two new `_Hom_` methods, one in chain_complex.py and one in simplicial_complex.py.  And then there is the issue of whether it plays well with the new category stuff...",
    "created_at": "2009-11-17T20:25:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48656",
    "user": "jhpalmieri"
}
```

I guess the only parts that need review are the two new `_Hom_` methods, one in chain_complex.py and one in simplicial_complex.py.  And then there is the issue of whether it plays well with the new category stuff...



---

archive/issue_comments_048657.json:
```json
{
    "body": "Replying to [comment:10 jhpalmieri]:\n> >As for the change in homset.py: I have removed this ugly run time type checking there. Instead, Hom(X, Y) looks for a method X._Hom_, and calls it if it exists. This _Hom_ method could typically be implemented in ChainComplexes.ParentMethods to achieve the current effect.\n> \n> I'm not sure what `ChainComplexes.ParentMethods` means, but we can just define, within the class `ChainComplex`, a method `_Hom_(self, other)`, right?\n\nIndeed.\n\n`ChainComplexes.ParentMethods` is the class in the `ChainComplexes` category containing the generic code that applies to all parents in this category. That could be useful later on if there is more than one implementation of such parents. No rush for now.",
    "created_at": "2009-11-17T20:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48657",
    "user": "nthiery"
}
```

Replying to [comment:10 jhpalmieri]:
> >As for the change in homset.py: I have removed this ugly run time type checking there. Instead, Hom(X, Y) looks for a method X._Hom_, and calls it if it exists. This _Hom_ method could typically be implemented in ChainComplexes.ParentMethods to achieve the current effect.
> 
> I'm not sure what `ChainComplexes.ParentMethods` means, but we can just define, within the class `ChainComplex`, a method `_Hom_(self, other)`, right?

Indeed.

`ChainComplexes.ParentMethods` is the class in the `ChainComplexes` category containing the generic code that applies to all parents in this category. That could be useful later on if there is more than one implementation of such parents. No rush for now.



---

archive/issue_comments_048658.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-17T20:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48658",
    "user": "nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_048659.json:
```json
{
    "body": "Replying to [comment:12 jhpalmieri]:\n> I guess the only parts that need review are the two new `_Hom_` methods, one in chain_complex.py and one in simplicial_complex.py.  \n\nI just looked at those, and this sounds good. I am setting the positive review back. Thanks!\n\n> And then there is the issue of whether it plays well with the new category stuff...\n\nAt first sight, it should work smoothly.\n\nFor the record: in the new category code, when a category is passed as optional argument, it's done as `category=...` rather than `cat=...`. I just checked, and this should not be an issue for _Hom_. You may want to change this for consistency though, now or later.",
    "created_at": "2009-11-17T20:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48659",
    "user": "nthiery"
}
```

Replying to [comment:12 jhpalmieri]:
> I guess the only parts that need review are the two new `_Hom_` methods, one in chain_complex.py and one in simplicial_complex.py.  

I just looked at those, and this sounds good. I am setting the positive review back. Thanks!

> And then there is the issue of whether it plays well with the new category stuff...

At first sight, it should work smoothly.

For the record: in the new category code, when a category is passed as optional argument, it's done as `category=...` rather than `cat=...`. I just checked, and this should not be an issue for _Hom_. You may want to change this for consistency though, now or later.



---

archive/issue_comments_048660.json:
```json
{
    "body": "I'll put up a new patch in just a minute.  (I was just imitating the code in rings/number_field/number_field.py and structure/parent.pyx, two places where I found pre-existing `_Hom_` methods.)",
    "created_at": "2009-11-17T20:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48660",
    "user": "jhpalmieri"
}
```

I'll put up a new patch in just a minute.  (I was just imitating the code in rings/number_field/number_field.py and structure/parent.pyx, two places where I found pre-existing `_Hom_` methods.)



---

archive/issue_comments_048661.json:
```json
{
    "body": "Replying to [comment:15 jhpalmieri]:\n> I'll put up a new patch in just a minute.\n\nThanks!\n\n> (I was just imitating the code in rings/number_field/number_field.py and structure/parent.pyx, two places where I found pre-existing `_Hom_` methods.)\n\nYup, you had no chance to guess otherwise. This part is seriously missing documentation.",
    "created_at": "2009-11-17T23:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48661",
    "user": "nthiery"
}
```

Replying to [comment:15 jhpalmieri]:
> I'll put up a new patch in just a minute.

Thanks!

> (I was just imitating the code in rings/number_field/number_field.py and structure/parent.pyx, two places where I found pre-existing `_Hom_` methods.)

Yup, you had no chance to guess otherwise. This part is seriously missing documentation.



---

archive/issue_comments_048662.json:
```json
{
    "body": "rebased version of patch. apply only this file.",
    "created_at": "2009-11-24T19:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48662",
    "user": "jhpalmieri"
}
```

rebased version of patch. apply only this file.



---

archive/issue_comments_048663.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T04:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48663",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_048664.json:
```json
{
    "body": "Attachment [trac_6099-rebased.patch](tarball://root/attachments/some-uuid/ticket6099/trac_6099-rebased.patch) by mhansen created at 2009-11-29 04:55:49",
    "created_at": "2009-11-29T04:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6099#issuecomment-48664",
    "user": "mhansen"
}
```

Attachment [trac_6099-rebased.patch](tarball://root/attachments/some-uuid/ticket6099/trac_6099-rebased.patch) by mhansen created at 2009-11-29 04:55:49
