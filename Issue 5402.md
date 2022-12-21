# Issue 5402: Sparse determinants are slow

Issue created by migration from Trac.

Original creator: jbandlow

Original creation time: 2009-02-28 20:16:47

Assignee: was

CC:  jbandlow

Keywords: determinant

The following timings should be able to be improved.

```
       sage: dd = {(0,0):1}
       sage: %timeit matrix(8,dd).det()
       10 loops, best of 3: 213 ms per loop
       sage: %timeit matrix(8,dd,sparse = False).det()
       100 loops, best of 3: 629 µs per loop
```

William suggested:
Likely the fix will be to implement
a 1-line function that is just

```
  return self.dense_matrix().det(*args, **kwds)
```

until there is somebody who wants to implement a sparse algorithm.


---

Comment by mhansen created at 2009-02-28 20:34:35

I would tend to avoid converting to a dense matrix by default since one often uses sparse matrices because they don't have enough memory to store the dense ones.


---

Comment by jbandlow created at 2009-02-28 22:49:10

Sure, but as of right now, I've been waiting over fifteen minutes for 

```
       sage: dd = {(0,0):1}
       sage: %time matrix(100,dd).det()
```

whereas

```
       sage: %time matrix(100,dd,sparse=False).det()
       CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s
       Wall time: 0.08 s
```


So, currently, for a matrix large enough to have memory issues, determinants are already completely infeasible.  So I don't think anything would be lost by the one-line change proposed by William.  Of course, writing a sparse algorithm that is competitive speed-wise, or could be used only for very large matrices, would be ideal.  But it took me some time today to figure out why computing ~1000 determinants of 8x8 sparse matrices was taking so long, and if there could be a quick fix to spare others from my pain, it would be nice. :)


---

Comment by mabshoff created at 2009-03-02 06:26:13

Yep, I agree with Jason's position.

We are doing the same for some other LA bits where the sparse methods takes longer *and* uses more memory than the dense method for many cases.

Cheers,

Michael


---

Comment by Bouillaguet created at 2013-01-03 14:41:00

Changing status from new to needs_review.


---

Comment by Bouillaguet created at 2013-01-03 14:41:00

Apparently, this issue has been fixed. The determinant that used to take 15 minutes now takes 0.05s...


---

Comment by kcrisman created at 2013-01-03 15:16:38

I wouldn't say that it's fixed.  Note the comparison is better but still they are not that close.

```
sage: dd = {(0,0):1}
sage: %timeit matrix(8,dd).det()
5 loops, best of 3: 2.83 ms per loop
sage: %timeit matrix(8,dd,sparse = False).det()
625 loops, best of 3: 147 µs per loop
sage: %timeit matrix(100,dd).det()
5 loops, best of 3: 228 ms per loop
sage: %timeit matrix(100,dd,sparse = False).det()
25 loops, best of 3: 15.2 ms per loop
```

It's just that everything is faster now.  How much faster would Moore's law say these should be after four years?


---

Comment by kcrisman created at 2013-01-03 15:16:38

Changing status from needs_review to needs_work.


---

Comment by Bouillaguet created at 2013-01-04 10:42:30

Replying to [comment:5 kcrisman]:
> {{{
> sage: %timeit matrix(100,dd).det()
> 5 loops, best of 3: 228 ms per loop
> sage: %timeit matrix(100,dd,sparse = False).det()
> 25 loops, best of 3: 15.2 ms per loop
> }}}
> It's just that everything is faster now.  How much faster would Moore's law say these should be after four years?

In comment 2, someone complains about this test running for 15 minutes. On your machine, it runs in 228ms (sparse case). This is about 4000x times faster. Moore's law tell you that the number of transistor on a chip doubles every 18 months, so that in 4 years we would have at the very maximum a 10x speedup.

So, there was clearly some improvement. 

However, if you look into it a bit deeper, then you'll see that in the sparse case, computing the determinant triggers the computation of the charpoly(), and the computation of the charpoly creates a dense version of the matrix, then runs the dense charpoly algorithm. I thus agree that this is suboptimal (in particular because linbox has fancy iterative methods for this kind of computation on sparse matrices).

