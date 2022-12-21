# Issue 6484: sage.combinat.ranker improvements

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-07-08 16:48:08

Assignee: nthiery

CC:  sage-combinat tscrim hivert virmaux

Keywords: rank, unrank

sage.combinat.ranker needs improvements:
 -  With:
    {{{
    sage: f = sage.combinat.ranker.rank_from_list([...]) 
    }}}

    f uses list.index, and is therefore O(n). This should be made O(1) with a hash table.

 - The rank / unrank objects produced by this library should be picklable.

 - ...?

patch under construction on the sage-combinat patch server.


---

Comment by nthiery created at 2015-04-27 17:27:17

Changing status from new to needs_review.


---

Comment by nthiery created at 2015-04-27 17:27:17

New commits:


---

Comment by nthiery created at 2015-04-27 17:28:02

This is essentially ``trac_6484-ranker-improvements-nt.patch`` from the Sage-Combinat queue, with further cleanup and doc.


---

Comment by nthiery created at 2015-04-27 17:29:10

Should we worry about backward compatibility and revert to l.index if any of the object is not hashable?


---

Comment by nthiery created at 2015-04-27 17:32:27

How much do we care about picklability right now? I am not sure how to implement it. On the other hand, fast rank would be very useful for #18311, ...


---

Comment by tscrim created at 2015-04-27 17:46:56

I'm okay with the hashability as we assume all elements to be hashable, nor is picklability important to me. However this now makes `rank_from_list` to be the `O(n)` function, and the function itself is not cached. So for large lists (or worse, say for a crystal where iteration is relatively expensive), this could lead to a pretty large slowdown. How about we just return the original implementation of `rank` as a cached function?


---

Comment by nthiery created at 2015-04-27 20:06:46

I Travis!

Replying to [comment:11 tscrim]:
> I'm okay with the hashability as we assume all elements to be hashable

Well, this hashabilitiy assumption was not there before this ticket. So technically speaking that's a backward incompatible change. I agree that in all use cases I can think of, the objects are hashable, so it probably is not a big deal.

>, nor is picklability important to me. However this now makes `rank_from_list` to be the `O(n)` function, and the function itself is not cached. So for large lists (or worse, say for a crystal where iteration is relatively expensive), this could lead to a pretty large slowdown. How about we just return the original implementation of `rank` as a cached function?

When `rank_from_list` is called, that's usually with the intention of calling it intensively afterward; in particular the ranker is typically stored in the calling object for all later reuse. At least, that's the case in all the current calls in the Sage library.

Being completely lazy and implementhing `rank_from_list` as a cached function on top of `list.index` would imply an overhead of `O(n^2)` instead of `O(n)` before we reach the limit state where the complexity in `O(1)`; not great. We could introduce some partial lazyness, making sure that the first time an object `x` is looked up, the cache is set for all objects before `x` in the list. What do you think? Is it worth it?

A note: the name `from_list` makes it relatively explicit that the iterable will be expanded anyway.

Cheers,
                          Nicolas


---

Comment by git created at 2015-04-27 20:22:15

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by nthiery created at 2015-04-27 20:23:38

This should fix the single error reported by the patchbot.


---

Comment by tscrim created at 2015-04-28 04:59:57

True, that would end up being `O(n^2)`. Since this seems to only be used in 2 places, `combinat.free_module.py` and `sets.finite_set_maps.py`, and in both places, the resulting function is cached, I think this would be okay as is. However, would you mind putting a warning about repeatedly recreating the function?


---

Comment by vdelecroix created at 2015-04-28 21:18:04

You know that with ``@`cached_function` instead of a plain dictionary you are building a 2-tuple containg a tuple enclosing the object and an empty tuple?

```
sage: r = rank_from_list(range(10))
sage: r.get_cache()
{((0,), ()): 0,
 ((1,), ()): 1,
 ((2,), ()): 2,
 ((3,), ()): 3,
 ((4,), ()): 4,
 ((5,), ()): 5,
 ((6,), ()): 6,
 ((7,), ()): 7,
 ((8,), ()): 8,
 ((9,), ()): 9}
```


What is wrong with

```
def rank_from_list(l):
    my_dict = {j:i for i,j in enumerate(l)}
    def rank(i):
        return my_dict[i]
```

It is not very clean, but at least cleaner. And also faster by the way.

