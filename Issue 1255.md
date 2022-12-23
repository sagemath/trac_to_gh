# Issue 1255: bug in permutation_automorphism_group

Issue created by migration from https://trac.sagemath.org/ticket/1255

Original creator: wdj

Original creation time: 2007-11-24 19:33:26

Assignee: wdj

I have found a code C which crashes C.permutation_automorphism_group().
This function basically is a wrapper for GAP's `MatrixAutomorphisms` 
function. The code that causes it to fail is [20,14] in
http://sage.math.washington.edu/home/wdj/research/coding-theory/sd_codes.sage


---

Comment by was created at 2007-11-25 18:48:18

Is this a bug in gap?  If so, make a Gap-only session that replicates it and report it to the Gap list asap.


---

Comment by was created at 2007-11-25 18:48:44

We are having trouble replicating this -- what hardware / os are you using?


---

Comment by rlm created at 2008-05-10 21:43:21

This definitely doesn't seem valid anymore:

```
sage: load /Users/rlmill/Desktop/sd_codes.sage
sage: time L = self_dual_codes(20)
CPU times: user 2.09 s, sys: 0.83 s, total: 2.92 s
Wall time: 3.10
sage: C = L[14][0]; C
Linear code of length 19, dimension 10 over Finite Field of size 2
sage: C.permutation_automorphism_group()
Permutation Group with generators [(10,19), (9,15)(16,17), (9,16)(15,17), (8,9)(17,18), (7,8)(16,17), (4,5)(13,14), (4,13)(5,14), (3,4)(12,14), (1,2)(5,13), (1,3)(2,12)]
```



---

Comment by rlm created at 2008-05-10 21:44:58

In fact, none of the codes from that function cause a "crash":

```
sage: for n in range(24):
....:     for C in self_dual_codes(n):
....:         G = C[0].permutation_automorphism_group()
....:         
sage: 
```



---

Comment by rlm created at 2008-05-11 02:08:14

David also says that he cannot reproduce the crash.


---

Comment by mabshoff created at 2008-08-31 04:25:18

Resolution: invalid


---

Comment by mabshoff created at 2008-08-31 04:25:18

Invalid.

Cheers,

Michael
