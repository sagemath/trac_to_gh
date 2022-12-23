# Issue 6027: get_memory_usage() sucks performance wise on OSX

Issue created by migration from https://trac.sagemath.org/ticket/6027

Original creator: mabshoff

Original creation time: 2009-05-12 07:13:49

Assignee: mabshoff

CC:  rdingman


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: timeit('get_memory_usage()')
5 loops, best of 3: 486 ms per loop
```

This causes sage/rings/tests.py to take forever in -long doctesting mode.
| Sage Version 3.4.2, Release Date: 2009-05-04                       |
| Type notebook() for the GUI, and license() for information.        |
See http://blog.kuriositaet.de/?p=257 for a more efficient way to get the current memory used.

Cheers,

Michael


---

Attachment

I've added a patch to get the memory usage of Sage on Darwin without spawning top and parsing the output. With this patch, get_memory_usage() will still report the same result that top reports for VSIZE (the link above doesn't do this).

Before patch:

sage: timeit('get_memory_usage()')
5 loops, best of 3: 156 ms per loop

After patch:

sage: timeit('get_memory_usage()')
125 loops, best of 3: 2.62 ms per loop

This has only been tested on OS X 10.5, Intel, 64-bit. It will likely work for PPC and 32-bit (still 10.5), but I'm not sure about 10.4 and earlier. I don't have access to hardware right now to test (and fix) this patch on all these other configurations. I'd be happy to finish up this patch if someone has machines to test on.


---

Comment by rdingman created at 2009-05-22 18:19:01

Also, for other platforms calling the underlying darwin_memory_usage() will just raise NotImplementeError. I also have not tested this patch on non-darwin to make sure the c code conditionally compiles correctly and that the behavior is reasonable.


---

Comment by mabshoff created at 2009-05-22 18:20:46

I have no doubt it will compile, so mark it for "needs review". Otherwise no one will look at this any time soon since those tickets tend to stay rotten in trac ;)

Once I have made it home I will look at this. I have some analog code for Solaris more or less ready to go and will extend this code as needed then.

Cheers,

Michael


---

Comment by was created at 2009-05-28 06:55:16

This isn't critical for 4.0.  This would be very nice to get into 4.0.1.


---

Comment by ncalexan created at 2009-06-15 19:17:27

Applies clean, tested fine on sage.math.  After patch on OS X 10.5:


```
sage: sage.misc.getusage.get_memory_usage()
141.22265625
sage: %timeit sage.misc.getusage.get_memory_usage()
100 loops, best of 3: 5.24 ms per loop
sage: sage.misc.darwin_utilities
sage.misc.darwin_utilities
sage: sage.misc.darwin_utilities.darwin_memory_usage()
148082688L
sage: %timeit sage.misc.darwin_utilities.darwin_memory_usage()
100 loops, best of 3: 5.22 ms per loop
```



---

Comment by rlm created at 2009-06-24 09:47:46

Resolution: fixed


---

Attachment

Positive review on William's additional patch, which is merged in sage-4.1.alpha1.


---

Comment by rdingman created at 2009-06-25 18:56:00

If someone has machines with OSX <= 10.4 that I can access I could port the code I wrote.
