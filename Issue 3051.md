# Issue 3051: Weyl Characters

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2008-04-28 22:52:26

Assignee: mhansen

CC:  sage-combinat

Keywords: Weyl characters, branching rules

This was announced here:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/74ed91d5153e6022?hl=en

See also:

http://groups.google.com/group/sage-devel/browse_thread/thread/f713ed4bf3df8c22?hl=en

At Mike Hansen and Nicolas Thiery's suggestions the default separator is now "," and the separator is configurable. 

I believe all branching rules to maximal subgroups of compact Lie groups are implemented with two (large) exceptions: reducible subgroups like A1 x A1, and branching rules involving the exceptional groups. Mike requested that the branching be made a method, and the new syntax is something like
chi.branch(B3,rule="symmetric"). However I left Branch as a standalone program and the
main docstring is Branch? This of course can be changed. 

An issue is that the caching is a substantial speedup but at a potentially large cost in memory. I hesitated to make it the default so cache=False is the default. But the user will be happier with cache=True.

It is possible to cache more aggressively. I have not implemented but know how to implement caching the results of multiplications instead of just the characters themselves.




---

Attachment


---

Comment by wdj created at 2008-04-29 00:03:19

Is this based on 3.0? I got:


```

applying /Users/wdj/sagefiles/9607.patch
abort: unable to find sage/combinat/crystals/crystals.py or sage/combinat/crystals/crystals.py for patching
```



---

Comment by mabshoff created at 2008-04-29 00:27:50

Things work perfectly to me:

```
sage$ patch -p1 --dry-run < 9607.patch\?format\=raw
patching file sage/combinat/crystals/crystals.py
patching file sage/combinat/root_system/all.py
patching file sage/combinat/root_system/cartan_type.py
patching file sage/combinat/root_system/weyl_characters.py
```

This is against 3.0.1.alpha1.

Cheers,

Michael


---

Comment by bump created at 2008-04-29 02:57:37

It's a patch against 3.0.

Dan


---

Comment by wdj created at 2008-04-29 03:18:49

Thanks. It's working now. I'm running sage -testall now but want to point out that the standard format for Python functions is all_lower_underscore. The function "Branch" is definitely non-standard naming.


---

Comment by wdj created at 2008-04-29 11:23:49

Applies cleanly to a 3.0 base and passes sage -testall on an ubuntu 7.10amd64 machine. (It did not apply cleanly on a macbook but possibly I made a mistake somewhere.) 

(1) This character theory stuff is a *great* contribution and I think that SAGE is lucky to have someone of Dan's abilities contributing code like this. However, I have some unfavorable comments.

(2) There is this capitalization issue. I think capitalizing the functions IrreducibleCharacterFreudenthal and Branch is confusing. (There may be other examples I am missing as well.) Classes are capitalized, not functions. Possibly you could drop 

```
irreducible_character_freudenthal = IrreducibleCharacterFreudenthal
branch = Branch
```

at the bottom of the file but even that I think is not enough. 

(3) Actually, I think branch is too generic to use and would prefer something like branch_character or something. (Who knows, maybe someone will write a Tableau class for characters of the symmetric group and friends and wants to use it in their module too. Who wins?)

(4) I think the documentation is great on one hand and lacking references on the other. I really hope the author will consider adding somewhere a REFERENCES: section to his docstrings (possibly to books or papers of his own) and specific (I mean page or Theorem or Definition numbers) citations thoughout his code. That way people will learn from it and be able to maintain it better, since with proper citations everyone will be one the same page.
 
I realize these are a little excessive and am happy to be over-ruled. But I don't yet give this a positive review.


---

Comment by bump created at 2008-04-29 12:18:37

I definitely agree that Branch -> branch_character should be done and the capitalization of the other function can be changed too. BTW Branch is globally exposed by IrreducibleCharacterFreudenthal is not (cf. all.py).

There is a question of whether Branch should be left globally exposed. Maybe this is not needed. The code in it could be moved to the branch method of Weyl character but since it's long and its docstring is long I left it alone.

About (4), I'm less eager to start expanding the docstring further.

I won't put up another patch yet since Mike Hansen may comment or revise it, and there could be further comments from others.

In view of Michael Abshoff's comments the caching should be left off by default and before considering turning it on by default it should be reimplemented  using weak references.


---

Attachment

name change: Branch -> branch_weyl_character


---

Comment by bump created at 2008-04-29 16:11:31

I added a second small patch that makes the name changes Branch -> branch_weyl_character and IrreducibleCharacterFreudenthal -> irreducible_character_freudenthal, addressing points (2) and (3) of David's review.


---

Comment by mhansen created at 2008-04-29 19:39:13

I'll go through and get it 100% doctested so it can go in.


---

Attachment


---

Comment by bump created at 2008-05-02 14:57:27

I added 9609.patch.

This gives doctests for most methods.

Removes an unimplemented method that was accidentally left.

