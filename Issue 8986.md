# Issue 8986: Add support for convex rational polyhedral cones

archive/issues_008986.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  vbraun davidloeffler\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8986\n\n",
    "created_at": "2010-05-18T09:06:31Z",
    "labels": [
        "geometry",
        "major",
        "enhancement"
    ],
    "title": "Add support for convex rational polyhedral cones",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8986",
    "user": "novoselt"
}
```
Assignee: mhampton

CC:  vbraun davidloeffler



Issue created by migration from https://trac.sagemath.org/ticket/8986





---

archive/issue_comments_082917.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-18T09:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82917",
    "user": "novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082918.json:
```json
{
    "body": "I will make some adjustments to this module following discussion here:\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/17743e17d67838ae",
    "created_at": "2010-05-21T03:57:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82918",
    "user": "novoselt"
}
```

I will make some adjustments to this module following discussion here:
http://groups.google.com/group/sage-devel/browse_thread/thread/17743e17d67838ae



---

archive/issue_comments_082919.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-21T03:57:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82919",
    "user": "novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082920.json:
```json
{
    "body": "New version of the patch depends on #9062 and actually makes some improvements to toric lattices. Switch of caching technique to allow efficient extension of class hierarchy is still pending.",
    "created_at": "2010-05-28T21:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82920",
    "user": "novoselt"
}
```

New version of the patch depends on #9062 and actually makes some improvements to toric lattices. Switch of caching technique to allow efficient extension of class hierarchy is still pending.



---

archive/issue_comments_082921.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-29T19:24:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82921",
    "user": "novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082922.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-04T13:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82922",
    "user": "vbraun"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082923.json:
```json
{
    "body": "Looks good! I have two comments:\n\n## Strict subcone\n\nI find `ConvexRationalPolyhedralCone.strict_subcone()` confusing: It does return a quotient cone, not a subcone. Maybe we can call it `strict_quotient()`?\n\n## point in cone\n\n`IntegralRayCollection.__contains__(ray)` tests whether `ray` is a reference to one of the generating rays. But this is then inherited by `ConvexRationalPolyhedralCone` Naively, I would have expected that it tests whether something is in the cone:\n\n```\nsage: octant = Cone([(1,0,0), (0,1,0), (0,0,1)]) \nsage: N = octant.lattice()\nsage: n = N(1,1,1)\nsage: n.set_immutable()\nsage: n in octant\nFalse\nsage: (1,0,0) in octant\nFalse\n```\n\nSimilarly there are issues with the immutablity as shown in the doctest.\n\nI would suggest the following:\n\n1) get rid of `IntegralRayCollection.__contains__(ray)`. If you need to test membership, its easy enough to search `self.rays()` or `self.rays_set()`:\n\n```\nsage: octant = Cone([(1,0,0), (0,1,0), (0,0,1)]) \nsage: N = octant.lattice()\nsage: N(1,0,0) in octant.rays()  # no problem with immutability\nTrue\nsage: n = N(1,0,0)\nsage: n.set_immutable()\nsage: n in octant.ray_set()  # slightly more efficient and its clear why n must be immutable\nTrue\n```\n\n\n2) tighten the rules for comparison of N/M-lattice objects:\n\n```\nsage: M = N.dual()\nsage: M(1,0,0) == N(1,0,0)   # this should raise an error\nFalse\nsage: (1,0,0) == N(1,0,0)    # should probably return true\nFalse\nsage: M(1,0,0) == (1,0,0)    # should probably return true as well\nFalse\nsage: (1,0,0) == (1,0,0)     # works as expected\nTrue\n```\n\nThis would fix the following:\n\n```\nsage: (1,0,0) in octant.rays()  # this should return true\nFalse\nsage: M(1,0,0) in octant.rays()  # this should definitely raise an error\nFalse\n```\n\n\n3) add methods `contains(n)` to `ConvexRationalPolyhedralCone` to test whether a N-lattice point is contained in the cone, e.g. (untested)\n\n\n```\n   def contains(self, *Nlist):\n      \"\"\"\n      Returns whether the cone contains the N-lattice points ``*Nlist``.\n      \n      EXAMPLES::\n\n          sage: cone = Cone([[1,0],[0,1]])\n          sage: n = cone.ray(0) + cone.ray(1)\n          sage: cone.contains(n)\n          True\n          sage: cone.contains( N(1,1), N(-1,1) )\n          False\n          sage: cone.contains([ N(1,1), N(-1,1) ])\n          False\n      \"\"\"\n      pts = flatten(Nlist)\n      assert all(n in self._lattice() for n in pts), 'The points '+str(pts)+' must be in the N-lattice.'\n      return all( self.polyhedron().contains(n) for n in pts )\n```\n \n\n4) `ConvexRationalPolyhedralCone.__contains__()` just calls `contains()`. This is syntactic sugar, but `__` methods alone don't show up in the documentation.",
    "created_at": "2010-06-04T13:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82923",
    "user": "vbraun"
}
```

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
```
 

