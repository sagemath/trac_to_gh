# Issue 8989: Add support for Fano toric varieties

Issue created by migration from https://trac.sagemath.org/ticket/8989

Original creator: novoselt

Original creation time: 2010-05-18 09:08:17

Assignee: AlexGhitza

CC:  vbraun




---

Comment by novoselt created at 2010-05-18 10:00:30

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-05-19 03:53:34

`kaehler_cone` function was moved to the general toric varieties.

There is still an unfinished discussion about the name of what is now called `FanoToricVariety`:
http://groups.google.com/group/sage-devel/browse_thread/thread/17743e17d67838ae


---

Comment by novoselt created at 2010-05-21 03:58:42

I will make some adjustments to this module following discussion here:
http://groups.google.com/group/sage-devel/browse_thread/thread/17743e17d67838ae


---

Comment by novoselt created at 2010-05-21 03:58:42

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2010-05-29 05:20:58

Names of all functions/classes were adjusted to work with Crepant Partial Resolutions of Fano toric varieties (CPR-Fano toric varieties).


---

Comment by novoselt created at 2010-05-29 19:25:56

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2010-06-17 22:03:55

Rebased patch with `_repr_` changed to be similar to plain toric varieties.


---

Comment by vbraun created at 2010-06-29 13:05:46

The functionality is fine, but I would prefer to rename some methods/variables:
  * `delta` -> `nabla`, `P_Delta` -> `delta` everywhere. The "delta in M, nabla in N" notation works much better in ASCII than `\Delta^\circ`.
  * `coordinate_indices` -> `coordinate_name_indices` in order to distinguish it better from coordinate_points. A doctest would be nice, too.

In addition to N/M lattice points we now have points of the (dual) polytope, yay. What does `point_to_variable()` refer to? At the same time I would like to avoid the lengthy `polyhedron_point_to_variable()`, and its not easy to find a good name. How about a `nabla_to_variable()` method that takes either the index of a nabla-point or actual coordinates of a point and returns the corresponding homogeneous coordinate?

Let me know what you think. After we decide on what to do I'd be happy to review it positively.


---

Comment by novoselt created at 2010-06-29 15:28:57

I switch to numbers for easier referencing:

1) I agree that delta/nabla work better in ASCII, but I am also going to add support for complete intersections where it is customary to use delta/nabla pair to denote polytopes dual in the nef-partition sense. While these polytopes will not be accessible at the level of toric variety (but only at the level of appropriate subschemes), I would prefer to avoid using nabla here as well and stick with `\Delta^\circ`.

2) Since I don't want to use nabla, I'd rather have delta to denote the polytope whose face fan we are subdividing. Since in general this polytope and its parts have more clear relation to the variety than its polar, I would prefer to use it as "the main one". This is not particularly customary but is quite natural when working with reflexive polytopes and that's what this module is about. As an example of similar notation in use I can give Nill's paper referenced in the module: arXiv:math/0405448v1 (both polytopes and fans live in the M lattice). Another reference is arXiv:0907.2701v1 [math.CO], but it does not help me to justify my taste ;-) I think I had plans to allow the user to switch from one style to another, but I don't see any clean way to do it, so probably it was not a very bright idea.

3) Despite my opposition to other changes, I would like to replace `delta` with `Delta`. I was avoiding using capitalized methods in general, but it does make sense here and I agree that for Kaehler/Mori methods capital is better.

4) `coordinate_indices` - will change and add tests.

5) I see your point against `point_to_variable`, but `nabla_to_variable` seems to be even more confusing to me... How about just `coordinate`?


```
sage: X = toric variety
sage: X.coordinate(9)
z5
sage: X.coordinate((1,-1,1))
z5
```

We can even expand it to

```
sage: X.coordinate("z5")
z5
sage: X.inject_variables()
sage: X.coordinate(z5)
z5
```

