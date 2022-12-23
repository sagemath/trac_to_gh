# Issue 2847: [with patch, needs review] more speedups to cyclotomic polynomials

Issue created by migration from https://trac.sagemath.org/ticket/2847

Original creator: robertwb

Original creation time: 2008-04-07 19:32:03

Assignee: somebody

Use some data provided by Michael Monagan, as well as take advantage of the fact (mentioned in the previous ticket by John Cremona) that $\Phi_{pn}(x) = \Phi_n(x^p)$ for $p|n$.


---

Attachment


---

Comment by cremona created at 2008-04-07 19:49:00

Code looks fine to me.  I haven't checked it yet as my machine is tied up doing --testall on 3.0.alpha2.


---

Comment by mabshoff created at 2008-04-07 20:55:39

The patch currently does not apply against my tree:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha3/devel/sage$ patch -p1 < trac_2847-cyclo-limits.patch
patching file sage/rings/polynomial/cyclotomic.pyx
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha3/devel/sage$ patch -p1 < trac_2847-cyclo-radical.patch
patching file sage/rings/polynomial/cyclotomic.pyx
Hunk #1 FAILED at 72.
1 out of 3 hunks FAILED -- saving rejects to file sage/rings/polynomial/cyclotomic.pyx.rej
```

Feel free to rebase against /scratch/mabshoff/release-cycle/sage-3.0.alpha3/devel/sage

Cheers,

Michael


---

Attachment


---

Comment by robertwb created at 2008-04-09 03:41:43

It was just a conflict with a random doctest. I rebased it against 3.0.alpha3. Apply 2847-cyclo-limits.patch and 2847-cyclo-radical-rebased.patch.


---

Comment by mhansen created at 2008-04-09 03:56:57

Looks good to me.


---

Comment by mabshoff created at 2008-04-09 04:07:55

Merged 2847-cyclo-limits.patch and 2847-cyclo-radical-rebased.patch in Sage 3.0.alpha3


---

Comment by mabshoff created at 2008-04-09 04:07:55

Resolution: fixed


---

Comment by mabshoff created at 2008-04-09 04:25:26

Hmm, after merging those two patches I get a new doctest failure:

```
sage -t -long devel/sage/sage/rings/polynomial/polynomial_ring.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha3/tmp/polynomial_ring.py", line 582:
    sage: S.cyclotomic_polynomial(12)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[5]>", line 1, in <module>
        S.cyclotomic_polynomial(Integer(12))###line 582:
    sage: S.cyclotomic_polynomial(12)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 600, in cyclotomic_polynomial
        return self(cyclotomic.cyclotomic_coeffs(n), check=True)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 1058, in __call__
        return polynomial_modn_dense_ntl.Polynomial_dense_mod_p(self, x, check, is_gen,construct=construct)
      File "polynomial_modn_dense_ntl.pyx", line 101, in sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_n.__init__
        x = self._dict_to_list(x, R(0))
    TypeError: 'NoneType' object is not callable
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_18
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.alpha3/tmp/.doctest_polynomial_ring.py

         [3.3 s]

The following tests failed:

        sage -t -long devel/sage/sage/rings/polynomial/polynomial_ring.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 3.3 seconds
```

Thoughts?

Cheers,

Michael


---

Attachment

Looks like this exposed a bug in the (Z/nZ)[x] __init__ method, which I have fixed in the attached patch.


---

Comment by mabshoff created at 2008-04-09 05:04:26

Thanks Robert. 2847-Zn_x-fix.patch fixes the issue. Merged in Sage 3.0.alpha3