4) `ConvexRationalPolyhedralCone.__contains__()` just calls `contains()`. This is syntactic sugar, but `__` methods alone don't show up in the documentation.



---

archive/issue_comments_082924.json:
```json
{
    "body": "Replying to [comment:5 vbraun]:\n> I find `ConvexRationalPolyhedralCone.strict_subcone()` confusing: It does return a quotient cone, not a subcone. Maybe we can call it `strict_quotient()`?\n\nAgreed. I just had to construct this object for equivalence checks and didn't really know how to call it.\n\n> 1) get rid of `IntegralRayCollection.__contains__(ray)`. If you need to test membership, its easy enough to search `self.rays()` or `self.rays_set()`:\nAgreed. \n\n> 2) tighten the rules for comparison of N/M-lattice objects:\n\n```\nsage: M(1,0,0) == N(1,0,0)   # this should raise an error\nFalse\n```\n\n\nDisagreed. Maybe it is silly to ask if an apple is equal to a car, but there is nothing criminal in it. I think that in general in Python you can compare any two objects and sort lists containing arbitrary objects. So I think that `False` is the correct answer in this case.\n\n>\n\n```\nsage: (1,0,0) == N(1,0,0)    # should probably return true\nFalse\nsage: M(1,0,0) == (1,0,0)    # should probably return true as well\nFalse\n```\n\n\nI kind of don't like that we have here a==b and c==a, but b!=c... Do you really want to have it in? It may be actually non-trivial to implement. I already had to tweak the coercion system so that sometimes it allows \"non-toric-lattice\" objects to be involved and sometimes it does not. In particular I had to make sure that elements of toric lattices are NOT coerced into ZZ^n.\n\nSo if you insist, I will try to make it work, but I cannot guarantee that I will be successful and personally I think that we should not change it, as long as this behaviour is clearly documented. (Probably it is not, but that's something which definitely can be fixed ;-))\n\n>\n\n```\nsage: M(1,0,0) in octant.rays()  # this should definitely raise an error\nFalse\n```\n\n\nAgain, I don't think that there should be any errors raised by comparison operations. `False` is an accurate answer to this question - and octant in the N-lattice does not contain any points of the M-lattice.\n\n> 3) add methods `contains(n)` to `ConvexRationalPolyhedralCone` to test whether a N-lattice point is contained in the cone, e.g. (untested)\n\nAgreed. It was on my list of things to do in the future, might as well do it now. \n\n> 4) `ConvexRationalPolyhedralCone.__contains__()` just calls `contains()`. This is syntactic sugar, but `__` methods alone don't show up in the documentation.\n\nVery good point!!! I knew that they don't show up, but didn't think about just making a \"common method\" alias.\n\nPlease comment on the points of disagreement and I will try to fix the issues in a couple of days. Thanks for a careful review!",
    "created_at": "2010-06-04T16:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82924",
    "user": "novoselt"
}
```

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

archive/issue_comments_082925.json:
```json
{
    "body": "I see your point that e.g. python sets will use the comparison and its probably a bad idea to tinker too much with it. So I agree with you that we should keep it the way it is and make the `contains()` method throw an error if the argument is not in the N-lattice. Some warning in the toric lattices documentation might be good that '==' always compares objects and says nothing about equivalence.",
    "created_at": "2010-06-04T16:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82925",
    "user": "vbraun"
}
```

I see your point that e.g. python sets will use the comparison and its probably a bad idea to tinker too much with it. So I agree with you that we should keep it the way it is and make the `contains()` method throw an error if the argument is not in the N-lattice. Some warning in the toric lattices documentation might be good that '==' always compares objects and says nothing about equivalence.



---

archive/issue_comments_082926.json:
```json
{
    "body": "Replying to [comment:7 vbraun]:\n> I see your point that e.g. python sets will use the comparison and its probably a bad idea to tinker too much with it. So I agree with you that we should keep it the way it is and make the `contains()` method throw an error if the argument is not in the N-lattice. Some warning in the toric lattices documentation might be good that '==' always compares objects and says nothing about equivalence.\n\nSo you want different behaviour for `contains` and `__contains__`? I just checked the following to see how things are in Sage now:\n\n```\nsage: g = Graph()\nsage: R = QQ[\"x,y\"]\nsage: g in R\nFalse\n```\n\nTo be consistent, I think that `x in cone` should accept any argument and return `False` if `x` is an object of any type that definitely cannot be in the cone. And I think it would be confusing to have different behaviour for `contains` and `__contains__`. In what kind of situations do you think it would be desirable to have an exception raised instead? Current framework already does not allow mixing elements of wrong toric lattices or even easily converting elements of one to another, so it does not seem to me that the current version will lead to any wrong results.",
    "created_at": "2010-06-04T17:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82926",
    "user": "novoselt"
}
```

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

archive/issue_comments_082927.json:
```json
{
    "body": "No, I definitely want `__contains__()` and `contains()` to be the same. I'm only concerned that a novice user of the package will write\n\n```\nsage: cone = Cone([[1,0],[0,1]])\nsage: (1,1) in cone\nFalse\n```\n\nand get the (in his eyes) wrong answer without any clue as to what went wrong. If that would be my first interaction with the package, I'd be convinced that its computations cannot be trusted :-). Once you understand the code it is of course obvious why it returned False. The difference to your example, where a ring is not in a graph, is that here it depends on the details of the coercion (or not) between `ZZ^n` and `ToricLattice` that will not be familiar to all users.\n\nOne could narrow it down to only raise an exception on tests that run into this problem, like a test along the lines of\n\n```\nif (!is_ToricLatticeElement(n)):\n  try:\n    [ ZZ(i) for i in n ]\n    raise ValueError, 'You probably want '+str(n)+' to be a N-lattice element.'\n  except:\n    return False   # whatever n is, its not in the cone\n```\n\nLet me know what you think!",
    "created_at": "2010-06-05T11:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82927",
    "user": "vbraun"
}
```

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

archive/issue_comments_082928.json:
```json
{
    "body": "Well, I am still against exceptions, however I have just checked this:\n\n```\nsage: F5 = GF(5)\nsage: F7 = GF(7)\nsage: 2 == F5(2)\nTrue\nsage: 2 == F7(2)\nTrue\nsage: F5(2) == F7(2)\nFalse\n```\n\nSo, since I like so much to invoke consistency reasons in my arguments, I retract my first reaction on 2) in your proposal. I think I will try to allow coercion of `ZZ^n` to any toric lattice of dimension `n`, but not backwards. Explicit casting from lattices to `ZZ^n` will be possible, but to go between two different toric lattices one will have to create a homomorphism or use double casting, i.e. I think that M(N(1,1)) should throw a `TypeError`. So the code from your comment will work like this:\n\n```\nsage: M = N.dual()\nsage: M(1,0,0) == N(1,0,0)   # this should raise an error - NO, RETURN FALSE\nFalse\nsage: (1,0,0) == N(1,0,0)    # should probably return true - YES\nFalse\nsage: M(1,0,0) == (1,0,0)    # should probably return true as well - YES\nFalse\nsage: (1,0,0) == (1,0,0)     # works as expected - YES\nTrue\nsage: (1,0,0) in octant.rays()  # this should return true - YES\nFalse\nsage: M(1,0,0) in octant.rays()  # this should definitely raise an error - NO, RETURN FALSE\nFalse\n```\n\nI think this way it's OK to be sloppy about lattices, especially if one just does not care about them. If one uses the very last command, then clearly (s)he is aware of toric lattices and should be able to interpret this `False` correctly.",
    "created_at": "2010-06-05T17:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82928",
    "user": "novoselt"
}
```

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

archive/issue_comments_082929.json:
```json
{
    "body": "Actually, your last example `M(1,0,0) in octant.rays()` is precisely where I would like some feedback to the user that he is probably doing something wrong. Confusing the polytope with its dual is precisely what a beginner in toric geometry might do, and I think it would be very helpful if there were more feedback than a successful completion of the command. \n\nHow about we don't raise exceptions and keep your \"mathematical\" sense of membership but use the python `warnings` module to print a warning. By default the warning would only occur the first time when the user aims for his foot...",
    "created_at": "2010-06-05T19:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82929",
    "user": "vbraun"
}
```

Actually, your last example `M(1,0,0) in octant.rays()` is precisely where I would like some feedback to the user that he is probably doing something wrong. Confusing the polytope with its dual is precisely what a beginner in toric geometry might do, and I think it would be very helpful if there were more feedback than a successful completion of the command. 

How about we don't raise exceptions and keep your "mathematical" sense of membership but use the python `warnings` module to print a warning. By default the warning would only occur the first time when the user aims for his foot...



---

archive/issue_comments_082930.json:
```json
{
    "body": "OK! Will work on this.",
    "created_at": "2010-06-05T19:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82930",
    "user": "novoselt"
}
```

OK! Will work on this.



---

archive/issue_comments_082931.json:
```json
{
    "body": "I have realized that `(1,0,0)` in the examples above is not a vector, but just a tuple. Then I have done the following test:\n\n```\nsage: (1,0,0) == vector([1,0,0])\nFalse\nsage: vector([1,0,0]) == (1,0,0)\nFalse\nsage: vector([1,0,0]) + (1,0,0)  \nTypeError: unsupported operand parent(s) for '+': 'Ambient free module of rank 3 over the principal ideal domain Integer Ring' and '<type 'tuple'>'\nsage: (1,0,0) + (1,0,0)        \n(1, 0, 0, 1, 0, 0)\n```\n\nIt is not really an issue of the coercion, it is just not possible to always use tuples as a replacement for lattice points. We made it, however, very easy to work with them:\n\n```\nsage: N(1,0,0) + N(1,0,0)        \nN(2, 0, 0)\n```\n\nSo I think that equality tests will remain as they are now. Operations involving \"pure\" vectors may need more work, perhaps:\n\n```\nsage: N(1,0,0) + vector((1,0,0))\nN(2, 0, 0)\nsage: vector((1,0,0)) + N(1,0,0) \n(2, 0, 0)\n```\n\nalthough this does not bother me too much and I would suggest leaving this as is until we see where and how it can cause problems. (Making the second line return `N(2,0,0)` can be a bit tricky.)\n\nWill post a new patch once I figure out how to work with warnings (never used them before).",
    "created_at": "2010-06-06T03:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82931",
    "user": "novoselt"
}
```

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

archive/issue_comments_082932.json:
```json
{
    "body": "Reviewer's comments taken into account.",
    "created_at": "2010-06-06T04:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82932",
    "user": "novoselt"
}
```

Reviewer's comments taken into account.



---

archive/issue_comments_082933.json:
```json
{
    "body": "Attachment\n\nOK, I think I have addressed all the points in the original review except 2) which is pretty much impossible to realize completely (originally I was thinking of (1,1,1) as vectors, but they are just tuples, see the above comment for vector behaviour in this situation). I have added a general warning about tuples in the main `ToricLattice` documentation.\n\nI added `__contains__` to `ToricLattice`, since I discovered that the inherited implementation is not suitable.\n\nI added `__contains__`, `_contains`, and `contains` to cones. The real job is done in `_contains`, two others call it. The reason for the third function is an attempt to make warnings show where the actual potential mistake was, which requires the same calling depth. Unfortunately, in my tests it worked as I wanted only if it was triggered by some library code, in the notebook for created functions and attached files it just shows `main`. But that may change and maybe the terminal behaves differently. Now `cone.contains(stuff)` will try its best to return `True` by interpreting `stuff` as a point in the ambient space of `cone`, i.e. in `cone.lattice().base_extend(RR)`. However, it will catch points from foreign lattices first and return `False` with a warning, visible the first time for each location.\n\nThat's how reviewer's code works with the new version of the patch:\n\n```\nsage: octant = Cone([(1,0,0), (0,1,0), (0,0,1)]) \nsage: N = octant.lattice()\nsage: n = N(1,1,1)\nsage: n.set_immutable()\nsage: n in octant # True was desired\nTrue\nsage: (1,0,0) in octant # True was desired\nTrue\nsage: N(1,0,0) in octant.rays()  # was and should be True\nTrue\nsage: n = N(1,0,0)\nsage: n.set_immutable()\nsage: n in octant.ray_set()  # was and should be True\nTrue\nsage: M = N.dual()\nsage: M(1,0,0) == N(1,0,0)   # Error was desired\nFalse\nsage: (1,0,0) == N(1,0,0)    # True was desired, but difficult to get\nFalse\nsage: M(1,0,0) == (1,0,0)    # True was desired, but difficult to get\nFalse\nsage: (1,0,0) == (1,0,0)     # works as expected\nTrue\nsage: (1,0,0) in octant.rays()  # True was desired, but difficult to get\nFalse\nsage: M(1,0,0) in octant.rays()  # Error was desired\nFalse\nsage: cone = Cone([[1,0],[0,1]])\nsage: (1,1) in cone # Was False\nTrue\nsage: M = cone.lattice().dual()\nsage: M(1,1) in cone # Now gives warning on the first attempt\n__main__:1: UserWarning: you have checked if a cone contains a point from another lattice, this is always False!\nFalse\n```\n\nI suppose two lines marked \"Error was desired\" can also give a warning the first time they are invoked, if we implement a custom `__eq__` in addition to `__cmp__` for `ToricLatticeElement`. Should this be done?",
    "created_at": "2010-06-06T05:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82933",
    "user": "novoselt"
}
```

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

archive/issue_comments_082934.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-06T05:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82934",
    "user": "novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082935.json:
```json
{
    "body": "I think the == comparison is not so critical, as it is the default python behavior to compare actual objects. Should not cause any confusion as long as one is somewhat familiar with Sage. So I'm happy with that.\n\nThe `Polyhedron` class already has a `contains()` method that tests for inclusion (I wrote it with toric varieties in mind :-).  `ConvexRationalPolyhedralCone._contains()` could have called that, saving a few lines of duplicate code. Not that big a deal, though. I'm happy to give it a positive review either way. Let me know what you think.",
    "created_at": "2010-06-06T13:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82935",
    "user": "vbraun"
}
```

I think the == comparison is not so critical, as it is the default python behavior to compare actual objects. Should not cause any confusion as long as one is somewhat familiar with Sage. So I'm happy with that.

The `Polyhedron` class already has a `contains()` method that tests for inclusion (I wrote it with toric varieties in mind :-).  `ConvexRationalPolyhedralCone._contains()` could have called that, saving a few lines of duplicate code. Not that big a deal, though. I'm happy to give it a positive review either way. Let me know what you think.



---

archive/issue_comments_082936.json:
```json
{
    "body": "Replying to [comment:15 vbraun]:\n> The `Polyhedron` class already has a `contains()` method that tests for inclusion (I wrote it with toric varieties in mind :-).  `ConvexRationalPolyhedralCone._contains()` could have called that, saving a few lines of duplicate code. Not that big a deal, though. I'm happy to give it a positive review either way. Let me know what you think.\n\nSo does `LatticePolytope` class, which was written with the same goal in mind ;-) As I have already complained somewhere, any calls to underlying `LatticePolytope` or `Polyhedron` objects can trigger system calls to other programs, which in many cases gives a huge overhead (compared to the rest of involved computations). So in this case I preferred to use a \"native\" way for cones to check if a point is inside. Of course, computing facet normals the first time will eventually call PALP to get facet normals of the corresponding polytope, but:\n\n1) there is a way to compute facet normals for a lot of polytopes (e.g. corresponding to all cones of a fan) with a single call to PALP, in which case the overhead is negligible;\n\n2) if a cone was pickled and unpickled, it definitely does not have polytope objects anymore, but it may still have facet normals, if they were computed before pickling;\n\n3) we may eventually write our own initial computation of facet normals at least in some cases, for example, for complete fans.\n\nRegarding 1) - the first call to `ReflexivePolytopes(3)` takes currently 5-10s. It reads a text file with vertices and then precomputes a bunch of stuff to save time later. Computing all this stuff without using group calls to PALP was taking about 15 minutes. I don't see any reasons why such calls cannot be done for Polyhedra, but I don't know how easy that would be. Do you think there is any point trying to implement it?\n\nTo summarize: please give a positive review to the present version ;-)",
    "created_at": "2010-06-06T16:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82936",
    "user": "novoselt"
}
```

Replying to [comment:15 vbraun]:
> The `Polyhedron` class already has a `contains()` method that tests for inclusion (I wrote it with toric varieties in mind :-).  `ConvexRationalPolyhedralCone._contains()` could have called that, saving a few lines of duplicate code. Not that big a deal, though. I'm happy to give it a positive review either way. Let me know what you think.

So does `LatticePolytope` class, which was written with the same goal in mind ;-) As I have already complained somewhere, any calls to underlying `LatticePolytope` or `Polyhedron` objects can trigger system calls to other programs, which in many cases gives a huge overhead (compared to the rest of involved computations). So in this case I preferred to use a "native" way for cones to check if a point is inside. Of course, computing facet normals the first time will eventually call PALP to get facet normals of the corresponding polytope, but:

1) there is a way to compute facet normals for a lot of polytopes (e.g. corresponding to all cones of a fan) with a single call to PALP, in which case the overhead is negligible;

2) if a cone was pickled and unpickled, it definitely does not have polytope objects anymore, but it may still have facet normals, if they were computed before pickling;

3) we may eventually write our own initial computation of facet normals at least in some cases, for example, for complete fans.

Regarding 1) - the first call to `ReflexivePolytopes(3)` takes currently 5-10s. It reads a text file with vertices and then precomputes a bunch of stuff to save time later. Computing all this stuff without using group calls to PALP was taking about 15 minutes. I don't see any reasons why such calls cannot be done for Polyhedra, but I don't know how easy that would be. Do you think there is any point trying to implement it?

To summarize: please give a positive review to the present version ;-)



---

archive/issue_comments_082937.json:
```json
{
    "body": "Oh I didn't notice that you use LatticePolytope/PALP to compute the facet normals. That limits the dimension a bit, but good enough for now. I think cython-izing `polyhedra` to call libcdd directly would be easy enough, but thats for the future :-)\n\nSo to summarize, I think the patch is ready for for inclusion. It also applies cleanly on top of Sage 4.4.3. Positive review.",
    "created_at": "2010-06-06T18:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82937",
    "user": "vbraun"
}
```

Oh I didn't notice that you use LatticePolytope/PALP to compute the facet normals. That limits the dimension a bit, but good enough for now. I think cython-izing `polyhedra` to call libcdd directly would be easy enough, but thats for the future :-)

So to summarize, I think the patch is ready for for inclusion. It also applies cleanly on top of Sage 4.4.3. Positive review.



---

archive/issue_comments_082938.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-06T18:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82938",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082939.json:
```json
{
    "body": "Thank you!\n\nDimension limit is exactly why I started using `Polyhedra`, however I didn't quite like the timings. For example, this is what I get on geom.math with toric patches applied:\n\n```\nsage: %time\nsage: o = lattice_polytope.octahedron(6) # no PALP calls\nCPU time: 0.00 s,  Wall time: 0.00 s\nsage: %time\nsage: len(o.faces()) # PALP call to get incidences (no Hasse diagram)\n6\nCPU time: 0.07 s,  Wall time: 0.13 s\nsage: %time\nsage: f = FaceFan(o)\nCPU time: 0.03 s,  Wall time: 0.06 s\nsage: %time\nsage: f.cone_lattice() # some calls to PALP\nFinite poset containing 730 elements\nCPU time: 0.18 s,  Wall time: 0.32 s\nsage: %time\nsage: p = Polyhedron(vertices=o.vertices().columns()) # almost all time is in cdd\nCPU time: 0.02 s,  Wall time: 3.84 s\nsage: %time\nsage: p.face_lattice() # all time in Sage\nFinite poset containing 730 elements\nCPU time: 8.36 s,  Wall time: 8.36 s\n```\n\n\nGiven the construction time of `p`, I am not even sure if calling cdd as a library will help a lot, but you mentioned that you also had some other library in mind. So while I am definitely interested in going to dimensions higher than 6, so far PALP seems to be the way to go. One possible modification for the future is to use PALP when possible and switch to alternatives when it does not work.",
    "created_at": "2010-06-06T19:27:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82939",
    "user": "novoselt"
}
```

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

archive/issue_comments_082940.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-01T16:24:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82940",
    "user": "novoselt"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_082941.json:
```json
{
    "body": "Attachment\n\nI made a systematic mistake in doctests of `__cmp__` methods of all patches, discovered in #9062. So now I am posting these one-line patches to fix them, please review!",
    "created_at": "2010-07-01T16:24:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82941",
    "user": "novoselt"
}
```

Attachment

I made a systematic mistake in doctests of `__cmp__` methods of all patches, discovered in #9062. So now I am posting these one-line patches to fix them, please review!



---

archive/issue_comments_082942.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-01T16:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82942",
    "user": "novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082943.json:
```json
{
    "body": "I noticed that, too. I haven't gotten around to fix it because I ran into this strange doctest failure in Sage-4.5alpha1 that worked beautifully in sage-4.4.4:\n\n```\nFile \"/home/vbraun/opt/sage-4.5.alpha1/devel/sage-main/sage/geometry/cone.py\", line 1535:\n    sage: c.faces()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/vbraun/opt/sage-4.5.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/vbraun/opt/sage-4.5.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/vbraun/opt/sage-4.5.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_33[10]>\", line 1, in <module>\n        c.faces()###line 1535:\n    sage: c.faces()\n      File \"/home/vbraun/opt/sage-4.5.alpha1/local/lib/python/site-packages/sage/geometry/cone.py\", line 1554, in faces\n        for level in self.face_lattice().level_sets())\n      File \"/home/vbraun/opt/sage-4.5.alpha1/local/lib/python/site-packages/sage/geometry/cone.py\", line 1433, in face_lattice\n        ray_to_facets, facet_to_rays, ConeFace)\n      File \"/home/vbraun/opt/sage-4.5.alpha1/local/lib/python/site-packages/sage/geometry/cone.py\", line 2259, in hasse_diagram_from_incidences\n        for atom, coatoms in enumerate(atom_to_coatoms))\n      File \"/home/vbraun/opt/sage-4.5.alpha1/local/lib/python/site-packages/sage/geometry/cone.py\", line 2259, in <genexpr>\n        for atom, coatoms in enumerate(atom_to_coatoms))\n    KeyError: (frozenset([0]), frozenset([0]))\n```\n\nAndrey, since its your code maybe you'll understand what is going on.",
    "created_at": "2010-07-01T16:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82943",
    "user": "vbraun"
}
```

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

archive/issue_comments_082944.json:
```json
{
    "body": "Thanks for finding it, will work on!",
    "created_at": "2010-07-01T16:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82944",
    "user": "novoselt"
}
```

Thanks for finding it, will work on!



---

archive/issue_comments_082945.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-01T16:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82945",
    "user": "novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082946.json:
```json
{
    "body": "I have finally built a copy of 4.5.alpha1 on geom.math and cannot reproduce this error, all tests passed. The error message above does not make any sense to me - how can a `KeyError` appear during enumeration of a list? Do you get the same error consistently every time? What configuration are you testing it on? Did you build 4.5.alpha1 from scratch? I will also run tests on my own computer, but it will take a few more hours to finish the build.",
    "created_at": "2010-07-01T22:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82946",
    "user": "novoselt"
}
```

I have finally built a copy of 4.5.alpha1 on geom.math and cannot reproduce this error, all tests passed. The error message above does not make any sense to me - how can a `KeyError` appear during enumeration of a list? Do you get the same error consistently every time? What configuration are you testing it on? Did you build 4.5.alpha1 from scratch? I will also run tests on my own computer, but it will take a few more hours to finish the build.



---

archive/issue_comments_082947.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-02T02:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82947",
    "user": "novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082948.json:
```json
{
    "body": "I installed 4.5.alpha1 on my machine (although it is not extremely different from geom: quite fresh Ubuntu 10.4 64bit running in a VirtualBox) and still don't have any issues...\n\nBy the way, I just noticed that the lines shown in the above exception do not exist in the patch on this ticket. Cone module is severely altered by the next ticket, in particular the Hasse diagram function was changed. Could it be that you accidentally skipped rebuilding sage after popping/pushing some patches of the sequence? That would probably lead to errors, although I would expect much more than one and with more sensible messages...\n\nAnyway, I claim that this ticket works fine for me on top of 4.5.alpha1, as well as others in the sequence.",
    "created_at": "2010-07-02T02:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82948",
    "user": "novoselt"
}
```

I installed 4.5.alpha1 on my machine (although it is not extremely different from geom: quite fresh Ubuntu 10.4 64bit running in a VirtualBox) and still don't have any issues...

By the way, I just noticed that the lines shown in the above exception do not exist in the patch on this ticket. Cone module is severely altered by the next ticket, in particular the Hasse diagram function was changed. Could it be that you accidentally skipped rebuilding sage after popping/pushing some patches of the sequence? That would probably lead to errors, although I would expect much more than one and with more sensible messages...

Anyway, I claim that this ticket works fine for me on top of 4.5.alpha1, as well as others in the sequence.



---

archive/issue_comments_082949.json:
```json
{
    "body": "Just a remark: it works fine for me as well, 4.5.alpha1 on 64-bit SuSE Linux, as long as I have #9062 installed. Volker: could you tell us exactly what setup you were using when it didn't work for you, and what patches you did/did not have installed at the time?",
    "created_at": "2010-07-02T09:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82949",
    "user": "davidloeffler"
}
```

Just a remark: it works fine for me as well, 4.5.alpha1 on 64-bit SuSE Linux, as long as I have #9062 installed. Volker: could you tell us exactly what setup you were using when it didn't work for you, and what patches you did/did not have installed at the time?



---

archive/issue_comments_082950.json:
```json
{
    "body": "I rebuilt 4.5.alpha1 overnight and it works now. Not sure what caused the problem. I can't rule out that I forgot to rebuild and/or some patch. Another possible problem was that I originally used parallel make for sage which died half way through because of a missing file. Since restarting the compilation succeeded, I had assumed that everything built OK. \n\nIn any case, the toric code works so I'll set it back to `positive_review`.",
    "created_at": "2010-07-02T10:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82950",
    "user": "vbraun"
}
```

I rebuilt 4.5.alpha1 overnight and it works now. Not sure what caused the problem. I can't rule out that I forgot to rebuild and/or some patch. Another possible problem was that I originally used parallel make for sage which died half way through because of a missing file. Since restarting the compilation succeeded, I had assumed that everything built OK. 

In any case, the toric code works so I'll set it back to `positive_review`.



---

archive/issue_comments_082951.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-02T10:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82951",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082952.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T08:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82952",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_082953.json:
```json
{
    "body": "One or more of #8986, #8987, and #9062 *may* cause the doctest failures listed at #9590.",
    "created_at": "2010-07-24T02:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8986#issuecomment-82953",
    "user": "mpatel"
}
```

One or more of #8986, #8987, and #9062 *may* cause the doctest failures listed at #9590.
