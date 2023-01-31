### Absolute dependencies on pexpect-maxima (#17753)

* *`calculus/desolvers.py`*: `desolve_*()`
* *`combinat/combinat.py`*: `euler_number()` (#17770 and #20763)
* *`geometry/lattice_polytope.py`*: `positive_integer_relations()` (see #20766)
* *`functions/orthogonal_polys.py`*: `hermite()` (#20297), `jacobi_P()` (#22326), `laguerre()` (#16813), `legendre_P/Q()` (#17151), `ultraspherical()` (#20428)
* *`functions/piecewise.py`*: `Piecewise.convolution()`
* *`matrix/matrix1.pyx`*: `Matrix._maxima_init_()`
* *`matrix/matrix_symbolic_dense.pyx`*: `Matrix_symbolic_dense.exp()` 
* *`structure/sage_object.pyx`*: `SageObject._maxima_()`, `_maxima_init_()`
* *`symbolic/assumptions.py`*: `GenericDeclaration.assume()`
* *`symbolic/expression.pyx`*: `Ex.assume()`, `forget()`, `assume_str()`, `assert()`, `expand_trig()`, `reduce_trig()`, `coefficients()` (#20455), `poly()` (#20455), `maxima_methods()`, `rectform()`, `simplify()`, `simplify_real()`, `simplify_rational()` (#21335), `simplify_log()`, `expand_log()`, `factor()` (#23835), `solve()`, `sum()`
* *`symbolic/maxima_wrapper.py`*: *
* *`calculus/calculus.py`*: `symbolic_expression_from_maxima_string()` called by `factor()` and indirectly by  `solve()`

### Optional dependencies on pexpect-maxima
* *`combinat/combinat.py`*: stirling_number2()
* *`symbolic/integration/*`*: Maxima in principle exchangeable but missing functionality in the alternatives

### Other dependencies on maxima_lib
* *`calculus/calculus.py`*: nintegral(), laplace(), inverse_laplace()
* *`calculus/desolvers.py`*:
* *`calculus/calculus.py`*:
* *`functions/other.py`*:
* *`functions/log.py`*:
* *`functions/piecewise.py`*: Piecewise.critical_points()
* *`functions/special.py`*: spherical_hankel1/2(), spherical_harmonic (#15024, #20939)
* *`matrix/matrix_symbolic_dense.pyx`*: Matrix_symbolic_dense.eigenvalues(), eigenvectors_left(), exp(), charpoly(), simplify_trig(), simplify_rational(), factor(), 
* *`schemes/projective/projective_morphism.py`*: SchemeMorphism_polynomial_projective_space.dynatomic_polynomial()
* *`symbolic/expression.pyx`*: Expression._maxima_(), taylor(), combine() (#21034), partial_fraction() (#25645), simplify_hypergeometric(), simplify_factorial(), canonicalize_radical()
* *`symbolic/relation.py`*: test_relation_maxima(), solve(), solve_ineq_univar(), solve_ineq_fourier()
