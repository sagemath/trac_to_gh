# Issue 5308: Removing __len__ for combinatorial classes

archive/issues_005308.json:
```json
{
    "body": "Assignee: hivert\n\nCC:  sage-combinat\n\nKeywords: __len__, count, combinatorial class\n\nAfter some discussion on sage-combinat-devel, it was decided that __len__ should no be used to get the size of a combinatorial class because. Indeed the specifications of __len__ says that it has to return a plain python int, whereas we want to deal with huge and even infinite sets. Unfortunately due to __len__ being called by list / filter / map and maybe some other functions, it is not possible to issue a warning. So it was decided to simply remove it and issue an error, telling to call .count() instead. \n\nSome part of combinat has to be fixed accordingly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5308\n\n",
    "created_at": "2009-02-18T19:04:08Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Removing __len__ for combinatorial classes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5308",
    "user": "hivert"
}
```
Assignee: hivert

CC:  sage-combinat

Keywords: __len__, count, combinatorial class

After some discussion on sage-combinat-devel, it was decided that __len__ should no be used to get the size of a combinatorial class because. Indeed the specifications of __len__ says that it has to return a plain python int, whereas we want to deal with huge and even infinite sets. Unfortunately due to __len__ being called by list / filter / map and maybe some other functions, it is not possible to issue a warning. So it was decided to simply remove it and issue an error, telling to call .count() instead. 

Some part of combinat has to be fixed accordingly.

Issue created by migration from https://trac.sagemath.org/ticket/5308





---

archive/issue_comments_040835.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-18T19:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40835",
    "user": "hivert"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040836.json:
```json
{
    "body": "I've attached a patch for the cleanup. It should apply cleanly on top of #5200. \n\nAuthor: Florent Hivert",
    "created_at": "2009-03-01T18:03:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40836",
    "user": "hivert"
}
```

I've attached a patch for the cleanup. It should apply cleanly on top of #5200. 

Author: Florent Hivert



---

archive/issue_comments_040837.json:
```json
{
    "body": "Attachment\n\nGood version of the file",
    "created_at": "2009-03-01T18:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40837",
    "user": "hivert"
}
```

Attachment

Good version of the file



---

