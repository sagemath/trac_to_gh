# Issue 9862: Error in sage/graphs/genus.pyx on ia64-Linux-suse

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-09-06 21:48:26

Assignee: mvngu

CC:  jhpalmieri mderickx

Reported by John Palmieri on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/9cab8cb98f0d6d51#9cab8cb98f0d6d51):

```
On iras (ia64-Linux-suse), after continuing the build, one failure:

sage -t -long "devel/sage/sage/graphs/genus.pyx"
**********************************************************************
File "/home/palmieri/iras/sage-4.5.2.alpha0/devel/sage/sage/graphs/
genus.pyx", line 129:
    sage: get_memory_usage(t)
Expected:
    0.0
Got:
    -0.28125
```


Related: #9584, which once mentioned this problem, but ended up fixing another.


---

Comment by mpatel created at 2010-09-07 09:38:07

* What happens if you run the test manually, on the Sage command-line?
 {{{#!python
sage: import sage.graphs.genus
sage: G = graphs.CompleteGraph(100)
sage: G = Graph(G, implementation='c_graph', sparse=False)
sage: t = get_memory_usage()
sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend._cg)
sage: gb = None  #indirect doctest
sage: get_memory_usage(t)
0.0
}}}

 * Could this be a bug in `sage.misc.getusage.get_memory_usage`?

 * Should we really test for equality?


---

Comment by jhpalmieri created at 2010-09-07 15:32:41

> What happens if you run the test manually, on the Sage command-line?

Well, right now I can't even get it to fail when running 

```
sage -t -long "devel/sage/sage/graphs/genus.pyx"
```

by itself.  I can only get it to fail reliably if I use parallel testing, say

```
sage -tp 2 -long "devel/sage/sage/graphs/"
```

I tried running the testsuite from one window and "sage -t ... genus.pyx" in another, but that didn't fail, either.

> Could this be a bug in sage.misc.getusage.get_memory_usage?

Is it reasonable to get negative numbers for this?  

Should we change the test to

```
sage: get_memory_usage(t) <= 0
True
```

?


---

Comment by mpatel created at 2010-09-07 22:28:14

Changing priority from major to blocker.


---

Comment by mderickx created at 2010-09-08 10:28:41

