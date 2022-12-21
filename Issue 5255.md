# Issue 5255: [with patch, needs review] Deprecating the use of iterator in CombinatorialClass

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-02-13 16:16:17

Assignee: mhansen

CC:  sage-combinat

Keywords: __iter__, iterator

Right now, when one want's to iterate along a combinatorial class C, there is at least three solution:

```
[ x for x in C.iterator() ]
[ x for x in C.__iter__() ]
[ x for x in C ]
```

There is no semantic differences beetween these three and there should not be any mesurable speedup for any. The latter solution is sintactically better and perfectly python/Sage idiomatic. So the goal of this patch is to mark the use of `C.iterator()` as deprecated *ASAP* (there are already 96 definition and something close to 400 uses in sage-combinat). 

A subsequent series of patches should apply this rule trough all combinatorial classes. Right now to avoid breaking doctests the raising of the deprecation warning is commented out. I'll uncomment it after the series of patches. 


---

Comment by hivert created at 2009-02-13 16:17:31

Patch proposal


---

Attachment


---

Comment by malb created at 2009-02-14 17:36:35

I think


```
it = C.__iter__() # indirect doctest 
```


should be 


```
it = iter(C) # indirect doctest 
```


i.e. one should avoid calling `__foo__` functions directly.


---

Attachment

The original patch looks good.  I made a few updates in the review patch.


---

Comment by hivert created at 2009-02-14 23:54:23

Replying to [comment:3 mhansen]:
> The original patch looks good.  I made a few updates in the review patch.

The review patch looks good to me.


---

Comment by mhansen created at 2009-02-15 00:27:19

Apply both patches.


---

Comment by mabshoff created at 2009-02-15 08:04:53

Merged both patches in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-15 08:04:53

Resolution: fixed