archive/issue_comments_040838.json:
```json
{
    "body": "When applying the patch on top of 3.4 with the following patches applied:\n\n```\nzephyr-/opt/sage/devel/sage>hg qapplied\ninteger_lists_lex-4549-submitted.patch\nsubsets_subwords-5200-submitted.2.patch\nsubsets_subwords-5200-review.patch\nsubwords_fix-5534-submitted.patch\ncombinatorialclass_iter_len_count_cleanup.patch\n```\n\nI get a reject in \n\n```\nzephyr-/opt/sage/devel/sage>cat sage/combinat/subset.py.rej\n--- subset.py\n+++ subset.py\n@@ -522,7 +522,7 @@\n             [0, 1, 3]\n             sage: S._multiplicities\n             [1, 2, 1]\n-            sage: Subsets([1,2,3,3], multiset=True).count()\n+            sage: Subsets([1,2,3,3], multiset=True).cardinality()\n             12\n             sage: S == loads(dumps(S))\n             True\n@@ -604,7 +604,7 @@\n             sage: S = Subsets([1,2,3,3],2, multiset=True)\n             sage: S._k\n             2\n-            sage: S.count()\n+            sage: S.cardinality()\n             4\n             sage: S.first()\n             [1, 2]\n```\n\n\nMoreover, the following tests get broken:\n\n```\n        sage -t  \"3.4.rc0/devel/sage-patches/sage/combinat/sf/ns_macdonald.py\"\n        sage -t  \"3.4.rc0/devel/sage-patches/sage/combinat/subset.py\"\n        sage -t  \"3.4.rc0/devel/sage-patches/sage/combinat/words/words.py\"\n```\n\neither by the deprecation warnings, or for words by a change of output: \n`96889010407L ->  96889010407`\n\nOther than this, the patch sounds good to me!",
    "created_at": "2009-04-02T06:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40838",
    "user": "nthiery"
}
```

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
@@ -522,7 +522,7 @@
             [0, 1, 3]
             sage: S._multiplicities
             [1, 2, 1]
-            sage: Subsets([1,2,3,3], multiset=True).count()
+            sage: Subsets([1,2,3,3], multiset=True).cardinality()
             12
             sage: S == loads(dumps(S))
             True
@@ -604,7 +604,7 @@
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

archive/issue_comments_040839.json:
```json
{
    "body": "In CartesianProduct, shouldn't we test first if it.cardinality works, and resort to len if this raised an AttributeError?\nLine 3 of the doc of InfiniteAbstractCombinatorialClass:\n- inerit -> inherit, wich -> which,  count -> cardinality, ...\nThe log of the patch should advertise this new class\nIn CyclicPermutations: leave at least a note that this deviates from the standard (__iter__/list take no argument), and should be cleaned up further at some point\nIn the examples (like in SemistandardTableaux), do we want to use: `[t for t in iterable]` or `list(iterable)`",
    "created_at": "2009-04-02T06:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40839",
    "user": "nthiery"
}
```

In CartesianProduct, shouldn't we test first if it.cardinality works, and resort to len if this raised an AttributeError?
Line 3 of the doc of InfiniteAbstractCombinatorialClass:
- inerit -> inherit, wich -> which,  count -> cardinality, ...
The log of the patch should advertise this new class
In CyclicPermutations: leave at least a note that this deviates from the standard (__iter__/list take no argument), and should be cleaned up further at some point
In the examples (like in SemistandardTableaux), do we want to use: `[t for t in iterable]` or `list(iterable)`



---

archive/issue_comments_040840.json:
```json
{
    "body": "I've looked over the changes to the words files. Everything looks good. To fix the problem with the doctests related to 96889010407L that nthiery mentioned above, just have Word_n.cardinality() (in sage/combinat/words/words.py) return a Sage Integer instead of a Python int.  If you do this, then it also deals with #4938.",
    "created_at": "2009-04-02T08:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40840",
    "user": "saliola"
}
```

I've looked over the changes to the words files. Everything looks good. To fix the problem with the doctests related to 96889010407L that nthiery mentioned above, just have Word_n.cardinality() (in sage/combinat/words/words.py) return a Sage Integer instead of a Python int.  If you do this, then it also deals with #4938.



---

archive/issue_comments_040841.json:
```json
{
    "body": "Addressed Nicolas reqests.",
    "created_at": "2009-04-02T08:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40841",
    "user": "hivert"
}
```

Addressed Nicolas reqests.



---

archive/issue_comments_040842.json:
```json
{
    "body": "Attachment\n\nDear Nicolas,\n\nI sumbmitted a new patch which should addres all the issues except this last one:   \n\n> In the examples (like in SemistandardTableaux), do we want to use: `[t for t in iterable]` or `list(iterable)`\n\nI think both kind of example should by advertised. IMHO, they both are very python idiomatic, the first one allows for extra condition, the second one is shorter. The only clear argument is that the first one is slightly faster:\n\n```\nsage: timeit(\"it = iter(Permutations(6)); list(it)\")\n125 loops, best of 3: 4.57 ms per loop\nsage: timeit(\"it = iter(Permutations(6)); list(it)\")\n125 loops, best of 3: 4.45 ms per loop\nsage: timeit(\"it = iter(Permutations(6)); [i for i in it]\")\n125 loops, best of 3: 4.64 ms per loop\nsage: timeit(\"it = iter(Permutations(6)); [i for i in it]\")\n125 loops, best of 3: 4.61 ms per loop\n```\n\nDo we really what to standardize all the doc on it ? \n\nCheers,\n\nFlorent",
    "created_at": "2009-04-02T08:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40842",
    "user": "hivert"
}
```

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

archive/issue_comments_040843.json:
```json
{
    "body": "Dear Franco,\n\n> I've looked over the changes to the words files. Everything looks good. To fix the problem with the doctests related to 96889010407L that nthiery mentioned above, just have Word_n.cardinality() (in sage/combinat/words/words.py) return a Sage Integer instead of a Python int.  If you do this, then it also deals with #4938.\n\nActually, the problem was that I forgot to re-export the patch from the\ncombinat server... \n\nI can't reproduce the problem on word but I don't have access to a 32bit machine. More precisely, `words.size_of_alphabet()` seems now to always return a sage integer. That should fix the problem. Can you please check it ?\n\nCheers,\n\nFlorent",
    "created_at": "2009-04-02T09:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40843",
    "user": "hivert"
}
```

Dear Franco,

> I've looked over the changes to the words files. Everything looks good. To fix the problem with the doctests related to 96889010407L that nthiery mentioned above, just have Word_n.cardinality() (in sage/combinat/words/words.py) return a Sage Integer instead of a Python int.  If you do this, then it also deals with #4938.

Actually, the problem was that I forgot to re-export the patch from the
combinat server... 

I can't reproduce the problem on word but I don't have access to a 32bit machine. More precisely, `words.size_of_alphabet()` seems now to always return a sage integer. That should fix the problem. Can you please check it ?

Cheers,

Florent



---

archive/issue_comments_040844.json:
```json
{
    "body": "Replying to [comment:9 hivert]:\n>       Dear Franco,\n>\n> I can't reproduce the problem on word but I don't have access to a 32bit machine. More precisely, `words.size_of_alphabet()` seems now to always return a sage integer. That should fix the problem. Can you please check it ?\n\nSorry it took so long: I had to compile sage on a 32-bit machine!\n\nThe last patch (combinatorialclass_iter_len_count_cleanup-5308-submitted.patch) applies cleanly to sage-3.4 on top of the patches for #5200 and #4549. I ran all the combinat doctests and all tests passed.\n\nYou get a positive review from me. I won't change the status though, since Nicolas might still have some issues.",
    "created_at": "2009-04-02T21:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40844",
    "user": "saliola"
}
```

Replying to [comment:9 hivert]:
>       Dear Franco,
>
> I can't reproduce the problem on word but I don't have access to a 32bit machine. More precisely, `words.size_of_alphabet()` seems now to always return a sage integer. That should fix the problem. Can you please check it ?

Sorry it took so long: I had to compile sage on a 32-bit machine!

The last patch (combinatorialclass_iter_len_count_cleanup-5308-submitted.patch) applies cleanly to sage-3.4 on top of the patches for #5200 and #4549. I ran all the combinat doctests and all tests passed.

You get a positive review from me. I won't change the status though, since Nicolas might still have some issues.



---

archive/issue_comments_040845.json:
```json
{
    "body": "Replying to [comment:8 hivert]:\n> > In the examples (like in SemistandardTableaux), do we want to use: `[t for t in iterable]` or `list(iterable)`\n> \n> I think both kind of example should by advertised. IMHO, they both are very python idiomatic, the first one allows for extra condition, the second one is shorter. The only clear argument is that the first one is slightly faster:\n> {{{\n> sage: timeit(\"it = iter(Permutations(6)); list(it)\")\n> 125 loops, best of 3: 4.57 ms per loop\n> sage: timeit(\"it = iter(Permutations(6)); list(it)\")\n> 125 loops, best of 3: 4.45 ms per loop\n> sage: timeit(\"it = iter(Permutations(6)); [i for i in it]\")\n> 125 loops, best of 3: 4.64 ms per loop\n> sage: timeit(\"it = iter(Permutations(6)); [i for i in it]\")\n> 125 loops, best of 3: 4.61 ms per loop\n> }}}\n> Do we really what to standardize all the doc on it ? \n\nGood point. The speed difference is too negligible that it seems likely to change in the future one way or the other. I guess we can just leave it as it is. Future will tell if any of the two form become more sage-combinat idiomatic. \n\nPositive review",
    "created_at": "2009-04-04T00:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40845",
    "user": "nthiery"
}
```

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

archive/issue_comments_040846.json:
```json
{
    "body": "Hmm, one last thing: In `def __len__(self): ` you deprecate `__len__` and tell people to use count. Isn't it possible to deprecate `__len__` and have it call count() automatically because that is the way it is supposed to work.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-04T00:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40846",
    "user": "mabshoff"
}
```

Hmm, one last thing: In `def __len__(self): ` you deprecate `__len__` and tell people to use count. Isn't it possible to deprecate `__len__` and have it call count() automatically because that is the way it is supposed to work.

Cheers,

Michael



---

archive/issue_comments_040847.json:
```json
{
    "body": "Replying to [comment:12 mabshoff]:\n> Hmm, one last thing: In `def __len__(self): ` you deprecate `__len__` and tell people to use count. Isn't it possible to deprecate `__len__` and have it call count() automatically because that is the way it is supposed to work.\n\nIt should say that one needs to use cardinality instead of `__len__`.\n\nThere are a few reasons why this doesn't work. One reason is that `__len__` must return a Python int. So, if the CombinatorialClass is too big, then calling `__len__` will raise an error, which is a bug.\n\nAnother problem is that some methods, like `__list__`, call `__len__` behind the scenes. This means that there would be deprecation warnings popping up in various places: for instance, `list(Permutations(3))` would give a warning, and it would be very confusing to a user not familiar with Python internals to see a warning about using `__len__` when they didn't obviously call `__len__`. Also the doctests would be littered with such deprecation warnings in various places (whenever `list/filter/map` are called). Instead, we decided to raise an `AttributeError`, which behaves nicely with Python's specifications on how `__len__` is to behave when called by `list/filter/map`, and also gives an appropriate error message when `len` is called directly. It really is a special case, where the usual deprecation procedure won't work.",
    "created_at": "2009-04-04T06:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40847",
    "user": "saliola"
}
```

Replying to [comment:12 mabshoff]:
> Hmm, one last thing: In `def __len__(self): ` you deprecate `__len__` and tell people to use count. Isn't it possible to deprecate `__len__` and have it call count() automatically because that is the way it is supposed to work.

It should say that one needs to use cardinality instead of `__len__`.

There are a few reasons why this doesn't work. One reason is that `__len__` must return a Python int. So, if the CombinatorialClass is too big, then calling `__len__` will raise an error, which is a bug.

Another problem is that some methods, like `__list__`, call `__len__` behind the scenes. This means that there would be deprecation warnings popping up in various places: for instance, `list(Permutations(3))` would give a warning, and it would be very confusing to a user not familiar with Python internals to see a warning about using `__len__` when they didn't obviously call `__len__`. Also the doctests would be littered with such deprecation warnings in various places (whenever `list/filter/map` are called). Instead, we decided to raise an `AttributeError`, which behaves nicely with Python's specifications on how `__len__` is to behave when called by `list/filter/map`, and also gives an appropriate error message when `len` is called directly. It really is a special case, where the usual deprecation procedure won't work.



---

archive/issue_comments_040848.json:
```json
{
    "body": "If its still possible, I'd rather seen this integrated in 3.4.1, to be sure that new users get good habits. \n\nFlorent",
    "created_at": "2009-04-04T08:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40848",
    "user": "hivert"
}
```

If its still possible, I'd rather seen this integrated in 3.4.1, to be sure that new users get good habits. 

Florent



---

archive/issue_comments_040849.json:
```json
{
    "body": "The patch needed a trivial rebase because of my review patch on #4549.\nThe rebased patch should apply cleanly on top of attachment:ticket:4549:integer_lists_lex-4549-submitted.patch and\nattachment:ticket:4549:integer_lists_lex-4549-review.patch\n\nCheers,\n\nFlorent",
    "created_at": "2009-04-04T15:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40849",
    "user": "hivert"
}
```

The patch needed a trivial rebase because of my review patch on #4549.
The rebased patch should apply cleanly on top of attachment:ticket:4549:integer_lists_lex-4549-submitted.patch and
attachment:ticket:4549:integer_lists_lex-4549-review.patch

Cheers,

Florent



---

archive/issue_comments_040850.json:
```json
{
    "body": "This patch introduces two trivial to fix doctest failures:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc0$ ./sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\nsage -t -long \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc0/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\", line 911:\n    sage: I.dimension()\nExpected:\n    verbose 0 (...: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.\n    0\nGot:\n    verbose 0 (891: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.\n    doctest:966: DeprecationWarning: The usage of iterator for combinatorial classes is deprecated. Please use the class itself\n    0\n**********************************************************************\n1 items had failures:\n   1 of  15 in __main__.example_17\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.rc0/tmp/.doctest_multi_polynomial_ideal.py\n\t [11.3 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\nTotal time for all tests: 11.3 seconds\nmabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc0$ ./sage -t -long devel/sage/doc/en/a_tour_of_sage/index.rst\nsage -t -long \"devel/sage/doc/en/a_tour_of_sage/index.rst\"  \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc0/devel/sage/doc/en/a_tour_of_sage/index.rst\", line 132:\n    sage: z = Partitions(10^8).count() #about 4.5 seconds\nExpected nothing\nGot:\n    doctest:1: DeprecationWarning: The usage of iterator for combinatorial classes is deprecated. Please use the class itself\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_9\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.rc0/tmp/.doctest_index.py\n\t [10.9 s]\nexit code: 1024\n```\n\nOnce those are fixed the positive review can be reinstated.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-05T00:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40850",
    "user": "mabshoff"
}
```

This patch introduces two trivial to fix doctest failures:

```
mabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc0$ ./sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py
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
mabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc0$ ./sage -t -long devel/sage/doc/en/a_tour_of_sage/index.rst
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