I find the test code which causes al the discussion in this ticket broken. The code tries to test if the deallocation of simple_connected_genus_backtracker works so to prevent memory leaks. But when I test it in sage (on os x 10.6 since I don't have acces to a suse installation) I get the following result with measuring how many memory the backtracker actually takes:


```
sage: import sage.graphs.genus
sage: G = graphs.CompleteGraph(100)
sage: G = Graph(G, implementation='c_graph', sparse=False)
sage: t = get_memory_usage()
sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend._cg)
sage: get_memory_usage(t)
0.0
sage: gb = None  #indirect doctest
sage: get_memory_usage(t)
0.0
```

So the backtracker seems to take an unmeasurable amount of memory in the first place, deallocation working properly is therefore not tested at all. (at least not os os x 10.6, I would love to see this test replicated on the machine on which the paralel doctesting gives errors).


---

Comment by mderickx created at 2010-09-08 10:38:59

I know that python uses a garbage collector, I don't really know the detailed workings of the garbage collector, neither do I know all the internals of the implementation of the graphs code used here. But I do know that from first sight there might be a possibility that the garbage collector might collect some garbagage created by the second assignment to G in between the two "get_memory_usage" statements.

There is an easy way to rule out this possibilty by changing the test code to:

```
sage: import sage.graphs.genus
sage: G = graphs.CompleteGraph(100)
sage: H = Graph(G, implementation='c_graph', sparse=False)
sage: t = get_memory_usage()
sage: gb = sage.graphs.genus.simple_connected_genus_backtracker(H._backend._cg)
sage: gb = None  #indirect doctest
sage: get_memory_usage(t)
0.0
```

In this way, you don't overwrite the reference to graphs.CompleteGraph(100) so there is no possibility of accidental garbage collection.


---

Comment by mpatel created at 2010-09-08 11:08:21

What if we use the [gc module](http://docs.python.org/library/gc.html) to wrap some lines in a `gc.enable()` / `gc.disable()` block?  Or use `gc.collect`?  There's also `sage.interfaces.expect.gc_disabled()`, a `with` statement context manager.


---

Comment by mderickx created at 2010-09-08 12:17:46

I think a gc.collect would be a good thing to do right before both of the get_memory_usage statements. I think it's even better then my previous suggestion to just rename change the second asignment to G in H. The first collect would be to make sure the measurements don't get messed up by things that where collectable already at the first get_memory_usage() statement.

The second collect would be to make sure that objects not already freed by the reference counting, but could be garbage collected still get freed. This should be done since these objects also wouldn't account to a memory leak.
I suggest a code similar to the following.

```
sage: import sage.graphs.genus
sage: import gc
sage: G = graphs.CompleteGraph(100)
sage: G = Graph(G, implementation='c_graph', sparse=False)
sage: gc.collect()   #random
54
sage: t = get_memory_usage()
sage: for i in xrange(10000):
....:     gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend._cg)
....:     gb = None  #indirect doctest
....:     
sage: gc.collect()
0
sage: get_memory_usage(t)
0.0

```


ps. I added the for loop to make sure that if there really is a memory leak, it will be found. As shown in my first remark, the memory used by the tested class is insignificant.


---

Comment by mpatel created at 2010-09-08 13:50:54

I ran mderickx's "gc.collect" test 100 times in the Sage CLI on bsd, redhawk, sage, and t2.math.  I always got 0.0 on the first three.  On t2, I sometimes got -1.0 or -2.0.


---

Comment by mpatel created at 2010-09-08 23:57:21

Looking at how differently `sage.misc.getusage.get_memory_usage` works on different types of systems --- in particular, the precision varies --- I think we'll also need to weaken the test to `get_memory_usage(t) <= 0`, as John suggests.  I don't know if there's a good general answer.

Does the iras test, when it fails, always give `-0.28125`?


---

Comment by drkirkby created at 2010-09-09 01:06:20

Replying to [comment:8 mpatel]:
> I ran mderickx's "gc.collect" test 100 times in the Sage CLI on bsd, redhawk, sage, and t2.math.  I always got 0.0 on the first three.  On t2, I sometimes got -1.0 or -2.0.

`t2.math` will use `prstat` for this. Other systems use other methods, including system calls and using `top`, which is very similar to `prstat`.


---

Comment by jhpalmieri created at 2010-09-09 01:09:27

> Does the iras test, when it fails, always give -0.28125?

I just reran the test and got `-0.25`.


---

Comment by mderickx created at 2010-09-09 07:47:47

I also think that testing equality might by to strikt. While reading the source code I read how get_memory_usage() works. And on linux it works by asking top or prstat or the /proc filesystem how much memory the entire  python process is using in which sage is running. To fully understand the fluctuations in the memory usage, we would need to know all the details of the implementation of the CPython virtual machine which interprets the python bytecode. 
I suspect that the virtual machine is not asking memory from the os using malloc for every python object it creates, but instead it uses malloc to sometimes ask for a chuck of memory in which it can fiddle around and only asks for a new peace of memory after it filled the old one (all this for performance reasons). So deallocating memory would also proably go in the same chunks. The scenario described above, and maybe many other scenarios might cause that changes in how many memory is used by python objects might not be in a 1-1 correspodence with changes in the total memory used by the python process.

I'm curious if the observed change in memory usages really has something to do with genus backtracker code. To bad I don't have acces to a linux machine with a sage install, for then I could test certain things myself. I really wonder if the problem also occurs if you change the assignment:
gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend._cg)
to something else.


The observed difference in precision is probably because of the way that python prints floats.

```
sage: 2.132311r-2.132311r
0.0
```



---

Comment by mderickx created at 2010-09-09 08:15:01

If we really want to do this cleanly, then we should use something like guppy: http://guppy-pe.sourceforge.net/. This frees us from worying about all the things that happen outside the python objects.


---

Comment by drkirkby created at 2010-09-09 10:07:58

Replying to [comment:12 mderickx]:
> I also think that testing equality might by to strikt. While reading the source code I read how get_memory_usage() works. And on linux it works by asking top or prstat or the /proc filesystem how much memory the entire  python process is using in which sage is running. 

`prstat` is *never* used on Linux - only on Solaris. To my knowledge, prstat does not exist on anything other than Solaris. 

`top` used to be commonly used on SunOS then Solaris systems, though it was never part of the operating system. But it has become increasing less useful with modern systems, so on Solaris at least, it is considered unreliable. 

The bit of code in Sage which uses `prstat` is only run on Solaris (aka SunOS) is:

```
   elif U == 'sunos':
        # Sun's 'prstat' command appends K, M or G depending on whether 
        # the memory usage is in KB. MB or GB. So we need to strip off 
        # the letter, and convert to a consistent unit of MB. 
        memory_in_KB_MB_or_GB = top().split()[3]
        if memory_in_KB_MB_or_GB.endswith("K"): 
            m = float(memory_in_KB_MB_or_GB.strip("K")) / 1024
        elif memory_in_KB_MB_or_GB.endswith("M"):
            m = float(memory_in_KB_MB_or_GB.strip("M"))
        elif memory_in_KB_MB_or_GB.endswith("G"):
            m = float(memory_in_KB_MB_or_GB.strip("G")) * 1024
```


I wrote that bit, since `top` is not standard on Solaris, and even if installed, it is not very useful with modern Solaris versions. 

These small numbers however are not going to be coming from the output of the `top` command either. 

Dave


---

Comment by mpatel created at 2010-10-09 05:14:55

In view of #9897, I'm deferring [merging] this to after 4.6.


---

Comment by mpatel created at 2010-10-09 05:14:55

Changing priority from blocker to major.


---

Comment by mpatel created at 2010-10-09 05:17:29

But I take it that our current plan is to update the doctest as Maarten suggests and not to test for equality?


---

Comment by mpatel created at 2010-11-24 10:23:08

This tests a leaky Cython function:

```python
cython('from stdlib cimport *\ndef leak(m=100000):\n    cdef double *arr = <double *>malloc(m * sizeof(double))')

def g(n=100, m=100000):
    import gc
#    import sage.graphs.genus
#    G = graphs.CompleteGraph(100)
#    G = Graph(G, implementation='c_graph', sparse=False)
    gc.collect()
    t = get_memory_usage()
    for i in xrange(n):
        leak(m)
#        gb = sage.graphs.genus.simple_connected_genus_backtracker(G._backend._cg)
#        gb = None  #indirect doctest
    gc.collect()
    return get_memory_usage(t)
```

For large enough `n` and `m`, `g(n,m) > 0.0`, but the threshold values will vary from system to system (because of `get_memory_usage`'s implementation, etc.).


---

Comment by mpatel created at 2010-11-24 10:40:12

I've attached a trial, not much-tested patch that uses Maarten's suggestions.


---

Comment by mpatel created at 2010-11-24 10:46:10

Changing status from new to needs_review.


---

Attachment

Tweak flaky test with Maarten Derickx's suggestions


---

Comment by mpatel created at 2010-11-24 11:04:47

The patch causes no problems for me on {bsd,sage,t2}.math and iras.skynet.


---

Comment by jdemeyer created at 2010-12-05 15:08:27

Changing priority from major to blocker.


---

Comment by jdemeyer created at 2010-12-14 15:39:22

Patch looks good to me.


---

Comment by jdemeyer created at 2010-12-14 15:39:22

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-12-19 09:34:27

Resolution: fixed
