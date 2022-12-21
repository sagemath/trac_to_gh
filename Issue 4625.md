# Issue 4625: improve pth power map for finite fields of characteristic p

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2008-11-26 15:58:21

Assignee: somebody

CC:  cremona

Keywords: field element, frobenius

The implementation of the pth_power method for FiniteFieldElement is naive; maybe it can be sped up.  cremona had the following suggestion in the discussion about ticket #4553:

```
Lastly, I think it would be more efficient to compute (and cache) the matrix of frobenius 
as a linear map, viewing F_q as an F_p-vector space of dimension d where q=p^d. I know 
an efficient way to do this (similar to tricks used in Berlekamp factorization). Then taking 
q'th roots would be easy (invert the matrix).
```


```
The linear algebra approach will have to wait until we have a common interface for all 
finite fields -- currently the functions available depend on q since they differ according 
to whether we use givaro or NTL or pari. (e.g. an element a in GF(q) sometimes has 
a._coordinates() but not always. So it's fine to go ahead with this one for now, perhaps 
with a note that a better implementation might be possible in future.
```



---

Comment by AlexGhitza created at 2010-01-01 23:15:18

Changing priority from minor to major.
