# Issue 5345: Optimize transpose for dense matrices

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-02-23 02:02:11

Assignee: rbeezer

Keywords: transpose

This patch has two changes to the transpose method in matrix_dense.pyx to provide about a 15% speedup.  If this is accepted, I'll look into the other non-sparse routines for transpose and antitranspose.

1.  A double loop indexes into the list of matrix entries using multiplication to create a reordered list for the transpose.  The effect of the multiplications is replaced by repeated additions.

2.  Retrieving the list in the original matrix makes a copy with list().  This has been replaced by the internal _list() to just reference the original.

Passes  sage -t  for  matrix2.pyx  and  matrix_dense.pyx

```
m = identity_matrix(5000)
time m.transpose()
```

Timings (user + system):

11.94s : Stock 3.3

11.20s : No multiplication

10.18s : No multiplication, with _list()



---

Attachment


---

Comment by mabshoff created at 2009-02-23 07:32:16

Changing priority from trivial to major.


---

Comment by mabshoff created at 2009-02-23 07:32:16

A 18% speed improvement is never "trivial" for something like a basic operation like this :)

Cheers,

Michael


---

Comment by ylchapuy created at 2009-02-23 20:07:39

I think we can obtain a much bigger speedup if we replace the inner loop:

```
...
    for i in xrange(nr):
        f.append(e[i*nc+j])
...
```

with

```
...
    f.extend(e[j::nc])
...
```


and we should do just the same thing for antitranspose a few lines further


---

Comment by rbeezer created at 2009-02-24 05:30:52

Yann - I like it.  And yes, the antitranspose definitely needs a similar treatment.

I swapped out the inner loop for the suggested slicing.  Same test run as listed above, and I got a total time of 10.14s.  So not a major speedup, but still a gain.

I'll get back to this in the next couple of days and maybe try to do some more timings with multiple runs with the cache'ing of the list turned off.


---

Comment by ylchapuy created at 2009-02-24 18:38:50

