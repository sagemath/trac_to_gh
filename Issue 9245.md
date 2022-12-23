# Issue 9245: Add library of toric varieties

Issue created by migration from https://trac.sagemath.org/ticket/9245

Original creator: vbraun

Original creation time: 2010-06-15 15:22:17

Assignee: AlexGhitza

CC:  novoselt

Here is some initial shot at constructing toric varieties "by name". It might be useful to write doctests for the toric varieties. Once the dust has settled we might want to load pickled objects, but for now we construct the fans from generating cones.

Obviously this relies on #8988, which isn't finished yet. Also, I haven't added the import to `all.py` to avoid patch rejects.


---

Attachment

Initial patch


---

Comment by novoselt created at 2010-06-15 16:09:13

I think all fans should have `check=False` option at construction, since you know what you are doing and the input should be correct. Also, after constructing the fan, but before passing it to the toric variety, it would be good to set `fan._is_complete = True` when it is indeed true. Perhaps, to avoid explicit setting of a private attribute (which is going to migrate to the shared cache of related fans eventually), we should allow an optional argument to `fan.is_complete(known=None)`, and if it is given, then we assume that the user indeed knows whether it is true or false and save it instead of computing, which can be costly. Let me know if you are OK with it and I'll include it into the final version of #8987.

With these tweaks there should be no need for pickling as everything should be fast enough anyway (and pickled objects are not allowed into the Sage tarball anymore, so either we will need to have an spkg constructing them, or will have to save them on the first run).

The last five names are very cryptic, but I suppose it can be OK, if they are eventually described in the docstring.


---

Comment by vbraun created at 2010-06-15 16:33:16

I agree about disabling checks eventually, but for now I think its good to catch potential bugs elsewhere.

Instead of repurposing `fan.is_complete()`, how about an extra optional argument to `RationalPolyhedralFan.__init__(assume_complete=False)`. Once `Fan` is finished I can migrate the construction from `Fan` to `RationalPolyhedralFan` to speed things up further.


---

Comment by novoselt created at 2010-06-15 16:56:47

Replying to [comment:2 vbraun]:
> I agree about disabling checks eventually, but for now I think its good to catch potential bugs elsewhere.

Good point!

> Instead of repurposing `fan.is_complete()`, how about an extra optional argument to `RationalPolyhedralFan.__init__(assume_complete=False)`.

OK!

> Once `Fan` is finished I can migrate the construction from `Fan` to `RationalPolyhedralFan` to speed things up further.

That can make things fragile and lead to extra works of putting rays into proper spaces and making them immutable. That's exactly what `Fan(..., check=False)` is taking care of, if it does it in a slow way - it is a bug that should be fixed ;-)

It may be a good idea to keep a dictionary of these named varieties, so that repetitive calls to, say, `P1xP1` will return the same object. Another option is to make `ToricVariety` to return unique varieties if they were already constructed before, but it can be quite tedious compared to affine and projective spaces.


---

Comment by mhansen created at 2010-06-20 02:08:57

Since all of the named toric varieties seem to have valid Python identifiers for names, it seems more consistent to follow the interfaces of named graphs.


```
sage: graphs.CompleteGraph(4)
```


You could have something like


```
sage: toric_varieties.Conifold()
```



---

Comment by vbraun created at 2010-06-22 10:42:43

Changing status from new to needs_review.


---

Comment by vbraun created at 2010-06-22 10:42:43

I've taken mhansen's advice and rewrote the patch accordingly. Now has 100% documentation and tests, and adds itself to `all.py` and the documentation.

The variable `toric_varieties._check` determines whether the fans are constructed with checking or not. For now it defaults to `True`.


---

Comment by novoselt created at 2010-06-22 22:09:13

I like the general organization of the current patch, but names are still a bit strange. Especially `Cube3` which is not a polyhedral fan at all. Is it possible to insert a detailed mathematical description into docstrings? I mean not the cones/rays, which are given, but what exactly has to be done to the "usual" cube to get `Cube2` and `Cube3`. For varieties coming from arXiv papers, it would be nice to have complete references including all authors and the title of the paper.

Also technical detail about the posted patch file itself: it seems that it is taken directly from the queue and lacks some header information, including the commit message.


---

Comment by vbraun created at 2010-06-25 15:57:52

Now with commit message. What is the recommended way of extracting a patch from the Mercurial queue?

  * I've added more explanations to the `Cube` examples and changed their names.
  * References are improved.
  * New example: weighted projective space P4_11169 and its resolution.


---

Attachment

Improved patch


---

Comment by novoselt created at 2010-06-26 00:29:35

Replying to [comment:7 vbraun]:
> Now with commit message. What is the recommended way of extracting a patch from the Mercurial queue?

I am not sure. I always put the patch in question on the top, then run Sage and use `hg_sage.export("tip", "trac_xxxx_description")` command.


---

Comment by novoselt created at 2010-06-29 06:16:09

