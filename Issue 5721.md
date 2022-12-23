# Issue 5721: [with patch, needs review] speed up irreducible_character_freudenthal

Issue created by migration from https://trac.sagemath.org/ticket/5721

Original creator: mhansen

Original creation time: 2009-04-09 01:59:42

Assignee: mhansen

CC:  bump sage-combinat

Before:


```
sage -t  "devel/sage-main/sage/combinat/root_system/weyl_characters.py"
	 [125.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 125.0 seconds
```


After:


```
	 [22.8 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 22.8 seconds
```



---

Attachment


---

Comment by bump created at 2009-04-09 18:06:48

This is highly desirable as a 3 to 5-fold speedup of all the functions in `weyl_character.py`.

I got some new errors with sage-3.4.1.rc1 after applying the patch.

I had failures in


```
combinat/root_system/ambient_space.py
combinat/sf/kschur.py
combinat/sf/jack.py
combinat/sf/hall_littlewood.py
```



---

Comment by mabshoff created at 2009-04-09 18:40:23

I will try this with my current 3.4.1.rc2 merge tree which has #5002 applied to see if there is any more trouble.

Mike: Any chance you can look into the failures Dan mentioned today? rc2 should drop toward the evening PST.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 19:30:47

I did glance over the patch and this is also something that needs to be fixed for 32 bit boxen:

```
 	182	    def __hash__(self): 
 	183	        """ 
 	184	        EXAMPLES:: 
 	185	         
 	186	            sage: e = RootSystem(['A',2]).ambient_space() 
 	187	            sage: hash(e.simple_root(0)) 
 	188	            -4601450286177489034          # 64-bit 
```


I am also not yet 100% convinced that *`@`cached_method* does not cause memory leaks, but I have no evidence or test case to prove my suspicion :)

Cheers,

Michael


---

Comment by bump created at 2009-04-09 22:03:00

If you take down the caching it's still an impressive speedup.

I ran `sage -t weyl_characters.py` three ways. First, unpatched 3.4.1.rc1. Second, with the patch.  Third, patched but with the caching removed from three files, `ambient_space.py`, `free_module.py` and `type_B.py`.

Without caching, it actually ran faster.

Run `sage -t weyl_characters.py` unpatched:

59.5 s

With Mike's patch:

16.0 s

With Mike's patch, caching disabled:

14.2 s


---

Comment by mabshoff created at 2009-04-11 00:31:39

If this gets its doctesting issues fixed I can see this in 3.4.1, but it is by no means critical or a blocker, so reassigning.

Cheers,

Michael


---

Comment by bump created at 2009-04-12 04:22:35

The problem seems to be in free_module.py.

In order for __cmp__ method to work with free group elements, no
terms may occur with zero coefficient. But debugging the failure in
jack.py we find that after Mike's patch:


```
sage: Z = ZonalPolynomials(QQ)
sage: p = Partition([2,2,1])
sage: a = p.hook_product(2)*Z(p)
sage: a._monomial_coefficients
{[1, 1, 1, 1, 1]: 0, [2, 1, 1, 1]: 0, [2, 2, 1]: 40}
```


referring to the patch, the fragment following the comment

`#Remove all entries that are equal to 0`

might be incorrect.

For efficiency, the changes in ambient_space.py seem more important than the changes in free_module.py. If we revert the changes in free_module.py we still get about a 3 fold speedup, running `sage -t weyl_characters.py` in about 19 seconds - see above for other timings.

But if we revert the changes in ambient_space.py there is no improvement.

The changes in free_module.py could therefore be abandoned.


---

Comment by bump created at 2009-04-12 05:08:40

Further testing suggests that it is the hash method in class `AmbientSpaceElement`
that is responsible for the most impressive speedup. Remove that method and the
code is still faster than without the patch, but not very much (48 seconds versus 59
for `sage -t weyl_characters.py`).

Removing this hash method has the effect of reordering the dictionaries
that underlie WeylCharacterRing and WeightRing elements. This is why Mike revised
three tests in weyl_characters.py. The change in test results is harmless, but it
seems to me that it raises a problem.

In view of this message:

http://groups.google.com/group/sage-combinat-devel/msg/7e52394814b7779e?hl=en

this would seem to imply that the results of the tests could be different for 64 bit and 32 bit.

Is this a concern?


---

Attachment

I have uploaded an abridgment to Mike's patch.

`trac_5721-part.patch` is a subset of the original patch.

It applies cleanly to rc2, introduces no new failures on
`sage --testall` and it is about a 3-fold speedup.

I took out the changes to `free-module.py`. I also
took down all calls to cached_method partly since
Michael Abshoff expressed a reservation, and partly
because my testing shows that these don't help.


---

Attachment

I have factored the patch trac_5721-part, and changed the doctests to be deterministic.

The first patch, trac_5721-a.patch contains *only* docstring revision.   The output of `.mlist()` is sorted in three places to make the test deterministic.

The second patch, trac_5721-b.patch contains only code revision. These changes are the same as in trac_5721-part.patch, and are a subset of Mike's original patch.

With the docstring changes, the tests pass either before or after the second patch. But after the second patch, there is a better than 3-fold speed improvement.

Dan


---

Comment by mhansen created at 2009-04-15 20:31:48

Looks good to me.

Apply trac_5721-a.patch trac_5721-b.patch


---

Comment by mhansen created at 2009-04-15 20:35:47

Note that we do need to test it on a 32-bit box to get the missing hash value.


---

Comment by mabshoff created at 2009-04-16 09:11:45

Here is the 32 bit run:

```
sage -t -long "devel/sage/sage/combinat/root_system/ambient_space.py"
**********************************************************************
File "/Users/mabshoff/sage-3.4.1.rc2/devel/sage/sage/combinat/root_system/ambient_space.py", line 185:
    sage: hash(e.simple_root(0))
Expected nothing
Got:
    549810038
**********************************************************************
```

I will post a reviewer patch shortly.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 09:34:58

This is a slightly  fixed up version of Dan and Mike's patch that adds the 32 bit hash


---

Attachment

Merged  trac_5721-a.patch and trac_5721-b.patch in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 09:35:29

Resolution: fixed