i.e. this method will try to convert any input to the appropriate generator of the coordinate ring. The only subtle point will be that "plain numbers" will refer to points of Delta rather than generators of the ring, but that's what one usually wants and there is `X.gen(n)` method for those who want exactly the n-th variable.


---

Comment by vbraun created at 2010-06-29 16:41:25

1-3) Which notation do you want to use for nef partitions? I would follow Batyrev/Materov and decompose `delta = sum delta_i in M` with the dual nef partition being `nabla = sum nabla_i in N`. 

Nill apparently doesn't want others to read his paper, and using his confusing notation is doing a great job at that. But then its his work and he can do whatever he pleases. The difference is that I would like the Sage package to be used by other people, and inventing your own notation which moreover conflicts with the standard notation is a big no-no.

5) `coordinate()` still does not clarify which points it refers to. Moreover, I think it is not an often-used function, so it does not deserve an abbreviated method name that might be confused with other, more often used functions. Ideally, once you have constructed the toric variety you shouldn't need to know how the points of the polyhedron were enumerated.


---

Comment by novoselt created at 2010-06-29 17:14:57

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2010-06-29 17:14:57

1-3) I am actually having second thoughts about all these names. I think this is basically the same issue as with `cone.N` vs. `cone.spanned_lattice` and to avoid imposing names on users and things like `Y = CPRFanoToricVariety(delta=X.nabla())` we should use some "neutral but descriptive names" and then indicate how it is related to the standard notation in documentation.

In this particular case I would prefer to replace `delta` with `polytope` everywhere in the code. Then one can write:

```
sage: Delta = some polytope
sage: nabla = Delta.polar()
sage: X = CPRFanoToricVariety(Delta)
sage: Y = CPRFanoToricVariety(nabla)
sage: X.polytope() is Delta
True
sage: Y.polytope() is nabla
True
```

or, if one prefers other names, something like

```
sage: Delta = some polytope
sage: Delta_circ = Delta.polar()
sage: X = CPRFanoToricVariety(Delta)
sage: Y = CPRFanoToricVariety(Delta_circ)
sage: X.polytope() is Delta
True
sage: Y.polytope() is Delta_circ
True
```

Moreover, it now will be possible to have some global switch to make `X` above correspond to the normal fan of `Delta`, rather than face one:

```
sage: Delta = some polytope
sage: nabla = Delta.polar()
sage: X = CPRFanoToricVariety(Delta)
sage: Y = CPRFanoToricVariety(nabla)
sage: X.polytope() is Delta.polar()
True
sage: Y.polytope() is nabla.polar()
True
```


Personally, I like Nill's paper, as well as his notation, and I certainly saw some other ones with notation different from Delta in M/nabla in N. I think our goal for Sage is to make as flexible and consistent package as possible, suitable both for beginners and "advancers". So I do agree that we should not enforce Nill's notation, but I also think that we should not hard-code any other (even though I have done it so far in this patch). Notation is always just notation, we should operate with more conceptual things...

5) Agreed. Assuming `delta` is renamed to `polytope`, I would then prefer `polytope_point_to_coordinate` taking either an index or an actual point as an argument. Long, but should be quite clear.


---

Comment by vbraun created at 2010-06-29 17:29:48

In principle I agree, but in practice you will need to distinguish the polytope from the dual polytope. And, conventionally, the "dual polytope" is what the `CPRFanoToricVariety` expects as its argument. The difference is that the fan is either the face fan or the normal fan of the polytope, so the roles of polytope and its dual are **not** interchangeable from the toric variety point of view.

In the cone case there is nothing that breaks the symmetry; A cone could be a cone in the N or M lattice or neither (like the Kaehler cone). 

Notation is of course arbitrary, but once established it does save a lot of writing/typing ;-)


---

Comment by novoselt created at 2010-06-29 17:57:15

A polytope and its dual are not interchangeable when you are talking about one particular toric variety, but if you are working with two varieties associated to these polytopes, things do become somewhat interchangeable...

