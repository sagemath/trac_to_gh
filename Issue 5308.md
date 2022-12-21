# Issue 5308: Removing __len__ for combinatorial classes

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-02-18 19:04:08

Assignee: hivert

CC:  sage-combinat

Keywords: __len__, count, combinatorial class

After some discussion on sage-combinat-devel, it was decided that __len__ should no be used to get the size of a combinatorial class because. Indeed the specifications of __len__ says that it has to return a plain python int, whereas we want to deal with huge and even infinite sets. Unfortunately due to __len__ being called by list / filter / map and maybe some other functions, it is not possible to issue a warning. So it was decided to simply remove it and issue an error, telling to call .count() instead. 

Some part of combinat has to be fixed accordingly.


---

Comment by hivert created at 2009-02-18 19:04:21

Changing status from new to assigned.


---

Comment by hivert created at 2009-03-01 18:03:37

I've attached a patch for the cleanup. It should apply cleanly on top of #5200. 

Author: Florent Hivert


---

Attachment

Good version of the file


---

Comment by nthiery created at 2009-04-02 06:13:57

When applying the patch on top of 3.4 with the following patches applied:

```
zephyr-/opt/sage/devel/sage>hg qapplied
integer_lists_lex-4549-submitted.patch
subsets_subwords-5200-submitted.2.patch
subsets_subwords-5200-review.patch
subwords_fix-5534-submitted.patch
combinatorialclass_iter_len_count_cleanup.patch
```

I get a reject in 

```
zephyr-/opt/sage/devel/sage>cat sage/combinat/subset.py.rej
--- subset.py
+++ subset.py
`@``@` -522,7 +522,7 `@``@`
             [0, 1, 3]
             sage: S._multiplicities
             [1, 2, 1]
-            sage: Subsets([1,2,3,3], multiset=True).count()
+            sage: Subsets([1,2,3,3], multiset=True).cardinality()
             12
             sage: S == loads(dumps(S))
             True
`@``@` -604,7 +604,7 `@``@`
             sage: S = Subsets([1,2,3,3],2, multiset=True)
             sage: S._k
             2
-            sage: S.count()
+            sage: S.cardinality()
             4
             sage: S.first()
             [1, 2]
```


Moreover, the following tests get broken:

```
        sage -t  "3.4.rc0/devel/sage-patches/sage/combinat/sf/ns_macdonald.py"
        sage -t  "3.4.rc0/devel/sage-patches/sage/combinat/subset.py"
        sage -t  "3.4.rc0/devel/sage-patches/sage/combinat/words/words.py"
```

either by the deprecation warnings, or for words by a change of output: 
`96889010407L ->  96889010407`

Other than this, the patch sounds good to me!


---

Comment by nthiery created at 2009-04-02 06:34:23

In CartesianProduct, shouldn't we test first if it.cardinality works, and resort to len if this raised an AttributeError?
Line 3 of the doc of InfiniteAbstractCombinatorialClass:
 - inerit -> inherit, wich -> which,  count -> cardinality, ...
The log of the patch should advertise this new class
In CyclicPermutations: leave at least a note that this deviates from the standard (__iter__/list take no argument), and should be cleaned up further at some point
In the examples (like in SemistandardTableaux), do we want to use: `[t for t in iterable]` or `list(iterable)`


---

Comment by saliola created at 2009-04-02 08:04:02

I've looked over the changes to the words files. Everything looks good. To fix the problem with the doctests related to 96889010407L that nthiery mentioned above, just have Word_n.cardinality() (in sage/combinat/words/words.py) return a Sage Integer instead of a Python int.  If you do this, then it also deals with #4938.


---

Comment by hivert created at 2009-04-02 08:46:47

Addressed Nicolas reqests.


---

Attachment

Dear Nicolas,

I sumbmitted a new patch which should addres all the issues except this last one:   

> In the examples (like in SemistandardTableaux), do we want to use: `[t for t in iterable]` or `list(iterable)`

I think both kind of example should by advertised. IMHO, they both are very python idiomatic, the first one allows for extra condition, the second one is shorter. The only clear argument is that the first one is slightly faster:

```
sage: timeit("it = iter(Permutations(6)); list(it)")
125 loops, best of 3: 4.57 ms per loop
sage: timeit("it = iter(Permutations(6)); list(it)")
125 loops, best of 3: 4.45 ms per loop
sage: timeit("it = iter(Permutations(6)); [i for i in it]")
125 loops, best of 3: 4.64 ms per loop
sage: timeit("it = iter(Permutations(6)); [i for i in it]")
125 loops, best of 3: 4.61 ms per loop
```

Do we really what to standardize all the doc on it ? 

Cheers,

Florent


---

Comment by hivert created at 2009-04-02 09:02:55

Dear Franco,

> I've looked over the changes to the words files. Everything looks good. To fix the problem with the doctests related to 96889010407L that nthiery mentioned above, just have Word_n.cardinality() (in sage/combinat/words/words.py) return a Sage Integer instead of a Python int.  If you do this, then it also deals with #4938.

Actually, the problem was that I forgot to re-export the patch from the
combinat server... 

I can't reproduce the problem on word but I don't have access to a 32bit machine. More precisely, `words.size_of_alphabet()` seems now to always return a sage integer. That should fix the problem. Can you please check it ?

Cheers,

Florent


---

Comment by saliola created at 2009-04-02 21:34:04

Replying to [comment:9 hivert]:
>       Dear Franco,
>
> I can't reproduce the problem on word but I don't have access to a 32bit machine. More precisely, `words.size_of_alphabet()` seems now to always return a sage integer. That should fix the problem. Can you please check it ?

Sorry it took so long: I had to compile sage on a 32-bit machine!

The last patch (combinatorialclass_iter_len_count_cleanup-5308-submitted.patch) applies cleanly to sage-3.4 on top of the patches for #5200 and #4549. I ran all the combinat doctests and all tests passed.

You get a positive review from me. I won't change the status though, since Nicolas might still have some issues.


---

Comment by nthiery created at 2009-04-04 00:44:48

Replying to [comment:8 hivert]:
> > In the examples (like in SemistandardTableaux), do we want to use: `[t for t in iterable]` or `list(iterable)`
> 
> I think both kind of example should by advertised. IMHO, they both are very python idiomatic, the first one allows for extra condition, the second one is shorter. The only clear argument is that the first one is slightly faster:
> {{{
> sage: timeit("it = iter(Permutations(6)); list(it)")
> 125 loops, best of 3: 4.57 ms per loop
> sage: timeit("it = iter(Permutations(6)); list(it)")
> 125 loops, best of 3: 4.45 ms per loop
> sage: timeit("it = iter(Permutations(6)); [i for i in it]")
> 125 loops, best of 3: 4.64 ms per loop
> sage: timeit("it = iter(Permutations(6)); [i for i in it]")
> 125 loops, best of 3: 4.61 ms per loop
> }}}
> Do we really what to standardize all the doc on it ? 

Good point. The speed difference is too negligible that it seems likely to change in the future one way or the other. I guess we can just leave it as it is. Future will tell if any of the two form become more sage-combinat idiomatic. 

Positive review


---

Comment by mabshoff created at 2009-04-04 00:56:44

Hmm, one last thing: In `def __len__(self): ` you deprecate `__len__` and tell people to use count. Isn't it possible to deprecate `__len__` and have it call count() automatically because that is the way it is supposed to work.

Cheers,

Michael


---

Comment by saliola created at 2009-04-04 06:39:16

Replying to [comment:12 mabshoff]:
> Hmm, one last thing: In `def __len__(self): ` you deprecate `__len__` and tell people to use count. Isn't it possible to deprecate `__len__` and have it call count() automatically because that is the way it is supposed to work.

It should say that one needs to use cardinality instead of `__len__`.

