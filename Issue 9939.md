# Issue 9939: Fix CHomP-related doctest errors

archive/issues_009939.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nCC:  @jhpalmieri @rbeezer @loefflerd @novoselt @vbraun\n\nWith the optional CHomP package in 4.5.3 on sage.math, I get some doctest failures:\n\n```python\nsage -t -long -only-optional=chomp \"devel/sage/sage/homology/cell_complex.py\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3-chomp/devel/sage/sage/homology/cell_complex.py\", line 470:\n    sage: S2.homology(dim=2, generators=True)  # optional - CHomP\nExpected:\n    (Z, [(0, 1, 2) - (0, 1, 3) + (0, 2, 3) - (1, 2, 3)])\nGot:\n    (Z, [-(0, 1, 2) + (0, 1, 3) - (0, 2, 3) + (1, 2, 3)])\n```\n\nThese vary from run to run:\n\n```python\nsage -t -long -only-optional=chomp \"devel/sage/sage/homology/tests.py\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3-chomp/devel/sage/sage/homology/tests.py\", line 10:\n    sage: test_random_chain_complex(trials=20)  # optional - CHomP\nExpected nothing\nGot:\n    Homology in dimension 4 according to CHomP: C11\n    Homology in dimension 4 according to Sage: C11\n    Chain complex: {4: [], 5: 27 x 29 dense matrix over Integer Ring}\n    Random testing has revealed a problem in test_random_chain_complex\n    Please report this bug!  You may be the first\n    person in the world to have seen this problem.\n    Please include this random seed in your bug report:\n    Random seed: 53567958912087940719696565588289296809\n    ValueError()\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3-chomp/devel/sage/sage/homology/tests.py\", line 11:\n    sage: test_random_chain_complex(level=2, trials=20)  # optional - CHomP\nExpected nothing\nGot:\n    Homology in dimension 36 according to CHomP: 0\n    Homology in dimension 36 according to Sage: 0\n    Chain complex: {36: 58 x 37 sparse matrix over Integer Ring, 37: 0 x 58 dense matrix over Integer Ring}   \n    Random testing has revealed a problem in test_random_chain_complex\n    Please report this bug!  You may be the first\n    person in the world to have seen this problem.\n    Please include this random seed in your bug report:\n    Random seed: 194608326129552863405536402610270411271\n    ValueError()\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3-chomp/devel/sage/sage/homology/tests.py\", line 12:\n    sage: test_random_chain_complex(level=4, trials=20)  # long time # optional - CHomP\nExpected nothing\nGot:\n    Homology in dimension 125 according to CHomP: Z^56\n    Homology in dimension 125 according to Sage: Z^56\n    Chain complex: {125: 0 x 173 dense matrix over Integer Ring, 126: 173 x 117 dense matrix over Integer Ring}\n    Random testing has revealed a problem in test_random_chain_complex\n    Please report this bug!  You may be the first\n    person in the world to have seen this problem.\n    Please include this random seed in your bug report:\n    Random seed: 35064267617427002531027772896998931605\n    ValueError()\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3-chomp/devel/sage/sage/homology/tests.py\", line 72:\n    sage: test_random_chain_complex(trials=2)  # optional - CHomP\nExpected nothing\nGot:\n    Homology in dimension -43 according to CHomP: 0\n    Homology in dimension -43 according to Sage: 0\n    Chain complex: {-43: 41 x 0 dense matrix over Integer Ring, -42: []}\n    Random testing has revealed a problem in test_random_chain_complex\n    Please report this bug!  You may be the first\n    person in the world to have seen this problem.\n    Please include this random seed in your bug report:\n    Random seed: 198276055669197070047963781696502632135\n    ValueError()\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9940\n\n",
    "created_at": "2010-09-18T08:29:30Z",
    "labels": [
        "component: algebraic topology",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Fix CHomP-related doctest errors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9939",
    "user": "https://github.com/qed777"
}
```
Assignee: @jhpalmieri

CC:  @jhpalmieri @rbeezer @loefflerd @novoselt @vbraun