Corrects a minor bug (`__repr__` misspelled somewhere).


---

Attachment

The patch 9610.patch completes the doctesting to 100%.

I found 2 bugs which are fixed. In _add_ some code had the wrong
indent level and this has been fixed. and `_neg_` was misspelled
somewhere.

Dan


---

Attachment

Added 9611.patch.

Minor bugfixes and improvements.

The bugfixes are in WeylCharacterRing's `__call__` method, which worked reasonably well over ZZ but not over a polynomial ring. After the patch, we first intercept integers, then try to coerce elements into the base ring, but we check the parent first since it is possible to coerce a list of integers into a polynomial ring.  In other words, we don't want to break calls like `R([2,1,0])`.

I found that changing the way `repr_lincomb` is called resulted in nicer output.

A parent method is added to elements.

More doctests are added in response to the problems I found in __call__ and there are revisions to old doctests in response to the revised lincomb call.


---

Attachment


---

Comment by bump created at 2008-05-06 19:01:15

I added a patch called 9673.patch.

This reimplements the Freudenthal multiplicity formula. 

Formerly, weight multiplicities are calculated in a region containing the positive Weyl chamber, then copied around using the action of the Weyl group. In the reimplementation, all weights are calculated using the recursion relations, without using the Weyl group action. This turns out to be much faster, as well as simpler.

One test result was changed because the weights of B3(spin) are calculated in a different order.


---

Attachment


---

Attachment


---

Comment by bump created at 2008-05-07 22:03:42

The last patch, 9674.patch is explained here:

http://groups.google.com/group/sage-combinat-devel/msg/82dd8255caa108cf

There are a lot of patches so I posted a single patch 3051-unified.patch
that is the union of the other patches.

I have changed the patch summary from [with patch, positive review pending changes]
to [with patch, needs review (again)] and hope that David Joyner and Mike Hansen
can look at it again.


---

Comment by wdj created at 2008-05-08 11:16:02

This passes sage -testall and applies cleanly. I'll look at it some more later this morning but wanted to post that info since it might save some time for anyone else looking at it.


---

Comment by bump created at 2008-05-08 12:13:33

I see I inadvertently omitted the changes to crystals.py from 9607.patch when I made the unified patch. I think it best if I leave those out for now since David has already run testall. If this patch can be reviewed as it is I can make another ticket later for the changes to crystals.py.


---

Comment by wdj created at 2008-05-08 13:13:34

Don't worry about that. If you want to make a new unified patch, do so and let me know. I'll re-run sage -testall.


---

Attachment

> Don't worry about that. If you want to make a new unified patch, do so and let me know. I'll re-run sage -testall.

Thanks.

I made a separate patch called 3051-1.patch containing just the changes to
crystals.py. This goes on top of 3051-1.unified.


---

Comment by wdj created at 2008-05-08 17:38:07

This patch 3051-1, applied on top of the 3051-unified patch, applies cleanly to 3.0.1. sage -testall 
failed on one module but then testing that module separately passes. 


```
----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx
Total time for all tests: 5283.6 seconds
Please see /home/wdj/wdj/sagefiles/sage-3.0.1/tmp/test.log for the complete log from this test.
wdj`@`wooster:~/wdj/sagefiles/sage-3.0.1$ ./sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx
sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx
         [4.8 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.8 seconds
```

I'm guessing that this failure is spurious. (It was done on an older machine, which has had
lots of such failures before.) I'll keep looking at this patch, but wanted to report this issue ASAP.


---

Comment by wdj created at 2008-05-08 18:09:48

More comments.

1. The class name Weight is IMHO too generic and is not consistent with SAGE's naming "standard". Better would be WeightRingElement (or WeightAlgebraElement?).

2. Perhaps this is a very minor point since this appears common with lots of other modules, but I think that legally when you simply license code under the GPL, the default is the latest version (which of course is GPLv3). Better is to specify "GPLv2 or later (at your preference)".

3. IMHO, this is a fantastic contribution by a leader in the field. Not to look a gift horse in the mouth, but I repeat that references to the literature would add value. I don't want to make a big deal of it though. If no one else does, I will add them myself later when I can get near my repn theory books (due to some home construction, those books are behind mounds of furniture at the moment).

So, modulo (1) above, I give this a positive review, but would like to hear what Mike Hansen has to say as well before renaming the Summary.


---

Comment by bump created at 2008-05-08 20:33:52

> 1. The class name Weight is IMHO too generic and is not consistent with SAGE's naming "standard". Better would be WeightRingElement? (or WeightAlgebraElement??).

I agree and will change it to WeightRingElement.

> 2. Perhaps this is a very minor point since this appears common with lots of other modules, but I think that legally when you simply license code under the GPL, the default is the latest version (which of course is GPLv3). Better is to specify "GPLv2 or later (at your preference)".

The copyright header is the same as the other files in the combinat directory.

