# Issue 5721: [with patch, needs review] speed up irreducible_character_freudenthal

archive/issues_005721.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  bump sage-combinat\n\nBefore:\n\n\n```\nsage -t  \"devel/sage-main/sage/combinat/root_system/weyl_characters.py\"\n\t [125.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 125.0 seconds\n```\n\n\nAfter:\n\n\n```\n\t [22.8 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 22.8 seconds\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5721\n\n",
    "created_at": "2009-04-09T01:59:42Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] speed up irreducible_character_freudenthal",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5721",
    "user": "mhansen"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/5721





---

archive/issue_comments_044695.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-09T02:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44695",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_044696.json:
```json
{
    "body": "This is highly desirable as a 3 to 5-fold speedup of all the functions in `weyl_character.py`.\n\nI got some new errors with sage-3.4.1.rc1 after applying the patch.\n\nI had failures in\n\n\n```\ncombinat/root_system/ambient_space.py\ncombinat/sf/kschur.py\ncombinat/sf/jack.py\ncombinat/sf/hall_littlewood.py\n```\n",
    "created_at": "2009-04-09T18:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44696",
    "user": "bump"
}
```

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

archive/issue_comments_044697.json:
```json
{
    "body": "I will try this with my current 3.4.1.rc2 merge tree which has #5002 applied to see if there is any more trouble.\n\nMike: Any chance you can look into the failures Dan mentioned today? rc2 should drop toward the evening PST.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T18:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44697",
    "user": "mabshoff"
}
```

I will try this with my current 3.4.1.rc2 merge tree which has #5002 applied to see if there is any more trouble.

Mike: Any chance you can look into the failures Dan mentioned today? rc2 should drop toward the evening PST.

Cheers,

Michael



---

archive/issue_comments_044698.json:
```json
{
    "body": "I did glance over the patch and this is also something that needs to be fixed for 32 bit boxen:\n\n```\n \t182\t    def __hash__(self): \n \t183\t        \"\"\" \n \t184\t        EXAMPLES:: \n \t185\t         \n \t186\t            sage: e = RootSystem(['A',2]).ambient_space() \n \t187\t            sage: hash(e.simple_root(0)) \n \t188\t            -4601450286177489034          # 64-bit \n```\n\n\nI am also not yet 100% convinced that **`@`cached_method** does not cause memory leaks, but I have no evidence or test case to prove my suspicion :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T19:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44698",
    "user": "mabshoff"
}
```

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


I am also not yet 100% convinced that **`@`cached_method** does not cause memory leaks, but I have no evidence or test case to prove my suspicion :)

Cheers,

Michael



---

archive/issue_comments_044699.json:
```json
{
    "body": "If you take down the caching it's still an impressive speedup.\n\nI ran `sage -t weyl_characters.py` three ways. First, unpatched 3.4.1.rc1. Second, with the patch.  Third, patched but with the caching removed from three files, `ambient_space.py`, `free_module.py` and `type_B.py`.\n\nWithout caching, it actually ran faster.\n\nRun `sage -t weyl_characters.py` unpatched:\n\n59.5 s\n\nWith Mike's patch:\n\n16.0 s\n\nWith Mike's patch, caching disabled:\n\n14.2 s",
    "created_at": "2009-04-09T22:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44699",
    "user": "bump"
}
```

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

archive/issue_comments_044700.json:
```json
{
    "body": "If this gets its doctesting issues fixed I can see this in 3.4.1, but it is by no means critical or a blocker, so reassigning.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-11T00:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44700",
    "user": "mabshoff"
}
```

If this gets its doctesting issues fixed I can see this in 3.4.1, but it is by no means critical or a blocker, so reassigning.

Cheers,

Michael



---

archive/issue_comments_044701.json:
```json
{
    "body": "The problem seems to be in free_module.py.\n\nIn order for __cmp__ method to work with free group elements, no\nterms may occur with zero coefficient. But debugging the failure in\njack.py we find that after Mike's patch:\n\n\n```\nsage: Z = ZonalPolynomials(QQ)\nsage: p = Partition([2,2,1])\nsage: a = p.hook_product(2)*Z(p)\nsage: a._monomial_coefficients\n{[1, 1, 1, 1, 1]: 0, [2, 1, 1, 1]: 0, [2, 2, 1]: 40}\n```\n\n\nreferring to the patch, the fragment following the comment\n\n`#Remove all entries that are equal to 0`\n\nmight be incorrect.\n\nFor efficiency, the changes in ambient_space.py seem more important than the changes in free_module.py. If we revert the changes in free_module.py we still get about a 3 fold speedup, running `sage -t weyl_characters.py` in about 19 seconds - see above for other timings.\n\nBut if we revert the changes in ambient_space.py there is no improvement.\n\nThe changes in free_module.py could therefore be abandoned.",
    "created_at": "2009-04-12T04:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44701",
    "user": "bump"
}
```

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

archive/issue_comments_044702.json:
```json
{
    "body": "Further testing suggests that it is the hash method in class `AmbientSpaceElement`\nthat is responsible for the most impressive speedup. Remove that method and the\ncode is still faster than without the patch, but not very much (48 seconds versus 59\nfor `sage -t weyl_characters.py`).\n\nRemoving this hash method has the effect of reordering the dictionaries\nthat underlie WeylCharacterRing and WeightRing elements. This is why Mike revised\nthree tests in weyl_characters.py. The change in test results is harmless, but it\nseems to me that it raises a problem.\n\nIn view of this message:\n\nhttp://groups.google.com/group/sage-combinat-devel/msg/7e52394814b7779e?hl=en\n\nthis would seem to imply that the results of the tests could be different for 64 bit and 32 bit.\n\nIs this a concern?",
    "created_at": "2009-04-12T05:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44702",
    "user": "bump"
}
```

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

archive/issue_comments_044703.json:
```json
{
    "body": "Attachment\n\nI have uploaded an abridgment to Mike's patch.\n\n`trac_5721-part.patch` is a subset of the original patch.\n\nIt applies cleanly to rc2, introduces no new failures on\n`sage --testall` and it is about a 3-fold speedup.\n\nI took out the changes to `free-module.py`. I also\ntook down all calls to cached_method partly since\nMichael Abshoff expressed a reservation, and partly\nbecause my testing shows that these don't help.",
    "created_at": "2009-04-12T13:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44703",
    "user": "bump"
}
```

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

archive/issue_comments_044704.json:
```json
{
    "body": "Attachment\n\nI have factored the patch trac_5721-part, and changed the doctests to be deterministic.\n\nThe first patch, trac_5721-a.patch contains *only* docstring revision.   The output of `.mlist()` is sorted in three places to make the test deterministic.\n\nThe second patch, trac_5721-b.patch contains only code revision. These changes are the same as in trac_5721-part.patch, and are a subset of Mike's original patch.\n\nWith the docstring changes, the tests pass either before or after the second patch. But after the second patch, there is a better than 3-fold speed improvement.\n\nDan",
    "created_at": "2009-04-13T17:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44704",
    "user": "bump"
}
```

Attachment

I have factored the patch trac_5721-part, and changed the doctests to be deterministic.

The first patch, trac_5721-a.patch contains *only* docstring revision.   The output of `.mlist()` is sorted in three places to make the test deterministic.

The second patch, trac_5721-b.patch contains only code revision. These changes are the same as in trac_5721-part.patch, and are a subset of Mike's original patch.

With the docstring changes, the tests pass either before or after the second patch. But after the second patch, there is a better than 3-fold speed improvement.

Dan



---

archive/issue_comments_044705.json:
```json
{
    "body": "Looks good to me.\n\nApply trac_5721-a.patch trac_5721-b.patch",
    "created_at": "2009-04-15T20:31:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44705",
    "user": "mhansen"
}
```

Looks good to me.

Apply trac_5721-a.patch trac_5721-b.patch



---

archive/issue_comments_044706.json:
```json
{
    "body": "Note that we do need to test it on a 32-bit box to get the missing hash value.",
    "created_at": "2009-04-15T20:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44706",
    "user": "mhansen"
}
```

Note that we do need to test it on a 32-bit box to get the missing hash value.



---

archive/issue_comments_044707.json:
```json
{
    "body": "Here is the 32 bit run:\n\n```\nsage -t -long \"devel/sage/sage/combinat/root_system/ambient_space.py\"\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.4.1.rc2/devel/sage/sage/combinat/root_system/ambient_space.py\", line 185:\n    sage: hash(e.simple_root(0))\nExpected nothing\nGot:\n    549810038\n**********************************************************************\n```\n\nI will post a reviewer patch shortly.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T09:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44707",
    "user": "mabshoff"
}
```

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

archive/issue_comments_044708.json:
```json
{
    "body": "This is a slightly  fixed up version of Dan and Mike's patch that adds the 32 bit hash",
    "created_at": "2009-04-16T09:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44708",
    "user": "mabshoff"
}
```

This is a slightly  fixed up version of Dan and Mike's patch that adds the 32 bit hash



---

archive/issue_comments_044709.json:
```json
{
    "body": "Attachment\n\nMerged  trac_5721-a.patch and trac_5721-b.patch in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T09:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44709",
    "user": "mabshoff"
}
```

Attachment

Merged  trac_5721-a.patch and trac_5721-b.patch in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_044710.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-16T09:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5721#issuecomment-44710",
    "user": "mabshoff"
}
```

Resolution: fixed
