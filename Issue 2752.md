# Issue 2752: Speedup for  all_paths()

Issue created by migration from Trac.

Original creator: vgermrk

Original creation time: 2008-04-01 13:42:54

Assignee: rlm

I speeded up the _all_paths()_ function for graphs.

The improvement is mainly based on 'getting rid of the recursion' :-)


On my machine (Pentium M) it's about 5 times faster, without more memory consumption.

-vgermrk-


---

Attachment


---

Comment by mabshoff created at 2008-04-01 14:11:16

This looks nice and despite vgermrk mentioning in IRC that the patch introduced more complicated code I think that it is fine [and not too complicated], especially since it removes paths_helper(). I am not sure if we really want to remove that code.

rlm: can you poke take a look? It would also be nice to see some figures of before and after with various graphs. Bonus points if someone  also measured memory consumption before and after.

Cheers,

Michael


---

Comment by rlm created at 2008-04-02 00:32:36

Changing priority from minor to major.


---

Comment by rlm created at 2008-04-02 00:32:36

The code looks good.  Very dense graphs on a small dumber of vertices see a major slowdown with this patch, although performance in the sparse case looks good.

Before:

```
  Order\Density0.0100000 0.0500000 0.1000000 0.2000000 0.3000000 0.5000000
     3         0.0000029 0.0000027 0.0000030 0.0000035 0.0000044 0.0000057
     4         0.0000024 0.0000027 0.0000030 0.0000041 0.0000063 0.0000121
     5         0.0000023 0.0000028 0.0000034 0.0000053 0.0000084 0.0000257
     6         0.0000024 0.0000031 0.0000036 0.0000073 0.0000134 0.0000551
     7         0.0000023 0.0000030 0.0000044 0.0000114 0.0000295 0.0001854
     8         0.0000023 0.0000033 0.0000056 0.0000151 0.0000718 0.0007517
     9         0.0000023 0.0000035 0.0000068 0.0000229 0.0001821 0.0026202
```


After:

```
  Order\Density0.0100000 0.0500000 0.1000000 0.2000000 0.3000000 0.5000000
     3         0.0000044 0.0000044 0.0000046 0.0000052 0.0000056 0.0000064
     4         0.0000041 0.0000044 0.0000048 0.0000057 0.0000070 0.0000100
     5         0.0000040 0.0000046 0.0000053 0.0000071 0.0000098 0.0000183
     6         0.0000040 0.0000047 0.0000056 0.0000100 0.0000136 0.0000386
     7         0.0000039 0.0000049 0.0000065 0.0000118 0.0000241 0.0001069
     8         0.0000040 0.0000048 0.0000073 0.0000173 0.0000491 0.0003567
     9         0.0000039 0.0000053 0.0000089 0.0000252 0.0001272 0.0014974
```


Timings for larger, sparser graphs might be on their way.


---

Comment by rlm created at 2008-04-02 00:33:24

Sorry, the comment about dense small graphs didn't get deleted before going to press - obviously not true :-)


---

Attachment


---

Comment by mabshoff created at 2008-04-02 01:36:19

Resolution: fixed


---

Comment by mabshoff created at 2008-04-02 01:36:19

Merged all_paths_speedup.patch in Sage 3.0.alpha0. All doctests pass with this patch applied.