Anyway, why don't we : a) close this ticket, considering that it is outdated and that the situation has changed, and b) open a "feature request" ticket related to sparse matrices over exact rings? I would be happy to look into this.


---

Comment by Bouillaguet created at 2013-01-04 10:42:30

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2013-01-04 14:53:55

> > It's just that everything is faster now.  How much faster would Moore's law say these should be after four years?
> 
> In comment 2, someone complains about this test running for 15 minutes. On your machine, it runs in 228ms (sparse case). This is about 4000x times faster. Moore's law tell you that the number of transistor on a chip doubles every 18 months, so that in 4 years we would have at the very maximum a 10x speedup.
Interestingly, other than that one, the rest indeed show a 4-10x speedup.

> However, if you look into it a bit deeper, then you'll see that in the sparse case, computing the determinant triggers the computation of the charpoly(), and the computation of the charpoly creates a dense version of the matrix, then runs the dense charpoly algorithm. I thus agree that this is suboptimal (in particular because linbox has fancy iterative methods for this kind of computation on sparse matrices).
> 
> Anyway, why don't we : a) close this ticket, considering that it is outdated and that the situation has changed, and b) open a "feature request" ticket related to sparse matrices over exact rings? I would be happy to look into this.
Well, given that we _already_ create the dense matrix, then William's fix seems like it would speed things up at least a little, or be no worse?  I don't see why we (by which I mean you and other people who compute such determinants!) couldn't try it out, _as well as_ of course creating a new ticket to use fancy methods.  Seem reasonable?


---

Comment by Bouillaguet created at 2013-01-04 15:09:19

Fair enough. I'll post a patch this week-end.


---

Comment by Bouillaguet created at 2013-01-04 15:09:19

Changing status from needs_review to needs_work.


---

Comment by Bouillaguet created at 2013-01-04 17:26:04

Changing status from needs_work to needs_review.


---

Attachment

With patch applied:

```
sage: dd = {(0,0):1}
sage: %timeit matrix(100,dd).det()
125 loops, best of 3: 7.04 ms per loop
sage: %timeit matrix(100,dd,sparse = False).det()
25 loops, best of 3: 16.3 ms per loop
```


So that now the sparse case is faster! I really don't understand why tough, because it converts the matrix to a dense representation before computing the (dense) det...


---

Comment by kcrisman created at 2013-01-04 17:50:15

I get the same thing.  With a heavy load on the same computer (accounting for non-sparse slowdown),

```
sage: dd = {(0,0):1}
sage: %timeit matrix(8,dd).det()
5 loops, best of 3: 207 µs per loop
sage: %timeit matrix(8,dd,sparse = False).det()
625 loops, best of 3: 240 µs per loop
sage: %timeit matrix(100,dd).det()
25 loops, best of 3: 11.2 ms per loop
sage: %timeit matrix(100,dd,sparse = False).det()
25 loops, best of 3: 23.3 ms per loop
```

Maybe the way we make dictionary-defined matrices dense with `sparse=False` is suboptimal?

I like the patch, though it would be nice if you could find someone who has worked with caching before just to check that that code is correct - I haven't really used it in the past and don't have time to find similar examples in the code now, my apologies.


---

Comment by Bouillaguet created at 2013-01-04 17:57:41

There is an example of caching (the one I just mimicked...) in matrix_sparse.pyx in the definition of charpoly().

I checked that caching works by computing a large sparse determinant twice : the first call takes a few seconds, while the second call returns instantly.

For the sake of easy reviewing :-) here is the code of charpoly() :


```python
def charpoly(self, var='x', **kwds):
        f = self.fetch('charpoly')
        if f is not None:
            return f.change_variable_name(var)
        f = self.dense_matrix().charpoly(var=var, **kwds)
        self.cache('charpoly', f)
        return f
```



---

Comment by kcrisman created at 2013-01-04 18:09:32

Well, there you have it.  And the way to test it worked was perfect.

Okay, open that other ticket, and then you have yourself a positive review.  Still unclear as to why it's _faster_ than the dense case...


---

Comment by Bouillaguet created at 2013-01-06 09:08:58

http://trac.sagemath.org/sage_trac/ticket/13915 is opened


---

Comment by kcrisman created at 2013-01-07 14:02:47

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-01-09 09:00:11

Resolution: fixed
