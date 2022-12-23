# Issue 5478: RestrictedPartitions is very slow and a huge memory hog

Issue created by migration from https://trac.sagemath.org/ticket/5478

Original creator: ddrake

Original creation time: 2009-03-11 03:46:36

Assignee: ddrake

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


---

Comment by ddrake created at 2009-03-11 03:58:12

Maybe I should add that I'm interested, of course, in *iterating* through all those partitions. Just running "`RestrictedPartitions(3000, [1000, 500, 100, 50, 10])`" is very fast because it just returns an iterator. The actual code I'm running is stuff like

```
sum(1 for p in RestrictedPartitions(...))
```



---

Comment by ddrake created at 2009-03-25 04:52:23

For ease of reviewing, I plan to have two patches here: the first one includes deprecation for RestrictedPartitions and fixes up some problems with the Partitions docstring. The second will actually implement the new `Partitions(..., parts_in=...)` code.


---

Comment by ddrake created at 2009-03-27 12:54:41

The second patch gets doctests working and adds the new functionality. I'm not entirely sure I did the deprecation stuff correctly; I added a deprecation warning, and then fiddled with all the doctests in the old RestrictedPartitions code so that it passes doctests.


---

Comment by ddrake created at 2009-03-28 02:29:35

A little ego update to the patch -- I added myself to the authors list. Anyone reviewing this might want to look at my test script: [restricted_partitions_test_suite.sage](http://sage.math.washington.edu/home/drake/restricted_partitions_test_suite.sage). I've run over 10,000 successful tests with it.


---

Comment by ddrake created at 2009-03-28 03:45:23

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

Comment by hivert created at 2009-04-07 08:02:05

Patch look good. However, before finishing my review I'm waiting it to be rebased on top of 3.4.1. Also some interface problem have been discussed by e-mail: It was decided more that one month ago that a combinatorial class should define:
   * `__iter__` instead of `iterator`.
   * `cardinality` instead of `count` or `len`.


Florent


---

Comment by mabshoff created at 2009-04-07 08:25:50

Please keep the subject standard so that the proper reports are picking up the right tickets.

Cheers,

Michael


---

Comment by ddrake created at 2009-04-09 02:23:34

deprecate RestrictedPartitions and fix up some documentation


---

Attachment

implement new Partitions class with parts_in keyword


---

Attachment

I've updated the patches to apply on top of 3.4.1.rc1.


---

Comment by hivert created at 2009-04-09 07:08:42

Anyone reviewing this might want to look at my test script: [restricted_partitions_test_suite.sage](http://sage.math.washington.edu/home/drake/restricted_partitions_test_suite.sage). I've run over 10,000 successful tests with it.

This script is great. I should be put in sage in one place or one other. If someone tries to optimize your code (eg: Cythonize), he surely will be happy to have your test code. Why not shipping it into the patch with a more explicit name and a one-line example on how to use it with the comment " #longtest " ?

Florent


---

Comment by hivert created at 2009-04-09 07:15:04

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

Comment by ddrake created at 2009-04-10 04:17:14

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

Comment by hivert created at 2009-04-12 15:51:05

Improved doctests for deprecation warnings.


---

Attachment

The patch looks good. The doctests passed except that depending on the base the doctests numbers may differ. So I added a review patch which replace the explicit doctest numbers with `...`. This should solve this problem. 

I'm giving a positive review... Though maybe someone should reread my trivial review patch. 

Concerning the script it is quite redundant with the .check() method we'll have with categories.   

Florent


---

Comment by ddrake created at 2009-04-12 23:19:01

Thanks for fixing up those line numbers in the doctests...I struggled a bit to get those right, and had forgotten about the "..." stuff.


---

Comment by mabshoff created at 2009-04-13 02:55:47

Merged all three patches in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 02:55:47

Resolution: fixed
