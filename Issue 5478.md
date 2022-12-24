# Issue 5478: RestrictedPartitions is very slow and a huge memory hog

archive/issues_005478.json:
```json
{
    "body": "Assignee: @dandrake\n\nCC:  sage-combinat\n\nKeywords: combinat, partitions, gap\n\nI have code that does the same as\n\n```\nRestrictedPartitions(3000, [1000, 500, 100, 50, 10])\n```\n\nbut about 5.5 times faster...and on my system,\n\n```\nRestrictedPartitions(5000, [1000, 500, 100, 50, 10])\n```\n\nuses over two gigabytes of memory, whereas my code takes about 9.2 seconds with minimal memory usage.\n\nI need to fiddle with my code so that it's a drop-in replacement for RestrictedPartitions, but I should have a patch up soon.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5478\n\n",
    "created_at": "2009-03-11T03:46:36Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "RestrictedPartitions is very slow and a huge memory hog",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5478",
    "user": "@dandrake"
}
```
Assignee: @dandrake

CC:  sage-combinat

Keywords: combinat, partitions, gap

I have code that does the same as

```
RestrictedPartitions(3000, [1000, 500, 100, 50, 10])
```

but about 5.5 times faster...and on my system,

```
RestrictedPartitions(5000, [1000, 500, 100, 50, 10])
```

uses over two gigabytes of memory, whereas my code takes about 9.2 seconds with minimal memory usage.

I need to fiddle with my code so that it's a drop-in replacement for RestrictedPartitions, but I should have a patch up soon.

Issue created by migration from https://trac.sagemath.org/ticket/5478





---

archive/issue_comments_042486.json:
```json
{
    "body": "Maybe I should add that I'm interested, of course, in *iterating* through all those partitions. Just running \"`RestrictedPartitions(3000, [1000, 500, 100, 50, 10])`\" is very fast because it just returns an iterator. The actual code I'm running is stuff like\n\n```\nsum(1 for p in RestrictedPartitions(...))\n```\n",
    "created_at": "2009-03-11T03:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42486",
    "user": "@dandrake"
}
```

Maybe I should add that I'm interested, of course, in *iterating* through all those partitions. Just running "`RestrictedPartitions(3000, [1000, 500, 100, 50, 10])`" is very fast because it just returns an iterator. The actual code I'm running is stuff like

```
sum(1 for p in RestrictedPartitions(...))
```




---

archive/issue_comments_042487.json:
```json
{
    "body": "For ease of reviewing, I plan to have two patches here: the first one includes deprecation for RestrictedPartitions and fixes up some problems with the Partitions docstring. The second will actually implement the new `Partitions(..., parts_in=...)` code.",
    "created_at": "2009-03-25T04:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42487",
    "user": "@dandrake"
}
```

For ease of reviewing, I plan to have two patches here: the first one includes deprecation for RestrictedPartitions and fixes up some problems with the Partitions docstring. The second will actually implement the new `Partitions(..., parts_in=...)` code.



---

archive/issue_comments_042488.json:
```json
{
    "body": "The second patch gets doctests working and adds the new functionality. I'm not entirely sure I did the deprecation stuff correctly; I added a deprecation warning, and then fiddled with all the doctests in the old RestrictedPartitions code so that it passes doctests.",
    "created_at": "2009-03-27T12:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42488",
    "user": "@dandrake"
}
```

The second patch gets doctests working and adds the new functionality. I'm not entirely sure I did the deprecation stuff correctly; I added a deprecation warning, and then fiddled with all the doctests in the old RestrictedPartitions code so that it passes doctests.



---

archive/issue_comments_042489.json:
```json
{
    "body": "A little ego update to the patch -- I added myself to the authors list. Anyone reviewing this might want to look at my test script: [restricted_partitions_test_suite.sage](http://sage.math.washington.edu/home/drake/restricted_partitions_test_suite.sage). I've run over 10,000 successful tests with it.",
    "created_at": "2009-03-28T02:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42489",
    "user": "@dandrake"
}
```

