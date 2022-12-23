# Issue 8986: Add support for convex rational polyhedral cones

Issue created by migration from https://trac.sagemath.org/ticket/8986

Original creator: novoselt

Original creation time: 2010-05-18 09:06:31

Assignee: mhampton

CC:  vbraun davidloeffler




---

Comment by novoselt created at 2010-05-18 09:31:39

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-05-21 03:57:16

I will make some adjustments to this module following discussion here:
http://groups.google.com/group/sage-devel/browse_thread/thread/17743e17d67838ae


---

Comment by novoselt created at 2010-05-21 03:57:16

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2010-05-28 21:39:29

New version of the patch depends on #9062 and actually makes some improvements to toric lattices. Switch of caching technique to allow efficient extension of class hierarchy is still pending.


---

Comment by novoselt created at 2010-05-29 19:24:48

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2010-06-04 13:16:02

Changing status from needs_review to needs_work.


---

Comment by vbraun created at 2010-06-04 13:16:02

Looks good! I have two comments:

## Strict subcone

I find `ConvexRationalPolyhedralCone.strict_subcone()` confusing: It does return a quotient cone, not a subcone. Maybe we can call it `strict_quotient()`?

## point in cone

`IntegralRayCollection.__contains__(ray)` tests whether `ray` is a reference to one of the generating rays. But this is then inherited by `ConvexRationalPolyhedralCone` Naively, I would have expected that it tests whether something is in the cone:

```
sage: octant = Cone([(1,0,0), (0,1,0), (0,0,1)]) 
sage: N = octant.lattice()
sage: n = N(1,1,1)
sage: n.set_immutable()
sage: n in octant
False
sage: (1,0,0) in octant
False
```

Similarly there are issues with the immutablity as shown in the doctest.

I would suggest the following:

1) get rid of `IntegralRayCollection.__contains__(ray)`. If you need to test membership, its easy enough to search `self.rays()` or `self.rays_set()`:

```
sage: octant = Cone([(1,0,0), (0,1,0), (0,0,1)]) 
sage: N = octant.lattice()
sage: N(1,0,0) in octant.rays()  # no problem with immutability
True
sage: n = N(1,0,0)
sage: n.set_immutable()
sage: n in octant.ray_set()  # slightly more efficient and its clear why n must be immutable
True
```


2) tighten the rules for comparison of N/M-lattice objects:

```
sage: M = N.dual()
sage: M(1,0,0) == N(1,0,0)   # this should raise an error
False
sage: (1,0,0) == N(1,0,0)    # should probably return true
False
sage: M(1,0,0) == (1,0,0)    # should probably return true as well
False
sage: (1,0,0) == (1,0,0)     # works as expected
True
```

This would fix the following:

```
sage: (1,0,0) in octant.rays()  # this should return true
False
sage: M(1,0,0) in octant.rays()  # this should definitely raise an error
False
```


3) add methods `contains(n)` to `ConvexRationalPolyhedralCone` to test whether a N-lattice point is contained in the cone, e.g. (untested)