Vincent


---

Comment by nthiery created at 2015-04-30 07:55:51

Ah, good point; I thought our cached functions had a special case for
one parameter functions. Other than that, using a cached function was
mostly a (failed) attempt at having something picklable as well.

So, let's see about speed with various implementations:

```
sage: l = range(100);
sage: d = { x:i for i,x in enumerate(l) }
sage: `@`cached_function
....: def rank_cached(): pass
sage: for i,x in enumerate(l):
....:     rank_cached.set_cache(i, x)
sage: def rank_dict(x):
....:     return d[x]
sage: rank_dict_getitem = d.__getitem__

sage: cython("""
l = range(100);
d = { x:i for i,x in enumerate(l) }
cpdef int rank_dict_cython(x):
    return d[x]
""")
sage: cython("""
l = range(100);
d = { x:i for i,x in enumerate(l) }
cpdef int rank_dict_cython_exception(x):
    try:
        return d[x]
    except KeyError:
        raise ValueError("%s is not blah blah blah"%x)
""")

sage: cython("""
cdef class RankFromList(dict):
    def __call__(self, x):
        try:
            return self[x]
        except KeyError:
            raise ValueError("%s is not blah blah blah"%x)
""")
sage: rank_dict_cython_class = RankFromList((x,i) for i,x in enumerate(l))
```


Here are the timings, in decreasing order:

```
sage: sage: %timeit rank_cached(50)
The slowest run took 41.96 times longer than the fastest. This could mean that an intermediate result is being cached 
1000000 loops, best of 3: 381 ns per loop
sage: sage: %timeit rank_dict(50)
The slowest run took 15.56 times longer than the fastest. This could mean that an intermediate result is being cached 
1000000 loops, best of 3: 245 ns per loop
sage: sage: %timeit rank_dict_cython_class(50)
The slowest run took 22.12 times longer than the fastest. This could mean that an intermediate result is being cached 
1000000 loops, best of 3: 226 ns per loop
sage: sage: %timeit rank_dict_cython_exception(50)
The slowest run took 36.63 times longer than the fastest. This could mean that an intermediate result is being cached 
1000000 loops, best of 3: 195 ns per loop
sage: sage: %timeit rank_dict_cython(50)
The slowest run took 31.18 times longer than the fastest. This could mean that an intermediate result is being cached 
1000000 loops, best of 3: 191 ns per loop
sage: sage: %timeit rank_dict_getitem(50)
The slowest run took 17.96 times longer than the fastest. This could mean that an intermediate result is being cached 
1000000 loops, best of 3: 173 ns per loop
```


Those timing seem to be consistent from one call to the other. Most of
the time this feature is used with non trivial objects where the
bottleneck is the computation of hash/equality of the objects. So we
don't necessarily need to optimize to the last bit.

In view of the above, the fastest is to return the `__getitem__`
method of the dictionary. The main caveat is that we don't have
control on the exception (a `KeyError` instead of a
`ValueError`). Maybe it is not so bad since a `KeyError` is a special
kind of `ValueError`.

The most flexible is to use a class. In particular, this would make
the ranker picklable (this can be useful: I have had cases where an
object would not pickle properly because one of it's attribute was a
ranker). This also opens the door for reintroducing laziness later
on. It's 30% slower than `getitem` which could be acceptable (I was in
fact expecting a smaller overhead; maybe I missed something in the
cythonization).

What do you think?

Cheers,
                         Nicolas


---

Comment by vdelecroix created at 2015-04-30 08:33:37

If pickling is an issue then I would go for `cdef class RankFromList` but with a more appropriated name. It is not possible to set `tp_getitem = tp_call` since the signatures are different.

If you create a Cython class, then please replace the `sage.combinat.words.morphism.CallableDict` with the new one.

Vincent


---

Comment by git created at 2015-05-03 23:17:33

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-05-03 23:30:48

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-05-03 23:39:53

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2015-05-04 06:24:33

Changing status from needs_review to needs_info.


---

Comment by vdelecroix created at 2015-05-04 06:24:33

Hello,

The final picture looks good. One good thing would be to clean the git history.

The fastest way to create a dictionary from a list is

```
cdef dict d = {x:i for i,x in enumerate(l)}
```

I guess it avoids the creation of the pair `(i,x)`.

