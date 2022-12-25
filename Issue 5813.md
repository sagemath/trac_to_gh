# Issue 5813: Update GSL to 1.112 (latest upstream)

archive/issues_005813.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n* What is new in gsl-1.12:\n\n** Upgraded to latest libtool, autoconf and automake (libtool-2.2.6,\n   autoconf-2.63, automake-1.10.2)\n\n** Improved the convergence of gsl_sf_gamma_inc_P for x/a ~=~ 1 and\n   large x,a.  Fixes problems with large arguments in cdf functions\n   such as gsl_cdf_chisq_Pinv(x,nu) [bug 24704].\n\n** Fixed gsl_ran_gamma_knuth to handle the case of a >= UINT_MAX [bug\n   #24897]\n\n** Added gsl_bspline_eval_deriv to compute bspline derivatives\n   (Rhys Ulerich)\n\n** Added a faster simplex mininimser gsl_multimin_fminimizer_nmsimplex2\n   which is O(N) instead of O(N^2) [bug #24418]\n\n** Improved the original chi-squared formula in gsl_monte_vegas to\n   avoid catastrophic cancellation [bug #24510].  The previous formula\n   could return incorrect or negative values for relative errors <\n   1e-8, which could occur when integrating very smooth functions.\n\n** Added new auxiliary functions gsl_cheb_order, gsl_cheb_size,\n   gsl_cheb_coeffs for Chebyshev series [bug #21830]\n\n** Updated license of the reference manual to GNU FDL version 1.3.\n\n** Fixed a bug where the gsl_isinf function would return +1 for -Inf\n   on systems where isinf(-Inf) returns the non-standard value +1.\n   [bug #24489]\n\n** Added missing functions gsl_vector_complex_{isnonneg,add,sub,mul,\n   div,scale,add_constant} and gsl_matrix_complex_float_isnonneg [bug\n   #22478]\n\n** Cross compilation should now work for x86 hosts.\n\n** Fixed a bug in gsl_interp_accel_find() where values lying on the\n   upper boundary between interpolation points could return the index\n   from the lower side. [bug #24211]\n\n** Fixed gsl_linalg_solve_cyc_tridiag so that its output respects the\n   solution vector's stride. Previously the x_stride value was ignored\n   causing the output to be incorrect for non-unit stride. [bug #24162]\n\n** Corrected a bug in the series calculation of gsl_sf_ellint_Kcomp\n   for k close to 1. [bug #24146]\n\n** Extended gsl_linalg_QRPT_update to handle rectangular matrices.\n   Corrected definition of the update formula in the manual for\n   both gsl_linalg_QR_update and gsl_linalg_QRPT_update.\n\n** Added routine gsl_linalg_cholesky_invert\n\n** Fixed a bug the simplex algorithm which caused the second highest\n   point to be incorrectly equal to the first when the first value was\n   the highest, which could cause suboptimal convergence. [bug #23192]\n\n** Fixed a problem with convergence for inverse gamma and chisq\n   distribitions, gsl_cdf_gamma_{P,Q}inv and gsl_cdf_chisq_{P,Q}inv.\n   [bug #23101]\n\n** Improved the handling of constant regions in Vegas by eliminating\n   spurious excess precision when computing box variances.\n\n** Fixed a potential division by zero in gsl_monte_miser when the\n   left/right weight factors decrease below 1.\n\n** Fixed incorrect dimensions check in gsl_matrix_sub{row,column}\n\n* What was new in gsl-1.11:\n\n** The GSL repository and bug database are now hosted at Savannah\n   http://savannah.gnu.org/projects/gsl/\n\n** Upgraded to latest libtool, autoconf and automake (libtool-2.2,\n   autoconf-2.61, automake-1.10.1)\n\n** Fixed underflow in ODE adaptive step size controller that could\n   cause step size to decrease to zero (bug #21933).\n\n** Improved the handling of the asymptotic regime in gsl_sf_bessel_jl.\n\n** Improved the handling of large arguments in cumulative distribution\n   functions using the incomplete beta function, such as gsl_cdf_fdist_P.\n\n** Fixed overflow bug in gsl_cdf_hypergeometric_{P,Q} for large\n   arguments (bug #22293).\n\n** gsl_ran_gaussian_ziggurat now handles generators with different\n   ranges explicitly, to minimise the number of function calls\n   required (bug #21820).  Also fixes bug #22446 (rng limit in\n   gsl_ran_chisq()).\n\n** Added missing error terms in gsl_sf_exp_mult_e10_e to prevent\n   the error being underestimated (bug #22041).  \n\n** Updated some constants to the CODATA 2006 values.\n\n** The hypergeometric function gsl_sf_hyperg_2F1 now handles the case\n   where x==1.\n\n** Fixed a bug in the brent minimiser which prevented optimal convergence.\n\n** Added functions for evaluating complex polynomials\n\n** The convergence condition for gsl_multiroots_test_delta now accepts\n   dxi == 0.\n\n** Improved functions gsl_ldexp and gsl_frexp to handle the full range\n   of double precision numbers in all cases.\n\n** Added new quasi random generators gsl_qrng_halton and\n   gsl_qrng_reversehalton which support dimensions up to 1229.\n\n** Added function gsl_multifit_linear_residuals for computing the\n   residuals of the fit\n```\n\n\nNote that Brian Gladman has a VS 2008 build project for GSL 1.12 at \n\n   http://gladman.plushost.co.uk/oldsite/computing/gnu_scientific_library.php\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5813\n\n",
    "created_at": "2009-04-17T19:50:29Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Update GSL to 1.112 (latest upstream)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5813",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
* What is new in gsl-1.12:

** Upgraded to latest libtool, autoconf and automake (libtool-2.2.6,
   autoconf-2.63, automake-1.10.2)

** Improved the convergence of gsl_sf_gamma_inc_P for x/a ~=~ 1 and
   large x,a.  Fixes problems with large arguments in cdf functions
   such as gsl_cdf_chisq_Pinv(x,nu) [bug 24704].

** Fixed gsl_ran_gamma_knuth to handle the case of a >= UINT_MAX [bug
   #24897]

** Added gsl_bspline_eval_deriv to compute bspline derivatives
   (Rhys Ulerich)

** Added a faster simplex mininimser gsl_multimin_fminimizer_nmsimplex2
   which is O(N) instead of O(N^2) [bug #24418]

** Improved the original chi-squared formula in gsl_monte_vegas to
   avoid catastrophic cancellation [bug #24510].  The previous formula
   could return incorrect or negative values for relative errors <
   1e-8, which could occur when integrating very smooth functions.

** Added new auxiliary functions gsl_cheb_order, gsl_cheb_size,
   gsl_cheb_coeffs for Chebyshev series [bug #21830]

** Updated license of the reference manual to GNU FDL version 1.3.

** Fixed a bug where the gsl_isinf function would return +1 for -Inf
   on systems where isinf(-Inf) returns the non-standard value +1.
   [bug #24489]

** Added missing functions gsl_vector_complex_{isnonneg,add,sub,mul,
   div,scale,add_constant} and gsl_matrix_complex_float_isnonneg [bug
   #22478]

** Cross compilation should now work for x86 hosts.

** Fixed a bug in gsl_interp_accel_find() where values lying on the
   upper boundary between interpolation points could return the index
   from the lower side. [bug #24211]

** Fixed gsl_linalg_solve_cyc_tridiag so that its output respects the
   solution vector's stride. Previously the x_stride value was ignored
   causing the output to be incorrect for non-unit stride. [bug #24162]

** Corrected a bug in the series calculation of gsl_sf_ellint_Kcomp
   for k close to 1. [bug #24146]

** Extended gsl_linalg_QRPT_update to handle rectangular matrices.
   Corrected definition of the update formula in the manual for
   both gsl_linalg_QR_update and gsl_linalg_QRPT_update.

** Added routine gsl_linalg_cholesky_invert

** Fixed a bug the simplex algorithm which caused the second highest
   point to be incorrectly equal to the first when the first value was
   the highest, which could cause suboptimal convergence. [bug #23192]

** Fixed a problem with convergence for inverse gamma and chisq
   distribitions, gsl_cdf_gamma_{P,Q}inv and gsl_cdf_chisq_{P,Q}inv.
   [bug #23101]

** Improved the handling of constant regions in Vegas by eliminating
   spurious excess precision when computing box variances.

** Fixed a potential division by zero in gsl_monte_miser when the
   left/right weight factors decrease below 1.

** Fixed incorrect dimensions check in gsl_matrix_sub{row,column}

* What was new in gsl-1.11:

** The GSL repository and bug database are now hosted at Savannah
   http://savannah.gnu.org/projects/gsl/

** Upgraded to latest libtool, autoconf and automake (libtool-2.2,
   autoconf-2.61, automake-1.10.1)

** Fixed underflow in ODE adaptive step size controller that could
   cause step size to decrease to zero (bug #21933).

** Improved the handling of the asymptotic regime in gsl_sf_bessel_jl.

** Improved the handling of large arguments in cumulative distribution
   functions using the incomplete beta function, such as gsl_cdf_fdist_P.

** Fixed overflow bug in gsl_cdf_hypergeometric_{P,Q} for large
   arguments (bug #22293).

** gsl_ran_gaussian_ziggurat now handles generators with different
   ranges explicitly, to minimise the number of function calls
   required (bug #21820).  Also fixes bug #22446 (rng limit in
   gsl_ran_chisq()).

** Added missing error terms in gsl_sf_exp_mult_e10_e to prevent
   the error being underestimated (bug #22041).  

** Updated some constants to the CODATA 2006 values.

** The hypergeometric function gsl_sf_hyperg_2F1 now handles the case
   where x==1.

** Fixed a bug in the brent minimiser which prevented optimal convergence.

** Added functions for evaluating complex polynomials

** The convergence condition for gsl_multiroots_test_delta now accepts
   dxi == 0.

** Improved functions gsl_ldexp and gsl_frexp to handle the full range
   of double precision numbers in all cases.

** Added new quasi random generators gsl_qrng_halton and
   gsl_qrng_reversehalton which support dimensions up to 1229.

** Added function gsl_multifit_linear_residuals for computing the
   residuals of the fit
```


Note that Brian Gladman has a VS 2008 build project for GSL 1.12 at 

   http://gladman.plushost.co.uk/oldsite/computing/gnu_scientific_library.php

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5813





---

archive/issue_events_006062.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2011-01-17T00:33:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5813",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5813#event-6062"
}
```



---

archive/issue_comments_045566.json:
```json
{
    "body": "We can close this as we're at 1.14 in Sage.",
    "created_at": "2011-01-17T00:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5813#issuecomment-45566",
    "user": "https://github.com/mwhansen"
}
```

We can close this as we're at 1.14 in Sage.



---

archive/issue_comments_045567.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2011-01-17T00:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5813#issuecomment-45567",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid
