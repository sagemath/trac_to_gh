
### Absolute dependencies on pexpect-maxima ([#17753](https://trac.sagemath.org/ticket/17753))

 * _`calculus/desolvers.py`_: `desolve_*()`
 * _`combinat/combinat.py`_: `euler_number()` ([#17770](https://trac.sagemath.org/ticket/17770) and [#20763](https://trac.sagemath.org/ticket/20763))
 * _`geometry/lattice_polytope.py`_: `positive_integer_relations()` (see [#20766](https://trac.sagemath.org/ticket/20766))
 * _`functions/orthogonal_polys.py`_: `hermite()` ([#20297](https://trac.sagemath.org/ticket/20297)), `jacobi_P()` ([#22326](https://trac.sagemath.org/ticket/22326)), `laguerre()` ([#16813](https://trac.sagemath.org/ticket/16813)), `legendre_P/Q()` ([#17151](https://trac.sagemath.org/ticket/17151)), `ultraspherical()` ([#20428](https://trac.sagemath.org/ticket/20428))
 * _`functions/piecewise.py`_: `Piecewise.convolution()`
 * _`matrix/matrix1.pyx`_: `Matrix._maxima_init_()`
 * _`matrix/matrix_symbolic_dense.pyx`_: `Matrix_symbolic_dense.exp()` 
 * _`structure/sage_object.pyx`_: `SageObject._maxima_()`, `_maxima_init_()`
 * _`symbolic/assumptions.py`_: `GenericDeclaration.assume()`
 * _`symbolic/expression.pyx`_: `Ex.assume()`, `forget()`, `assume_str()`, `assert()`, `expand_trig()`, `reduce_trig()`, `coefficients()` ([#20455](https://trac.sagemath.org/ticket/20455)), `poly()` ([#20455](https://trac.sagemath.org/ticket/20455)), `maxima_methods()`, `rectform()`, `simplify()`, `simplify_real()`, `simplify_rational()` ([#21335](https://trac.sagemath.org/ticket/21335)), `simplify_log()`, `expand_log()`, `factor()` ([#23835](https://trac.sagemath.org/ticket/23835)), `solve()`, `sum()`
 * _`symbolic/maxima_wrapper.py`_: *
 * _`calculus/calculus.py`_: `symbolic_expression_from_maxima_string()` called by `factor()` and indirectly by  `solve()`


### Optional dependencies on pexpect-maxima
 * _`combinat/combinat.py`_: stirling_number2()
 * _`symbolic/integration/*`_: Maxima in principle exchangeable but missing functionality in the alternatives


### Other dependencies on maxima_lib
 * _`calculus/calculus.py`_: nintegral(), laplace(), inverse_laplace()
 * _`calculus/desolvers.py`_:
 * _`calculus/calculus.py`_:
 * _`functions/other.py`_:
 * _`functions/log.py`_:
 * _`functions/piecewise.py`_: Piecewise.critical_points()
 * _`functions/special.py`_: spherical_hankel1/2(), spherical_harmonic ([#15024](https://trac.sagemath.org/ticket/15024), [#20939](https://trac.sagemath.org/ticket/20939))
 * _`matrix/matrix_symbolic_dense.pyx`_: Matrix_symbolic_dense.eigenvalues(), eigenvectors_left(), exp(), charpoly(), simplify_trig(), simplify_rational(), factor(), 
 * _`schemes/projective/projective_morphism.py`_: SchemeMorphism_polynomial_projective_space.dynatomic_polynomial()
 * _`symbolic/expression.pyx`_: Expression._maxima_(), taylor(), combine() ([#21034](https://trac.sagemath.org/ticket/21034)), partial_fraction() ([#25645](https://trac.sagemath.org/ticket/25645)), simplify_hypergeometric(), simplify_factorial(), canonicalize_radical()
 * _`symbolic/relation.py`_: test_relation_maxima(), solve(), solve_ineq_univar(), solve_ineq_fourier()