My point is that if I have created a standalone polytope, called it `Delta`, and cooked up a toric variety `X` from it one way or another, then it is cool if `X.Delta()` gives me exactly this `Delta` back. However, if I now used the same construction to create a toric variety `Y` associated to `Delta.polar()` or maybe some other polytope `nabla`, it is confusing that `Delta.polar() == Y.Delta()` or `nabla == Y.Delta()`.

In mathematics it is more or less OK to abuse notation and use the same names describing different objects, or to say "everything will be the same up to relabelling." When it is not enough, one can also start putting tildes, primes, daggers, etc. on similar but different objects to make them a little bit different. But method names cannot be slightly altered or "relabeled in an obvious way." So it is not that I don't want to use standard notation, I just don't think that it is usable in tasks involving more than one object - if you want to work with them at the same time, they must have different names/notation.

The polytope whose face fan is used has the advantage of being uniquely determined (with the agreement of using primitive vectors along the rays), while many different polytopes may give the same normal fan. So it seems to me that using just `polytope` makes sense. If you don't like it, how about `fan_polytope`? (`spanned_polytope`? `face_polytope`?..)


---

Comment by vbraun created at 2010-06-29 18:23:18

That was precisely my point: Since you have a `CPRFanoToricVariety_field` object in front of you when calling any method, you cannot freely exchange polyhedron and dual polyhedron any more. There is no confusion in `my_toric_variety.nabla()`.

I agree that comparisons with other variables might be confusing, but the problem is that the other variable is confusingly-named. I can always write `not_X = X; X == not_X` and will get `True`. But that is not `X`'s fault, nor can `X` do anything to prevent it. As soon as the user refrains from creating local variables named `nabla` or `delta` everything is fine. Mirror symmetry becomes

```
X.nabla() == Y.delta()
```


Furthermore:
  * `fan_polytope` still does not distinguish face/normal fan
  * `spanned_polytope` is spanned by what, the rays or the monomials?
  * `face_polytope` don't like it either ;-)
Its hard to say "the polytope whose face-fan is the fan of the toric variety" in a python identifier without agreeing on some sort of code.


---

Comment by novoselt created at 2010-06-29 21:04:39

Well, I guess I mostly agree, I probably went over the top in my struggle for the best and cleanest names ever ;-) So while I think that it is quite likely to have `nabla` and `delta` as local variables, it does make sense to use them for methods.

However, I am still against assigning different names to polar polytopes. In the notation for nef-partitions that you have cited, `delta` and `nabla` are not polar, in fact, they are not dual in any sense by themselves, but their decompositions are dual and their polars are expressed as convex hulls of Minkowski summands. I envision for complete intersections methods like

```
sage: CI.Delta()
sage: CI.Delta(i)
sage: CI.nabla()
sage: CI.nabla(j)
```

and while these are different objects from toric varieties, I would like same-named methods to return the same things.

So if you really don't want `Delta` to denote the polytope whose face fan is used for the toric variety, I propose `X.Delta()` to return the polytope whose normal fan is used. Indices of points used for coordinates will refer to `X.Delta().polar()`. If you would like to have a "direct" access to this polytope from `X`, then I think the method should be called `X.Delta_polar()`. While its implementation will be trivial, it is probably good to have it, since it will allow us to put appropriate documentation there related to toric varieties, rather than just taking polar polytopes. That gives us also `Delta_polar_point_to_coordinate` which is a bit lengthy, but I don't mind it and you think that it will not be used very often, so it should not be a problem.

Does it sound like a good compromise?


---

Comment by vbraun created at 2010-06-30 17:05:56

So just to get this straight, there will be a `CompleteIntersection` class (to be implemented in the future) analogous to the already-implemented `AnticanonicalHypersurface`. Only `CompleteIntersection` will know about the nef partition, but not the ambient `CPRFanoToricVariety_field`.

Then, there will be methods (perhaps with `_star` instead of `_polar`)

