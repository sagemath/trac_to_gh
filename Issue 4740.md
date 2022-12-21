# Issue 4740: Fix memory leak in finite field coercion

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-12-08 11:23:21

Assignee: robertwb

CC:  burcin robertwb simonking

Burcin reported at #4639:

```
sage: F = GF(13)
sage: get_memory_usage()
708.02734375
sage: for _ in xrange(10000):
....:     t = F.coerce(F(234234))
....:     
sage: get_memory_usage()
728.15234375
sage: for _ in xrange(100000):
    t = F.coerce(F(234234))
....:     
sage: get_memory_usage()
932.3125
sage: for _ in xrange(100000):
    t = F.coerce(F(234234))
....:     
sage: get_memory_usage()
1136.35546875
```

Since the patch by RobertWB at that ticket fixes the issue Burcin reported, but not the original one I am moving it over to this ticket.

Cheers,

Michael


---

Attachment

Patch by RobertWB, originally from #4639


---

Comment by mabshoff created at 2008-12-08 11:28:57

Patch by RobertWB, review by William. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-08 11:52:40

This patch causes a failure with the pickle jar:

```
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/structure/sage_object.pyx", line 371, in __main__.example_16
Failed example:
    sage.structure.sage_object.unpickle_all(std)###line 682:_sage_    >>> sage.structure.sage_object.unpickle_all(std)
Expected:
    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    ** failed:  _class__sage_rings_finite_field_morphism_FiniteFieldHomset__.sobj
    Failed:
    _class__sage_rings_finite_field_morphism_FiniteFieldHomset__.sobj
    Successfully unpickled 453 objects.
    Failed to unpickle 1 objects.
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_16
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-12-15 18:42:48

Once the pickling issue is fixed this should go in.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-15 18:42:48

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-12-21 00:53:34

Robert,

the leak seems to be gone in 3.2.2:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: F = GF(13)
sage: get_memory_usage()
689.02734375
sage: for _ in xrange(10000):
....:     t = F.coerce(F(234234))
....:     
sage: get_memory_usage()
689.02734375
sage: for _ in xrange(100000):
....:     t = F.coerce(F(234234))
....:     
sage: get_memory_usage()
689.02734375
sage: for _ in xrange(100000):
....:     t = F.coerce(F(234234))
....:     
sage: get_memory_usage()
689.02734375
sage: 
```

Should we close this ticket as won't fix or is the patch her still relevant? In that case we should update the ticket to reflect the actual issue being fixed here.
| Sage Version 3.2.2, Release Date: 2008-12-18                       |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael


---

Comment by robertwb created at 2008-12-21 09:57:41

Changing priority from blocker to major.


---

Comment by robertwb created at 2008-12-21 09:57:41

The patch is still relevant here. What is going on is every time coerce is called, a new homset is created. Creating a new homset doesn't leak anymore, but it's still sub-optimal. 

I don't know that I'll have time to look into this anytime soon, but it's not a blocker anymore as the leak is solved elsewhere.


---

Comment by mabshoff created at 2008-12-21 09:59:53

ok, 

I renamed the ticket then.

Cheers,

Michael


---

Comment by SimonKing created at 2010-06-14 08:30:44

Hi Robert,

accidentally I found this rather old ticket.

Replying to [comment:5 robertwb]:
> The patch is still relevant here. What is going on is every time coerce is called, a new homset is created. Creating a new homset doesn't leak anymore, but it's still sub-optimal. 

Is this still the case? In what situation is the homset created? Is it not cached? In what files does it occur?

Cheers,
Simon


---

Comment by mderickx created at 2011-01-08 01:00:34

I also found this ticket. It could be very well that this is still causing memory leaks. Look for example at the reference chain that is keeping ModularSymbols alive at #10548


---

Comment by mhansen created at 2013-07-22 15:10:29

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2013-07-22 15:10:29

I think homesets are still created each time.  We could try the following patch which does fix the issue.  The timings also improved:

Before:

```
sage: %timeit t = F.coerce(F(234234))
10000 loops, best of 3: 197 us per loop
```


After:

```
sage: %timeit t = F.coerce(F(234234))
10000 loops, best of 3: 23.4 us per loop
```


Simon -- see any issues here?


---

Attachment

Apply trac_4740.patch


---

Comment by SimonKing created at 2013-07-22 16:40:25

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2013-07-22 16:40:25

Replying to [comment:9 mhansen]:
> Simon -- see any issues here?

Yes, and a quite severe issue.

The problem is, as often, unique versus non-unique parent structures. For coercion, we need that the domain and codomain of a coercion from A to B are not just equal but identical to A and B. But with `UniqueRepresentation`, the given input arguments are compared by equality, not by identity. That's why it was a conscious decision to use `TripleDict` for caching homsets.

The cache is provided by the `Hom()` function in sage.categories.homset. If homsets are really created over and over again, then there seems to be a rogue call to `Homset(...)`. The solution is not to make `Homset` a cached class, but to call the `Hom()` function instead.


---

Comment by SimonKing created at 2013-07-22 16:44:06

PS: For the same reason I don't like Robert's original patch.

I think we should first find out where the homset constructor is called when Hom should be called instead.


---

Comment by SimonKing created at 2013-07-22 16:53:36

Interesting. I found the following, by inserting a print statement into `Homset.__init__`:

```
sage: F = GF(13)
sage: x = F(234234)
calling Homset Integer Ring Finite Field of size 13 Category of euclidean domains
sage: x = F(234234)   # the homset is created only once, which is fine
sage: t = F.coerce(F(234234))   # there is a homset created...
calling Homset Finite Field of size 13 Finite Field of size 13 Category of rings
sage: t = F.coerce(F(234234))   # ... repeatedly
calling Homset Finite Field of size 13 Finite Field of size 13 Category of rings
sage: t = F.coerce(F(234234))
calling Homset Finite Field of size 13 Finite Field of size 13 Category of rings
sage: I = F.coerce_map_from(F)  # creating a coerce map, the homset is created again, but...
calling Homset Finite Field of size 13 Finite Field of size 13 Category of rings
sage: t = F.coerce(F(234234))   # ... now the problem is fixed!
sage: t = F.coerce(F(234234))
```


This seems to suggest that
 1. `F.coerce` seems to use a cached coerce map from F to F, but if it isn't cached, it would create the coerce map repeatedly.
 2. It re-creates the coercion map such that the parent of the coercion map is re-created as well.


---

Comment by SimonKing created at 2013-07-22 17:13:45

I just tried to use `trace("F.coerce(x)")` to see what happens. And now, it seems to me that `Hom()` is called as it should---but its cache is broken, for a reason that I don't understand.


---

Comment by SimonKing created at 2013-07-22 17:21:14

I found the problem!!

The homset is stored in the cache, but it is then immediately erased again. Apparently, a strong reference to the homset is missing.


---

Comment by SimonKing created at 2013-07-22 17:26:07

Next observation: If one creates

```
sage: I = F.coerce_map_from(F)
```

and then does `del I`, the homset is again erased from the cache.

But this must not happen! Namely, `F.coerce_map_from(...)` is supposed to use a cache. Granted, the cache is again using weak keys (via `MonoDict`), but as long as `F` is kept in memory, the coercion from F to F must not vanish.


---

Comment by SimonKing created at 2013-07-22 17:34:47

Look at the following snippet from `Parent.coerce_map_from(self,S)`:

```python
        if S == self:
            # non-unique parents
            if unique_parent_warnings:
                print "Warning: non-unique parents %s"%(type(S))
            return self._generic_convert_map(S)
```

`self._generic_convert_map(S)` does not do caching.

Hence, the general problem is: A coercion from self to self will never be cached.


---

Comment by SimonKing created at 2013-07-22 17:37:30

I see two potential solutions, and the "info" I am seeking is: What would you prefer?

We could

 1. let `F.coerce_map_from(F)` use the cache (I think this is what I would prefer), or
 2. let `F.coerce(x)` avoid creating a morphism, if the parent of x is F.

It might even make sense to do both, 2. for efficiency.


---

Comment by SimonKing created at 2013-07-22 17:37:30

Changing status from needs_work to needs_info.


---

Comment by SimonKing created at 2013-07-22 18:06:29

I didn't notice that `self.coerce_map_from(S)` also has a special case when `S is self`. However, the result is again not cached.

```python
        if S is self:
            from sage.categories.homset import Hom
            return Hom(self, self).identity()
```



---

Comment by SimonKing created at 2013-07-22 18:11:54

Replying to [comment:19 SimonKing]:
>  2. let `F.coerce(x)` avoid creating a morphism, if the parent of x is F.

Hm. On second thought, do we really want that `F.coerce(x) is x`? I guess it is better to preserve the current behaviour and return a copy of x.


---

Comment by SimonKing created at 2013-07-22 18:25:29

Changing status from needs_info to needs_review.


---

Comment by SimonKing created at 2013-07-22 18:25:29

What do people think about the patch that I just attached?

We now have

```
sage: F = GF(13)
sage: F.coerce_map_from(F) is F.coerce_map_from(F)
True
sage: x = F(234234)
sage: %timeit t = F.coerce(x)
1000000 loops, best of 3: 862 ns per loop
```

and used to have

```
sage: F = GF(13)
sage: F.coerce_map_from(F) is F.coerce_map_from(F)
False
sage: x = F(234234)
sage: %timeit t = F.coerce(x)
10000 loops, best of 3: 132 us per loop
```


Apply trac4740-cache_coerce_from_self.patch​


---

Comment by SimonKing created at 2013-07-22 18:27:43

PS: The memleak in the ticket description has already been fixed elsewhere, this is now only about efficiency.


---

Comment by SimonKing created at 2013-07-22 19:11:36

It seems that the patchbot tries to apply both patches. Trying to get it right:

Apply trac4740-cache_coerce_from_self.patch​


---

Comment by SimonKing created at 2013-07-22 20:07:39

For the record: All tests pass, and I really don't see why the patchbot is trying to apply _two_ patches.


---

Comment by mhansen created at 2013-07-23 00:16:38

Your changes look good to me.  I knew the patch I posted was probably dodgy, but you'd be the one who'd have the best grasp on it.

Thanks!


---

Comment by mhansen created at 2013-07-23 00:16:38

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-16 21:37:56

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-08-16 21:37:56

This needs to be rebased to sage-5.12.beta0 + #14516 + #14519.


---

Attachment

Cache coercion from self to self


---

Comment by SimonKing created at 2013-08-17 07:53:02

Done! The only change concerns the new syntax for debug options. I guess I may revert to "positive review".

Apply trac4740-cache_coerce_from_self.patch​


---

Comment by SimonKing created at 2013-08-17 07:53:02

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-08-20 12:56:42

Resolution: fixed
