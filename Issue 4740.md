# Issue 4740: Fix memory leak in finite field coercion

archive/issues_004740.json:
```json
{
    "body": "Assignee: robertwb\n\nCC:  burcin robertwb simonking\n\nBurcin reported at #4639:\n\n```\nsage: F = GF(13)\nsage: get_memory_usage()\n708.02734375\nsage: for _ in xrange(10000):\n....:     t = F.coerce(F(234234))\n....:     \nsage: get_memory_usage()\n728.15234375\nsage: for _ in xrange(100000):\n    t = F.coerce(F(234234))\n....:     \nsage: get_memory_usage()\n932.3125\nsage: for _ in xrange(100000):\n    t = F.coerce(F(234234))\n....:     \nsage: get_memory_usage()\n1136.35546875\n```\n\nSince the patch by RobertWB at that ticket fixes the issue Burcin reported, but not the original one I am moving it over to this ticket.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4740\n\n",
    "created_at": "2008-12-08T11:23:21Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "title": "Fix memory leak in finite field coercion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4740",
    "user": "mabshoff"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/4740





---

archive/issue_comments_035790.json:
```json
{
    "body": "Attachment [trac_4740_coerce-leak.patch](tarball://root/attachments/some-uuid/ticket4740/trac_4740_coerce-leak.patch) by mabshoff created at 2008-12-08 11:25:06\n\nPatch by RobertWB, originally from #4639",
    "created_at": "2008-12-08T11:25:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35790",
    "user": "mabshoff"
}
```

Attachment [trac_4740_coerce-leak.patch](tarball://root/attachments/some-uuid/ticket4740/trac_4740_coerce-leak.patch) by mabshoff created at 2008-12-08 11:25:06

Patch by RobertWB, originally from #4639



---

archive/issue_comments_035791.json:
```json
{
    "body": "Patch by RobertWB, review by William. \n\nCheers,\n\nMichael",
    "created_at": "2008-12-08T11:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35791",
    "user": "mabshoff"
}
```

Patch by RobertWB, review by William. 

Cheers,

Michael



---

archive/issue_comments_035792.json:
```json
{
    "body": "This patch causes a failure with the pickle jar:\n\n```\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/structure/sage_object.pyx\", line 371, in __main__.example_16\nFailed example:\n    sage.structure.sage_object.unpickle_all(std)###line 682:_sage_    >>> sage.structure.sage_object.unpickle_all(std)\nExpected:\n    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.\n    Successfully unpickled ... objects.\n    Failed to unpickle 0 objects.\nGot:\n    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.\n    ** failed:  _class__sage_rings_finite_field_morphism_FiniteFieldHomset__.sobj\n    Failed:\n    _class__sage_rings_finite_field_morphism_FiniteFieldHomset__.sobj\n    Successfully unpickled 453 objects.\n    Failed to unpickle 1 objects.\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_16\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-12-08T11:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35792",
    "user": "mabshoff"
}
```

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

archive/issue_comments_035793.json:
```json
{
    "body": "Once the pickling issue is fixed this should go in.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-15T18:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35793",
    "user": "mabshoff"
}
```

Once the pickling issue is fixed this should go in.

Cheers,

Michael



---

archive/issue_comments_035794.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-12-15T18:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35794",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_035795.json:
```json
{
    "body": "Robert,\n\nthe leak seems to be gone in 3.2.2:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: F = GF(13)\nsage: get_memory_usage()\n689.02734375\nsage: for _ in xrange(10000):\n....:     t = F.coerce(F(234234))\n....:     \nsage: get_memory_usage()\n689.02734375\nsage: for _ in xrange(100000):\n....:     t = F.coerce(F(234234))\n....:     \nsage: get_memory_usage()\n689.02734375\nsage: for _ in xrange(100000):\n....:     t = F.coerce(F(234234))\n....:     \nsage: get_memory_usage()\n689.02734375\nsage: \n```\n\nShould we close this ticket as won't fix or is the patch her still relevant? In that case we should update the ticket to reflect the actual issue being fixed here.\n| Sage Version 3.2.2, Release Date: 2008-12-18                       |\n| Type notebook() for the GUI, and license() for information.        |\nCheers,\n\nMichael",
    "created_at": "2008-12-21T00:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35795",
    "user": "mabshoff"
}
```

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

archive/issue_comments_035796.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2008-12-21T09:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35796",
    "user": "robertwb"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_035797.json:
```json
{
    "body": "The patch is still relevant here. What is going on is every time coerce is called, a new homset is created. Creating a new homset doesn't leak anymore, but it's still sub-optimal. \n\nI don't know that I'll have time to look into this anytime soon, but it's not a blocker anymore as the leak is solved elsewhere.",
    "created_at": "2008-12-21T09:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35797",
    "user": "robertwb"
}
```

The patch is still relevant here. What is going on is every time coerce is called, a new homset is created. Creating a new homset doesn't leak anymore, but it's still sub-optimal. 

I don't know that I'll have time to look into this anytime soon, but it's not a blocker anymore as the leak is solved elsewhere.



---

archive/issue_comments_035798.json:
```json
{
    "body": "ok, \n\nI renamed the ticket then.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-21T09:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35798",
    "user": "mabshoff"
}
```

ok, 

I renamed the ticket then.

Cheers,

Michael



---

archive/issue_comments_035799.json:
```json
{
    "body": "Hi Robert,\n\naccidentally I found this rather old ticket.\n\nReplying to [comment:5 robertwb]:\n> The patch is still relevant here. What is going on is every time coerce is called, a new homset is created. Creating a new homset doesn't leak anymore, but it's still sub-optimal. \n\nIs this still the case? In what situation is the homset created? Is it not cached? In what files does it occur?\n\nCheers,\nSimon",
    "created_at": "2010-06-14T08:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35799",
    "user": "SimonKing"
}
```

Hi Robert,

accidentally I found this rather old ticket.

Replying to [comment:5 robertwb]:
> The patch is still relevant here. What is going on is every time coerce is called, a new homset is created. Creating a new homset doesn't leak anymore, but it's still sub-optimal. 

Is this still the case? In what situation is the homset created? Is it not cached? In what files does it occur?

Cheers,
Simon



---

archive/issue_comments_035800.json:
```json
{
    "body": "I also found this ticket. It could be very well that this is still causing memory leaks. Look for example at the reference chain that is keeping ModularSymbols alive at #10548",
    "created_at": "2011-01-08T01:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35800",
    "user": "mderickx"
}
```

I also found this ticket. It could be very well that this is still causing memory leaks. Look for example at the reference chain that is keeping ModularSymbols alive at #10548



---

archive/issue_comments_035801.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-07-22T15:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35801",
    "user": "mhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_035802.json:
```json
{
    "body": "I think homesets are still created each time.  We could try the following patch which does fix the issue.  The timings also improved:\n\nBefore:\n\n```\nsage: %timeit t = F.coerce(F(234234))\n10000 loops, best of 3: 197 us per loop\n```\n\n\nAfter:\n\n```\nsage: %timeit t = F.coerce(F(234234))\n10000 loops, best of 3: 23.4 us per loop\n```\n\n\nSimon -- see any issues here?",
    "created_at": "2013-07-22T15:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35802",
    "user": "mhansen"
}
```

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

archive/issue_comments_035803.json:
```json
{
    "body": "Attachment [trac_4740.patch](tarball://root/attachments/some-uuid/ticket4740/trac_4740.patch) by mhansen created at 2013-07-22 15:11:42\n\nApply trac_4740.patch",
    "created_at": "2013-07-22T15:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35803",
    "user": "mhansen"
}
```

Attachment [trac_4740.patch](tarball://root/attachments/some-uuid/ticket4740/trac_4740.patch) by mhansen created at 2013-07-22 15:11:42

Apply trac_4740.patch



---

archive/issue_comments_035804.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-07-22T16:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35804",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_035805.json:
```json
{
    "body": "Replying to [comment:9 mhansen]:\n> Simon -- see any issues here?\n\nYes, and a quite severe issue.\n\nThe problem is, as often, unique versus non-unique parent structures. For coercion, we need that the domain and codomain of a coercion from A to B are not just equal but identical to A and B. But with `UniqueRepresentation`, the given input arguments are compared by equality, not by identity. That's why it was a conscious decision to use `TripleDict` for caching homsets.\n\nThe cache is provided by the `Hom()` function in sage.categories.homset. If homsets are really created over and over again, then there seems to be a rogue call to `Homset(...)`. The solution is not to make `Homset` a cached class, but to call the `Hom()` function instead.",
    "created_at": "2013-07-22T16:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35805",
    "user": "SimonKing"
}
```

Replying to [comment:9 mhansen]:
> Simon -- see any issues here?

Yes, and a quite severe issue.

The problem is, as often, unique versus non-unique parent structures. For coercion, we need that the domain and codomain of a coercion from A to B are not just equal but identical to A and B. But with `UniqueRepresentation`, the given input arguments are compared by equality, not by identity. That's why it was a conscious decision to use `TripleDict` for caching homsets.

The cache is provided by the `Hom()` function in sage.categories.homset. If homsets are really created over and over again, then there seems to be a rogue call to `Homset(...)`. The solution is not to make `Homset` a cached class, but to call the `Hom()` function instead.



---

archive/issue_comments_035806.json:
```json
{
    "body": "PS: For the same reason I don't like Robert's original patch.\n\nI think we should first find out where the homset constructor is called when Hom should be called instead.",
    "created_at": "2013-07-22T16:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35806",
    "user": "SimonKing"
}
```

PS: For the same reason I don't like Robert's original patch.

I think we should first find out where the homset constructor is called when Hom should be called instead.



---

archive/issue_comments_035807.json:
```json
{
    "body": "Interesting. I found the following, by inserting a print statement into `Homset.__init__`:\n\n```\nsage: F = GF(13)\nsage: x = F(234234)\ncalling Homset Integer Ring Finite Field of size 13 Category of euclidean domains\nsage: x = F(234234)   # the homset is created only once, which is fine\nsage: t = F.coerce(F(234234))   # there is a homset created...\ncalling Homset Finite Field of size 13 Finite Field of size 13 Category of rings\nsage: t = F.coerce(F(234234))   # ... repeatedly\ncalling Homset Finite Field of size 13 Finite Field of size 13 Category of rings\nsage: t = F.coerce(F(234234))\ncalling Homset Finite Field of size 13 Finite Field of size 13 Category of rings\nsage: I = F.coerce_map_from(F)  # creating a coerce map, the homset is created again, but...\ncalling Homset Finite Field of size 13 Finite Field of size 13 Category of rings\nsage: t = F.coerce(F(234234))   # ... now the problem is fixed!\nsage: t = F.coerce(F(234234))\n```\n\n\nThis seems to suggest that\n1. `F.coerce` seems to use a cached coerce map from F to F, but if it isn't cached, it would create the coerce map repeatedly.\n2. It re-creates the coercion map such that the parent of the coercion map is re-created as well.",
    "created_at": "2013-07-22T16:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35807",
    "user": "SimonKing"
}
```

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

archive/issue_comments_035808.json:
```json
{
    "body": "I just tried to use `trace(\"F.coerce(x)\")` to see what happens. And now, it seems to me that `Hom()` is called as it should---but its cache is broken, for a reason that I don't understand.",
    "created_at": "2013-07-22T17:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35808",
    "user": "SimonKing"
}
```

I just tried to use `trace("F.coerce(x)")` to see what happens. And now, it seems to me that `Hom()` is called as it should---but its cache is broken, for a reason that I don't understand.



---

archive/issue_comments_035809.json:
```json
{
    "body": "I found the problem!!\n\nThe homset is stored in the cache, but it is then immediately erased again. Apparently, a strong reference to the homset is missing.",
    "created_at": "2013-07-22T17:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35809",
    "user": "SimonKing"
}
```

I found the problem!!

The homset is stored in the cache, but it is then immediately erased again. Apparently, a strong reference to the homset is missing.



---

archive/issue_comments_035810.json:
```json
{
    "body": "Next observation: If one creates\n\n```\nsage: I = F.coerce_map_from(F)\n```\n\nand then does `del I`, the homset is again erased from the cache.\n\nBut this must not happen! Namely, `F.coerce_map_from(...)` is supposed to use a cache. Granted, the cache is again using weak keys (via `MonoDict`), but as long as `F` is kept in memory, the coercion from F to F must not vanish.",
    "created_at": "2013-07-22T17:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35810",
    "user": "SimonKing"
}
```

Next observation: If one creates

```
sage: I = F.coerce_map_from(F)
```

and then does `del I`, the homset is again erased from the cache.

But this must not happen! Namely, `F.coerce_map_from(...)` is supposed to use a cache. Granted, the cache is again using weak keys (via `MonoDict`), but as long as `F` is kept in memory, the coercion from F to F must not vanish.



---

archive/issue_comments_035811.json:
```json
{
    "body": "Look at the following snippet from `Parent.coerce_map_from(self,S)`:\n\n```python\n        if S == self:\n            # non-unique parents\n            if unique_parent_warnings:\n                print \"Warning: non-unique parents %s\"%(type(S))\n            return self._generic_convert_map(S)\n```\n\n`self._generic_convert_map(S)` does not do caching.\n\nHence, the general problem is: A coercion from self to self will never be cached.",
    "created_at": "2013-07-22T17:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35811",
    "user": "SimonKing"
}
```

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

archive/issue_comments_035812.json:
```json
{
    "body": "I see two potential solutions, and the \"info\" I am seeking is: What would you prefer?\n\nWe could\n\n1. let `F.coerce_map_from(F)` use the cache (I think this is what I would prefer), or\n2. let `F.coerce(x)` avoid creating a morphism, if the parent of x is F.\n\nIt might even make sense to do both, 2. for efficiency.",
    "created_at": "2013-07-22T17:37:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35812",
    "user": "SimonKing"
}
```

I see two potential solutions, and the "info" I am seeking is: What would you prefer?

We could

1. let `F.coerce_map_from(F)` use the cache (I think this is what I would prefer), or
2. let `F.coerce(x)` avoid creating a morphism, if the parent of x is F.

It might even make sense to do both, 2. for efficiency.



---

archive/issue_comments_035813.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2013-07-22T17:37:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35813",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_035814.json:
```json
{
    "body": "I didn't notice that `self.coerce_map_from(S)` also has a special case when `S is self`. However, the result is again not cached.\n\n```python\n        if S is self:\n            from sage.categories.homset import Hom\n            return Hom(self, self).identity()\n```\n",
    "created_at": "2013-07-22T18:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35814",
    "user": "SimonKing"
}
```

I didn't notice that `self.coerce_map_from(S)` also has a special case when `S is self`. However, the result is again not cached.

```python
        if S is self:
            from sage.categories.homset import Hom
            return Hom(self, self).identity()