This transpose function has another problem, it copies the entries multiple times which is very bad for memory usage. For example I can't transpose a 5000x5000 matrix on my laptop.
I suggest something like this (but maybe I'm missing something here?)

```
        (nc, nr) = (self.ncols(), self.nrows())
        trans = self.new_matrix(nrows = nc, ncols = nr,
                                copy=False,
                                coerce=False)
        for j in xrange(nc):
            for i in xrange(nr):
                trans[j,i]=self[i,j]

        if self.subdivisions is not None:
            row_divs, col_divs = self.get_subdivisions()
            trans.subdivide(col_divs, row_divs)
        return trans
```

(sorry, no time to do a proper patch right now)

PS: I also think that there should be an optimized version af transpose in matrix_integer_dense.pyx, but it's probably for another ticket.


---

Attachment


---

Comment by ylchapuy created at 2009-02-24 21:27:59

I had no time to do it, but of course I did it... Patch added implementing the idea above, plus unsafe access. It's a standalone patch (no need to apply yours) based on sage-3.3.

sage -testall successful.

And some statistics:

```
Before:

sage: m=identity_matrix(3000)
sage: time m2=m.transpose(); m3=m.antitranspose()
CPU times: user 14.13 s, sys: 1.11 s, total: 15.44 s
Wall time: 15.44 s
sage: get_memory_usage()
1254.28125

After:

sage: m=identity_matrix(3000)
sage: time m2=m.transpose(); m3=m.antitranspose()
CPU times: user 2.92 s, sys: 0.46 s, total: 3.38 s
Wall time: 3.38 s
sage: get_memory_usage()
835.6171875
```


I hope it's not too rude to make a patch for your ticket...

Cheers,
      Yann


---

Comment by rbeezer created at 2009-02-25 05:07:58

Yann,

No problem with working up a patch.  I'm learning my way around Sage, and I've got plenty else to keep me busy.

Yes, I think the original worked with four copies of the matrix entries, so this version will just access the original and make the new transposed version, cutting out two copies.

For the record:  5000 x 5000 identity matrix as above, on same hardware.  Your changes result in 2.46s total time for me, so I'm seeing almost a 5x speedup.

I can't find a transpose() in matrix_integer_dense.pyx.  But if there's more like this to be done, would you like to do it on a new ticket (and cc me)?  I didn't see any other matrix classes that might benefit from this sort of speedup - most seemed cython-ized already, both dense and sparse.

I'm going to give this a positive review for the logic, but I don't feel qualified to comment on the cython-ization, since I'm not at all familiar with that, and I'm not sure about policy for the "unsafe" methods.  So I'll change the summary to needing a second look.

Rob


---

Comment by ylchapuy created at 2009-02-25 10:09:52

(if someone is interested, a patch for matrix_integer_dense is proposed in #5369)


---

Comment by mhansen created at 2009-02-25 18:24:12

Looks good.  Apply only trac-5345-transpose-matrix-dense.patch


---

Comment by mabshoff created at 2009-02-28 21:03:31

Resolution: fixed


---

Comment by mabshoff created at 2009-02-28 21:03:31

Merged trac-5345-transpose-matrix-dense.patch in Sage 3.4.rc0.

Cheers,

Michael


---

Comment by mvngu created at 2009-03-01 05:26:57

Replying to [comment:6 ylchapuy]:
> And some statistics:
> {{{
> Before:
> 
> sage: m=identity_matrix(3000)
> sage: time m2=m.transpose(); m3=m.antitranspose()
> CPU times: user 14.13 s, sys: 1.11 s, total: 15.44 s
> Wall time: 15.44 s
> sage: get_memory_usage()
> 1254.28125
> 
> After:
> 
> sage: m=identity_matrix(3000)
> sage: time m2=m.transpose(); m3=m.antitranspose()
> CPU times: user 2.92 s, sys: 0.46 s, total: 3.38 s
> Wall time: 3.38 s
> sage: get_memory_usage()
> 835.6171875
> }}}
Is it possible for you to provide some information on the computer/system architecture that you used to get the above statistics? The improved performance is great news and I'll include this in the release tour at
[http://wiki.sagemath.org/sage-3.4](http://wiki.sagemath.org/sage-3.4)
And it would also be good to have some info about the hardware under which you arrived at the above statistics.


---

Comment by ylchapuy created at 2009-03-01 09:51:39

Replying to [comment:11 mvngu]:
> Replying to [comment:6 ylchapuy]:
> > And some statistics:
> > {{{
> > Before:
> > 
> > sage: m=identity_matrix(3000)
> > sage: time m2=m.transpose(); m3=m.antitranspose()
> > CPU times: user 14.13 s, sys: 1.11 s, total: 15.44 s
> > Wall time: 15.44 s
> > sage: get_memory_usage()
> > 1254.28125
> > 
> > After:
> > 
> > sage: m=identity_matrix(3000)
> > sage: time m2=m.transpose(); m3=m.antitranspose()
> > CPU times: user 2.92 s, sys: 0.46 s, total: 3.38 s
> > Wall time: 3.38 s
> > sage: get_memory_usage()
> > 835.6171875
> > }}}
> Is it possible for you to provide some information on the computer/system architecture that you used to get the above statistics? The improved performance is great news and I'll include this in the release tour at
> [http://wiki.sagemath.org/sage-3.4](http://wiki.sagemath.org/sage-3.4)
> And it would also be good to have some info about the hardware under which you arrived at the above statistics.

It was on my laptop:

```
Intel(R) Core(TM)2 Duo CPU     T5450  `@` 1.66GHz
MemTotal:      2066004 kB
Linux my-laptop 2.6.24-23-generic #1 SMP Thu Feb 5 15:00:25 UTC 2009 i686 GNU/Linux
```



---

Comment by rbeezer created at 2009-03-01 19:10:57

Replying to [comment:11 mvngu]:
> Is it possible for you to provide some information on the computer/system architecture that you used to get the above statistics? The improved performance is great news and I'll include this in the release tour at
> [http://wiki.sagemath.org/sage-3.4](http://wiki.sagemath.org/sage-3.4)
> And it would also be good to have some info about the hardware under which you arrived at the above statistics.

Minh,

Timings for size 5000 identity matrix (at very top, then buried in the middle of comment 7 are on stock KUbuntu 8.10 with 3 GHz dual-core processor (Intel(R) Core(TM)2 Duo CPU  E8500 `@` 3.16GHz) with 8 GB memory.

Rob


---

Comment by mvngu created at 2009-03-02 01:11:27

Thanks to Rob and Yann for the architecture info. For future reference, any optimization is very welcome. But for people who don't live on trac, a summary including timing and memory statistics as well as system architectures can be very useful. Of course any developer who has an account on sage.math can get the timing and memory statistics. But sage.math is not a regular PC or laptop; it's a powerful multi-core (over 20 cores, I think) machine with over *100* GB of RAM.


---

Comment by mabshoff created at 2009-03-02 01:23:30

Replying to [comment:14 mvngu]:

Hi Minh,

> Thanks to Rob and Yann for the architecture info. For future reference, any optimization is very welcome. But for people who don't live on trac, a summary including timing and memory statistics as well as system architectures can be very useful. Of course any developer who has an account on sage.math can get the timing and memory statistics. But sage.math is not a regular PC or laptop; it's a powerful multi-core (over 20 cores, I think) machine with over *100* GB of RAM.

The relative improvement will be identical, i.e. the fact that there are many core and a lot of RAM does have zero impact on CPU bound improvements like this. Indeed, due to the nature of the CPU and memory topology sage.math might actually see less of an improvement in certain cases.

Cheers,

Michael


---

Comment by ylchapuy created at 2009-03-04 19:16:30

Replying to [comment:11 mvngu]:
> The improved performance is great news and I'll include this in the release tour at
> [http://wiki.sagemath.org/sage-3.4](http://wiki.sagemath.org/sage-3.4)
> And it would also be good to have some info about the hardware under which you arrived at the above statistics.

As you can see 15.44s --> 3.38s on my machine, or 11.94s --> 2.46s on Rob's one represent more than a 15% improved performance :). You should change the release tour accordingly.


---

Comment by mvngu created at 2009-03-05 03:32:38

Replying to [comment:16 ylchapuy]:
> As you can see 15.44s --> 3.38s on my machine, or 11.94s --> 2.46s on 
> Rob's one represent more than a 15% improved performance :). You should
> change the release tour accordingly.
This might be a stupid question: For the record, can you please provide a mathematical formula for calculating the percentage improvement in time/memory? For example, if p1 is the previous performance time and p2 is the new and improved performance time, how do I calculate the percentage improvement? This assumes that both p1 and p2 are both expressed in the same unit of measurement, e.g. seconds.


---

Comment by rbeezer created at 2009-03-05 05:41:57

Replying to [comment:17 mvngu]:
> This might be a stupid question: For the record, can you please provide a mathematical formula for calculating the percentage improvement in time/memory? For example, if p1 is the previous performance time and p2 is the new and improved performance time, how do I calculate the percentage improvement? This assumes that both p1 and p2 are both expressed in the same unit of measurement, e.g. seconds.

Minh,

For small changes, I'd quote (p1-p2)/p1 as a percentage.  So 10 seconds down to 8 seconds would be a 20% improvement.  When that percentage gets close to 100%, (like over 50%, 60%, 70%) I'd switch to a factor as a "speedup" given by p1/p2.  From 10 seconds down to 1 seconds would be an 90% improvement, but I'd quote a 10x (10 times) factor.  So for the release tour, I'd just quote a 5x or a "factor of 5" improvement for these results.  The really curious can come see the exact numbers for themselves.  Hope this helps.

Rob


---

Comment by mvngu created at 2009-03-05 06:15:50

Replying to [comment:18 rbeezer]:
> For small changes, I'd quote (p1-p2)/p1 as a percentage.  So 10 seconds down to
> 8 seconds would be a 20% improvement.  When that percentage gets close to 100%,
> (like over 50%, 60%, 70%) I'd switch to a factor as a "speedup" given by p1/p2. 
> From 10 seconds down to 1 seconds would be an 90% improvement, but I'd quote a 
> 10x (10 times) factor.  So for the release tour, I'd just quote a 5x or a "factor
> of 5" improvement for these results.  The really curious can come see the exact
> numbers for themselves.  Hope this helps.
Thanks, Rob. That certainly helps.