The documentation can be more precise

```
No error is issued in case of duplicate value in ``l``. Instead,
the rank function returns the position of some of the duplicates::
```

The rank of the *last value* is returned not just *some*. It would possible to use `PyDict_MergeFromSeq2` to return the first though. But it is not clear to me that it is what we want.

Sided note: I am pretty sure that with #18330 that something better can be done so that `__call__` becomes as fast as `__getitem__` (up to a C function call). But not for this ticket.

Vincent


---

Comment by git created at 2015-05-04 20:30:12

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by nthiery created at 2015-05-04 20:31:14

Replying to [comment:22 vdelecroix]:
> The fastest way to create a dictionary from a list is
> {{{
> cdef dict d = {x:i for i,x in enumerate(l)}
> }}}
> I guess it avoids the creation of the pair `(i,x)`.

I hesitated about this; however we are creating a `CallableDict` not a
dict at the end. So using this notation means we are first
constructing a dictionary and then copying it into the `CallableDict`.
This is indeed slightly faster for lists of trivial objects:


```
sage: l = range(1000)
sage: %timeit rank_from_list(l)           # using generator expression
1000 loops, best of 3: 145 µs per loop

sage: %timeit rank_from_list(l)           # using {...}
10000 loops, best of 3: 109 µs per loop
```


But not anymore for lists of objects with non trivial hash/eq:

```
sage: l = list(Permutations(8))
sage: %timeit rank_from_list(l)           # using generator expression
The slowest run took 10.96 times longer than the fastest. This could mean that an intermediate result is being cached 
1 loops, best of 3: 18.8 ms per loop

sage: %timeit rank_from_list(l)           # using {..}
The slowest run took 10.08 times longer than the fastest. This could mean that an intermediate result is being cached 
1 loops, best of 3: 21.7 ms per loop
```


Note that we can hope for the generator expression to be optimized in
the long run when ranker.py will be cythonized.

> The documentation can be more precise
> {{{
> No error is issued in case of duplicate value in ``l``. Instead,
> the rank function returns the position of some of the duplicates::
> }}}
> The rank of the *last value* is returned not just *some*.

This is on purpose: I don't want to set this behavior in stone, in
order to leave room for future reimplementations. In any cases it's
explicitly said that this function is meant for lists without
duplicates.

> Sided note: I am pretty sure that with #18330 that something better can be done so that `__call__` becomes as fast as `__getitem__` (up to a C function call). But not for this ticket.

Great!
----
New commits:


---

Comment by vdelecroix created at 2015-05-05 06:50:35


```
sage -t --long src/sage/sets/finite_set_map_cy.pyx
**********************************************************************
File "src/sage/sets/finite_set_map_cy.pyx", line 491,
in sage.sets.finite_set_map_cy.FiniteSetMap_Set.setimage
Failed example:
    with fs.clone() as fs3:
          fs3.setimage("z", 2)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: 'z' is not in list
Got:
    Traceback (most recent call last):
    ....
    ValueError: 'z' is not in dict
**********************************************************************
File "src/sage/sets/finite_set_map_cy.pyx", line 497,
in sage.sets.finite_set_map_cy.FiniteSetMap_Set.setimage
Failed example:
    with fs.clone() as fs3:
          fs3.setimage(1, 4)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: 1 is not in list
Got:
    Traceback (most recent call last):
    ...
    ValueError: 1 is not in dict
```



---

Comment by vdelecroix created at 2015-05-05 06:50:35

Changing status from needs_info to needs_work.


---

Comment by git created at 2015-05-05 08:25:07

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by nthiery created at 2015-05-05 08:27:50

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2015-05-05 08:27:50

Ah, shoot, I knew I had to update the doctests there ... Thanks for the report. Fixed!

Speaking of patchbot blues: do we care about lazy importing the module? Or should it be `words` and `ranker` that should be lazy imported in the first place? Also, I am surprised about the warning about non ascii character given that I declared the encoding of the file to be utf-8.


---

Comment by nthiery created at 2015-05-05 08:41:08

For the record: I opened an issue about the false positive report by the ascii plugin of the patchbot: https://github.com/robertwb/sage-patchbot/issues/65


---

Comment by vdelecroix created at 2015-05-05 14:16:07

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-05-06 21:03:26

Resolution: fixed