With the optional CHomP package in 4.5.3 on sage.math, I get some doctest failures:

```python
sage -t -long -only-optional=chomp "devel/sage/sage/homology/cell_complex.py"
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3-chomp/devel/sage/sage/homology/cell_complex.py", line 470:
    sage: S2.homology(dim=2, generators=True)  # optional - CHomP
Expected:
    (Z, [(0, 1, 2) - (0, 1, 3) + (0, 2, 3) - (1, 2, 3)])
Got:
    (Z, [-(0, 1, 2) + (0, 1, 3) - (0, 2, 3) + (1, 2, 3)])
```

These vary from run to run:

```python
sage -t -long -only-optional=chomp "devel/sage/sage/homology/tests.py"
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3-chomp/devel/sage/sage/homology/tests.py", line 10:
    sage: test_random_chain_complex(trials=20)  # optional - CHomP
Expected nothing
Got:
    Homology in dimension 4 according to CHomP: C11
    Homology in dimension 4 according to Sage: C11
    Chain complex: {4: [], 5: 27 x 29 dense matrix over Integer Ring}
    Random testing has revealed a problem in test_random_chain_complex
    Please report this bug!  You may be the first
    person in the world to have seen this problem.
    Please include this random seed in your bug report:
    Random seed: 53567958912087940719696565588289296809
    ValueError()
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3-chomp/devel/sage/sage/homology/tests.py", line 11:
    sage: test_random_chain_complex(level=2, trials=20)  # optional - CHomP
Expected nothing
Got:
    Homology in dimension 36 according to CHomP: 0
    Homology in dimension 36 according to Sage: 0
    Chain complex: {36: 58 x 37 sparse matrix over Integer Ring, 37: 0 x 58 dense matrix over Integer Ring}   
    Random testing has revealed a problem in test_random_chain_complex
    Please report this bug!  You may be the first
    person in the world to have seen this problem.
    Please include this random seed in your bug report:
    Random seed: 194608326129552863405536402610270411271
    ValueError()
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3-chomp/devel/sage/sage/homology/tests.py", line 12:
    sage: test_random_chain_complex(level=4, trials=20)  # long time # optional - CHomP
Expected nothing
Got:
    Homology in dimension 125 according to CHomP: Z^56
    Homology in dimension 125 according to Sage: Z^56
    Chain complex: {125: 0 x 173 dense matrix over Integer Ring, 126: 173 x 117 dense matrix over Integer Ring}
    Random testing has revealed a problem in test_random_chain_complex
    Please report this bug!  You may be the first
    person in the world to have seen this problem.
    Please include this random seed in your bug report:
    Random seed: 35064267617427002531027772896998931605
    ValueError()
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3-chomp/devel/sage/sage/homology/tests.py", line 72:
    sage: test_random_chain_complex(trials=2)  # optional - CHomP
Expected nothing
Got:
    Homology in dimension -43 according to CHomP: 0
    Homology in dimension -43 according to Sage: 0
    Chain complex: {-43: 41 x 0 dense matrix over Integer Ring, -42: []}
    Random testing has revealed a problem in test_random_chain_complex
    Please report this bug!  You may be the first
    person in the world to have seen this problem.
    Please include this random seed in your bug report:
    Random seed: 198276055669197070047963781696502632135
    ValueError()
```


Issue created by migration from https://trac.sagemath.org/ticket/9940





---

archive/issue_comments_098786.json:
```json
{
    "body": "I think we could fix the doctest failures by changing `A != B` to `not A == B`, because very brief testing suggests that `==` works for these objects, but that wouldn't fix the underlying issue.",
    "created_at": "2010-09-18T17:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98786",
    "user": "https://github.com/jhpalmieri"
}
```

I think we could fix the doctest failures by changing `A != B` to `not A == B`, because very brief testing suggests that `==` works for these objects, but that wouldn't fix the underlying issue.



---