A little ego update to the patch -- I added myself to the authors list. Anyone reviewing this might want to look at my test script: [restricted_partitions_test_suite.sage](http://sage.math.washington.edu/home/drake/restricted_partitions_test_suite.sage). I've run over 10,000 successful tests with it.



---

archive/issue_comments_042490.json:
```json
{
    "body": "Some benchmarks (all on sage.math):\n\n\n```\nBEFORE\nsage: get_memory_usage()\n695.7421875\nsage: ps = RestrictedPartitions(100, ([1,6..100] + [4,9..100]))\nsage: %time sum(1 for p in ps)\nCPU times: user 26.89 s, sys: 1.11 s, total: 28.00 s\nWall time: 28.69 s\n74040\nsage: get_memory_usage()\n1781.41796875\n```\n\n\n\n```\nAFTER\nsage: get_memory_usage()\n699.828125\nsage: ps = Partitions(100, parts_in=([1,6..100] + [4,9..100]))\nsage: %time sum(1 for p in ps)\nCPU times: user 4.96 s, sys: 0.02 s, total: 4.98 s\nWall time: 4.98 s\n74040\nsage: get_memory_usage()\n699.828125\n```\n\n\nThe above example which prompted this ticket:\n\n\n```\nBEFORE\nsage: get_memory_usage()\n695.73828125\nsage: ps = RestrictedPartitions(3000, [10,50,100,500,1000])\nsage: %time sum(1 for p in ps)\nCPU times: user 5.69 s, sys: 0.21 s, total: 5.90 s\nWall time: 6.05 s\n3506\nsage: get_memory_usage()\n935.48046875\n```\n\n\n\n```\nAFTER\nsage: get_memory_usage()\n699.82421875\nsage: ps = Partitions(3000, parts_in=[10,50,100,500,1000])\nsage: %time sum(1 for p in ps)\nCPU times: user 1.08 s, sys: 0.00 s, total: 1.08 s\nWall time: 1.09 s\n3506\nsage: get_memory_usage()\n699.82421875\n```\n",
    "created_at": "2009-03-28T03:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42490",
    "user": "@dandrake"
}
```

Some benchmarks (all on sage.math):


```
BEFORE
sage: get_memory_usage()
695.7421875
sage: ps = RestrictedPartitions(100, ([1,6..100] + [4,9..100]))
sage: %time sum(1 for p in ps)
CPU times: user 26.89 s, sys: 1.11 s, total: 28.00 s
Wall time: 28.69 s
74040
sage: get_memory_usage()
1781.41796875
```



```
AFTER
sage: get_memory_usage()
699.828125
sage: ps = Partitions(100, parts_in=([1,6..100] + [4,9..100]))
sage: %time sum(1 for p in ps)
CPU times: user 4.96 s, sys: 0.02 s, total: 4.98 s
Wall time: 4.98 s
74040
sage: get_memory_usage()
699.828125
```


The above example which prompted this ticket:


```
BEFORE
sage: get_memory_usage()
695.73828125
sage: ps = RestrictedPartitions(3000, [10,50,100,500,1000])
sage: %time sum(1 for p in ps)
CPU times: user 5.69 s, sys: 0.21 s, total: 5.90 s
Wall time: 6.05 s
3506
sage: get_memory_usage()
935.48046875
```



```
AFTER
sage: get_memory_usage()
699.82421875
sage: ps = Partitions(3000, parts_in=[10,50,100,500,1000])
sage: %time sum(1 for p in ps)
CPU times: user 1.08 s, sys: 0.00 s, total: 1.08 s
Wall time: 1.09 s
3506
sage: get_memory_usage()
699.82421875
```




---

archive/issue_comments_042491.json:
```json
{
    "body": "Patch look good. However, before finishing my review I'm waiting it to be rebased on top of 3.4.1. Also some interface problem have been discussed by e-mail: It was decided more that one month ago that a combinatorial class should define:\n* `__iter__` instead of `iterator`.\n* `cardinality` instead of `count` or `len`.\n\n\nFlorent",
    "created_at": "2009-04-07T08:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42491",
    "user": "@hivert"
}
```

Patch look good. However, before finishing my review I'm waiting it to be rebased on top of 3.4.1. Also some interface problem have been discussed by e-mail: It was decided more that one month ago that a combinatorial class should define:
* `__iter__` instead of `iterator`.
* `cardinality` instead of `count` or `len`.


Florent



---

archive/issue_comments_042492.json:
```json
{
    "body": "Please keep the subject standard so that the proper reports are picking up the right tickets.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-07T08:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42492",
    "user": "mabshoff"
}
```

Please keep the subject standard so that the proper reports are picking up the right tickets.

Cheers,

Michael



---

archive/issue_comments_042493.json:
```json
{
    "body": "deprecate RestrictedPartitions and fix up some documentation",
    "created_at": "2009-04-09T02:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42493",
    "user": "@dandrake"
}
```

deprecate RestrictedPartitions and fix up some documentation



---

archive/issue_comments_042494.json:
```json
{
    "body": "Attachment [trac_5478-1.patch](tarball://root/attachments/some-uuid/ticket5478/trac_5478-1.patch) by @dandrake created at 2009-04-09 02:24:31\n\nimplement new Partitions class with parts_in keyword",
    "created_at": "2009-04-09T02:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42494",
    "user": "@dandrake"
}
```

Attachment [trac_5478-1.patch](tarball://root/attachments/some-uuid/ticket5478/trac_5478-1.patch) by @dandrake created at 2009-04-09 02:24:31

implement new Partitions class with parts_in keyword



---

archive/issue_comments_042495.json:
```json
{
    "body": "Attachment [trac_5478-2.patch](tarball://root/attachments/some-uuid/ticket5478/trac_5478-2.patch) by @dandrake created at 2009-04-09 02:25:27\n\nI've updated the patches to apply on top of 3.4.1.rc1.",
    "created_at": "2009-04-09T02:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42495",
    "user": "@dandrake"
}
```

Attachment [trac_5478-2.patch](tarball://root/attachments/some-uuid/ticket5478/trac_5478-2.patch) by @dandrake created at 2009-04-09 02:25:27

I've updated the patches to apply on top of 3.4.1.rc1.



---

archive/issue_comments_042496.json:
```json
{
    "body": "Anyone reviewing this might want to look at my test script: [restricted_partitions_test_suite.sage](http://sage.math.washington.edu/home/drake/restricted_partitions_test_suite.sage). I've run over 10,000 successful tests with it.\n\nThis script is great. I should be put in sage in one place or one other. If someone tries to optimize your code (eg: Cythonize), he surely will be happy to have your test code. Why not shipping it into the patch with a more explicit name and a one-line example on how to use it with the comment \" #longtest \" ?\n\nFlorent",
    "created_at": "2009-04-09T07:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42496",
    "user": "@hivert"
}
```

Anyone reviewing this might want to look at my test script: [restricted_partitions_test_suite.sage](http://sage.math.washington.edu/home/drake/restricted_partitions_test_suite.sage). I've run over 10,000 successful tests with it.

This script is great. I should be put in sage in one place or one other. If someone tries to optimize your code (eg: Cythonize), he surely will be happy to have your test code. Why not shipping it into the patch with a more explicit name and a one-line example on how to use it with the comment " #longtest " ?

Florent



---

archive/issue_comments_042497.json:
```json
{
    "body": "Some comment on the first patch:\n\nI'm not a native English speaker but it seems to me that \n  If ``starting=p`` is passed, then the combinatorial class of partitions greater than or equal to `p` in lexicographic order is returned. \nis clearer if phrased\n  If ``starting=p`` is passed, then the combinatorial class of partitions with part greater than or equal to `p` in lexicographic order is returned. \n\nIn the same way\n  If ``ending=p`` is passed, then the combinatorial class of partitions at most `p` in lexicographic order is returned. \nis better phrased\n  If ``ending=p`` is passed, then the combinatorial class of partitions with part at most `p` in lexicographic order is returned.\n\nOtherwise the rest of the first patch looks good. I'm working on the second one.\n\nFlorent",
    "created_at": "2009-04-09T07:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42497",
    "user": "@hivert"
}
```

Some comment on the first patch:

I'm not a native English speaker but it seems to me that 
  If ``starting=p`` is passed, then the combinatorial class of partitions greater than or equal to `p` in lexicographic order is returned. 
is clearer if phrased
  If ``starting=p`` is passed, then the combinatorial class of partitions with part greater than or equal to `p` in lexicographic order is returned. 

In the same way
  If ``ending=p`` is passed, then the combinatorial class of partitions at most `p` in lexicographic order is returned. 
is better phrased
  If ``ending=p`` is passed, then the combinatorial class of partitions with part at most `p` in lexicographic order is returned.

Otherwise the rest of the first patch looks good. I'm working on the second one.

Florent



---

archive/issue_comments_042498.json:
```json
{
    "body": "Replying to [comment:10 hivert]:\n> Some comment on the first patch:\n> \n> I'm not a native English speaker but it seems to me that \n>   If ``starting=p`` is passed, then the combinatorial class of partitions greater than or equal to `p` in lexicographic order is returned. \n> is clearer if phrased\n>   If ``starting=p`` is passed, then the combinatorial class of partitions with part greater than or equal to `p` in lexicographic order is returned.\n\n\"p\" refers to a partition, not to a part, so the text is okay. Perhaps we should make that more clear, though. I plan on opening a ticket to improve the documentation in partition.py, so we can do that then.\n\nReplying to [comment:9 hivert]:\n> > Anyone reviewing this might want to look at my test script: restricted_partitions_test_suite.sage. I've run over 10,000 successful tests with it.\n> \n> This script is great. I should be put in sage in one place or one other. If someone tries to \n> optimize your code (eg: Cythonize), he surely will be happy to have your test code. Why not \n> shipping it into the patch with a more explicit name and a one-line example on how to use it \n> with the comment \" #longtest \" ? \n\nWell, right now, the script only halts if it finds an error, so it would be a really, really long test. :)\n\nThe tests also can use lots of memory, since it puts a list of the partitions into memory. But if anyone thinks (a mildly modified version of) the script should get run on a \"long\" test, I'm happy to have it included.",
    "created_at": "2009-04-10T04:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42498",
    "user": "@dandrake"
}
```

Replying to [comment:10 hivert]:
> Some comment on the first patch:
> 
> I'm not a native English speaker but it seems to me that 
>   If ``starting=p`` is passed, then the combinatorial class of partitions greater than or equal to `p` in lexicographic order is returned. 
> is clearer if phrased
>   If ``starting=p`` is passed, then the combinatorial class of partitions with part greater than or equal to `p` in lexicographic order is returned.

"p" refers to a partition, not to a part, so the text is okay. Perhaps we should make that more clear, though. I plan on opening a ticket to improve the documentation in partition.py, so we can do that then.

Replying to [comment:9 hivert]:
> > Anyone reviewing this might want to look at my test script: restricted_partitions_test_suite.sage. I've run over 10,000 successful tests with it.
> 
> This script is great. I should be put in sage in one place or one other. If someone tries to 
> optimize your code (eg: Cythonize), he surely will be happy to have your test code. Why not 
> shipping it into the patch with a more explicit name and a one-line example on how to use it 
> with the comment " #longtest " ? 

Well, right now, the script only halts if it finds an error, so it would be a really, really long test. :)

The tests also can use lots of memory, since it puts a list of the partitions into memory. But if anyone thinks (a mildly modified version of) the script should get run on a "long" test, I'm happy to have it included.



---

archive/issue_comments_042499.json:
```json
{
    "body": "Improved doctests for deprecation warnings.",
    "created_at": "2009-04-12T15:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42499",
    "user": "@hivert"
}
```

Improved doctests for deprecation warnings.



---

archive/issue_comments_042500.json:
```json
{
    "body": "Attachment [trac_5478-review.patch](tarball://root/attachments/some-uuid/ticket5478/trac_5478-review.patch) by @hivert created at 2009-04-12 16:08:06\n\nThe patch looks good. The doctests passed except that depending on the base the doctests numbers may differ. So I added a review patch which replace the explicit doctest numbers with `...`. This should solve this problem. \n\nI'm giving a positive review... Though maybe someone should reread my trivial review patch. \n\nConcerning the script it is quite redundant with the .check() method we'll have with categories.   \n\nFlorent",
    "created_at": "2009-04-12T16:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42500",
    "user": "@hivert"
}
```

Attachment [trac_5478-review.patch](tarball://root/attachments/some-uuid/ticket5478/trac_5478-review.patch) by @hivert created at 2009-04-12 16:08:06

The patch looks good. The doctests passed except that depending on the base the doctests numbers may differ. So I added a review patch which replace the explicit doctest numbers with `...`. This should solve this problem. 

I'm giving a positive review... Though maybe someone should reread my trivial review patch. 

Concerning the script it is quite redundant with the .check() method we'll have with categories.   

Florent



---

archive/issue_comments_042501.json:
```json
{
    "body": "Thanks for fixing up those line numbers in the doctests...I struggled a bit to get those right, and had forgotten about the \"...\" stuff.",
    "created_at": "2009-04-12T23:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42501",
    "user": "@dandrake"
}
```

Thanks for fixing up those line numbers in the doctests...I struggled a bit to get those right, and had forgotten about the "..." stuff.



---

archive/issue_comments_042502.json:
```json
{
    "body": "Merged all three patches in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T02:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42502",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_042503.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T02:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5478#issuecomment-42503",
    "user": "mabshoff"
}
```

Resolution: fixed
