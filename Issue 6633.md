# Issue 6633: optimize computation of matrices of Hecke operators on modular symbols spaces

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-07-26 22:48:38

Assignee: craigcitro

CC:  alexghitza

Compare the following, both on 64-bit OS X:

```
SAGE-4.1:

sage: S = ModularSymbols(225,2,sign=1).cuspidal_subspace()
sage: time z = [S.hecke_matrix(n) for n in [1..S.dimension()*2]]
CPU times: user 1.14 s, sys: 0.03 s, total: 1.17 s
Wall time: 1.18 s

and


Magma V2.15-11    Sun Jul 26 2009 15:46:04 on flat     [Seed = 672054977]
Type ? for help.  Type <Ctrl>-D to quit.
> M := CuspidalSubspace(ModularSymbols(225,2,1));
> time K := [HeckeOperator(M, n) : n in [1..Dimension(M)*2]];
Time: 0.070
> 
```


Magma is 16.7 times faster at computing those Hecke matrices. I think I seriously screwed up in deciding on an algorithm for computing Hecke matrices back in 2005 when I first implemented this stuff.  I need to basically just reimplement tightly in Cython code for doing this (most of the relevant corresponding magma code for this operation is in C, by the way).   In particular, I use matrix multiplication for reducing modular the relations, which is evidently very bad. 
