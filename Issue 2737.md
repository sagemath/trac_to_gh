# Issue 2737: add balanced_sum to Sage

Issue created by migration from https://trac.sagemath.org/ticket/2737

Original creator: mhansen

Original creation time: 2008-03-31 11:49:00

Assignee: somebody




---

Attachment


---

Comment by mhansen created at 2008-03-31 11:51:26

I've added my initial patch.  There is *major* code duplication through.


---

Comment by robertwb created at 2008-03-31 16:00:06

Can you post some timings? For most types summation won't be helped by balancing it (compared to say multiplication) because the basic algorithm is already linear. Unless there are non-trivial improvements, I don't think it's worth the code duplication.


---

Comment by mhansen created at 2008-03-31 16:03:46

I don't know of any good benchmarks (since I don't have any personal interest in this).  However, this is from Joel:


```

About a month ago, I mailed sage-devel with a related issue:

sage: N=1000
sage: R.<x,y>=QQ[]
sage: L2=[x^i for i in range(N)]
sage: sum(L2)
...

The above sum behaves quadratically since it appears that singular goes
through it's whole list of monomials when it adds a single monomial.  This
was much improved by a divide and conquer sum approach.  I didn't bother to
write the generic function though.

I'm just noting that if you've written the generic code, I think it should be
included because there are some types for which the small additions are
expensive.  Whether or not this should replace 'sum' in the sage global
namespace, I'm not so certain.
```



---

Comment by jason created at 2009-07-19 05:05:14

I fixed a bug, added some documentation, and rebased the patch to 4.1.  I think my changes are minor enough that I can still review the patch.  Positive review.

Mike is right, though.  There is some major code duplication that eventually should be factored out.


---

Comment by jason created at 2009-07-19 05:10:56

Some timing info for the tour, comparing balanced sum with the builtin sum.


```
sage: a=range(10e6)          
sage: %timeit sum(a)         
10 loops, best of 3: 2.58 s per loop
sage: %timeit balanced_sum(a)
10 loops, best of 3: 891 ms per loop
sage: balanced_sum(a)==sum(a)
True
```



---

Comment by jason created at 2009-07-19 06:21:13

A more drastic example:


```
sage: a=[[i] for i in range(10e4)]                    
sage: %time b=sum(a,[])                                       
CPU times: user 209.95 s, sys: 0.57 s, total: 210.51 s
Wall time: 245.69 s
sage: a==[[i] for i in range(10e4)]  
True
sage: b==range(10e4)                 
True
sage: %time c=balanced_sum(a, [])
CPU times: user 0.11 s, sys: 0.00 s, total: 0.11 s
Wall time: 0.12 s
sage: a==[[i] for i in range(10e4)]
True
sage: c==range(10e4)               
True
```


However, I also uncovered a bug because the function does not copy its arguments (it modified the lists it was using, giving an incorrect sum).  I'm posting a revised patch.  This revised patch should be reviewed.


---

Comment by jason created at 2009-07-19 06:27:14

Apply just the trac-2737-balancedsum-rebased-bug-fixed.patch patch.


---

Comment by jason created at 2009-07-19 06:48:35

apply instead of previous patch


---

Attachment

Positive review to the second patch. I don't see an easy way to get rid of code duplication, so I think this is worth it.


---

Comment by mvngu created at 2009-07-25 23:28:22

Merged `trac-2737-balancedsum-rebased-bug-fixed.patch`.


---

Comment by mvngu created at 2009-07-25 23:28:22

Resolution: fixed


---

Comment by mvngu created at 2009-08-20 05:18:49

Replying to [comment:6 jason]:
> Some timing info for the tour, comparing balanced sum with the builtin sum.
> 

```
sage: a=range(10e6)          
sage: %timeit sum(a)         
10 loops, best of 3: 2.58 s per loop
sage: %timeit balanced_sum(a)
10 loops, best of 3: 891 ms per loop
sage: balanced_sum(a)==sum(a)
True
```

This is what I get on sage.math:

```
sage: L = range(10e6)
sage: %time sum(L);
CPU times: user 0.51 s, sys: 0.00 s, total: 0.51 s
Wall time: 0.51 s
sage: %time balanced_sum(L);
CPU times: user 0.78 s, sys: 0.00 s, total: 0.78 s
Wall time: 0.79 s
sage: %timeit sum(L);
10 loops, best of 3: 504 ms per loop
sage: %timeit balanced_sum(L);
10 loops, best of 3: 753 ms per loop
```

Looks like `balanced_sum()` is worse off than the built-in `sum()` for this particular example.


---

Comment by jason created at 2009-08-20 06:47:19

So I guess my computer is slow.  The builtin sum is *fast*.  However, when it costs a fixed high cost to add two elements together (like the lists above), I think the balanced sum is a clear, clear winner.  The list example above should show great improvement, even on sage.math.