There are a few reasons why this doesn't work. One reason is that `__len__` must return a Python int. So, if the CombinatorialClass is too big, then calling `__len__` will raise an error, which is a bug.

Another problem is that some methods, like `__list__`, call `__len__` behind the scenes. This means that there would be deprecation warnings popping up in various places: for instance, `list(Permutations(3))` would give a warning, and it would be very confusing to a user not familiar with Python internals to see a warning about using `__len__` when they didn't obviously call `__len__`. Also the doctests would be littered with such deprecation warnings in various places (whenever `list/filter/map` are called). Instead, we decided to raise an `AttributeError`, which behaves nicely with Python's specifications on how `__len__` is to behave when called by `list/filter/map`, and also gives an appropriate error message when `len` is called directly. It really is a special case, where the usual deprecation procedure won't work.


---

Comment by hivert created at 2009-04-04 08:27:48

If its still possible, I'd rather seen this integrated in 3.4.1, to be sure that new users get good habits. 

Florent


---

Comment by hivert created at 2009-04-04 15:31:45

The patch needed a trivial rebase because of my review patch on #4549.
The rebased patch should apply cleanly on top of attachment:ticket:4549:integer_lists_lex-4549-submitted.patch and
attachment:ticket:4549:integer_lists_lex-4549-review.patch

Cheers,

Florent


---

Comment by mabshoff created at 2009-04-05 00:06:54

This patch introduces two trivial to fix doctest failures:

```
mabshoff`@`sage:/scratch/mabshoff/sage-3.4.1.rc0$ ./sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py
sage -t -long "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 911:
    sage: I.dimension()
Expected:
    verbose 0 (...: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.
    0
Got:
    verbose 0 (891: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.
    doctest:966: DeprecationWarning: The usage of iterator for combinatorial classes is deprecated. Please use the class itself
    0
**********************************************************************
1 items had failures:
   1 of  15 in __main__.example_17
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.rc0/tmp/.doctest_multi_polynomial_ideal.py
	 [11.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
Total time for all tests: 11.3 seconds
mabshoff`@`sage:/scratch/mabshoff/sage-3.4.1.rc0$ ./sage -t -long devel/sage/doc/en/a_tour_of_sage/index.rst
sage -t -long "devel/sage/doc/en/a_tour_of_sage/index.rst"  
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage/doc/en/a_tour_of_sage/index.rst", line 132:
    sage: z = Partitions(10^8).count() #about 4.5 seconds
Expected nothing
Got:
    doctest:1: DeprecationWarning: The usage of iterator for combinatorial classes is deprecated. Please use the class itself
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_9
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.rc0/tmp/.doctest_index.py
	 [10.9 s]
exit code: 1024
```

Once those are fixed the positive review can be reinstated.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-05 00:08:16

This ticket also fixes #4938 which should be closed afterwards.

Cheers,

Michael


---

Attachment

Hopefully final version


---

Comment by hivert created at 2009-04-05 07:51:19

Replying to [comment:16 mabshoff]:
> This patch introduces two trivial to fix doctest failures:

 * Oups !!! I probably let the first pass because it's typically one of the few files that triggers the pexpect issue on my fast testing machine...

 * Next time I'll check also the .rst files. 

These should be fixed right now. Re-uploaded a new patch and re marked as positive reviewed. 

Cheers,

Florent


---

Comment by mabshoff created at 2009-04-05 23:26:19

I have had to update the hunk applied to sage/rings/polynomial/multi_polynomial_ideal.py due to #5485, but I am doctesting the patch now ;)

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-05 23:52:59

Merged in Sage 3.4.1.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-05 23:52:59

Resolution: fixed


---

Comment by mabshoff created at 2009-04-05 23:58:14

Slightly rebased version of Florent's last patch


---

Attachment

FYI: Merged trac_5308_combinatorialclass_iter_len_count_cleanup-5308-rebased.patch in Sage 3.4.1.rc1.

Cheers,

Michael
