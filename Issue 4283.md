# Issue 4283: [with proto-patch]A Speed-up Patch for NTL's ZZXFactoring.c

Issue created by migration from https://trac.sagemath.org/ticket/4283

Original creator: anovocin

Original creation time: 2008-10-14 14:26:40

Assignee: tbd

Keywords: NTL, LLL, Univariate

The goal of this patch is to speed-up NTL's factoring algorithm for polynomials in Z[X].  The speed-up comes from using fpLLL rather than NTL's native LLL algorithm.  We do this by converting a ZZ_mat of ZZ's (NTL's multi-precision integers) and passing them into a mat_ZZ<mpz_t> matrix of mpz_t's (fpLLL's native format).  Then run fpLLL on the new matrix and pass the entries back to NTL.  I don't replace NTL's LLL just pass what should be an already reduced basis to NTL's LLL.  (NTL computes extra information that would require a hack into fpLLL to get and might not be worth it.)  This patch allows NTL to beat MAGMA on many examples (it still is a little slower than MAGMA (but faster than SAGE) on irreducible polynomials).  I think that the cross over between Pari's factoring and NTL's factoring should be re-evaluated (currently Pari is used for polynomials of degree 30 through 300) if not just use NTL for all polynomials now.  


---

Comment by anovocin created at 2008-10-14 14:27:44

Changing status from new to assigned.


---

Comment by anovocin created at 2008-10-14 14:27:44

Changing assignee from tbd to anovocin.


---

Attachment
