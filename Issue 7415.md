# Issue 7415: improve cycle decomposition

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2009-11-08 22:38:16

Assignee: mhansen

CC:  sage-combinat

Keywords: permutation

Let's continue using binary search to improve the permutation methods.



---

Comment by ylchapuy created at 2009-11-08 22:45:58

Changing status from new to needs_review.


---

Attachment

For the record,

before:

```
sage: p= Permutations(1000)[1234567123413251514514513541]
sage: timeit('p.to_cycles()')
125 loops, best of 3: 5.27 ms per loop
sage: timeit('p.to_cycles(singletons=False)')
125 loops, best of 3: 4.37 ms per loop
sage: p= Permutations(1000).random_element()
sage: timeit('p.to_cycles()')
5 loops, best of 3: 440 ms per loop
sage: timeit('p.to_cycles(singletons=False)')
5 loops, best of 3: 441 ms per loop
```


after:

```
sage: p= Permutations(1000)[1234567123413251514514513541]
sage: timeit('p.to_cycles()')
125 loops, best of 3: 4.68 ms per loop
sage: timeit('p.to_cycles(singletons=False)')
125 loops, best of 3: 2.35 ms per loop
sage: p= Permutations(1000).random_element()
sage: timeit('p.to_cycles()')
25 loops, best of 3: 21.1 ms per loop
sage: timeit('p.to_cycles(singletons=False)')
25 loops, best of 3: 23.3 ms per loop
```


it can be slightly slower for small permutations with `singletons=False` (because of the way we construct L), but I think it's worth it.


---

Comment by hivert created at 2009-11-09 08:53:12

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2009-11-09 08:53:12

Replying to [comment:1 ylchapuy]:

> it can be slightly slower for small permutations with `singletons=False` (because of the way we construct L), but I think it's worth it.

It is indeed in both cases:

Before

```
sage: for i in range(8): timeit('[p.to_cycles(True) for p in Permutations(i)]')
....: 
625 loops, best of 3: 16.5 µs per loop
625 loops, best of 3: 22.3 µs per loop
625 loops, best of 3: 41.3 µs per loop
625 loops, best of 3: 114 µs per loop
625 loops, best of 3: 450 µs per loop
125 loops, best of 3: 2.45 ms per loop
25 loops, best of 3: 15.8 ms per loop
5 loops, best of 3: 118 ms per loop
sage: for i in range(8): timeit('[p.to_cycles(False) for p in Permutations(i)]')
....: 
625 loops, best of 3: 32.4 µs per loop
625 loops, best of 3: 20.8 µs per loop
625 loops, best of 3: 39.3 µs per loop
625 loops, best of 3: 109 µs per loop
625 loops, best of 3: 441 µs per loop
125 loops, best of 3: 2.41 ms per loop
25 loops, best of 3: 15.4 ms per loop
5 loops, best of 3: 113 ms per loop
```


After:

```
sage: for i in range(8): timeit('[p.to_cycles(True) for p in Permutations(i)]')
....: 
625 loops, best of 3: 23.2 µs per loop
625 loops, best of 3: 26.3 µs per loop
625 loops, best of 3: 49.6 µs per loop
625 loops, best of 3: 136 µs per loop
625 loops, best of 3: 542 µs per loop
125 loops, best of 3: 2.9 ms per loop
25 loops, best of 3: 18.1 ms per loop
5 loops, best of 3: 137 ms per loop
sage: for i in range(8): timeit('[p.to_cycles(False) for p in Permutations(i)]')
....: 
625 loops, best of 3: 22.4 µs per loop
625 loops, best of 3: 25 µs per loop
625 loops, best of 3: 49.2 µs per loop
625 loops, best of 3: 134 µs per loop
625 loops, best of 3: 542 µs per loop
125 loops, best of 3: 2.92 ms per loop
25 loops, best of 3: 18.8 ms per loop
5 loops, best of 3: 137 ms per loop
```

Why not having the bost of the two world devising a cut-of point ? 

Once again sorry to give you more work,

Florent


---

Comment by hivert created at 2009-11-09 09:24:03

Actually after some experiment I find out that this is a not a so good idea to use list + bisect. As it should be in a reasonable world, using python set is faster ! I'm preparing a new patch for this. 

Cheers,

Florent


---

Comment by hivert created at 2009-11-09 15:21:39

Changing status from needs_work to needs_review.


---

Attachment

Hi Yann,

I just uploaded a new patch which contains four different methods:
 - `to_cycles      ` : use a binary vector
 - `_to_cycles_orig` : the original implementation
 - `_to_cycles_set ` : the modification of your implementation using a sage set
 - `_to_cycles_list` : your implementation
I left in the code a little command to benchmark these four functions:

On small permutations the results are:

```
sage: for size in range(9): # not tested
 print size
 lp = Permutations(size).list()
 timeit('[p.to_cycles(False) for p in lp]')
 timeit('[p._to_cycles_set(False) for p in lp]')
 timeit('[p._to_cycles_list(False) for p in lp]')
 timeit('[p._to_cycles_orig(False) for p in lp]') 

0
625 loops, best of 3: 4.6 µs per loop
625 loops, best of 3: 16.8 µs per loop
625 loops, best of 3: 7.59 µs per loop
625 loops, best of 3: 2.97 µs per loop
1
625 loops, best of 3: 4.18 µs per loop
625 loops, best of 3: 9.06 µs per loop
625 loops, best of 3: 7.6 µs per loop
625 loops, best of 3: 4.78 µs per loop
2
625 loops, best of 3: 11.3 µs per loop
625 loops, best of 3: 22.1 µs per loop
625 loops, best of 3: 20.2 µs per loop
625 loops, best of 3: 12.9 µs per loop
3
625 loops, best of 3: 42 µs per loop
625 loops, best of 3: 73.3 µs per loop
625 loops, best of 3: 72.7 µs per loop
625 loops, best of 3: 47.7 µs per loop
4
625 loops, best of 3: 192 µs per loop
625 loops, best of 3: 325 µs per loop
625 loops, best of 3: 333 µs per loop
625 loops, best of 3: 224 µs per loop
5
625 loops, best of 3: 1.08 ms per loop
125 loops, best of 3: 1.75 ms per loop
125 loops, best of 3: 1.87 ms per loop
625 loops, best of 3: 1.33 ms per loop
6
125 loops, best of 3: 7.34 ms per loop
25 loops, best of 3: 11.8 ms per loop
25 loops, best of 3: 12.8 ms per loop
25 loops, best of 3: 9.28 ms per loop
7
5 loops, best of 3: 58.5 ms per loop
5 loops, best of 3: 91.1 ms per loop
5 loops, best of 3: 99.1 ms per loop
5 loops, best of 3: 72.7 ms per loop
8
5 loops, best of 3: 501 ms per loop
5 loops, best of 3: 772 ms per loop
5 loops, best of 3: 866 ms per loop
5 loops, best of 3: 631 ms per loop
```

On bigger permutations (I don't test the original implantation which is very slow:

```
for size in [10, 20, 50, 75, 100, 200, 500, 1000, # not tested
      2000, 5000, 10000, 15000, 20000, 30000,
      50000, 80000, 100000]: 
   print(size)
   lp = [Permutations(size).random_element() for i in range(20)]
   timeit("[p.to_cycles() for p in lp]")
   timeit("[p._to_cycles_set() for p in lp]")
   timeit("[p._to_cycles_list() for p in lp]") # not tested

10
625 loops, best of 3: 276 µs per loop
625 loops, best of 3: 367 µs per loop
625 loops, best of 3: 442 µs per loop
20
625 loops, best of 3: 428 µs per loop
625 loops, best of 3: 492 µs per loop
625 loops, best of 3: 687 µs per loop
50
625 loops, best of 3: 872 µs per loop
625 loops, best of 3: 905 µs per loop
625 loops, best of 3: 1.45 ms per loop
75
625 loops, best of 3: 1.21 ms per loop
625 loops, best of 3: 1.19 ms per loop
125 loops, best of 3: 2.08 ms per loop
100
125 loops, best of 3: 1.53 ms per loop
625 loops, best of 3: 1.5 ms per loop
125 loops, best of 3: 2.68 ms per loop
200
125 loops, best of 3: 2.94 ms per loop
125 loops, best of 3: 2.66 ms per loop
125 loops, best of 3: 5.31 ms per loop
500
125 loops, best of 3: 7.5 ms per loop
125 loops, best of 3: 7.2 ms per loop
25 loops, best of 3: 14.7 ms per loop
1000
25 loops, best of 3: 14.8 ms per loop
25 loops, best of 3: 13.9 ms per loop
25 loops, best of 3: 31.3 ms per loop
2000
25 loops, best of 3: 29.1 ms per loop
25 loops, best of 3: 28.1 ms per loop
5 loops, best of 3: 72.8 ms per loop
5000
5 loops, best of 3: 74 ms per loop
5 loops, best of 3: 69.1 ms per loop
5 loops, best of 3: 252 ms per loop
10000
5 loops, best of 3: 146 ms per loop
5 loops, best of 3: 151 ms per loop
5 loops, best of 3: 833 ms per loop
15000
5 loops, best of 3: 229 ms per loop
5 loops, best of 3: 236 ms per loop
5 loops, best of 3: 1.71 s per loop
20000
5 loops, best of 3: 317 ms per loop
5 loops, best of 3: 331 ms per loop
5 loops, best of 3: 2.85 s per loop
30000
5 loops, best of 3: 472 ms per loop
5 loops, best of 3: 553 ms per loop
5 loops, best of 3: 6.01 s per loop
50000
5 loops, best of 3: 844 ms per loop
5 loops, best of 3: 1.02 s per loop
5 loops, best of 3: 15.9 s per loop
80000
5 loops, best of 3: 1.45 s per loop
5 loops, best of 3: 1.81 s per loop
                    > 2 min...
100000
5 loops, best of 3: 1.87 s per loop
5 loops, best of 3: 2.43 s per loop
                    > 2 min ...
```

Since the default implementation is only beated by less that 10% I haven't written any algorithm selection. I kept the other implementation because there are some plan to optimize the datastructure for permutations so that those timings can change. 

I also took the chance to completely rewrite random_element which was incredibly slow. 

Considering your function as positively reviewed by me, can you please review mine ? 

Cheers,

Florent


---

Comment by hivert created at 2009-11-09 15:22:19

Changing assignee from mhansen to hivert.


---

Comment by ylchapuy created at 2009-11-09 22:41:50

Changing status from needs_review to positive_review.


---

Attachment

Nice work.

I added a tiny patch to correct two typos, otherwise it seems good to me.
Here is the positive review.

Cheers,
 Yann

(note: apply only the last two patches)


---

Comment by mhansen created at 2009-11-12 06:50:09

Resolution: fixed