```




---

archive/issue_comments_035815.json:
```json
{
    "body": "Replying to [comment:19 SimonKing]:\n>  2. let `F.coerce(x)` avoid creating a morphism, if the parent of x is F.\n\nHm. On second thought, do we really want that `F.coerce(x) is x`? I guess it is better to preserve the current behaviour and return a copy of x.",
    "created_at": "2013-07-22T18:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35815",
    "user": "SimonKing"
}
```

Replying to [comment:19 SimonKing]:
>  2. let `F.coerce(x)` avoid creating a morphism, if the parent of x is F.

Hm. On second thought, do we really want that `F.coerce(x) is x`? I guess it is better to preserve the current behaviour and return a copy of x.



---

archive/issue_comments_035816.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2013-07-22T18:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35816",
    "user": "SimonKing"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_035817.json:
```json
{
    "body": "What do people think about the patch that I just attached?\n\nWe now have\n\n```\nsage: F = GF(13)\nsage: F.coerce_map_from(F) is F.coerce_map_from(F)\nTrue\nsage: x = F(234234)\nsage: %timeit t = F.coerce(x)\n1000000 loops, best of 3: 862 ns per loop\n```\n\nand used to have\n\n```\nsage: F = GF(13)\nsage: F.coerce_map_from(F) is F.coerce_map_from(F)\nFalse\nsage: x = F(234234)\nsage: %timeit t = F.coerce(x)\n10000 loops, best of 3: 132 us per loop\n```\n\n\nApply trac4740-cache_coerce_from_self.patch\u200b",
    "created_at": "2013-07-22T18:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35817",
    "user": "SimonKing"
}
```

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

archive/issue_comments_035818.json:
```json
{
    "body": "PS: The memleak in the ticket description has already been fixed elsewhere, this is now only about efficiency.",
    "created_at": "2013-07-22T18:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35818",
    "user": "SimonKing"
}
```

PS: The memleak in the ticket description has already been fixed elsewhere, this is now only about efficiency.



---

archive/issue_comments_035819.json:
```json
{
    "body": "It seems that the patchbot tries to apply both patches. Trying to get it right:\n\nApply trac4740-cache_coerce_from_self.patch\u200b",
    "created_at": "2013-07-22T19:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35819",
    "user": "SimonKing"
}
```

It seems that the patchbot tries to apply both patches. Trying to get it right:

Apply trac4740-cache_coerce_from_self.patch​



---

archive/issue_comments_035820.json:
```json
{
    "body": "For the record: All tests pass, and I really don't see why the patchbot is trying to apply *two* patches.",
    "created_at": "2013-07-22T20:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35820",
    "user": "SimonKing"
}
```

For the record: All tests pass, and I really don't see why the patchbot is trying to apply *two* patches.



---

archive/issue_comments_035821.json:
```json
{
    "body": "Your changes look good to me.  I knew the patch I posted was probably dodgy, but you'd be the one who'd have the best grasp on it.\n\nThanks!",
    "created_at": "2013-07-23T00:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35821",
    "user": "mhansen"
}
```

Your changes look good to me.  I knew the patch I posted was probably dodgy, but you'd be the one who'd have the best grasp on it.

Thanks!



---

archive/issue_comments_035822.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-07-23T00:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35822",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_035823.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-08-16T21:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35823",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_035824.json:
```json
{
    "body": "This needs to be rebased to sage-5.12.beta0 + #14516 + #14519.",
    "created_at": "2013-08-16T21:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35824",
    "user": "jdemeyer"
}
```

This needs to be rebased to sage-5.12.beta0 + #14516 + #14519.



---

archive/issue_comments_035825.json:
```json
{
    "body": "Attachment [trac4740-cache_coerce_from_self.patch](tarball://root/attachments/some-uuid/ticket4740/trac4740-cache_coerce_from_self.patch) by SimonKing created at 2013-08-17 07:51:54\n\nCache coercion from self to self",
    "created_at": "2013-08-17T07:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35825",
    "user": "SimonKing"
}
```

Attachment [trac4740-cache_coerce_from_self.patch](tarball://root/attachments/some-uuid/ticket4740/trac4740-cache_coerce_from_self.patch) by SimonKing created at 2013-08-17 07:51:54

Cache coercion from self to self



---

archive/issue_comments_035826.json:
```json
{
    "body": "Done! The only change concerns the new syntax for debug options. I guess I may revert to \"positive review\".\n\nApply trac4740-cache_coerce_from_self.patch\u200b",
    "created_at": "2013-08-17T07:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35826",
    "user": "SimonKing"
}
```

Done! The only change concerns the new syntax for debug options. I guess I may revert to "positive review".

Apply trac4740-cache_coerce_from_self.patch​



---

archive/issue_comments_035827.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-08-17T07:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35827",
    "user": "SimonKing"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_035828.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-08-20T12:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4740#issuecomment-35828",
    "user": "jdemeyer"
}
```

Resolution: fixed