archive/issue_comments_040851.json:
```json
{
    "body": "This ticket also fixes #4938 which should be closed afterwards.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-05T00:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40851",
    "user": "mabshoff"
}
```

This ticket also fixes #4938 which should be closed afterwards.

Cheers,

Michael



---

archive/issue_comments_040852.json:
```json
{
    "body": "Attachment\n\nHopefully final version",
    "created_at": "2009-04-05T07:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40852",
    "user": "hivert"
}
```

Attachment

Hopefully final version



---

archive/issue_comments_040853.json:
```json
{
    "body": "Replying to [comment:16 mabshoff]:\n> This patch introduces two trivial to fix doctest failures:\n\n* Oups !!! I probably let the first pass because it's typically one of the few files that triggers the pexpect issue on my fast testing machine...\n\n* Next time I'll check also the .rst files. \n\nThese should be fixed right now. Re-uploaded a new patch and re marked as positive reviewed. \n\nCheers,\n\nFlorent",
    "created_at": "2009-04-05T07:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40853",
    "user": "hivert"
}
```

Replying to [comment:16 mabshoff]:
> This patch introduces two trivial to fix doctest failures:

* Oups !!! I probably let the first pass because it's typically one of the few files that triggers the pexpect issue on my fast testing machine...

* Next time I'll check also the .rst files. 