```
CI.Delta(i), i=1..r
CI.nabla(i), i=1..r
CI.Delta() = convex hull( CI.Delta(i) )
CI.Delta_polar() = Minkowski sum( CI.nabla(i) )
CI.nabla() = convex hull( CI.nabla(i) )
CI.nabla_polar(j) = Minkowski sum( CI.Delta(i) )
```

for the usual polytopology of nef partitions. The only relations to the polytopes of the ambient toric variety are

```
cpr_fano.Delta() == CI.Delta()
cpr_fano.Delta_polar() == CI.Delta_polar()
```


That would be fine with me. A `Delta_polar_to_coordinate` method is ok, too.


---

Comment by novoselt created at 2010-07-02 06:23:47

Changing status from needs_work to needs_review.


---

Attachment

OK, here are the changes:

 * Toric variety `X` is now associated to the normal fan of `Delta`.

 * Respectively, "old" `delta` was changed to `Delta_polar`.

 * The class takes as input and stores inside `Delta_polar`, since that's what is most relevant.

 * The factory function accepts either `Delta` or `Delta_polar` (without explicit clarification it is `Delta`, which means that #9245 will break a little bit, the fix is to put `Delta_polar=polytope` on line 180).

 * `P_Delta` did not mean "polar to Delta", it is `\mathbb{P}_{\Delta}`, so it remains the same, except that in the new version `Delta` refers to the polytope in the `M` lattice. (I did not really mention any lattices in the documentation, using normal/face fans to distinguish the relation of `Delta` and `Delta_polar` to `X`.)

 * `coordinate_indices` are renamed to `coordinate_name_indices` and have several doctests explaining why there is probably no need to use this parameter (not like I want to remove it, I just hope that usually the defaults will work nicely). 

 * `coefficient_name_indices` are added to the hypersurface constructor, it was kind of a bug that originally it was not there - the idea is to treat creation of names in the same fashion everywhere. I even think that my `normalize_names` function should replace the one in `Parent`, but the relevant discussion on sage-devel died without responses, so for now it is used in toric varieties only.

 * `point_to_variable` is renamed to `coordinate_point_to_coordinate`, despite of discussion above. While working on its documentation, I decided that this is the most natural name given that there are `coordinate_points` and this function takes an element from there and transforms it into a coordinate. If you disagree with this argument and still prefer `Delta_polar_point_to_coordinate`, I'll change it.


---

Comment by novoselt created at 2010-07-02 06:30:34

Oh, and regarding your last comment on complete intersections - yes, that's what I plan to implement once I get to it. In principle, I already have all the code, it just has to be rewritten for the new framework and documented, as well as other things ;-) For now my next target is reviewing your posted patches.


---

Comment by vbraun created at 2010-07-02 10:37:16

I'm happy with the new names!


---

Comment by vbraun created at 2010-07-02 10:37:16

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2010-07-02 11:12:58

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2010-07-02 11:12:58

I just noticed that `CPRFanoToricVariety` does not construct a default `ToricLattice`:

```
sage: toric_varieties.Conifold().fan().lattice()
3-d lattice N
sage: toric_varieties.P2().fan().lattice()
Ambient free module of rank 2 over the principal ideal domain Integer Ring
```

Is there any particular reason why this is not done in the same way as `ToricVariety`?


---

Comment by novoselt created at 2010-07-02 21:21:54

It is a bug somewhere. Looking into it.


---

Attachment


---

Comment by novoselt created at 2010-07-02 22:10:02

As it is plainly written in the documentation of `Fan`, "it is usually **NOT** a good idea to use ``normalize=False`` option" ;-)

I didn't not use your doctest since it depends on the next ticket, but added a similar one. Now all fans of CPR-Fano varieties will live in lattice `N`, there is no way to change it, and I don't want to allow such a change since ultimately this lattice should be deduced from the given polytope, which should know its ambient lattice.


---

Comment by novoselt created at 2010-07-02 22:10:02

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2010-07-03 13:36:29

Works for me!


---

Comment by vbraun created at 2010-07-03 13:36:29

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 08:49:03

Resolution: fixed