It probably makes sense to return `CPRFanoToricVariety` objects for those varieties that fall into this class, it will be also useful for writing more examples and tests for them. This will make this ticket to depend on #8989, but that one is pretty much settled already anyway.
If you are OK with this dependence, I don't mind making necessary changes here myself.


---

Comment by vbraun created at 2010-06-29 13:09:38

Agree! I'll make the changes later today.


---

Comment by vbraun created at 2010-06-29 13:09:38

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2010-06-29 14:29:02

One potential drawback to be aware of: for CPR-Fano toric varieties rays will have to be given as indices of points of the corresponding lattice polytope with vertices in front. You do have control over the order of vertices, but points are listed in the way in which PALP returns them. Of course, it matters only for (partially) resolved varieties, when you do need to have rays corresponding to points.


---

Comment by vbraun created at 2010-06-29 19:54:07

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2010-06-29 19:54:07

Here is the new patch. The `_make_CPRFanoToricVariety` method renumber the cones to refer to point indices.


---

Comment by novoselt created at 2010-06-29 21:51:29

* I don't think that `coordinate_points=ray2point.values()` does what you want - the order of elements in the dictionary is unpredictable. I think that 

```
ray2point = dict([ (i, points.index(r)) for i,r in enumerate(rays)]) 
```

 should be replaced with

```
ray2point = [points.index(r) for r in rays]
```


 * Is there any reason why coordinate names are given in constructor functions? It seems to me that they would look better next to the rays in the data block.


---

Comment by vbraun created at 2010-06-30 09:09:03

Thanks, good catch... I was somehow under the impression that the dict sorts by keys. In any case, your solution is cleaner.

My reason for splitting off the ray/cones data into a separate structure was that one could use it to reverse lookup a toric variety. The first step would be to check the "combinatorial" isomorphism of the cones, and only later the slower "lattice" isomorphism of the fan. For the coordinate names, on the other hand, we don't need a fast way to list them all, so that data can just stay in the individual methods.


---

Comment by vbraun created at 2010-07-02 10:41:05

Refreshed patch to work correctly with the final version of the `CPRFanoToricVarieties` patch.


---

Attachment

Updated patch


---

Comment by novoselt created at 2010-07-02 20:41:48

1) Can we replace C with A whenever it refers to complex numbers, e.g. `C2` ===> `A2` with documentation "Return the affine plane `\mathbb{A}^2` as a toric variety. ..."? I know that usually one thinks of complex numbers in toric geometry (I do it always), but the default field is the rational one and I think it would be better to have "neutral" names. Note that there is already no reference to the base field in all projective spaces, which is good, I think.

2) I think the module looks better in the documentation if its description on the first line is "Library of toric varieties" without "a". Although I can't really judge how bad it is from the English point of view not to have an article ;-)

3) In general the module docstring should include more information according to http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files
At the very least you should add yourself as the initial author, some description of how it works also can be nice.

4) Unfortunately, it is not very consistent in Sage, but I try to follow http://www.python.org/dev/peps/pep-0257/ cited in the beginning of http://sagemath.org/doc/developer/conventions.html#python-coding-conventions in the part of having a single line "command type" description in the beginning of docstrings, i.e. in most cases "Return ..." In many cases Sage uses "Returns ..." and the example in Developer's Guide is even worse: "This function returns ..." I definitely do not require you to follow the style I have chosen, but it can be nice if you follow it anyway for consistency purposes ;-)

5) Following Developer's Guide, the input block of `Cube_deformation` should look like

```
INPUT:

    - ``k`` -- integer. The case ``k=0`` is :meth:`Cube_face_fan`. 
```


6) I think it will be good for cross-linking compiled documentation if all functions have one of these output blocks (in addition to the more mathematical description of the output which they already have):

```
OUTPUT:

- :class:`toric variety
  <sage.schemes.generic.toric_variety.ToricVariety_field>`.

OUTPUT:

- :class:`CPR-Fano toric variety
  <sage.schemes.generic.fano_toric_variety.CPRFanoToricVariety_field>`.
```


7) I think it will be good if all examples displayed rays and names of coordinates, like

```
sage: Conifold = toric_varieties.Conifold()
sage: Conifold
3-d affine toric variety
sage: Conifold.fan().ray_matrix()
[0 0 1 1]
[0 1 0 1]
[1 1 1 1]
sage: Conifold.gens()
(u, x, y, v)
```

It will make the compiled documentation more informative.

8) `check=self._check` should be passed to constructors of toric varieties as well. Once we are confident that the rest of the code is correct and set `self._check=False` by default, my hope is that there will be no "# long time" comments in this module.

9) `sage -coverage` shows doctests of private functions as possibly wrong, there should be a comment "# indirect doctest" in their examples.

10) It also shows `TestSuite` error which I propose to ignore so far. There isn't really anything to test for such a class and I don't think there is any point in pickling it. If somebody disagrees, at least it will be easy for them to track down this module and do whatever is necessary.

Let me know what you think!


---

Comment by novoselt created at 2010-07-02 20:45:41