```
   def contains(self, *Nlist):
      """
      Returns whether the cone contains the N-lattice points ``*Nlist``.
      
      EXAMPLES::

          sage: cone = Cone([[1,0],[0,1]])
          sage: n = cone.ray(0) + cone.ray(1)
          sage: cone.contains(n)
          True
          sage: cone.contains( N(1,1), N(-1,1) )
          False
          sage: cone.contains([ N(1,1), N(-1,1) ])
          False
      """
      pts = flatten(Nlist)
      assert all(n in self._lattice() for n in pts), 'The points '+str(pts)+' must be in the N-lattice.'
      return all( self.polyhedron().contains(n) for n in pts )
}}} 

4) `ConvexRationalPolyhedralCone.__contains__()` just calls `contains()`. This is syntactic sugar, but `__` methods alone don't show up in the documentation.


---

Comment by novoselt created at 2010-06-04 16:09:57

Replying to [comment:5 vbraun]:
> I find `ConvexRationalPolyhedralCone.strict_subcone()` confusing: It does return a quotient cone, not a subcone. Maybe we can call it `strict_quotient()`?

Agreed. I just had to construct this object for equivalence checks and didn't really know how to call it.

> 1) get rid of `IntegralRayCollection.__contains__(ray)`. If you need to test membership, its easy enough to search `self.rays()` or `self.rays_set()`:
Agreed. 

> 2) tighten the rules for comparison of N/M-lattice objects:

```
sage: M(1,0,0) == N(1,0,0)   # this should raise an error
False
```


Disagreed. Maybe it is silly to ask if an apple is equal to a car, but there is nothing criminal in it. I think that in general in Python you can compare any two objects and sort lists containing arbitrary objects. So I think that `False` is the correct answer in this case.

>

```
sage: (1,0,0) == N(1,0,0)    # should probably return true
False
sage: M(1,0,0) == (1,0,0)    # should probably return true as well
False
```


I kind of don't like that we have here a==b and c==a, but b!=c... Do you really want to have it in? It may be actually non-trivial to implement. I already had to tweak the coercion system so that sometimes it allows "non-toric-lattice" objects to be involved and sometimes it does not. In particular I had to make sure that elements of toric lattices are NOT coerced into ZZ^n.

So if you insist, I will try to make it work, but I cannot guarantee that I will be successful and personally I think that we should not change it, as long as this behaviour is clearly documented. (Probably it is not, but that's something which definitely can be fixed ;-))

>

```
sage: M(1,0,0) in octant.rays()  # this should definitely raise an error
False
```


Again, I don't think that there should be any errors raised by comparison operations. `False` is an accurate answer to this question - and octant in the N-lattice does not contain any points of the M-lattice.

> 3) add methods `contains(n)` to `ConvexRationalPolyhedralCone` to test whether a N-lattice point is contained in the cone, e.g. (untested)

Agreed. It was on my list of things to do in the future, might as well do it now. 

> 4) `ConvexRationalPolyhedralCone.__contains__()` just calls `contains()`. This is syntactic sugar, but `__` methods alone don't show up in the documentation.

Very good point!!! I knew that they don't show up, but didn't think about just making a "common method" alias.

Please comment on the points of disagreement and I will try to fix the issues in a couple of days. Thanks for a careful review!


---

Comment by vbraun created at 2010-06-04 16:31:40

I see your point that e.g. python sets will use the comparison and its probably a bad idea to tinker too much with it. So I agree with you that we should keep it the way it is and make the `contains()` method throw an error if the argument is not in the N-lattice. Some warning in the toric lattices documentation might be good that '==' always compares objects and says nothing about equivalence.


---

Comment by novoselt created at 2010-06-04 17:41:46

Replying to [comment:7 vbraun]:
> I see your point that e.g. python sets will use the comparison and its probably a bad idea to tinker too much with it. So I agree with you that we should keep it the way it is and make the `contains()` method throw an error if the argument is not in the N-lattice. Some warning in the toric lattices documentation might be good that '==' always compares objects and says nothing about equivalence.

So you want different behaviour for `contains` and `__contains__`? I just checked the following to see how things are in Sage now:

```
sage: g = Graph()
sage: R = QQ["x,y"]
sage: g in R
False
```

To be consistent, I think that `x in cone` should accept any argument and return `False` if `x` is an object of any type that definitely cannot be in the cone. And I think it would be confusing to have different behaviour for `contains` and `__contains__`. In what kind of situations do you think it would be desirable to have an exception raised instead? Current framework already does not allow mixing elements of wrong toric lattices or even easily converting elements of one to another, so it does not seem to me that the current version will lead to any wrong results.


---

Comment by vbraun created at 2010-06-05 11:12:20

No, I definitely want `__contains__()` and `contains()` to be the same. I'm only concerned that a novice user of the package will write

```
sage: cone = Cone([[1,0],[0,1]])
sage: (1,1) in cone
False
```

and get the (in his eyes) wrong answer without any clue as to what went wrong. If that would be my first interaction with the package, I'd be convinced that its computations cannot be trusted :-). Once you understand the code it is of course obvious why it returned False. The difference to your example, where a ring is not in a graph, is that here it depends on the details of the coercion (or not) between `ZZ^n` and `ToricLattice` that will not be familiar to all users.

One could narrow it down to only raise an exception on tests that run into this problem, like a test along the lines of

```
if (!is_ToricLatticeElement(n)):
  try:
    [ ZZ(i) for i in n ]
    raise ValueError, 'You probably want '+str(n)+' to be a N-lattice element.'
  except:
    return False   # whatever n is, its not in the cone