archive/issue_comments_098787.json:
```json
{
    "body": "Changing assignee from @jhpalmieri to joyner.",
    "created_at": "2010-09-18T17:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98787",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from @jhpalmieri to joyner.



---

archive/issue_comments_098788.json:
```json
{
    "body": "Changing component from algebraic topology to group theory.",
    "created_at": "2010-09-18T17:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98788",
    "user": "https://github.com/jhpalmieri"
}
```

Changing component from algebraic topology to group theory.



---

archive/issue_comments_098789.json:
```json
{
    "body": "Adding a couple names of people who know this part well.",
    "created_at": "2010-09-19T01:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98789",
    "user": "https://github.com/kcrisman"
}
```

Adding a couple names of people who know this part well.



---

archive/issue_comments_098790.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-10-27T17:51:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98790",
    "user": "https://github.com/jhpalmieri"
}
```

Changing priority from major to critical.



---

archive/issue_comments_098791.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-19T17:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98791",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098792.json:
```json
{
    "body": "Here is a very simple patch.  With this, all doctests pass on sage.math (so this doesn't appear to break anything) and also \n\n```\nsage -t -long -only-optional=chomp \"devel/sage/sage/homology/tests.py\"\n```\n\npasses.\n\nI don't know enough about the additive abelian group code to know if this is completely safe.  I don't know why it wouldn't be, but could someone who knows what they're doing look at this?",
    "created_at": "2010-11-19T17:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98792",
    "user": "https://github.com/jhpalmieri"
}
```

Here is a very simple patch.  With this, all doctests pass on sage.math (so this doesn't appear to break anything) and also 

```
sage -t -long -only-optional=chomp "devel/sage/sage/homology/tests.py"
```

passes.

I don't know enough about the additive abelian group code to know if this is completely safe.  I don't know why it wouldn't be, but could someone who knows what they're doing look at this?



---

archive/issue_comments_098793.json:
```json
{
    "body": "It seems that other comparisons are not working properly either,\n\n\n```\nsage: G=AdditiveAbelianGroup([0,0])\nsage: H=AdditiveAbelianGroup([0,0])\nsage: G==H\nTrue\nsage: G!=H\nTrue\nsage: G<=H\nTrue\nsage: H<=G\nFalse\n```\n\n\n`AdditiveAbelianGroup` is implemented as a quotient of finitely-generated modules over ZZ, V/W, and you can get these two modules as follows:\n\n\n```\nsage: G._V\nAmbient free module of rank 2 over the principal ideal domain Integer Ring\nsage: G._W\nFree module of degree 2 and rank 0 over Integer Ring\nEchelon basis matrix:\n[]\n```\n\n\nThe equality of G and H is determined by the `__eq__` method in `sage.modules.fg_pid.fgp_module.FGP_Module_class` which does the obvious thing, checking the equality of the V and W modules.\n\nI cannot seem to figure out how the \"non-equality\" comparison is accomplished.  I get the impression this could be the logical negation of the equality comparison, automatically, but inserting print statements various places does not verify that hypothesis.\n\nIf I rebuild the quotient of modules from the relevant pieces of G and H, then equality and non-equality both behave as expected.\n\n\n```\nsage: X=sage.modules.fg_pid.fgp_module.FGP_Module(G._V, G._W)\nsage: Y=sage.modules.fg_pid.fgp_module.FGP_Module(H._V, H._W)\nsage: X==Y\nTrue\nsage: X!=Y\nFalse\n```\n\n\nSo I am at a bit of a loss to understand what is broken in the non-equality of G and H.  But still, a suggestion.  Since equality is implemented in the FGP_Module class, maybe the non-equality, as just the logical opposite, should be implemented at the same level?  In other words, use the same logic as in the patch, but place it as\n`sage.modules.fg_pid.fgp_module.FGP_Module_class.__ne__`?  Does that make sense?",
    "created_at": "2010-11-26T23:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98793",
    "user": "https://github.com/rbeezer"
}
```

It seems that other comparisons are not working properly either,


```
sage: G=AdditiveAbelianGroup([0,0])
sage: H=AdditiveAbelianGroup([0,0])
sage: G==H
True
sage: G!=H
True
sage: G<=H
True
sage: H<=G
False
```


`AdditiveAbelianGroup` is implemented as a quotient of finitely-generated modules over ZZ, V/W, and you can get these two modules as follows:


```
sage: G._V
Ambient free module of rank 2 over the principal ideal domain Integer Ring
sage: G._W
Free module of degree 2 and rank 0 over Integer Ring
Echelon basis matrix:
[]
```


The equality of G and H is determined by the `__eq__` method in `sage.modules.fg_pid.fgp_module.FGP_Module_class` which does the obvious thing, checking the equality of the V and W modules.

I cannot seem to figure out how the "non-equality" comparison is accomplished.  I get the impression this could be the logical negation of the equality comparison, automatically, but inserting print statements various places does not verify that hypothesis.

If I rebuild the quotient of modules from the relevant pieces of G and H, then equality and non-equality both behave as expected.


```
sage: X=sage.modules.fg_pid.fgp_module.FGP_Module(G._V, G._W)
sage: Y=sage.modules.fg_pid.fgp_module.FGP_Module(H._V, H._W)
sage: X==Y
True
sage: X!=Y
False
```


So I am at a bit of a loss to understand what is broken in the non-equality of G and H.  But still, a suggestion.  Since equality is implemented in the FGP_Module class, maybe the non-equality, as just the logical opposite, should be implemented at the same level?  In other words, use the same logic as in the patch, but place it as
`sage.modules.fg_pid.fgp_module.FGP_Module_class.__ne__`?  Does that make sense?



---

archive/issue_comments_098794.json:
```json
{
    "body": "Replying to [comment:7 rbeezer]:\n> So I am at a bit of a loss to understand what is broken in the non-equality of G and H.  \n\nMe too.\n\n> But still, a suggestion.  Since equality is implemented in the FGP_Module class, maybe the non-equality, as just the logical opposite, should be implemented at the same level?  In other words, use the same logic as in the patch, but place it as\n> `sage.modules.fg_pid.fgp_module.FGP_Module_class.__ne__`?  Does that make sense?\n\nIt sort of makes sense, and it seems to fix the nonequality problem, but since nonequality already works for these modules, it doesn't seem perfect.  It also doesn't affect the problems with < and >:\n\n```\nsage: G=AdditiveAbelianGroup([0,0])\nsage: H=AdditiveAbelianGroup([0,0])\nsage: G < H\nTrue\nsage: H < G\nFalse\n```\n\nI would really like to understand what's going on here.  I won't be completely happy with a patch until then, I think.",
    "created_at": "2010-11-27T21:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98794",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:7 rbeezer]:
> So I am at a bit of a loss to understand what is broken in the non-equality of G and H.  

Me too.

> But still, a suggestion.  Since equality is implemented in the FGP_Module class, maybe the non-equality, as just the logical opposite, should be implemented at the same level?  In other words, use the same logic as in the patch, but place it as
> `sage.modules.fg_pid.fgp_module.FGP_Module_class.__ne__`?  Does that make sense?

It sort of makes sense, and it seems to fix the nonequality problem, but since nonequality already works for these modules, it doesn't seem perfect.  It also doesn't affect the problems with < and >:

```
sage: G=AdditiveAbelianGroup([0,0])
sage: H=AdditiveAbelianGroup([0,0])
sage: G < H
True
sage: H < G
False
```

I would really like to understand what's going on here.  I won't be completely happy with a patch until then, I think.



---

archive/issue_comments_098795.json:
```json
{
    "body": "Replying to [comment:8 jhpalmieri]:\n> I would really like to understand what's going on here.  I won't be completely happy with a patch until then, I think.\n\nMe too.  I think we see it the same way.  My guess is that I don't totally understand some corner of Python (rather than not understanding Sage).  \n\nShould we appeal to sage-devel for some insight?  I'm happy to compose something, probably after posting some more evidence of my confusion here on the ticket.  Can I use your name too to make a stronger case for this not being a newbie FAQ?  \n\nRob",
    "created_at": "2010-11-27T23:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98795",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:8 jhpalmieri]:
> I would really like to understand what's going on here.  I won't be completely happy with a patch until then, I think.

Me too.  I think we see it the same way.  My guess is that I don't totally understand some corner of Python (rather than not understanding Sage).  

Should we appeal to sage-devel for some insight?  I'm happy to compose something, probably after posting some more evidence of my confusion here on the ticket.  Can I use your name too to make a stronger case for this not being a newbie FAQ?  

Rob



---

archive/issue_comments_098796.json:
```json
{
    "body": "OK, just popped into sage-devel and see its done............  ;-)\n\nRob",
    "created_at": "2010-11-27T23:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98796",
    "user": "https://github.com/rbeezer"
}
```

OK, just popped into sage-devel and see its done............  ;-)

Rob



---

archive/issue_comments_098797.json:
```json
{
    "body": "I'm not sure if this helps, but [this documentation about rich comparisons](http://docs.python.org/reference/datamodel.html#object.__ne__) says\n\n  There are no implied relationships among the comparison operators. The truth of `x==y` does not imply that `x!=y` is false. Accordingly, when defining `__eq__()`, one should also define `__ne__()` so that the operators will behave as expected.\n\nThe [entry for __cmp__](http://docs.python.org/reference/datamodel.html#object.__cmp__) says\n\n  If no `__cmp__()`, `__eq__()` or `__ne__()` operation is defined, class instances are compared by object identity (\"address\").\n\nDoes not having defined `sage.modules.fg_pid.fgp_module.FGP_Module_class.__ne__` mean that `G != H` amounts to `id(G) != id(H)`?\n\nIt seems the only other class that derives [directly] from `FGP_Module_class` is `sage.geometry.toric_lattice.ToricLattice_quotient`, which also doesn't define its own `__eq__` and `__ne__`:\n\n```python\nsage: N1 = ToricLattice(3)\nsage: sublattice1 = N1.submodule([(1,1,0), (3,2,1)])\nsage: Q1 = N1/sublattice1\nsage: N2 = ToricLattice(3)\nsage: sublattice2 = N2.submodule([(1,1,0), (3,2,1)])\nsage: Q2 = N2/sublattice2\nsage: Q1 == Q2\nTrue\nsage: Q1 != Q2\nTrue\n```\n\nIs this expected?",
    "created_at": "2010-11-28T03:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98797",
    "user": "https://github.com/qed777"
}
```

I'm not sure if this helps, but [this documentation about rich comparisons](http://docs.python.org/reference/datamodel.html#object.__ne__) says

  There are no implied relationships among the comparison operators. The truth of `x==y` does not imply that `x!=y` is false. Accordingly, when defining `__eq__()`, one should also define `__ne__()` so that the operators will behave as expected.

The [entry for __cmp__](http://docs.python.org/reference/datamodel.html#object.__cmp__) says

  If no `__cmp__()`, `__eq__()` or `__ne__()` operation is defined, class instances are compared by object identity ("address").

Does not having defined `sage.modules.fg_pid.fgp_module.FGP_Module_class.__ne__` mean that `G != H` amounts to `id(G) != id(H)`?

It seems the only other class that derives [directly] from `FGP_Module_class` is `sage.geometry.toric_lattice.ToricLattice_quotient`, which also doesn't define its own `__eq__` and `__ne__`:

```python
sage: N1 = ToricLattice(3)
sage: sublattice1 = N1.submodule([(1,1,0), (3,2,1)])
sage: Q1 = N1/sublattice1
sage: N2 = ToricLattice(3)
sage: sublattice2 = N2.submodule([(1,1,0), (3,2,1)])
sage: Q2 = N2/sublattice2
sage: Q1 == Q2
True
sage: Q1 != Q2
True
```

Is this expected?



---

archive/issue_comments_098798.json:
```json
{
    "body": "Replying to [comment:11 mpatel]:\n> It seems the only other class that derives [directly] from `FGP_Module_class` is `sage.geometry.toric_lattice.ToricLattice_quotient`, which also doesn't define its own `__eq__` and `__ne__`:\n\n```python\nsage: N1 = ToricLattice(3)\nsage: sublattice1 = N1.submodule([(1,1,0), (3,2,1)])\nsage: Q1 = N1/sublattice1\nsage: N2 = ToricLattice(3)\nsage: sublattice2 = N2.submodule([(1,1,0), (3,2,1)])\nsage: Q2 = N2/sublattice2\nsage: Q1 == Q2\nTrue\nsage: Q1 != Q2\nTrue\n```\n\n> Is this expected?\n\nI think what I find the most confusing is that comparisons work well for finitely generated free modules, but not for the derived classes.  If they behaved badly in all cases, I would know how to fix it, and while adding a `__ne__` method for `FGP_Module_class` (and perhaps `__lt__` and `__gt__` methods, although I'm not sure what they should return: I suppose `self.is_submodule(other) and self != other`) would probably make the comparisons work, I still wouldn't understand why that was the right place to do it.\n\nSo one question is, is the right thing to do to add methods `__ne__`, `__lt__`, and `__gt__`, and perhaps `__ge__` and `__le__`, to `FGP_Module_class`?\n\nI'm marking this as \"needs work\", because we should address comparisons like `H<G` at the same time as `H!=G`.",
    "created_at": "2010-11-28T04:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98798",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:11 mpatel]:
> It seems the only other class that derives [directly] from `FGP_Module_class` is `sage.geometry.toric_lattice.ToricLattice_quotient`, which also doesn't define its own `__eq__` and `__ne__`:

```python
sage: N1 = ToricLattice(3)
sage: sublattice1 = N1.submodule([(1,1,0), (3,2,1)])
sage: Q1 = N1/sublattice1
sage: N2 = ToricLattice(3)
sage: sublattice2 = N2.submodule([(1,1,0), (3,2,1)])
sage: Q2 = N2/sublattice2
sage: Q1 == Q2
True
sage: Q1 != Q2
True
```

> Is this expected?

I think what I find the most confusing is that comparisons work well for finitely generated free modules, but not for the derived classes.  If they behaved badly in all cases, I would know how to fix it, and while adding a `__ne__` method for `FGP_Module_class` (and perhaps `__lt__` and `__gt__` methods, although I'm not sure what they should return: I suppose `self.is_submodule(other) and self != other`) would probably make the comparisons work, I still wouldn't understand why that was the right place to do it.

So one question is, is the right thing to do to add methods `__ne__`, `__lt__`, and `__gt__`, and perhaps `__ge__` and `__le__`, to `FGP_Module_class`?

I'm marking this as "needs work", because we should address comparisons like `H<G` at the same time as `H!=G`.



---

archive/issue_comments_098799.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-28T04:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98799",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_098800.json:
```json
{
    "body": "Replying to [comment:11 mpatel]:\n> Is this expected?\n\nNo, we derived separate classes for toric lattices and related objects to make sure that elements of different lattices of the same dimension don't mix in wrong ways (especially elements of dual lattices). Otherwise the behaviour is left the same as for base classes.",
    "created_at": "2010-11-28T04:32:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98800",
    "user": "https://github.com/novoselt"
}
```

Replying to [comment:11 mpatel]:
> Is this expected?

No, we derived separate classes for toric lattices and related objects to make sure that elements of different lattices of the same dimension don't mix in wrong ways (especially elements of dual lattices). Otherwise the behaviour is left the same as for base classes.



---

archive/issue_comments_098801.json:
```json
{
    "body": "Oh, I see: `FGP_Module` is a **function** which returns identical objects (via the `__init__` method of `FGP_Module_class`) if you pass it the same input.  If you do this:\n\n```\nsage: G=AdditiveAbelianGroup([0,0])\nsage: from sage.modules.fg_pid.fgp_module import FGP_Module_class\nsage: M1 = FGP_Module_class(G.V(), G.W())\nsage: M2 = FGP_Module_class(G.V(), G.W())\nsage: M1 == M2\nTrue\nsage: M1 != M2\nTrue\nsage: M1 < M2\nTrue\nsage: M1 > M2\nFalse\n```\n\nSo adding these comparisons to `FGP_Module_class` might be the right thing to do, to deal with the case when people construct these modules without using the helper function `FGP_Module`, using the class instead.",
    "created_at": "2010-11-28T04:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98801",
    "user": "https://github.com/jhpalmieri"
}
```

Oh, I see: `FGP_Module` is a **function** which returns identical objects (via the `__init__` method of `FGP_Module_class`) if you pass it the same input.  If you do this:

```
sage: G=AdditiveAbelianGroup([0,0])
sage: from sage.modules.fg_pid.fgp_module import FGP_Module_class
sage: M1 = FGP_Module_class(G.V(), G.W())
sage: M2 = FGP_Module_class(G.V(), G.W())
sage: M1 == M2
True
sage: M1 != M2
True
sage: M1 < M2
True
sage: M1 > M2
False
```

So adding these comparisons to `FGP_Module_class` might be the right thing to do, to deal with the case when people construct these modules without using the helper function `FGP_Module`, using the class instead.



---

archive/issue_comments_098802.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-28T05:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98802",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098803.json:
```json
{
    "body": "Here's a patch.",
    "created_at": "2010-11-28T05:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98803",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a patch.



---

archive/issue_comments_098804.json:
```json
{
    "body": "Attachment [trac_9940-ne.patch](tarball://root/attachments/some-uuid/ticket9940/trac_9940-ne.patch) by @rbeezer created at 2010-11-28 20:28:24\n\nI think implementing less-than, etc as submodule tests is the right way to go as well.\n\nPatch passes all long tests, and with the experimental package `chomp` installed, patched version also passes:\n\n\n```\nsage -t -long -only-optional=chomp \"devel/sage/sage/homology/tests.py\"\n```\n\n\nI also installed the (in-progress) patch at #9773 which builds finitely-generated groups on top of this module quotient code.  Limited testing indicates that (a) the current patch behaves as expected, and (b) the comparison methods will apply properly to the subclasses.\n\nDocumentation looks good when previewed in the notebook (since it is not included in the reference manual).\n\nSo: positive review.  Thanks, John, for pursuing this one.\n\nRob",
    "created_at": "2010-11-28T20:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98804",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9940-ne.patch](tarball://root/attachments/some-uuid/ticket9940/trac_9940-ne.patch) by @rbeezer created at 2010-11-28 20:28:24

I think implementing less-than, etc as submodule tests is the right way to go as well.

Patch passes all long tests, and with the experimental package `chomp` installed, patched version also passes:


```
sage -t -long -only-optional=chomp "devel/sage/sage/homology/tests.py"
```


I also installed the (in-progress) patch at #9773 which builds finitely-generated groups on top of this module quotient code.  Limited testing indicates that (a) the current patch behaves as expected, and (b) the comparison methods will apply properly to the subclasses.

Documentation looks good when previewed in the notebook (since it is not included in the reference manual).

So: positive review.  Thanks, John, for pursuing this one.

Rob



---

archive/issue_comments_098805.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-28T20:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98805",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098806.json:
```json
{
    "body": "Replying to [comment:16 rbeezer]:\n> So: positive review.  Thanks, John, for pursuing this one.\n\nWell, I was helped a lot by Mitesh's pointer to the Python docs for `__cmp__`.",
    "created_at": "2010-11-29T04:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98806",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:16 rbeezer]:
> So: positive review.  Thanks, John, for pursuing this one.

Well, I was helped a lot by Mitesh's pointer to the Python docs for `__cmp__`.



---

archive/issue_events_010066.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2010-12-02T16:09:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9939#event-10066"
}
```



---

archive/issue_comments_098807.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-12-02T16:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9939#issuecomment-98807",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