These should be fixed right now. Re-uploaded a new patch and re marked as positive reviewed. 

Cheers,

Florent



---

archive/issue_comments_040854.json:
```json
{
    "body": "I have had to update the hunk applied to sage/rings/polynomial/multi_polynomial_ideal.py due to #5485, but I am doctesting the patch now ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-05T23:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40854",
    "user": "mabshoff"
}
```

I have had to update the hunk applied to sage/rings/polynomial/multi_polynomial_ideal.py due to #5485, but I am doctesting the patch now ;)

Cheers,

Michael



---

archive/issue_comments_040855.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-05T23:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40855",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc1.

Cheers,

Michael



---

archive/issue_comments_040856.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-05T23:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40856",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040857.json:
```json
{
    "body": "Slightly rebased version of Florent's last patch",
    "created_at": "2009-04-05T23:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40857",
    "user": "mabshoff"
}
```

Slightly rebased version of Florent's last patch



---

archive/issue_comments_040858.json:
```json
{
    "body": "Attachment\n\nFYI: Merged trac_5308_combinatorialclass_iter_len_count_cleanup-5308-rebased.patch in Sage 3.4.1.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T00:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5308#issuecomment-40858",
    "user": "mabshoff"
}
```

Attachment

FYI: Merged trac_5308_combinatorialclass_iter_len_count_cleanup-5308-rebased.patch in Sage 3.4.1.rc1.

Cheers,

Michael