```

Let me know what you think!


---

Comment by novoselt created at 2010-06-05 17:22:40

Well, I am still against exceptions, however I have just checked this:

```
sage: F5 = GF(5)
sage: F7 = GF(7)
sage: 2 == F5(2)
True
sage: 2 == F7(2)
True
sage: F5(2) == F7(2)
False
```

So, since I like so much to invoke consistency reasons in my arguments, I retract my first reaction on 2) in your proposal. I think I will try to allow coercion of `ZZ^n` to any toric lattice of dimension `n`, but not backwards. Explicit casting from lattices to `ZZ^n` will be possible, but to go between two different toric lattices one will have to create a homomorphism or use double casting, i.e. I think that M(N(1,1)) should throw a `TypeError`. So the code from your comment will work like this:

```
sage: M = N.dual()
sage: M(1,0,0) == N(1,0,0)   # this should raise an error - NO, RETURN FALSE
False
sage: (1,0,0) == N(1,0,0)    # should probably return true - YES
False
sage: M(1,0,0) == (1,0,0)    # should probably return true as well - YES
False
sage: (1,0,0) == (1,0,0)     # works as expected - YES
True
sage: (1,0,0) in octant.rays()  # this should return true - YES
False
sage: M(1,0,0) in octant.rays()  # this should definitely raise an error - NO, RETURN FALSE
False
```

I think this way it's OK to be sloppy about lattices, especially if one just does not care about them. If one uses the very last command, then clearly (s)he is aware of toric lattices and should be able to interpret this `False` correctly.


---

Comment by vbraun created at 2010-06-05 19:46:59

Actually, your last example `M(1,0,0) in octant.rays()` is precisely where I would like some feedback to the user that he is probably doing something wrong. Confusing the polytope with its dual is precisely what a beginner in toric geometry might do, and I think it would be very helpful if there were more feedback than a successful completion of the command. 

How about we don't raise exceptions and keep your "mathematical" sense of membership but use the python `warnings` module to print a warning. By default the warning would only occur the first time when the user aims for his foot...


---

Comment by novoselt created at 2010-06-05 19:54:57

OK! Will work on this.


---

Comment by novoselt created at 2010-06-06 03:00:08

I have realized that `(1,0,0)` in the examples above is not a vector, but just a tuple. Then I have done the following test:

```
sage: (1,0,0) == vector([1,0,0])
False
sage: vector([1,0,0]) == (1,0,0)
False
sage: vector([1,0,0]) + (1,0,0)  
TypeError: unsupported operand parent(s) for '+': 'Ambient free module of rank 3 over the principal ideal domain Integer Ring' and '<type 'tuple'>'
sage: (1,0,0) + (1,0,0)        
(1, 0, 0, 1, 0, 0)
```

It is not really an issue of the coercion, it is just not possible to always use tuples as a replacement for lattice points. We made it, however, very easy to work with them:

```
sage: N(1,0,0) + N(1,0,0)        
N(2, 0, 0)
```

So I think that equality tests will remain as they are now. Operations involving "pure" vectors may need more work, perhaps:

```
sage: N(1,0,0) + vector((1,0,0))
N(2, 0, 0)
sage: vector((1,0,0)) + N(1,0,0) 
(2, 0, 0)
```

although this does not bother me too much and I would suggest leaving this as is until we see where and how it can cause problems. (Making the second line return `N(2,0,0)` can be a bit tricky.)

Will post a new patch once I figure out how to work with warnings (never used them before).


---

Comment by novoselt created at 2010-06-06 04:43:36

Reviewer's comments taken into account.


---

Attachment

OK, I think I have addressed all the points in the original review except 2) which is pretty much impossible to realize completely (originally I was thinking of (1,1,1) as vectors, but they are just tuples, see the above comment for vector behaviour in this situation). I have added a general warning about tuples in the main `ToricLattice` documentation.

I added `__contains__` to `ToricLattice`, since I discovered that the inherited implementation is not suitable.

I added `__contains__`, `_contains`, and `contains` to cones. The real job is done in `_contains`, two others call it. The reason for the third function is an attempt to make warnings show where the actual potential mistake was, which requires the same calling depth. Unfortunately, in my tests it worked as I wanted only if it was triggered by some library code, in the notebook for created functions and attached files it just shows `main`. But that may change and maybe the terminal behaves differently. Now `cone.contains(stuff)` will try its best to return `True` by interpreting `stuff` as a point in the ambient space of `cone`, i.e. in `cone.lattice().base_extend(RR)`. However, it will catch points from foreign lattices first and return `False` with a warning, visible the first time for each location.

That's how reviewer's code works with the new version of the patch:

```
sage: octant = Cone([(1,0,0), (0,1,0), (0,0,1)]) 
sage: N = octant.lattice()
sage: n = N(1,1,1)
sage: n.set_immutable()
sage: n in octant # True was desired
True
sage: (1,0,0) in octant # True was desired
True
sage: N(1,0,0) in octant.rays()  # was and should be True
True
sage: n = N(1,0,0)
sage: n.set_immutable()
sage: n in octant.ray_set()  # was and should be True
True
sage: M = N.dual()
sage: M(1,0,0) == N(1,0,0)   # Error was desired
False
sage: (1,0,0) == N(1,0,0)    # True was desired, but difficult to get
False
sage: M(1,0,0) == (1,0,0)    # True was desired, but difficult to get
False
sage: (1,0,0) == (1,0,0)     # works as expected
True
sage: (1,0,0) in octant.rays()  # True was desired, but difficult to get
False
sage: M(1,0,0) in octant.rays()  # Error was desired
False
sage: cone = Cone([[1,0],[0,1]])
sage: (1,1) in cone # Was False
True
sage: M = cone.lattice().dual()
sage: M(1,1) in cone # Now gives warning on the first attempt
__main__:1: UserWarning: you have checked if a cone contains a point from another lattice, this is always False!
False
```

I suppose two lines marked "Error was desired" can also give a warning the first time they are invoked, if we implement a custom `__eq__` in addition to `__cmp__` for `ToricLatticeElement`. Should this be done?


---

Comment by novoselt created at 2010-06-06 05:21:11

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2010-06-06 13:25:51

I think the == comparison is not so critical, as it is the default python behavior to compare actual objects. Should not cause any confusion as long as one is somewhat familiar with Sage. So I'm happy with that.

The `Polyhedron` class already has a `contains()` method that tests for inclusion (I wrote it with toric varieties in mind :-).  `ConvexRationalPolyhedralCone._contains()` could have called that, saving a few lines of duplicate code. Not that big a deal, though. I'm happy to give it a positive review either way. Let me know what you think.


---

Comment by novoselt created at 2010-06-06 16:10:52

Replying to [comment:15 vbraun]:
> The `Polyhedron` class already has a `contains()` method that tests for inclusion (I wrote it with toric varieties in mind :-).  `ConvexRationalPolyhedralCone._contains()` could have called that, saving a few lines of duplicate code. Not that big a deal, though. I'm happy to give it a positive review either way. Let me know what you think.

So does `LatticePolytope` class, which was written with the same goal in mind ;-) As I have already complained somewhere, any calls to underlying `LatticePolytope` or `Polyhedron` objects can trigger system calls to other programs, which in many cases gives a huge overhead (compared to the rest of involved computations). So in this case I preferred to use a "native" way for cones to check if a point is inside. Of course, computing facet normals the first time will eventually call PALP to get facet normals of the corresponding polytope, but:

1) there is a way to compute facet normals for a lot of polytopes (e.g. corresponding to all cones of a fan) with a single call to PALP, in which case the overhead is negligible;

2) if a cone was pickled and unpickled, it definitely does not have polytope objects anymore, but it may still have facet normals, if they were computed before pickling;

3) we may eventually write our own initial computation of facet normals at least in some cases, for example, for complete fans.

Regarding 1) - the first call to `ReflexivePolytopes(3)` takes currently 5-10s. It reads a text file with vertices and then precomputes a bunch of stuff to save time later. Computing all this stuff without using group calls to PALP was taking about 15 minutes. I don't see any reasons why such calls cannot be done for Polyhedra, but I don't know how easy that would be. Do you think there is any point trying to implement it?

To summarize: please give a positive review to the present version ;-)


---

Comment by vbraun created at 2010-06-06 18:15:56

Oh I didn't notice that you use LatticePolytope/PALP to compute the facet normals. That limits the dimension a bit, but good enough for now. I think cython-izing `polyhedra` to call libcdd directly would be easy enough, but thats for the future :-)

So to summarize, I think the patch is ready for for inclusion. It also applies cleanly on top of Sage 4.4.3. Positive review.


---

Comment by vbraun created at 2010-06-06 18:15:56

Changing status from needs_review to positive_review.


---

Comment by novoselt created at 2010-06-06 19:27:09

Thank you!

Dimension limit is exactly why I started using `Polyhedra`, however I didn't quite like the timings. For example, this is what I get on geom.math with toric patches applied:

```
sage: %time
sage: o = lattice_polytope.octahedron(6) # no PALP calls
CPU time: 0.00 s,  Wall time: 0.00 s
sage: %time
sage: len(o.faces()) # PALP call to get incidences (no Hasse diagram)
6
CPU time: 0.07 s,  Wall time: 0.13 s
sage: %time
sage: f = FaceFan(o)
CPU time: 0.03 s,  Wall time: 0.06 s
sage: %time
sage: f.cone_lattice() # some calls to PALP
Finite poset containing 730 elements
CPU time: 0.18 s,  Wall time: 0.32 s
sage: %time
sage: p = Polyhedron(vertices=o.vertices().columns()) # almost all time is in cdd
CPU time: 0.02 s,  Wall time: 3.84 s
sage: %time
sage: p.face_lattice() # all time in Sage
Finite poset containing 730 elements
CPU time: 8.36 s,  Wall time: 8.36 s
```


Given the construction time of `p`, I am not even sure if calling cdd as a library will help a lot, but you mentioned that you also had some other library in mind. So while I am definitely interested in going to dimensions higher than 6, so far PALP seems to be the way to go. One possible modification for the future is to use PALP when possible and switch to alternatives when it does not work.


---

Comment by novoselt created at 2010-07-01 16:24:44

Changing status from positive_review to needs_work.


---

Attachment

I made a systematic mistake in doctests of `__cmp__` methods of all patches, discovered in #9062. So now I am posting these one-line patches to fix them, please review!


---

Comment by novoselt created at 2010-07-01 16:25:20

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2010-07-01 16:31:05

I noticed that, too. I haven't gotten around to fix it because I ran into this strange doctest failure in Sage-4.5alpha1 that worked beautifully in sage-4.4.4:

```
File "/home/vbraun/opt/sage-4.5.alpha1/devel/sage-main/sage/geometry/cone.py", line 1535:
    sage: c.faces()
