This page gives an overview of open symbolics issues.  If you notice a symbolics or calculus issue that is not listed on this page, feel free to add it to the relevant section below.

## Other Symbolic pages
* [Symbolic functions](symbolics-functions)
* [wiki page](http://wiki.sagemath.org/symbolics) to coordinate work on new symbolics functionality.
* [symbolics/maxima](symbolics-maxima) dependencies on maxima
* [symbolics/nonzero](symbolics-nonzero) solving the zero comparison problem
* [Pynac](http://pynac.org) bugs are tracked in [the github issue tracker](https://github.com/pynac/pynac/issues).
* [symbolics/switch_todo](http://wiki.sagemath.org/symbolics/switch_todo) old TODO list for symbolics backend switch to pynac

## Wikipedia links and some papers
* [https://en.wikipedia.org/wiki/Symbolic_computation](https://en.wikipedia.org/wiki/Symbolic_computation)
* [https://en.wikipedia.org/wiki/Expression_(mathematics)](https://en.wikipedia.org/wiki/Expression_(mathematics))
* [https://en.wikipedia.org/wiki/Richardson%27s_theorem](https://en.wikipedia.org/wiki/Richardson%27s_theorem)
* [https://en.wikipedia.org/wiki/Unification_(computer_science)](https://en.wikipedia.org/wiki/Unification_(computer_science))
* [Watt, Making computer algebra more symbolic](https://scholar.google.de/scholar?cluster=16052742886444301118&hl=en&as_sdt=2005&sciodt=0,5)
* [Watt, What happened to languages for symbolic mathematical computation](https://scholar.google.de/scholar?cluster=13863445001122388860&hl=en&as_sdt=2005&sciodt=0,5)

## Links for these tickets
* [calculus or symbolics tickets tagged `needs_review`](https://trac.sagemath.org/query?status=needs_review&group=type&component=calculus&component=symbolics&order=priority&col=id&col=summary&col=priority&col=reviewer&col=author&col=dependencies&row=description)
* [calculus or symbolics tickets tagged `needs_{work,info}`](https://trac.sagemath.org/query?status=needs_info&status=needs_work&group=type&component=calculus&component=symbolics&order=priority&col=id&col=summary&col=priority&col=author&col=dependencies&row=description)
* [calculus or symbolics tickets still tagged `new`](https://trac.sagemath.org/query?status=new&component=calculus&component=symbolics&group=type&col=id&col=summary&col=priority&col=author&col=reviewer&col=dependencies&order=priority)

## Solve tickets
* Unsolved or wrongly solved expressions by type:
  * univar. polynomial: #11941, #18900, #10311, #20436
  * polynomial in sin(x),cos(x): #3745
  * polynomial equation system: #6231, #15499, #9625
  * poly fraction system: #15859
  * polynomial plus sqrt: #14215
  * poly fraction with trig. functions: #14628, #14736, #14738, #16593
  * linear system with complicated coefficients: #21873
  * exponential equation/system: #18006, #8862, #20068
  * mixed system: #16753, #22149
  * using conjugate: #18488
  * polynomial inequality: #14229
* Spurious/missed solutions
  * #2617 -  solve() can return undefined points as "solutions"
  * #11941 - Solve and assumptions too aggressive with cube root of negative numbers
  * #18902 - spurious results as inequality solution
  * #20755 - Bug in solve due to a bug in symbolic_expression_from_maxima_string
  * #21939 - Solving with respect to a dummy variable behaves wrong
  * #24939 - solve should not convert floating point to rationals when solving
* Enhancements
  * #1291  - recurrence solving
  * #5201  - matrices as input
  * #15859 - allow to_poly_solve force on multiple equations
  * #19000 - add an SMT-solver layer
* Change defaults/interface
  * #5679 - solve should convert additional args to SR
  * #6231 - what to do with systems and multiplicities
  * #10213 - default `solution_dict`
  * #10750 - additional args are not handled uniformly
  * #14736 - trig case where to_poly_solve True works, but not force
  * #22018 - Some debug(?) message when solving an inequality
  * #23136 - Allow giac algorithm in solve
  * #23992 - solve() doesn't solve some system solvable by (standalone) Maxima's solve()
  * #24102 - solve(....solution_dict=True) produces nonsense
  * #24142 - Improve interface to SymPy solvers
  * #24477 - solve(x, [x], solution_dict=True) error

## Integration tickets
* Bug, solved upstream
  * #17469
* Bug, not fixed yet upstream (indefinite/symbolic int)
  * #15504 - log(1+x)/x
  * #15747 - bus or segmentation fault in integral computation
  * #17469 - an integral that keeps haunting
  * #18822 - sqrt * sqrt
  * #21057 - Assumption ignored in indefinite integral computation
  * #22138 - Wrong Maxima integral result for even exponents
  * #24008 - exp(acos)
  * #24117 - `integrate(sqrt(1-4*sin(x)^2),x)` is wrong
  * #24316 - sqrt(sin,cos...)
  * #25636 - ECL crash: x^m/sqrt(a + b*x^(2 - m))
  * `abs_integrate`-related errors (see #12731 for possibly disabling or raising warning always with it)
    * #13097 - integral of ln(1+4/5*sin(x))
    * #11590 - `sgn()` function (not reported upstream?)
    * #14591 - cosh integral incorrect because of abs_integrate
    * #17183 - another abs_integrate error
    * #17468 - log(abs(sin())) problem
    * #17511 - abs(sin(x)) and abs(cos(x)) are flat-out wrong
    * #17910 - unsolved piecewise integrals metaticket
    * #23271 - abs(sin(x)*cos(x))
* definite integrals
  * #11164 - sin(x)/x
  * #11493 - two different results with same numeric integral
  * #11655 - Maxima missing rectform simplification after integral()
  * #12145
  * #13718
  * #14213
  * #14274 - GSL fail on simpler divergent integrals
  * #14764 - Let Mathematica free integration work with definite integrals
  * #14976 - integration with non symbolic bounds broken
  * #15219 - numerical integral of `f(x) = x` fails
  * #15496 - Incorrect result for divergent integral
  * #16788 - segfault in numerical_integral()
  * #16905 - really long intervals for integration
  * #17606 - Calculation involving nintegral works with Sage 6.3 but not with Sage 6.4
  * #18059 - runaway 'unable to simplify to float approximation'
  * #18599 - sqrt(cot<sup>2</sup>)
  * #18821 - sqrt(cos)*sin
  * #20467 - stackoverflow in sin(k*x)/x*erf(x<sup>2</sup>)
  * #21440 - cos(2*pi*x)
  * #22567 - GSL: Unevaluated integrals to infinity have nonsense numeric value
  * #22671 - ((1+x)<sup>(1/5)</sup>/(1-x)).integrate(x,2.,3.)
  * #22676 - Different results from definite integral methods
  * #24008 - exponential integral of arccos
  * #24587 - integral(sqrt(1-cos(x)), x, 0, 2*pi)
* Changing interface
  * #2787  - change to `integrate(f,(x,a,b))`
  * #7763  - unify interface for numerical integration
  * #8321  - numerical integration with arbitrary precision
  * #21667 - Redundant integrate() & integral() in functional.py and integral.py
  * #21905 - Better error message from integrate
* floats in integrals: #12152, #14821
* Other
  * #3732  - Unnecessary interaction
  * #13511, #17608 - principal values
  * #17109 - Wrong indefinite integral of some odd functions between opposite endpoints
  * #17249 - redundant assumption question
  * #22410 - Implement Rubi integrator
  * #22650 - implement integrals resulting in 2F1 and AppellF1 expressions

## simplify/expand tickets
* #10038 - wrap Maxima's demoivre and exponentialize into some simplify*
* #10073 - held variables aren't restored
* #10137 - rewrite function for symbolic expressions
* #10268 - add Ginac method to `simplify_rational`
* #10552 - more elementwise simplifications for symbolic matrices
* #13099 - Add a loop argument to simplify_full
* #14608 - Symbolic functions break the `__hash__` contract
* #17065 - use Maxima's trigrat() in symbolic simplify
* #17066 - simplify hypergeometric() when it's a polynomial
* #17737 - wrap Maxima's factorial/gamma conversions/expansions
* #18697 - evalf as soon as a FP number and no symbols are present
* #19995 - full_simplify involving square root without success
* #20520 - apply Maxima's simpsum in sum() and simplify*()
* #21307 - Maxima crash: `TypeError` when simplifying factorial ratio
* #21335 - Extend normalize() and use it instead of Maxima in simplify_rational()
* #21574 - simplify_log() does not
* #22027 - Simplifying 0<sup>x</sup> gives 0, with no assumptions on x
* #22467, #22495 - simplify_hypergeometric bug
* #22607 - Add reduce_trig() to applied "full simplify" methods
* #22621 - Improve sqrt products simplification
* #22699 - simplify arccos+arcsin when appropriate
* #23738 - simplify_full() fails to simplify a log expression
* #24231 - Maxima's demoivre() doesn't work with hyperbolic functions

## desolve tickets
* #8616 - get desolve to automatically deduce variables
* #9825 - Maxima temporary variables from diffeq confuse Sage
* #11482 - power series solutions
* #11653 - ODE whose solution implies integration limits
* #14092 - Error with supposedly normal DE problem
* #14877 - number of initial conditions in desolve_system
* #16653 - immediately get all integral/ODE solutions instead of asking for assumption
* #16793 - assumption is not used
* #17739 - enhance desolve output from separable ODEs
* #20068 - Another diffeq question
* #21789 - possible bug in boundary condition handling in Sage (not Maxima)
* #22849 - Heaviside in numerical resolutions

## limit and summation tickets
* #13269 - indeterminate limit result
* #14677 - Limit computation causes Sage to crash
* #15395 - Wrong limit for sequence
* #16422 - cancellation of two indefinite limits
* #17428 - wrong limit in derivative
* #17553 - substitute_function() can leave limits unevaluated
* #17709 - Maxima limit() regression
* #17878 - Wrong answer for a simple limit
* #17892 - Sage cannot work with Maxima's symbolic limit
* #19203 - hold for limit
* #20452 - spurious limit computation
* #22700 - add sympy limit examples
* #26060 - another wrong Maxima limit that is correct in Sympy

## series() and taylor()
* #6119  - deprecate taylor() in favor of series()
* #9555  - Series expansions at singularities don't work
* #12589 - series yields wrong result
* #15830 - extracting coefficient x-1 out of symbolic series wrong
* #15854 - series of x<sup>s</sup>, when s is symbolic
* #17400 - simplify_full returns odd result from symbolic series input
* #18500 - coercion of Laurent series to SR
* #19149 - Sister Celine's method for hypergeometric series
* #19997 - advanced symbolic series of Order any expression
* #19998 - missing operator in symbolic series
* #20090 - implement asec/acsc series at infinity
* #20846 - Maxima does not handle symbolic series
* #21899 - Incorrect Series Expansions of zeta(s) around 1
* #22201 - Further series speed improvements

## limitations of Piecewise functions
* #11225 - improve plotting
* #8994 - convolution support
* See also [the Maxima pw.mac package](http://sourceforge.net/projects/piecewisefunc/)

## conversion to/from other rings
* numpy objects: #8824
* vector: #16761, vector-valued functions: #11180, #11807, #12302, #11507
* #12745 - Coercion problem with Algebraic Real Field
* #14277 - Equality of symbolic expressions inside matrix
* #14504 - finite field coercion fails for extended fields
* #14602 - Symbolic expression to number fields
* #17782 - implement expression.polynomial(...,sparse=True)
* #17825 - wrong/weird conversion from SR to `InfinityRing`
* #18500 - coercion of Laurent series to SR
* #19231 - SR should not coerce into QQbar
* #20454 - conversion from SR[] to SR
* #20812 - derivative of integer wrt to variable in polynomial ring should belong to that ring, not symbolic ring

## fast_float deprecation
* #5572 - fast_callable improvements (including deprecating fast_float)
* #13559 - fast_float yields infinity when Python does, but should handle bigger numbers
* #16899 - Allow complex functions in implicit_plot
* #24536 - find_local_maximum/minimum() fails with expressions containing complex numbers

## performance
* #12786 - solve_mod is horribly slow for linear systems

## expression tree and substitutions
* #6480 - .subs_expr() method doesn't work for argument of D derivative operator
* #9329  - improve documentation of how to access parts of the expression tree
* #10169 - Operands and Operator of symbolic expressions
* #12577 - make _convert() public
* #14270 - Remove function call syntax for symbolic expressions
* #15733 - substitution in symbolic function fails with latex_name
* #17504 - solve() breaks substitute_function()
* #17757 - substitute_function with var argument
* #18396 - Handle substitutions of partial sums and products
* #21071 - substitution in denominator is skipped
* #21754 - Held symbolic powers cannot be approximated numerically
* #21758 - Hold symbolic powers unevaluated if evaluation fails
* #22102 - Substitutions inside piecewise functions don't work
* #22401 - Let substitute_function handle anon functions explicitly
* #22926 - Symbolic has_operator()
* #23304 - hold=True does not always prevent evaluation
* #23964 - f.subs(I==...) does not work
* #24255 - Warn with substitution of derived classes using equality
* #24283 - Implement Expression.has_function(...)
* #24428 - Substitution should be the same as numerical evaluation
* #30378 - `(x^2).subs({x: sqrt(x)})` returns `sqrt(x)` instead of `x`

## relation/equality, unknown results, tristate logic
* #7660  - arithmetic with equations and inequalities confusing
* #12554 - Adding a "swap" method to equation objects
* #17700 - wrong symbolic results in case the answer is not known
* #11613 - `RealInterval` expression comparisons broken
* #18259 - comparison of symbolic functions
* #19040 - defuse bool(x!=0) performance bomb
* #19162 - symbolic relations metaticket
* #20127 - test_relation: uncaught `NoConvergence`
* #20784 - not all symbolic equations stay unevaluated
* #21070 - comparison with wildcard raises error
* #21862 - Symbolic methods work inconsistently on relational expressions
* #24658 - Don't call Maxima with no-variable symbolic relation tests

## variable domains and assumptions
* #3277  - context for calculus assumptions
* #6862  - Mixing of different domains for symbolic variables
* #11941 - Solve and assumptions too aggressive with cube root of negative numbers
* #18745 - implement forgetting of assumptions on specific expressions
* #18999 - basic assumptions on symbolic functions
* #19670 - Consistency and redundancy of verbal assumptions
* #20132 - add symbolic domains posint, crational
* #21981 - Assuming a variable is prime
* #22022 - floor of real x should be known to be at most x
* #22025 - minus of real x should be known to be at most abs(x)
* #22162 - Return Unknown from ex.is_xyz() if Pynac returns false
* #24351 - Even assumption / variable domain / query
* #24352 - Implement Expression.is_nonzero(); apply to ex.__nonzero__()
* #24368 - Rational assumption / variable domain / query
* #24392 - strange handling of variables in assume
* #28538 - Segfault for boolean evaluation of expression with assumptions
* #29938 - comparison with infinity does not take assumptions into account

## specific Pynac/GiNaC issues
* #6756  - Implement `diff` format symbolic derivative in new symbolics
* #10069 - Typesetting with hold=True can be weird
* #10268 - add Ginac method to `simplify_rational`
* #11428 - customizable latex for GiNaC functions
* #11576 - generate sequences of variables
* #12589 - series yields wrong result
* #18630 - Expression.is_positive/negative incomplete
* #18697 - any FP number in an Expression without symbol should trigger evaluation
* #20824 - Expression.coefficient() problems
* #21009 - Fix symbolic GCD to accept any expression
* #21071 - substitution in denominator is skipped
* #21758 - Hold symbolic powers unevaluated if evaluation fails
* #22435 - Random build failure in pynac
* #23304 - hold=True does not always prevent evaluation
* #23368 - More immediate symbolic powers simplification
* #23964 - f.subs(I==...) does not work
* #24211 - Some trivial identities and simplifications missed by Sage (pynac ?)

## Maxima interface
* #6862 - Maxima default domain is real, not complex
* #9825  - interpret Maxima's temporary variables
* #11651 - Decide what to do with e<sup>(y=x)</sup>
* #12032 - Symbolics code passes ungrammatical expressions to maxima
* #12809 - Solve does not give consistent results when a dummy variable is involved
* #13071 - maxima interface integration problem
* #13773 - Translate maxima's if() function to Sage's cases()
* #16335 - dictionary of symbolic expressions (functions) raises Maxima-error
* #17892 - Sage cannot work with Maxima's symbolic limit
* #19151 - expression manipulations that do not preserve function latex_name and print_latex_func
* #19909 - segmentation fault: symbolic sum containing real
* #20221 - Wrap ratsubst
* #20755 - Bug in solve due to a bug in symbolic_expression_from_maxima_string
* #20846 - Maxima does not handle symbolic series
* #21444 - SR.wild and maxima don't mix
* #21907 - Bug in Maxima interface wrt polylog
* #21974 - Assuming x==0, x<sup>x</sup> raises a non-informative error from Maxima
* #22027 - Simplifying 0<sup>x</sup> gives 0, with no assumptions on x
* #22763 - Assumptions on symbols not preserved with some unevaluated integrals
* #22850 - Change specific heaviside() interface to Maxima
* #22857 - Using symbolic variables in domain 'positive' makes Sage crash
* #23138 - Cache assumptions and only send to Maxima when needed
* #23328 - Undefined limit product $INF * $ZEROB in lim-times

## SymPy interface
* #16816 - support SymPy's sum of roots
* #21412 - Convert piecewise functions to SymPy
* #22700 - Add more sympy limit examples
* #24078 - Set assumptions in SymPy too when doing assume()
* #24142 - Improve interface to SymPy solvers
* #24334 - sympy symbol -> SR drops assumptions

## Giac interface
* #23015 - Convert rootof function from giac
* #23016 - Dirac delta derivative conversion from giac
* #23136 - Allow giac algorithm in solve 

## FriCAS interface

* #28630 - Wrong conversion from fricas

## Other
* #11210 - add residues
* #17559 - Incorrect caching of variables' latex_name attribute
* #17958 - implement declare_var
* #18081 - Expression.factor_list() result inconsistent
* #18092 - evaluating symbolic expressions within ring of values
* #19046 - Fix mma free algorithm when no answer
* #19093 - bug in units conversion
* #20411 - Injecting shorthands for the most usual units
* #20859 - Simplify the logic handling the `EvaluationMethods` mixin class for Expression
* #21067 - Symbolic factor_list() should do integer factorisation of integers/rationals
* #22055 - implement Remez algorithm
* #22393 - sage_input for SR
* #22813 - Pass number of variables to var
* #23332 - Calculating eigenvectors of symbolic matrices leads to a crash.
* #24537 - Make find_local_maximum/minimum() handle symbolic functions
* #24850 - Provide convenient Expression.convert_numeric()

## Tickets fixed
* #24800 - bug with a system involving square roots, apparently do to an interface issue, Sage not being able to parse conditional answer provided by Maxima
* #24425 - Fix inherently failing random_expr doctest
* #24440 - Infinite loop from proving an expression
* #24773 - Delayed/Conditional Substitution
* #5574  - taking symbolic powers should coerce objects to symbolic expressions
* #24418 - bug numerical_approx(2^(450232897/4888643760))
* #23545 - segmentation fault with coefficients() on symbolic expressions
* #23845 - Doctest improvements to symbolic GCD
* #24236 - Structural comparison of expressions
* #24028 - Held definite integrals don't translate to SymPy
* #17935 - recognize SymPy's `NonElementaryIntegral`
* #22322 - allow sympy algorithm in solve
* #18787 - Mod numbers are ignored
* #22071 - Expression._latex_() triggers “dangerous” comparisons
* #23224 - wrong symbolic comparison of log
* #24147 - Segfault with ex.coefficients
* #17565 - ugly LaTeX of unevaluated sums
* #8603 - fix Fourier transforms of piecewise
* #17935 - recognize Sympy's `NonElementaryIntegral`
* #5091  - find_root should call fast_float
* #11332 - 65x penalty in performance for using float instead of `RealNumber`
* #16801 - Not all sympy function results get translated to Sage
* #22566 - SymPy's ceiling() is not translated to Sage
* #23923 - Interface cases function with SymPy's piecewise
* #10035 - Create hold context
* #18970 - always simplify log(a<sup>m</sup>,a) to m for any a,m coercible to Integer
* #21391 - Disallow mixing of pos.char.ring elements and symbolic variables
* #20204 - problems with constructing or converting to SymPy expressions
* #14305 - Clarify assumptions and domains in Maxima
* #23793 - Bug in symbolic GCD computations involving complex I
* #23861 - Make Expression normalization work with symbolic powers
* #22525 - Improper expressions from SR(string)
* #15298 - two copies of I
* #19996 - wrong result extracting symbolic coefficient (rational exponent)
* #21973 - is_negative() is False when assuming x < 0
* #22155 - Add more logic flags to more functions
* #23135 - Conjugate does not distribute over a sum
* #23496 - sympy patch for abstract function
* #22709 - to_poly_solve=True actually raises exception
* #17968 - exp(x<sup>3</sup>) from 1 to 2
* #22672 - Definite integral of (1-x)<sup>(1/5)</sup>/sqrt(x) crashes with both GSL and Maxima
* #22915 - Distribute symbolic sums over the terms of their first (sum) argument
* #22733 - Bug with first call to ex.series()
* #20179 - add a free_variables() method
* #22026 - Even reals are integers
* #22894 - Symbolic expression.is_exact()
* #22005 - sum(1/((2*n+1)<sup>2</sup>-4)<sup>2</sup>, n, 0, oo, algorithm='maxima') is wrong
* #20084 - residue: mathematically wrong output
* #22833 - fix a calculus doctest (giac, laplace, integration)
* #22909 - Indexed SR variables
* #22706 - Add more conversions from giac
* #22995 - Dummy inverse Laplace for giac
* #22997 - Parse unevaluated integral from giac
* #13733 - integration (but note unwanted interactions)
* #22937 - Implement a "distribute" method
* #21801 - Maxima summation bug
* #22959 - series() yields wrong result depending on precision
* #22090 - Gosper algorithm
* #22422 - Laplace transform involving time-shifts
* #22641 - Fix integration with Mathematica online
* #22891 - Add giac interface to integrate
* #22057 - Resultant of symbolic polynomials
* #22174 - Interface expression conversion to gamma() and normalization
* #22017 Unreadable real solution for a very simple equation
* #20162 - properties of converted finite field elements are wrong
* #10284 - Infinite loop in gcd() via pynac-0.2.1
* #20089 - let pynac.pyx use mpmath for arccos
* #20455 - rewrite buggy Expression.coefficients() without Maxima
* #15605 - (-1)<sup>(2/3)</sup> evaluates to 1
* #21428 - AssertionError plotting real part of complex function with float coefficients
* #14878 - very slow taylor expansion for composite functions
* #21730 - Add dedicated symbolic series tests
* #21223 - SymmetricFunctions over SymbolicRing broken
* #16724 - simplify_rational() takes very long or forever
* #20752 - Wrong simplification in symbolic trigonometry involving fractions
* #20858 - Option to combine symbolic fractions recursively
* #19775 - normalization in Pynac buggy
* #20888 - Support GinacFunction._print_latex_() customization
* #21007 - Unhelpful error when conversion to Symbolic Ring fails
* #10034 - simplify_trig of f(a/b*pi) without Maxima
* #19464 - ExpressionTreeWalker fails on some functions
* #20456 - assume(x>0) sets integer flag
* #16491 - unify output of trigonometric functions for complex input
* #14801 - Improved piecewise functions
* #9424 - numerically evaluate sums (also in [functions page](symbolics-functions))
* #16397 - symbolic cmp, stopgap #19465
* #16203 - conversion from SR.series() to PowerSeries(SR) gives unexpected result
* #15451 - limit wrongly gives ZeroDivisionError
* #17402 - SR.power_series cannot handle symbolic series
* #18094 - multiplication of powerseries wrapped in SR wrong
* #19259 - subrings of the symbolic ring
* #17659 - factor out SymbolicSeries from Expression
* #12967 - comparison of pi and infinity wrong
* #19035 - sync elementary assumptions on symbols/functions with Pynac
* #19310 - Pynac hashes are restricted to 32 bits
* #17624 - Coerce factorization of polynomial to symbolic expression
* #14211 - Crash in GiNaC::Number_T::hash()
* #10048 - deprecate substitute_expression()
* #12588 - abs(pi*I) should return pi
* #18921 - integer variable domain
* #18568 - wrong expansion of (x+sqrt(2)*x)^2
* #18695 - propagate the variable domain to the assumptions database
* #17321 - Pynac RuntimeError: comparing typeid's
* #12257 - 1.0*pi should *not* be pi
* #18482 - Unicode art for symbolics
* #15304 - is_polynomial() returns wrong results
* #14326 - Substituting numeric one in symbolic expression gives symbolic one
* #18257 - fix symbolic/pynac.pyx doctests
* #17759 - convenience class symbolic ExpressionTreeWalker(Converter)
* #17849 - substitute_function should not evaluate expression
* #18255 - Remove silly LimitedPrecisionConstant class
* #18088 - Inconsistency with 0^0
* #13326 - Bug in comparisons of infinite values
* #12807 - Taking the real part of a sum of exponentials ...
* #17394 - TypeError in Expression.simplify_hypergeometric()
* #15355 - representation of CIF-element plus SR-element
* #8949, #9769 - numpy object handling
* #15047 - LaTeX typeseting of SR.wild should prefix $ with \
* #18084 - Fix bad library uses of var()
* #18054 - Add is_finite method for the Symbolic Ring
* #18040 - Minimal polynomials of matrices over SymbolicRing
* #10846 - Conversion of PowerSeries -> SR bug
* #17799 - refactor `real_set.RealInterval`
* #9427  - fricas integrator
* #3021  - add curl and divergence functions to vectors
* #16643 integrate() infinite loop
* #15346 - implement simplify_sum and call it from full_simplify
* #15571 - Incorrect zero test of complex symbolic expressions
* #10629 - performance of checking if (c/d)<sup>(a/b)</sup> is rational
* #12922 - add implicit derivative
* #9824 - improve desolve system documentation for initial conditions
* #14630 - add `simplify_real`
* #16201 - default precision for symbolic power series from SR.series()
* #16213 - SR.series should simplify its terms
* #17399 - fix coefficients for symbolic series
* #8969 - `!=` in inputting and outputting with Maxima not handled right
* #10444 - make solve documentation better
* #13286 - special case of one variable, one equation, variable in list
* #10914 - Integral bug
* #11233 - Integral bug
* #11445 - Integral bug
* #11238 - Integral bug
* #11656 - additional assumptions needed for simplification
* #16941 - Add a hold parameter for symbolic integrals
* #9908 - a sum returns hypergeometric functions  (also in [functions page](symbolics-functions))
* #11894 - about an infinite sum appearing on NMBRTHRY list.
* #12708 - waiting for new upstream (Maxima) release.
* #13712 - wrong result from infinite sum (Maxima bug).
* #13526 simple incorrect limit
* #9421 - if `c` is already a variable it shouldn't come out as a constant
* #16007 - give solution constants of ODEs unique names
* #11785 - simplifying complex exponentials needs `rectform`
* #12322 - invalid simplification of complex logarithm
* #14306 regression in solve
* #3520 - `simplify_radical` does weird things
* #11912 - clarify and rename `simplify_radical`
* #21940 - Positive raised by a positive power is not known to be real
* #21946 - solve(x==x, x) returns [x == r1]
* #1773 - piecewise and symbolic don't play well together
* #12123 - another convolution bug
* #24726 - Sage silently accepts symbolic expressions with two comparison operators
* #23417 - fast construction of symbolic sums
* #24768 - Powers of symbolic sums inconsistence
* #23313 - Add more conversions from giac II
* #23835 - Replace Maxima with Pynac/Singular in Expression.factor()
