# Issue 8905: Memory leak in echelon over QQ

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2010-05-06 12:19:17

Assignee: tbd

CC:  mderickx

Keywords: memleak echelonize

Apparently there is a memory leak in Sage-4.4 when one echelonizes a matrix over ``QQ``:

```
sage: MS = MatrixSpace(QQ,8)
sage: M = MS.random_element()
sage: N = copy(M)
sage: N.echelonize()
sage: N==M
False
sage: mem = get_memory_usage()
sage: n = 0
sage: while(1):
....:     n+=1
....:     if get_memory_usage()>mem:
....:         mem = get_memory_usage()
....:         print mem,n
....:     N = copy(M)
....:     N.echelonize()
....:
797.95703125 1
798.0859375 32
798.21484375 71
798.34375 110
798.47265625 155
798.6015625 199
798.8515625 202
798.98046875 243
799.109375 292
799.23828125 329
799.37109375 371
799.5 406
799.79296875 426
799.921875 471
800.05078125 530
800.1796875 582
800.30859375 634
800.61328125 666
...
```


Here I show that the critical step really is the echelon form:

```
sage: MS = MatrixSpace(QQ,8)
sage: M = MS.random_element()
sage: N = copy(M)
sage: mem = get_memory_usage()
sage: n = 0
sage: while(1):
....:     n+=1
....:     if get_memory_usage()>mem:
....:         mem = get_memory_usage()
....:         print mem,n
....:     N = copy(M)
....:
797.92578125 1
```

The memory consumption is stable at that point. So, copying ``M`` is no problem, but computing the echelon form is!


---

Comment by SimonKing created at 2010-05-06 14:57:27

Similarly, one gets

```
sage: MS = MatrixSpace(QQ,8)
sage: M = MS.random_element()
sage: M = M.stack(M)
sage: v = copy(M).left_kernel()
sage: n = 0
sage: mem = get_memory_usage()
sage: while(1):
....:     n+=1
....:     if get_memory_usage()>mem:
....:         mem = get_memory_usage()
....:         print mem,n
....:     v = copy(M).left_kernel()
....:
800.3828125 27
800.51171875 62
800.640625 94
800.76953125 151
801.05078125 168
801.1796875 187
801.30859375 221
801.4375 256
801.56640625 278
801.71484375 314
802.08984375 375
802.21875 423
802.34765625 460
802.4765625 497
802.60546875 521
802.8984375 610
803.02734375 635
803.15625 690
```

I guess the two are related.


---

Comment by mderickx created at 2011-01-08 01:08:16

I guess #10262 might explain both of these leaks. I wouldn't find it strange that somewhere in both algorithms scalar*vector multiplication happens.


---

Comment by mmezzarobba created at 2015-04-11 17:37:27

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2015-04-11 17:37:27

Seems to be fixed indeed.


```
┌────────────────────────────────────────────────────────────────────┐
│ SageMath Version 6.6.rc2, Release Date: 2015-04-02                 │
[...]
sage: MS = MatrixSpace(QQ,8)
sage: M = MS.random_element()
sage: N = copy(M)
sage: N.echelonize()
sage: N==M
False
sage: mem = get_memory_usage()
sage: n = 0
sage: while(1):
....:     n+=1
....:     if get_memory_usage()>mem:
....:         mem = get_memory_usage()
....:         print mem,n
....:     N = copy(M)
....:     N.echelonize()
....:
1006.625 2302
1006.875 19154
1007.0078125 27590
1007.2578125 36321
```



---

Comment by SimonKing created at 2015-04-11 18:01:50

Marco, the numbers you are giving indicate that the memory leak is smaller than before. But why do you think it is fixed?


---

Comment by SimonKing created at 2015-04-11 18:01:50

Changing status from needs_review to needs_info.


---

Comment by mmezzarobba created at 2015-04-11 19:00:13

Changing status from needs_info to needs_work.


---

Comment by mmezzarobba created at 2015-04-11 19:00:13

Replying to [comment:10 SimonKing]:
> Marco, the numbers you are giving indicate that the memory leak is smaller than before. But why do you think it is fixed?

No, you are right, I misread the results. It looks like we are still leaking about 16 bytes per call.


---

Comment by nbruin created at 2015-04-11 19:48:44

Replying to [comment:11 mmezzarobba]:
> No, you are right, I misread the results. It looks like we are still leaking about 16 bytes per call.

I wouldn't be so quick to conclude linear behaviour from so few data points. I'm getting:

```
1130.9375 1
1131.1875 5107
1131.4375 22580
1131.6875 39743
```

and no further increase up to `n=738068` (after which I gave up). Echelonization over QQ likely leads to very complicated memory use (lots of allocation/deallocation), so together with non-deterministic gc (because parents only clear on triggered GC) you expect that the memory layout shows a lot of short-term fluctuations: fragmentation will lead to slowly increasing memory footprint; hopefully stabilizing over long periods. The numbers above are quite consistent with that. Certainly gc.objects() is not showing any significant object accumulation, so any leak would have to be outside python.

I see no indication of a memory leak here anymore, but I guess you could valgrind it to be certain.


---

Comment by mmezzarobba created at 2015-04-11 20:48:28

Yes, I came to the same conclusion after letting it run for a bit longer:

```
1005.9921875 376
1006.2421875 2015
1006.4921875 19150
1006.4921875 20000
1006.640625 30356
1006.890625 36624
1006.890625 40000
1006.890625 60000
1006.890625 80000
1007.140625 95959
1007.140625 100000
1007.140625 6000000
```



---

Comment by mmezzarobba created at 2015-04-13 12:09:55

Setting the ticket to duplicate/positive_review as we agree that the problem is fixed and there is no obvious regression test to add.


---

Comment by mmezzarobba created at 2015-04-13 12:09:55

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2015-04-13 17:45:39

Resolution: fixed