Exception raised:
    Traceback (most recent call last):
      File "/home/vbraun/opt/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/vbraun/opt/sage-4.5.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/vbraun/opt/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_33[10]>", line 1, in <module>
        c.faces()###line 1535:
    sage: c.faces()
      File "/home/vbraun/opt/sage-4.5.alpha1/local/lib/python/site-packages/sage/geometry/cone.py", line 1554, in faces
        for level in self.face_lattice().level_sets())
      File "/home/vbraun/opt/sage-4.5.alpha1/local/lib/python/site-packages/sage/geometry/cone.py", line 1433, in face_lattice
        ray_to_facets, facet_to_rays, ConeFace)
      File "/home/vbraun/opt/sage-4.5.alpha1/local/lib/python/site-packages/sage/geometry/cone.py", line 2259, in hasse_diagram_from_incidences
        for atom, coatoms in enumerate(atom_to_coatoms))
      File "/home/vbraun/opt/sage-4.5.alpha1/local/lib/python/site-packages/sage/geometry/cone.py", line 2259, in <genexpr>
        for atom, coatoms in enumerate(atom_to_coatoms))
    KeyError: (frozenset([0]), frozenset([0]))
```

Andrey, since its your code maybe you'll understand what is going on.


---

Comment by novoselt created at 2010-07-01 16:36:04

Thanks for finding it, will work on!


---

Comment by novoselt created at 2010-07-01 16:36:04

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2010-07-01 22:01:07

I have finally built a copy of 4.5.alpha1 on geom.math and cannot reproduce this error, all tests passed. The error message above does not make any sense to me - how can a `KeyError` appear during enumeration of a list? Do you get the same error consistently every time? What configuration are you testing it on? Did you build 4.5.alpha1 from scratch? I will also run tests on my own computer, but it will take a few more hours to finish the build.


---

Comment by novoselt created at 2010-07-02 02:08:44

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2010-07-02 02:08:44

I installed 4.5.alpha1 on my machine (although it is not extremely different from geom: quite fresh Ubuntu 10.4 64bit running in a VirtualBox) and still don't have any issues...

By the way, I just noticed that the lines shown in the above exception do not exist in the patch on this ticket. Cone module is severely altered by the next ticket, in particular the Hasse diagram function was changed. Could it be that you accidentally skipped rebuilding sage after popping/pushing some patches of the sequence? That would probably lead to errors, although I would expect much more than one and with more sensible messages...

Anyway, I claim that this ticket works fine for me on top of 4.5.alpha1, as well as others in the sequence.


---

Comment by davidloeffler created at 2010-07-02 09:01:39

Just a remark: it works fine for me as well, 4.5.alpha1 on 64-bit SuSE Linux, as long as I have #9062 installed. Volker: could you tell us exactly what setup you were using when it didn't work for you, and what patches you did/did not have installed at the time?


---

Comment by vbraun created at 2010-07-02 10:01:24

I rebuilt 4.5.alpha1 overnight and it works now. Not sure what caused the problem. I can't rule out that I forgot to rebuild and/or some patch. Another possible problem was that I originally used parallel make for sage which died half way through because of a missing file. Since restarting the compilation succeeded, I had assumed that everything built OK. 

In any case, the toric code works so I'll set it back to `positive_review`.


---

Comment by vbraun created at 2010-07-02 10:01:24

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 08:47:04

Resolution: fixed


---

Comment by mpatel created at 2010-07-24 02:58:54

One or more of #8986, #8987, and #9062 _may_ cause the doctest failures listed at #9590.
