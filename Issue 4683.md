# Issue 4683: memory leak when performing the calculation CDF(I)^2

Issue created by migration from https://trac.sagemath.org/ticket/4683

Original creator: ggrafendorfer

Original creation time: 2008-12-03 01:12:51

Assignee: somebody

Using sage 3.2 (compiled from sources) on a 32-bit Core Duo machine running Debian Etch,
when performing

```
georg@HILBERT:~/Daten/Sync/Phd/Code/sde$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2, Release Date: 2008-11-20                         |
| Type notebook() for the GUI, and license() for information.        |
sage: v = [CDF(i)^2 for n in range(50000)]
sage: v = [CDF(i)^2 for n in range(50000)]
sage: v = [CDF(i)^2 for n in range(50000)]
```

memory consumption increases about 70Mb which each command (at least on my machine),
this does not happen if one writes

```
sage: v = [CDF(i^2.) for n in range(50000)]
```

, however, results are the same,

Georg



---

Comment by mabshoff created at 2008-12-03 01:15:28

Hi Georg,

this looks like a dupe of #4639.

Cheers,

Michael


---

Comment by ggrafendorfer created at 2008-12-03 01:49:41

A yes, probably, I'm sorry, did not look ...
Georg


---

Comment by mabshoff created at 2008-12-17 04:00:57

#4639 fixes the vast majority of the problem here, but:

```
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
421.88671875
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
422.140625
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
422.15234375
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
422.40625
```

So still some small leak to go. I will poke around post 3.2.2.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-06-03 07:50:15

Hmmm:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
134.1328125
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
136.578125
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
136.7734375
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
136.7734375
sage: get_memory_usage()
136.7734375
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
136.7734375
```



---

Comment by wjp created at 2010-01-17 23:19:09

I don't see any growth in memory usage anymore either. I guess we can safely close it.


---

Comment by wjp created at 2010-01-17 23:19:09

Resolution: fixed