11) In addition to low-dimensional spaces, it may be nice to add `A(n)` and `P(n)` constructors for affine and projective spaces of arbitrary dimension with `(-1,...,-1)` always being the first (i.e. the zeroth) ray for `P(n)`. This is optional and can wait, of course.


---

Comment by vbraun created at 2010-07-02 20:55:02

1) On the issue of default base field: Having something else as the complex numbers as base field is going to haunt us soon. In my "cohomology" patch I just treated any characteristic zero field as C since working over rational numbers is going to be much harder. The topology over R is already much more complicated... Considering that most people will want the base field to be complex numbers, how are we going to deal with that?

I'm fine with your remaining comments.


---

Comment by novoselt created at 2010-07-02 21:20:32

I have already though about it quite a bit and I think that we should just explain in the documentation of all relevant functions that the base field is considered to be complex no matter what it actually is. I wrote some comments about it in the beginning of `toric_variety` module.

Changing the default base field to `CC` is not as good a solution as it may seem to be at first, since it is nice to have exact representation and in many cases `QQ` is exactly what one wants to use. I have also played with finite fields a month ago and they do seem to be useful.

Another issue is with "parameters" - for example, generic anticanonical hypersurfaces are realized as subschemes of toric varieties over things like Frac(QQ[a1, a2, a3]). I am not aware of a better representaion in Sage when I need to keep some coefficients undetermined (and I do need it almost always, usually I switch to all-numbers only for analysis of singularities).

My original plan was even to allow working over polynomial rings and use integers as default, since it may be faster, but that seems to be too much of a deviation from real life.

To summarize - I think that `QQ` is the best default choice and when possible we should avoid putting any assumptions on the base field, but when we really want it to be `CC`, we should think (and document it) that mathematically our variety is over `CC`, but on the computer it may be represented differently.


---

Comment by vbraun created at 2010-07-02 21:52:14

Note: `ToricVariety()` has no `check=` argument, only `CPRFanoToricVariety()` has.

Updated patch follows.


---

Attachment

Updated patch


---

Comment by novoselt created at 2010-07-02 22:40:53

Looks great!

Just a couple more little picks:

 * `Cube_deformation(k)` does NOT "Construct a sequence of toric varieties with torsion in the Chow group" since for every given `k` it will return only a particular element of the sequence. In the OUTPUT block of this function, can we turn "toric variety" into a hyperlink?

 * I don't quite like that other outputs will look in the documentation like "An instance of toric variety." I am totally fine without the dash in the beginning, but I'd prefer either plain-language "Toric variety." or a longer but more code-accurate "An instance of `ToricVariety_field`." given by one of these:

```
OUTPUT:

:class:`Toric variety
<sage.schemes.generic.toric_variety.ToricVariety_field>`.

OUTPUT:

An instance of
:class:`~sage.schemes.generic.toric_variety.ToricVariety_field`.
```


The second point is optional, if "An instance of toric variety." is exactly what you want, it is OK with me.


---

Comment by novoselt created at 2010-07-02 23:04:49

Hmm... Now that the choice of rays and coordinates is nicely shown:

 * Why does `A2` list basis vectors in the reverse order, (0,1) first and then (1,0)? Wouldn't it be better if the ray matrix of affine spaces was the identity one?

 * For `P2` my choice of coordinates would be x-(1,0), y-(0,1), z-(-1,-1) so that z is the "extra" coordinate compared to the affine space.

 * For `P1xP1` I used (s:t) as coordinates on one copy and (x:y) on another. Here it is (s:x) and (t:y). I don't really have a strong preference, but it does bug me it this case that notation is different.

 * `A2_Z2` got missed while adding ray matrices and coordinates.


---

Comment by vbraun created at 2010-07-03 12:22:37

I settled on "INPUT: A toric variety" since I like articles... I also beautified some coordinate choices. Finally, new methods `ToricVarietyFactory.A(n)` and `ToricVarietyFactory.P(n)` added.


---

Attachment

Updated patch


---

Attachment


---

Comment by novoselt created at 2010-07-03 19:01:11

I have added extra checks to constructors with parameters and made `P(n)` to return a Fano variety, as it was described in the documentation, but the code was for a plain toric variety.

I have also put (-1,-1,-1) as the last ray of `P(3)`. I have no idea what I was thinking when I asked to have it first. Maybe I was thinking about `z1, z2, z3` coordinates for `A(3)` and `z0, z1, z2, z3` for `P(3)`, but I think it is more consistent to let `A(3)` have default coordinates `z0, z1, z2` and then projectivization adds `z3` in the end. On the level of fans it definitely makes more sense to put the extra element in the back.

All tests pass for me on 4.5.alpha1, positive review once you approve (hopefully ;-)) my patch!


---

Comment by vbraun created at 2010-07-03 19:06:22

looks good to me!


---

Comment by vbraun created at 2010-07-03 19:06:22

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 10:03:18

Resolution: fixed


---

Comment by mpatel created at 2010-07-20 10:03:18

I've merged

 * [attachment:trac_9245_named_toric_varieties.3.patch]
 * [attachment:trac_9245_toric_library_reviewer.patch]

into 4.5.2.alpha0.
