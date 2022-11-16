Sage is missing symbolic definitions for many special functions that we are capable of evaluating numerically. Some of these are even provided in symbolic form by Maxima.


## Tips for implementing new functions
 * Implementing a symbolic function involves subclassing `sage.symbolic.function.BuiltinFunction` and defining most or all of the following:
   * Custom evaluation (`_eval_`)
   * Numeric evaluation (`_evalf_`)
   * Differentiation (`_derivative_`)
   * Conjugate (`_conjugate_`)
   * Imaginary and real part methods (`_{imag,real}_part_`)  
 * Returning None in `_eval_` leaves the function symbolic with the given input.
 * See [sage.functions.other.Function_gamma_inc](http://git.sagemath.org/sage.git/tree/src/sage/functions/other.py#n856) or [sage.functions.trig.Function_cot](http://git.sagemath.org/sage.git/tree/src/sage/functions/trig.py#n330) for examples.
 * regarding the maxima(_lib) interfaces see also http://trac.sagemath.org/ticket/16671#comment:6
 * ticket [#17130](https://trac.sagemath.org/ticket/17130) added code that makes `_eval_` and `_evalf_` much simpler, see [#12455](https://trac.sagemath.org/ticket/12455) or [#17151](https://trac.sagemath.org/ticket/17151) for example


## Tickets related to improving an existing function or implementing a new one

 * [#6466](https://trac.sagemath.org/ticket/6466) Implement functional derivative and Euler-Lagrange equation
 * [#8383](https://trac.sagemath.org/ticket/8383) make symbolic versions of moebius, sigma and euler_phi
 * [#9874](https://trac.sagemath.org/ticket/9874) derivative of ceil and floor
 * [#9935](https://trac.sagemath.org/ticket/9935) Make a symbolic mod function
 * [#10050](https://trac.sagemath.org/ticket/10050) wrap the polylogarithm functions from pynac
 * [#10071](https://trac.sagemath.org/ticket/10071) make a few held functions able to evaluate
 * [#10636](https://trac.sagemath.org/ticket/10636) Make Bessel zeros available as symbolic entities
 * [#12074](https://trac.sagemath.org/ticket/12074) real nth root function
 * [#12179](https://trac.sagemath.org/ticket/12179) Binomial of integer (mod n) returns integer
 * [#13050](https://trac.sagemath.org/ticket/13050) allow different algorithms for evaluating erf
 * [#13869](https://trac.sagemath.org/ticket/13869) Gamma of complex numbers incorrectly simplifies to factorial
 * [#14897](https://trac.sagemath.org/ticket/14897) binomial(x, m) gives incorrect answer when m is float
 * [#15344](https://trac.sagemath.org/ticket/15344) asin(2.0) should not return NaN
 * [#15354](https://trac.sagemath.org/ticket/15354) Make elliptic_j function symbolic
 * [#15497](https://trac.sagemath.org/ticket/15497) Make lcm() symbolic
 * [#16202](https://trac.sagemath.org/ticket/16202) agm(x,y)
 * [#16670](https://trac.sagemath.org/ticket/16670) make all orthogonal polynomials symbolic
 * [#16816](https://trac.sagemath.org/ticket/16816) symbolic sums of roots
 * [#17722](https://trac.sagemath.org/ticket/17722) lower incomplete gamma as gamma(a,0,x)
 * [#17970](https://trac.sagemath.org/ticket/17970) implement Meijer G function
 * [#18141](https://trac.sagemath.org/ticket/18141) special values of transcendental functions
 * [#18956](https://trac.sagemath.org/ticket/18956) incomplete gamma identities
 * [#19032](https://trac.sagemath.org/ticket/19032) qgamma function
 * [#19461](https://trac.sagemath.org/ticket/19461) Pochhammer symbols
 * [#20615](https://trac.sagemath.org/ticket/20615) derivative of Bessel with respect to order
 * [#21215](https://trac.sagemath.org/ticket/21215) Periodic piecewise functions
 * [#21274](https://trac.sagemath.org/ticket/21274) frac(x) immediate simplifications
 * [#21560](https://trac.sagemath.org/ticket/21560) return Infinity from factorial of negative integer
 * [#21639](https://trac.sagemath.org/ticket/21639) Implement derivative of gegenbauer(n,a,x) wrt to a
 * [#21655](https://trac.sagemath.org/ticket/21655) Return (d/dn)f with f(n,x).diff(n) instead of runtime error
 * [#21945](https://trac.sagemath.org/ticket/21945) Symbolic min/max
 * [#22028](https://trac.sagemath.org/ticket/22028) Symbolic catalan number
 * [#22146](https://trac.sagemath.org/ticket/22146) Symbolic eta function
 * [#22399](https://trac.sagemath.org/ticket/22399) piecewise and hypergeometric functions fail their TestSuite: _test_category, _test_pickling
 * [#22569](https://trac.sagemath.org/ticket/22569) Symbolic fibonacci
 * [#22651](https://trac.sagemath.org/ticket/22651) symbolic AppellF1
 * [#22713](https://trac.sagemath.org/ticket/22713) multiple zeta
 * [#22873](https://trac.sagemath.org/ticket/22873) No evaluation with gamma of ball arguments
 * [#24171](https://trac.sagemath.org/ticket/24171) Formal set membership function
 * [#24176](https://trac.sagemath.org/ticket/24176) Implement formal Set comprehension
 * [#24365](https://trac.sagemath.org/ticket/24365) Nonnumeric integer expressions not handled by floor/ceil
 * [#24554](https://trac.sagemath.org/ticket/24554) Refactoring in Chebyshev functions
 * [#24603](https://trac.sagemath.org/ticket/24603) chebyshev_T/U fail with float/complex argument
 * [#24604](https://trac.sagemath.org/ticket/24604) No evaluation with some functions
 * [#24861](https://trac.sagemath.org/ticket/24861) Formal diff (Option to hold for derivative)


## other symbolic function tickets
 * [#12449](https://trac.sagemath.org/ticket/12449) - symbolic functions on basic types improvements
 * [#14270](https://trac.sagemath.org/ticket/14270) - remove deprecated function-call syntax
 * [#14608](https://trac.sagemath.org/ticket/14608) - Symbolic functions break the __hash__ contract
 * [#15021](https://trac.sagemath.org/ticket/15021) - Return unevaluated derivative from BuiltinFunction
 * [#15025](https://trac.sagemath.org/ticket/15025) - automatically injected function does not work with desolve
 * [#15200](https://trac.sagemath.org/ticket/15200) - _evalf_ handling of backends
 * [#17547](https://trac.sagemath.org/ticket/17547) - BuiltinFunction overriding GiNaC function is allowed
 * [#17701](https://trac.sagemath.org/ticket/17701) - SR(f) or diff(f,t) should work even with NewSymbolicFunction
 * [#18259](https://trac.sagemath.org/ticket/18259) - comparison of symbolic functions
 * [#20812](https://trac.sagemath.org/ticket/20812) - derivative of integer wrt to variable in polynomial ring should belong to that ring, not symbolic ring
 * [#24398](https://trac.sagemath.org/ticket/24398) - Document function initialization parameters
 * [#24832](https://trac.sagemath.org/ticket/24832) - Extend function domain with some symbolic function calls


## Tickets of this type closed

 * [#24212](https://trac.sagemath.org/ticket/24212) Fresnel integrals
 * [#24411](https://trac.sagemath.org/ticket/24411) Move gamma functions into their own file
 * [#17790](https://trac.sagemath.org/ticket/17790) BuiltinFunction doesn't pass non-SR-coercible arguments to function code
 * [#22024](https://trac.sagemath.org/ticket/22024) symbolic placeholder for complex root
 * [#22079](https://trac.sagemath.org/ticket/22079) Infinite loop in ceil() function
 * [#23224](https://trac.sagemath.org/ticket/23224) wrong symbolic comparison of log
 * [#18386](https://trac.sagemath.org/ticket/18386) polylog quirks
 * [#20191](https://trac.sagemath.org/ticket/20191) implement ExprCondPair equivalent
 * [#19906](https://trac.sagemath.org/ticket/19906) dilog(RR) should return an element of RR
 * [#11349](https://trac.sagemath.org/ticket/11349) Implement Inverse Erf function
 * [#17505](https://trac.sagemath.org/ticket/17505) symbolic product
 * [#21819](https://trac.sagemath.org/ticket/21819) Rewrite error functions and documentation
 * [#22209](https://trac.sagemath.org/ticket/22209) Differentiation of conj/imag/real/abs functions
 * [#22844](https://trac.sagemath.org/ticket/22844) symbolic limit
 * [#10070](https://trac.sagemath.org/ticket/10070) make heaviside and step play nicely together.
 * [#19439](https://trac.sagemath.org/ticket/19439) Different infinities returned by zeta/polylog
 * [#21657](https://trac.sagemath.org/ticket/21657) Import abs in functions/all.py
 * [#20939](https://trac.sagemath.org/ticket/20939) Remove pexpect-Maxima usage in Y(m,n)
 * [#21906](https://trac.sagemath.org/ticket/21906) Bug in bessel_K
 * [#22004](https://trac.sagemath.org/ticket/22004) Allow algorithm='sympy' in symbolic_sum function
 * [#16813](https://trac.sagemath.org/ticket/16813) Legendre functions/polynomials
 * [#21365](https://trac.sagemath.org/ticket/21365) cot(float) returns complex
 * [#21614](https://trac.sagemath.org/ticket/21614) Make atan2(0,0) return NaN
 * [#21645](https://trac.sagemath.org/ticket/21645) Full symbolic sum function
 * [#16671](https://trac.sagemath.org/ticket/16671) implement harmonic number function H_n
 * [#17678](https://trac.sagemath.org/ticket/17678) special values of Bessel functions
 * [#20139](https://trac.sagemath.org/ticket/20139) implement trigonometric symmetry simplifications
 * [#18832](https://trac.sagemath.org/ticket/18832) - non-numeric non-symbolic BuiltinFunction arguments?
 * [#16587](https://trac.sagemath.org/ticket/16587) - f(expr).n() fails for all generalized functions
 * [#12521](https://trac.sagemath.org/ticket/12521) evaluate log gamma for complex input
 * [#14896](https://trac.sagemath.org/ticket/14896) Symbolic hypergeometric confluent
 * [#15024](https://trac.sagemath.org/ticket/15024) More Hankel functions available
 * [#16697](https://trac.sagemath.org/ticket/16697) implement symbolic lower incomplete gamma function
 * [#15046](https://trac.sagemath.org/ticket/15046) Symbolic elliptic integrals
 * [#17770](https://trac.sagemath.org/ticket/17770) Euler numbers revamp
 * [#19464](https://trac.sagemath.org/ticket/19464) floor/ceil don't accept hold
 * [#20297](https://trac.sagemath.org/ticket/20297) ECL crash with Hermite polynomials
 * [#20428](https://trac.sagemath.org/ticket/20428) crash with ultraspherical polynomials
 * [#20098](https://trac.sagemath.org/ticket/20098) Re/Im(tanh) wrong formula
 * [#16221](https://trac.sagemath.org/ticket/16221) add Struve functions
 * [#19834](https://trac.sagemath.org/ticket/19834) implement symbolic Stieltjes constants
 * [#19836](https://trac.sagemath.org/ticket/19836) expansion of zeta using stieltjes-constants
 * [#19425](https://trac.sagemath.org/ticket/19425) - Order function in symbolic ring: error calling operator
 * [#17447](https://trac.sagemath.org/ticket/17447) Clarify and complete documentation of function()
 * [#19336](https://trac.sagemath.org/ticket/19336) bug in lambert_w._print_latex_()
 * [#12588](https://trac.sagemath.org/ticket/12588) abs(pi*I) should return pi
 * [#18954](https://trac.sagemath.org/ticket/18954) special values of trig. functions with arguments (m/n)*pi
 * [#17151](https://trac.sagemath.org/ticket/17151) symbolic Laguerre / associated Laguerre polynomials
 * [#17953](https://trac.sagemath.org/ticket/17953) symbolic function args prevent forced conversion of result to numeric
 * [#18091](https://trac.sagemath.org/ticket/18091) symbolic floor,ceil,factorial need _evalf_ too
 * [#10074](https://trac.sagemath.org/ticket/10074) Improve less-used hyperbolic functions
 * [#12455](https://trac.sagemath.org/ticket/12455) Make Airy functions symbolic
 * [#15017](https://trac.sagemath.org/ticket/15017) Symbolic spherical harmonic
 * [#2516](https://trac.sagemath.org/ticket/2516) hypergeometric function
 * [#12596](https://trac.sagemath.org/ticket/12596) improve incomplete elliptic integrals docs
 * [#9130](https://trac.sagemath.org/ticket/9130) Access to beta function
 * [#3401](https://trac.sagemath.org/ticket/3401) extend li to work with complex arguments
 * [#7357](https://trac.sagemath.org/ticket/7357) add non offset logarithm
 * [#8983](https://trac.sagemath.org/ticket/8983) erf(0) should return 0
 * [#4498](https://trac.sagemath.org/ticket/4498) symbolic arg function 
 * [#11143](https://trac.sagemath.org/ticket/11143) exponential integral
 * [#10075](https://trac.sagemath.org/ticket/10075) Make log gamma symbolic
 * [#11155](https://trac.sagemath.org/ticket/11155) abs(pi+I) = pi+I (new `_eval_` method for `abs()`)
 * [#11423](https://trac.sagemath.org/ticket/11423) Make atan2(0,0) consistent
 * [#14996](https://trac.sagemath.org/ticket/14996) Lots more elliptic functions
 * [#1173](https://trac.sagemath.org/ticket/1173) implement numerical evaluation of erf at complex arguments
 * [#3426](https://trac.sagemath.org/ticket/3426) bessel_K function is broken
 * [#4102](https://trac.sagemath.org/ticket/4102) make bessel_J symbolic
 * [#4230](https://trac.sagemath.org/ticket/4230) implement arbitrary precision Bessel Y 
 * [#9424](https://trac.sagemath.org/ticket/9424) make symbolic summation numerically evaluable
 * [#20312](https://trac.sagemath.org/ticket/20312) - parent of argument lost with GinacFunctions

== Tickets to make == 

 * implement `parabolic_cylinder_d` 
 * add maxima conversion for `elliptic_kc` ([#15046](https://trac.sagemath.org/ticket/15046))
 * Associated Legendre functions


## Special functions defined in Maxima
Notes from Benjamin Jones ([#11143](https://trac.sagemath.org/ticket/11143))
(http://maxima.sourceforge.net/docs/manual/en/maxima_16.html#SEC56)

```
hankel_1 (v,z)                 Hankel function of the 1st kind
hankel_2 (v,z)                 Hankel function of the 2nd kind
struve_h (v,z)                 Struve H function
struve_l (v,z)                 Struve L function
```

 * Notes: None of these functions are currently exposed at the top level in Sage. Evaluation is possible using mpmath.  [#15024](https://trac.sagemath.org/ticket/15024) adds Hankel.  [#16221](https://trac.sagemath.org/ticket/16221) is for Struve.

```
assoc_legendre_p[v,u] (z)      Associated Legendre function of degree v and order u 
assoc_legendre_q[v,u] (z)      Associated Legendre function, 2nd kind
```

 * These are not Maxima's `legendre_p(n,x)` and `legendre_q(n,x)` functions, which correspond to `legendre_P(n,x)` and `legendre_Q(n,x)` in Sage.

```
%f[p,q] ([], [], expr)         Generalized Hypergeometric function
hypergeometric(l1, l2, z)      Hypergeometric function
slommel
%m[u,k] (z)                    Whittaker function, 1st kind
%w[u,k] (z)                    Whittaker function, 2nd kind
```

 * Notes: `hypergeometric(l1, l2, z)` needs a conversion to Sage's `hypergeometric_U` (see [#2516](https://trac.sagemath.org/ticket/2516)). The others can be evaluated using mpmath. `slommel` is presumably mpmath's `lommels1()` or `lommels2()` (or both?). This isn't well documented in Maxima.

```
expintegral_e (v,z)            Exponential integral E
expintegral_e1 (z)             Exponential integral E1
expintegral_ei (z)             Exponential integral Ei
expintegral_li (z)             Logarithmic integral Li
expintegral_si (z)             Exponential integral Si
expintegral_ci (z)             Exponential integral Ci
expintegral_shi (z)            Exponential integral Shi
expintegral_chi (z)            Exponential integral Chi
erfc (z)                       Complement of the erf function
```

 * Notes: This was done in [#11143](https://trac.sagemath.org/ticket/11143)!

```
kelliptic (z)                  Complete elliptic integral of the first 
                               kind (K)
parabolic_cylinder_d (v,z)     Parabolic cylinder D function
```

 * Notes: `kelliptic(z)` needs a conversion to `elliptic_kc` in Sage (done in [#15046](https://trac.sagemath.org/ticket/15046))
and `parabolic_cylinder_d (v,z)` does not seem to be exposed at top level. It can be evaluated by mpmath.

```
inverse_jacobi_cd
inverse_jacobi_cn
inverse_jacobi_cs
inverse_jacobi_dc
inverse_jacobi_dn
inverse_jacobi_ds
inverse_jacobi_nc
inverse_jacobi_nd
inverse_jacobi_ns
inverse_jacobi_sc
inverse_jacobi_sd
inverse_jacobi_sn
jacobi_cd
jacobi_cn
jacobi_cs
jacobi_dc
jacobi_dn
jacobi_ds
jacobi_nc
jacobi_nd
jacobi_ns
jacobi_sc
jacobi_sd
jacobi_sn
```
 * It turns out there are a slew of elliptic functions that we only have thinly wrapped and could make better - see [this Maxima page](http://maxima.sourceforge.net/docs/manual/en/maxima_16.html).  Basically, all of these are in Sage, but could be made more native. This was done in [#14996](https://trac.sagemath.org/ticket/14996).

```
dgauss_a
dgauss_b
dkummer_m
dkummer_u
gauss_a
gauss_b
kummer_m
kummer_u 
```
 * These are some specific functions defined in Maxima's `contrib_ode` package, some of which we may have.  Some hypergeometric function returned by certain ODE solvers in Maxima and which mpmath can evaluate are out there too (maybe same ones?). See [#2516](https://trac.sagemath.org/ticket/2516), for instance.