# Issue 417: Faster GF(p^n) arithmetic for p^n >= 2^16

Issue created by migration from https://trac.sagemath.org/ticket/417

Original creator: malb

Original creation time: 2007-08-10 15:15:29

Assignee: somebody

CC:  ylchapuy mderickx

The Pari+Python interface is too slow. ntl.ZZ_pE+Cython should be much faster.


---

Comment by mabshoff created at 2007-10-27 20:14:17

Hmm, could this have been fixed by the NTL wrapper rewrite?

Cheers,

Michael


---

Comment by malb created at 2007-10-30 15:01:09

No, this was not fixed by the NTL wrapper rewrite. NTL still needs to be actually used internally by `FiniteField`. This ticket requires two new implementations. GF(p<sup>n</sup>) for p < (sizeof(long)<<3) and for p >= (sizeof(long)<<3). These are different classes in NTL and should both be wrapped.


---

Comment by johanbosman created at 2011-08-18 17:19:28

Replying to [ticket:417 malb]:
> The Pari+Python interface is too slow. ntl.ZZ_pE+Cython should be much faster.
I completely agree.  How much work has been done on this yet and how much work still needs to be done?


---

Comment by malb created at 2011-08-18 17:30:32

I don't think anybody worked on this much. GF(2<sup>e</sup>) was switched to NTL, but nothing else happened. 

However, the GF(2<sup>e</sup>) should be a reasonable starting point for doing other fields (word-sized primes and general primes). 

Also, we should eventually move sparse moduli interally but that's for another project :)
