# Issue 9939: Fix CHomP-related doctest errors

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-09-18 08:29:30

Assignee: jhpalmieri

CC:  jhpalmieri rbeezer davidloeffler novoselt vbraun

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



---

Comment by jhpalmieri created at 2010-09-18 17:54:33

I think we could fix the doctest failures by changing `A != B` to `not A == B`, because very brief testing suggests that `==` works for these objects, but that wouldn't fix the underlying issue.


---

Comment by jhpalmieri created at 2010-09-18 17:54:46

Changing assignee from jhpalmieri to joyner.


---

Comment by jhpalmieri created at 2010-09-18 17:54:46

Changing component from algebraic topology to group theory.


---

Comment by kcrisman created at 2010-09-19 01:29:06

Adding a couple names of people who know this part well.


---

Comment by jhpalmieri created at 2010-10-27 17:51:00

Changing priority from major to critical.


---

Comment by jhpalmieri created at 2010-11-19 17:47:54

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-11-19 17:47:54

Here is a very simple patch.  With this, all doctests pass on sage.math (so this doesn't appear to break anything) and also 

```
sage -t -long -only-optional=chomp "devel/sage/sage/homology/tests.py"
```

passes.

I don't know enough about the additive abelian group code to know if this is completely safe.  I don't know why it wouldn't be, but could someone who knows what they're doing look at this?


---

Comment by rbeezer created at 2010-11-26 23:24:37

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

Comment by jhpalmieri created at 2010-11-27 21:04:05

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

Comment by rbeezer created at 2010-11-27 23:49:58

Replying to [comment:8 jhpalmieri]:
> I would really like to understand what's going on here.  I won't be completely happy with a patch until then, I think.

Me too.  I think we see it the same way.  My guess is that I don't totally understand some corner of Python (rather than not understanding Sage).  

Should we appeal to sage-devel for some insight?  I'm happy to compose something, probably after posting some more evidence of my confusion here on the ticket.  Can I use your name too to make a stronger case for this not being a newbie FAQ?  

Rob


---

Comment by rbeezer created at 2010-11-27 23:51:13

OK, just popped into sage-devel and see its done............  ;-)

Rob


---

Comment by mpatel created at 2010-11-28 03:31:55

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

Comment by jhpalmieri created at 2010-11-28 04:27:55

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

Comment by jhpalmieri created at 2010-11-28 04:27:55

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2010-11-28 04:32:00

Replying to [comment:11 mpatel]:
> Is this expected?

No, we derived separate classes for toric lattices and related objects to make sure that elements of different lattices of the same dimension don't mix in wrong ways (especially elements of dual lattices). Otherwise the behaviour is left the same as for base classes.


---

Comment by jhpalmieri created at 2010-11-28 04:38:01

Oh, I see: `FGP_Module` is a *function* which returns identical objects (via the `__init__` method of `FGP_Module_class`) if you pass it the same input.  If you do this:

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

Comment by jhpalmieri created at 2010-11-28 05:56:54

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-11-28 05:56:54

Here's a patch.


---

Attachment

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

Comment by rbeezer created at 2010-11-28 20:28:24

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-11-29 04:26:22

Replying to [comment:16 rbeezer]:
> So: positive review.  Thanks, John, for pursuing this one.

Well, I was helped a lot by Mitesh's pointer to the Python docs for `__cmp__`.


---

Comment by jdemeyer created at 2010-12-02 16:09:42

Resolution: fixed
