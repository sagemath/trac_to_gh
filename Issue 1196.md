# Issue 1196: inefficiency and inconsistency in calculus numerical conversion

Issue created by migration from https://trac.sagemath.org/ticket/1196

Original creator: was

Original creation time: 2007-11-18 04:14:40

Assignee: was


```
> David Harvey did mention to
> me that getting a numerical approximation of sqrt(2) called maxima, so

That's not exactly true, since "Exiting Maxima..." is not printed out below:

sage: float(sqrt(2))
1.4142135623730951
sage: quit
Exiting SAGE (CPU time 0m0.01s, Wall time 0m5.91s).

What happens is that if one requests a numerical *float* approximation
to sqrt(2), then first a float approximation to 2 is computed, then
the math.sqrt method is called on it.  

Unfortunately, evidently right now if one requests a high-precision
numerical approximation Sage currently does
end up calling Maxima:


sage: RealField(100) ( sqrt(2) )
1.4142135623730950488016887242
sage: 
Exiting spawned Maxima process.

I consider this a mistake in implementation, which should be optimized. 

Notice that

sage: sqrt( RealField(100)(2) )
1.4142135623730950488016887242

does not call Maxima anywhere. 

I just investigated, and n(sqrt(2), 100) calls maxima only to simplify
sqrt(2) before even beginning to do any numerical approximation. 
This isn't consistent with how the other coercions (e.g., to float) work.   So I've posted
a patch that changes this behavior.  After applying this patch:

sage: RealField(100) ( sqrt(2) )
1.4142135623730950488016887242
sage: quit
(no "exiting maxima") 
```


NOTE: I've attached two patches.  The first implements the change described above.
The second fixes some resulting doctest failures, and also optimizes computation
of sec, csc, and cot for mpfr elements. 



---

Attachment

patch 1 of 2


---

Comment by was created at 2007-11-18 04:15:26

patch 2 of 2


---

Attachment


---

Comment by mabshoff created at 2007-11-20 15:50:45

Merged in 2.8.13.rc1.


---

Comment by mabshoff created at 2007-11-20 15:50:45

Resolution: fixed