> 3. IMHO, this is a fantastic contribution by a leader in the field. Not to look a gift horse in the mouth, but I repeat that references to the literature would add value. I don't want to make a big deal of it though. If no one else does, I will add them myself later when I can get near my repn theory books (due to some home construction, those books are behind mounds of furniture at the moment).

Dynkin's paper is already cited, where maximal subgroups of Lie groups are classified. Also Humpfrey's book on Lie algebras is already cited. However I will add some references. I can add references to books of Goodman and Wallach and Bump and a further citation of Humpfrey's book(for highest weight theory) and (for branching rules) papers of Howe, Chye and Willenbring and of R.C. King.

Can you (or anyone) think of anything else that would be good to cite?

I'll put up another patch (I hope by 5PM PDT) addressing (1) and (3) but not (2) since the comment applies systematically in combinat/.


---

Attachment


---

Attachment


---

Comment by bump created at 2008-05-09 00:19:28

The patch 3051-2.patch is in response to items (1) and (2) of David's report.  I changed Weight -> WeightRingElement, and added some more references. 

The patch 3051-2.patch goes on top of 3051-unifed.patch and 3041-1.patch.

The patch 3051-unified-1.patch is a single unified patch containing all changes. It thus supercedes 3051-unified.patch.


---

Comment by wdj created at 2008-05-09 10:36:25

This patch 3051-unified-1.patch applied cleanly to 3.0.1 and passes sage -testall. I give this a very positive review. Very nice work. I think Mike Hansen should look at it since it is based on some work he has done or at least knows better than I. However, since it is around the end of the semester, I 'm not sure if he will have time to do that before 3.0.2 is released. So, I changed the summary to "one positive review".


---

Attachment

Goes on top of 3051-unified-1.patch. Revises the __repr to avoid string notation and adds _coerce_impl methods


---

Comment by bump created at 2008-05-17 05:01:36

Both David Joyner and Mike Hansen disliked the string notation followed in earlier versions of the patch. This has been removed and replaced by Mike's suggestion, `A2(1,1,0)` for example.

Also, _coerce_impl methods were added to WeylCharacterRing and WeightRing, so that now the two rings can *always* parse their own output.


---

Attachment

Unified patch equivalent to 3051-unified-1.patch plus 3051-3.patch plus 3051-4.patch


---

Comment by bump created at 2008-05-17 14:28:00

I realized that I'd forgotten to revise the doctest in crystals.py after the notational change. The patch 3051-4.patch fixes the doctest. I revised and reposted 3051-unified-2.patch accordingly.


---

Comment by wdj created at 2008-05-17 14:51:44

Really, or someone should look at this instead of me but to help out a little, I thought I'd at least do some testing. Oddly enough, I had trouble applying it to a newly made clone:


```
wdj`@`wooster:/mnt/drive_hda1/sagefiles/sage-3.0.2.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.2.alpha1, Release Date: 2008-05-11                |
| Type notebook() for the GUI, and license() for information.        |
Loading SAGE library. Current Mercurial branch is: weyl2
sage: hg_sage.apply("/home/wdj/wdj/sagefiles/3051-unified-2.patch")
cd "/mnt/drive_hda1/sagefiles/sage-3.0.2.alpha0/devel/sage" && hg status
cd "/mnt/drive_hda1/sagefiles/sage-3.0.2.alpha0/devel/sage" && hg status
cd "/mnt/drive_hda1/sagefiles/sage-3.0.2.alpha0/devel/sage" && hg import   "/home/wdj/wdj/sagefiles/3051-unified-2.patch"
applying /home/wdj/wdj/sagefiles/3051-unified-2.patch
patching file sage/combinat/crystals/crystals.py
Hunk #1 FAILED at 103
Hunk #2 succeeded at 231 with fuzz 2 (offset 1 line).
1 out of 2 hunks FAILED -- saving rejects to file sage/combinat/crystals/crystals.py.rej
file sage/combinat/root_system/weyl_characters.py already exists
1 out of 1 hunk FAILED -- saving rejects to file sage/combinat/root_system/weyl_characters.py.rej
abort: patch failed to apply
sage:                               
```


The previous version of this patch applied and  passed sage -testall except for crystal, as you already pointed out.


---

Comment by bump created at 2008-05-17 18:20:29

You must have had a leftover weyl_characters.py in your directory since I don't think this file is in
the repository. At least it's not in sage-3.0.2.alpha0. The patch creates this file.


```
1 out of 2 hunks FAILED -- saving rejects to file sage/combinat/crystals/crystals.py.rej
file sage/combinat/root_system/weyl_characters.py already exists
```



---

Attachment


---

Comment by mhansen created at 2008-05-18 00:07:15

Sorry it's taken so long -- I've been awfully busy this week. I've attached a patch which makes a few minor changes to docstrings / doctests.

Apply only the last two patches.


---

Comment by mabshoff created at 2008-05-18 00:13:47

Merged 3051-unified-2.patch and 3051-doctest.patch in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-18 00:13:47

Resolution: fixed
