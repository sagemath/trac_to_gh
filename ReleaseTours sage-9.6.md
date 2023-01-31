# Sage 9.6 Release Tour

Sage 9.6 was released on May 15, 2022.

A total of 83 people were involved as authors
or reviewers of code contributions to Sage 9.6.

Here is an overview of some of the main changes
in this version.

## User interface, plotting and graphics

### JupyterLab 3.3

[JupyterLab](https://jupyter.org/), the latest web-based interactive development environment for notebooks, code, and data, is slated to replace the now-classic Jupyter notebook interface.  The version of JupyterLab in the Sage distribution has been upgraded to the major new version 3.3. #32069, #33607

After `./sage -i jupyterlab_widgets`, you can run it using 

```
./sage -n jupyterlab
```
Also two new interface variants are provided: 

```
./sage -n nbclassic
```
and

```
./sage -n retrolab
```

### LaTeX displays in JupyterLab

Users of Sage in [JupyterLab](https://jupyter.org/) got used to expressions displayed at center in the LaTeX display mode. For compatibility with displays in classic Jupyter, we decided to change the behavior so that now expressions are displayed aligned left by default.

If you belong to the minority preferring centered displays, you can set your preference by

```
dm = get_display_manager()   
dm.preferences.align_latex = 'center'  # or 'left'
```
in the `~/.sage/init.sage` script.

### Interactive graph editing with phitigra

With the new optional package [phitigra](https://pypi.org/project/phitigra) (use `./sage -i phitigra` to install), graphs can be edited by interactively placing vertices, edges, etc.  This works both in the classic Jupyter notebook and in JupyterLab. It can also be used to make animations (see the demo notebook at https://github.com/jfraymond/phitigra for examples). Done in #30540 and #33639.

![](https://trac.sagemath.org/raw-attachment/wiki/ReleaseTours/sage-9.6/editor.png)

### Hyperbolic plots

* Added the ability to choose the hyperbolic model for hyperbolic plots. #22081

### Graphics with TikZ

The `TikzPicture` module which was developed in the [slabbe](https://pypi.org/project/slabbe/) package for more than 5 years is now in Sage. This was done in ticket #20343. The module is within the new file `sage/misc/latex_standalone.py` and its documentation in the reference manual is available here: https://doc.sagemath.org/html/en/reference/misc/sage/misc/latex_standalone.html. Below are some usage examples.

First example shows that it takes any tikz picture string as input:

```
sage: from sage.misc.latex_standalone import TikzPicture
sage: s = '\\begin{tikzpicture}\n\\draw[->,green,very thick](0,0) -- (1,1);\\end{tikzpicture}'
sage: t = TikzPicture(s)
sage: t        # in Jupyter, rich representation will show the image instead
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}
\draw[->,green,very thick](0,0) -- (1,1);\end{tikzpicture}
\end{document}
sage: path_to_file = t.pdf() # and opens the image in a viewer
```
![](https://wiki.sagemath.org/ReleaseTours/sage-9.6?action=AttachFile&do=get&target=tikz_arrow.png)

Of course, conversion to pdf format necessitates `pdflatex` or `lualatex`. If `lualatex` is available it uses it in preference to `pdflatex` because it handles better the very big pictures in terms of memory limits.

One can provide a local filename to save to, or convert the image to other formats (using pdftocairo or imagemagick external packages):

```
sage: path_to_file = t.pdf('file.pdf')  # when providing a filename, it just saves 
                                        # the file locally, does not open in a viewer
sage: path_to_file = t.png() # conversion to png
sage: path_to_file = t.svg() # to svg
sage: path_to_file = t.tex() # print the tex source to a file
```

Another example with graphs where additional usepackage are necessary to compile the image correctly:

```
sage: from sage.misc.latex_standalone import TikzPicture
sage: g = graphs.PetersenGraph()
sage: t = TikzPicture(latex(g), standalone_config=["border=4mm"], usepackage=['tkz-graph'])
sage: t        # in Jupyter, rich representation will show the image instead
\documentclass[tikz]{standalone}
\standaloneconfig{border=4mm}
\usepackage{tkz-graph}
\begin{document}
\begin{tikzpicture}
\definecolor{cv0}{rgb}{0.0,0.0,0.0}
\definecolor{cfv0}{rgb}{1.0,1.0,1.0}
\definecolor{clv0}{rgb}{0.0,0.0,0.0}
\definecolor{cv1}{rgb}{0.0,0.0,0.0}
---
65 lines not printed (3695 characters in total).
Use print to see the full content.
---
\Edge[lw=0.1cm,style={color=cv6v8,},](v6)(v8)
\Edge[lw=0.1cm,style={color=cv6v9,},](v6)(v9)
\Edge[lw=0.1cm,style={color=cv7v9,},](v7)(v9)
%
\end{tikzpicture}
\end{document}
sage: _ = t.pdf()               # or t.png() or t.svg()
```
![](https://wiki.sagemath.org/ReleaseTours/sage-9.6?action=AttachFile&do=get&target=tikz_graph.png)

```
sage: from sage.misc.latex_standalone import TikzPicture
sage: V = [[1,0,1],[1,0,0],[1,1,0],[0,0,-1],[0,1,0],[-1,0,0],[0,1,1],[0,0,1],[0,-1,0]]
sage: P = Polyhedron(vertices=V).polar()
sage: s = P.projection().tikz([674,108,-731],112)
sage: t = TikzPicture(s)
sage: _ = t.pdf()               # or t.png() or t.svg()
```
![](https://wiki.sagemath.org/ReleaseTours/sage-9.6?action=AttachFile&do=get&target=tikz_polyhedron.png)

The module also contains a class `Standalone`, from which the class `TikzPicture` inherits:

```
sage: from sage.misc.latex_standalone import Standalone
sage: s = Standalone('Hello World', usepackage=['amsmath'], standalone_config=['beamer=true','border=1mm'])
sage: s        # in Jupyter, rich representation will show the image instead
\documentclass{standalone}
\standaloneconfig{beamer=true}
\standaloneconfig{border=1mm}
\usepackage{amsmath}
\begin{document}
Hello World
\end{document}
sage: _ = s.pdf()               # or s.png() or s.svg()
```
![](https://wiki.sagemath.org/ReleaseTours/sage-9.6?action=AttachFile&do=get&target=tikz_hello.png)

Another example using `Standalone` with a tableau:

```
sage: P = Permutations(10)
sage: p = P.random_element()
sage: p
[3, 10, 1, 9, 5, 6, 7, 2, 8, 4]
sage: t = p.to_tableau_by_shape([3,3,3,1])
sage: t
[[2, 8, 4], [5, 6, 7], [10, 1, 9], [3]]
sage: s = Standalone(latex(t), standalone_config=["border=1mm"])
sage: s
\documentclass{standalone}
\standaloneconfig{border=1mm}
\begin{document}
{\def\lr#1{\multicolumn{1}{|@{\hspace{.6ex}}c@{\hspace{.6ex}}|}{\raisebox{-.3ex}{$#1$}} }
\raisebox{-.6ex}{$\begin{array}[b]{*{3}c}\cline{1-3}
\lr{2}&\lr{8}&\lr{4}\\\cline{1-3}
\lr{5}&\lr{6}&\lr{7}\\\cline{1-3}
\lr{10}&\lr{1}&\lr{9}\\\cline{1-3}
\lr{3}\\\cline{1-1}
\end{array}$}
}
\end{document}
sage: _ = s.pdf()               # or s.png() or s.svg()
```
![](https://wiki.sagemath.org/ReleaseTours/sage-9.6?action=AttachFile&do=get&target=tikz_tableau.png)

In a next step, a method `tikz()` will be added to graphs, polytopes, posets, etc. to return an object of type `TikzPicture` see #33002.

### Complex plots

The complex plotting package [phase_mag_plot](https://github.com/davidlowryduda/phase_mag_plot) has been incorporated into Sage. Now `complex_plot` allows contouring, tiling, and `matplotlib`-compatible colormaps. This was added in ticket #33416.

To use a colormap, one can pass in a string as in

```
sage: complex_plot((x - 5)*sqrt(x), (-10, 10), (-10, 10), cmap='twilight')
```
![](https://wiki.sagemath.org/ReleaseTours/sage-9.6?action=AttachFile&do=get&target=cmap_twilight.png)

Contouring or tiling are enabled through keyword options. To look smooth, it's typically necessary to plot the function on additional points through the use of `plot_points`. This looks like

```
sage: complex_plot((x - 5)*sqrt(x), (-10, 10), (-10, 10), cmap='twilight', plot_points=500, contoured=True)
```
![](https://wiki.sagemath.org/ReleaseTours/sage-9.6?action=AttachFile&do=get&target=cmap_twilight_contour.png)

```
sage: complex_plot((x - 5)*sqrt(x), (-10, 10), (-10, 10), cmap='twilight', plot_points=500, tiled=True)
```
![](https://wiki.sagemath.org/ReleaseTours/sage-9.6?action=AttachFile&do=get&target=cmap_twilight_tiled.png)

## Linear algebra

### NumPy integration

The new classes `Matrix_numpy_integer_dense` and `Vector_numpy_integer_dense` implement matrices and vectors with 64-bit integer entries backed by `numpy` arrays. #32465.

As a first application, several methods of `GenericGraph` that return matrices, such as `adjacency_matrix`, now accept keyword arguments that can select the matrix implementation. #33377, #33387, #33388, #33389

```
sage: graphs.PathGraph(5).adjacency_matrix(sparse=False, implementation='numpy')
[0 1 0 0 0]
[1 0 1 0 0]
[0 1 0 1 0]
[0 0 1 0 1]
[0 0 0 1 0]
sage: type(_)
<class 'sage.matrix.matrix_numpy_integer_dense.Matrix_numpy_integer_dense'>
```

### CombinatorialFreeModule improvements

Performing sums and similar constructions for `CombinatorialFreeModule` have been made faster. #33267

## Symbolics

### SymPy 1.10.1

SymPy has been upgraded to version 1.10.1 ([release notes](https://github.com/sympy/sympy/wiki/release-notes-for-1.10)). #33398, #33547, #33584

### ImageSet

Sage 9.6 defines a new class `ImageSet`. #32121

```
sage: ImageSet(sin, RealSet.open(0, pi/4))
Image of (0, 1/4*pi) by The map sin from (0, 1/4*pi)
sage: _.an_element()
1/2*sqrt(-sqrt(2) + 2)

sage: sos(x,y) = x^2 + y^2; sos
(x, y) |--> x^2 + y^2
sage: ImageSet(sos, ZZ^2)
Image of
 Ambient free module of rank 2 over the principal ideal domain Integer Ring by
 The map (x, y) |--> x^2 + y^2 from Vector space of dimension 2 over Symbolic Ring
sage: _.an_element()
1
sage: ImageSet(sos, Set([(3, 4), (3, -4)]))
Image of {...(3, -4)...} by
 The map (x, y) |--> x^2 + y^2 from Vector space of dimension 2 over Symbolic Ring
sage: _.an_element()
25
```

The new class mirrors and translates to [SymPy's ImageSet](https://docs.sympy.org/latest/modules/sets.html#imageset):

```
sage: from sage.sets.image_set import ImageSet
sage: S = ImageSet(sin, RealSet.open(0, pi/4)); S
Image of (0, 1/4*pi) by The map sin from (0, 1/4*pi)
sage: S._sympy_()
ImageSet(Lambda(x, sin(x)), Interval.open(0, pi/4))
```

Most methods of `ImageSet` are actually provided by its base class, the new class `ImageSubobject`. 
For all morphisms in the `Sets` category, there is now a default method `image`, which constructs an instance of either `ImageSubobject` or `ImageSet`.

### Orthogonal polynomials

Three classes of classical (discrete) orthogonal polynomials in the Askey scheme have been added: #33393

* Krawtchouk polynomials
* Hahn polynomials
* Meixner polynomials

### Spherical harmonics

Various issues regarding spherical harmonics have been fixed (#33117, #33501). In particular, the
Condon-Shortley phase has been added, so that Sage's spherical harmonics now agree with those of
Wikipedia, SymPy, SciPy and Mathematica. For instance

```
sage: theta, phi = var('theta phi')
sage: spherical_harmonic(1, 1, theta, phi)
-1/4*sqrt(3)*sqrt(2)*e^(I*phi)*sin(theta)/sqrt(pi)
```
This clearly agrees with SymPy's spherical harmonics: 

```
sage: from sympy import Ynm
sage: Ynm(1, 1, theta, phi).expand(func=True) 
-sqrt(6)*exp(I*phi)*sin(theta)/(4*sqrt(pi))
```

## Polyhedral geometry and linear programming

### polymake 4.6

polymake, a comprehensive system for computations in polyhedral geometry, tropical geometry, etc., has been upgraded to version 4.6 ([release notes](https://polymake.org/doku.php/news/release_4_6)). #33251

### CyLP

The new optional package [CyLP](https://github.com/coin-or/CyLP) (`./sage -i cylp`) provides a detailed interface to [Clp](https://github.com/coin-or/Clp), the COIN-OR linear programming solver, and [Cbc](https://github.com/coin-or/Cbc), the COIN-OR branch-and-cut solver for mixed-integer linear programs. #33847 

In a future version of Sage, CyLP is intended to provide a replacement for the Sage-specific backend interface to Clp and Cbc, [sage-numerical-backends-coin](https://pypi.org/project/sage-numerical-backends-coin/); see Meta-ticket #26511.

### Equivariant Ehrhart theory

Sage 9.6 allows for the calculation of the H*-series (also known as the φ-series) of a rational polytope which is invariant under the linear action of a finite group, as introduced by Alan Stapledon as part of equivariant Ehrhart theory #27637.
The computation is made with the method `Hstar_function` of a rational polytope.
The fixed subset of a polytope under the action of a group element may also be computed via the methods `fixed_subpolytope` or `fixed_subpolytopes`.

As an example, consider the action of the symmetric group S3 on the 2-dimensional permutahedron in 3-dimensional space, given by permuting the three basis vectors.
As shown by Ardila, Supina, and Vindas Meléndez, the corresponding H*-series is polynomial and effective:

```
sage: p3 = polytopes.permutahedron(3, backend = 'normaliz')      
sage: G = p3.restricted_automorphism_group(output='permutation') 
sage: reflection12 = G([(0,2),(1,4),(3,5)])                      
sage: reflection23 = G([(0,1),(2,3),(4,5)])                      
sage: S3 = G.subgroup(gens=[reflection12, reflection23])         
sage: S3.is_isomorphic(SymmetricGroup(3))                        
True
sage: p3.Hstar_function(S3, output='complete')
{'Hstar': chi_0*t^2 + (chi_0 + chi_1 + chi_2)*t + chi_0,
 'Hstar_as_lin_comb': (t^2 + t + 1, t, t),
 'conjugacy_class_reps': [(), (0,1)(2,3)(4,5), (0,3,4)(1,5,2)],
 'character_table': [ 1  1  1]
 [ 1 -1  1]
 [ 2  0 -1],
 'is_effective': True}
sage: p3.fixed_subpolytope(reflection12)
A 1-dimensional polyhedron in QQ^3 defined as the convex hull of 2 vertices
sage: p3.fixed_subpolytope(reflection12).vertices()
(A vertex at (3/2, 3/2, 3), A vertex at (5/2, 5/2, 1))
```

## Manifolds

### Improved Manifold constructor

The `structure` parameter of the `Manifold` constructor has new, more convenient defaulting behavior. #33001

When parameters such as `diff_degree` or `metric_name` are given, the implied structure is selected:

```
sage: M = Manifold(3, 'M', diff_degree=0); M
3-dimensional topological manifold M
sage: M = Manifold(3, 'M', diff_degree=2); M
3-dimensional differentiable manifold M
sage: M = Manifold(3, 'M', metric_name='g'); M
3-dimensional Riemannian manifold M
```

### Symplectic manifolds

Symplectic structures have been added to Sage (#30362).

The standard symplectic vector space can be obtained as follows:

```
sage: M.<q, p> = manifolds.StandardSymplecticSpace(2, symplectic_name='omega')
sage: omega = M.symplectic_form()
saga: omega.display()
omega = -dq∧dp
```

To use an existing `2`-form as a symplectic form use the new `wrap` method.

```
sage: from sage.manifolds.differentiable.symplectic_form import SymplecticForm
sage: M = manifolds.Sphere(2, coordinates='stereographic')
sage: vol_form = M.induced_metric().volume_form()
sage: omega = SymplecticForm.wrap(vol_form, 'omega', r'\omega')
sage: omega.display()
omega = -4/(y1^4 + y2^4 + 2*(y1^2 + 1)*y2^2 + 2*y1^2 + 1) dy1∧dy2
```

Currently, the following operations from symplectic geometry are supported: 
- Musical isomorphism (flat/sharp) between vector fields and `1`-forms.
- Poisson tensor
- Liouville volume form
- Poisson bracket of functions
- Hamiltonion vector fields
- Symplectic Hodge dual of a differential form

### Projective spaces

Real projective spaces have been added to the manifold catalog (#33221).
For example, one can construct the real projective plane.

```
sage: RP2 = manifolds.RealProjectiveSpace(); RP2
2-dimensional topological manifold RP2
sage: latex(RP2)
\mathbb{RP}^{2}
```

There are three charts. Considering an immersion in three-dimensional Euclidean space,
the chart corresponds to a choice of one (out of three possible) coordinates to be always nonzero.
The coordinates listed are the two other coordinates assuming that the nonzero coordinate is always one.

```
sage: C0, C1, C2 = RP2.top_charts()
sage: p = RP2.point((2,0), chart = C0)
sage: q = RP2.point((0,3), chart = C0)
sage: p in C0.domain()
True
sage: p in C1.domain()
True
sage: C1(p)
(1/2, 0)
sage: p in C2.domain()
False
sage: q in C0.domain()
True
```

The point `q` looks like `(1,0,3)` in ambient Euclidean space, so
it is not in the domain of the chart `C1`. It also has the form
`(1/3,0,1)` when considered in the chart `C2`. 

```
sage: q in C1.domain()
False
sage: q in C2.domain()
True
sage: C2(q)
(1/3, 0)
```

If both coordinates in a local chart are nonzero then that point
is in the domain of all charts. The change of coordinates is found
by normalizing the appropriate chart. So for example, the point
`(1, 2, 3)` is the same as the point `(1/2, 1, 3/2)` is the same as the point
`(1/3, 2/3, 1)`, which is reflected by defining `r` to be a point in the
default chart `C0`.

```
sage: r = RP2.point((2,3))
sage: r in C0.domain() and r in C1.domain() and r in C2.domain()
True
sage: C0(r) # corresponding to (1, 2, 3)
(2, 3)
sage: C1(r) # corresponding to (1/2, 1, 3/2)
(1/2, 3/2)
sage: C2(r) # corresponding to (1/3, 2/3, 1)
(1/3, 2/3)
```

### Internal code improvements and bug fixes

Some performance improvements have been implemented (#33110):

- use the first Bianchi identity in the computation of the Riemann tensor
- compute volume forms with contravariant indices only as needed
- no try to simplify trivial expressions consisting only of a single number or symbolic variable 

Some bugs have been corrected: #32953, #33399, #33780.
## Algebra

### lrcalc 2.1

lrcalc, Anders Buch's Littlewood-Richardson Calculator, has been upgraded to the major new version 2.1 [changelog](https://bitbucket.org/asbuch/lrcalc/src/master/ChangeLog). #31355

### Finitely presented modules over graded algebras

Sage 9.6 allows the construction of finitely presented modules over graded algebras, even algebras which are infinite and/or noncommutative like the mod *p* Steenrod algebra. Some homological algebra is implemented in general, and more tools are implemented specifically for modules over the Steenrod algebra (#32505, #30680).

```
sage: from sage.modules.fp_graded.module import FPModule
sage: E.<x,y> = ExteriorAlgebra(QQ)
# M has one generator g in degree 0 and two relations, x*g and y*g.
# That is, M is QQ as a trivial E-module.
sage: M = FPModule(E, [0], [[x], [y]])
# Free resolution:
sage: M.resolution(3)
[Module morphism:
   From: Free graded left module on 1 generator over 
          The exterior algebra of rank 2 over Rational Field
   To:   Finitely presented left module on 1 generator and 2 relations over 
          The exterior algebra of rank 2 over Rational Field
   Defn: g[0] |--> g[0],
 Module morphism:
   From: Free graded left module on 2 generators over 
          The exterior algebra of rank 2 over Rational Field
   To:   Free graded left module on 1 generator over 
          The exterior algebra of rank 2 over Rational Field
   Defn: g[1, 0] |--> x*g[0]
         g[1, 1] |--> y*g[0],
 Module morphism:
   From: Free graded left module on 3 generators over 
          The exterior algebra of rank 2 over Rational Field
   To:   Free graded left module on 2 generators over 
          The exterior algebra of rank 2 over Rational Field
   Defn: g[2, 0] |--> x*g[1, 0]
         g[2, 1] |--> y*g[1, 0] + x*g[1, 1]
         g[2, 2] |--> y*g[1, 1],
 Module morphism:
   From: Free graded left module on 4 generators over 
          The exterior algebra of rank 2 over Rational Field
   To:   Free graded left module on 3 generators over 
          The exterior algebra of rank 2 over Rational Field
   Defn: g[3, 0] |--> x*g[2, 0]
         g[3, 1] |--> y*g[2, 0] + x*g[2, 1]
         g[3, 2] |--> y*g[2, 1] + x*g[2, 2]
         g[3, 3] |--> y*g[2, 2]]
```

There is a new thematic tutorial providing many details and examples.

### Miscellaneous improvements

* Ideal membership over quotient rings can now be decided (by reducing to ideal membership in the parent ring). #33237
* Iterating over (some) infinite modules (including ℤ*<sup>n</sup>*) now enumerates the entire module, in a "natural" order. #33287
* `BinaryQF.solve_integer()` now also works for quadratic forms of square discriminant. #33026
* `Quaternion fractional ideals` (including orders) now support the usual operations (e.g., `a*I`, `I*a`, `I+J`). #32264
* `AdditiveAbelianGroupWrapper` now exposes `.discrete_log()` for (multi-dimensional) logarithms in finite abelian groups. #32384
* Graded submodules of graded modules now know they are graded (with respect to the ambient grading); similarly for filtered submodules. #33321
* Polynomials now evaluate faster on monomial inputs. #33165
* Implement specialized code for summing terms and monomials in `CombinatorialFreeModule`. #33267
* Improvements and fixes to `skew_by()` in symmetric functions. #33313
* Attempt to invert elements generically in a finite dimensional algebra. #33250
* Tensor products of finite dimensional modules know they are finite dimensional (Sage does not currently have any structure for infinite tensor products, which can have some subtleties). #30252
* Improved coercions and conversions with Laurent polynomials and their fraction field. #31320 #33477
* Faster evaluation of univariate polynomials with monomials. #33165

## Number theory

### Elliptic curves

* Elliptic-curve DLP and Weil pairings over finite fields are now *much* faster (thanks to PARI). #33121
* Scalar multiplication on elliptic curves over finite fields is now significantly faster (thanks to PARI). #33147
* Computing the Weierstraß ℘ function of an elliptic curve is now significantly faster (thanks to PARI). #33223
* Classes used by the Monsky-Washnitzer curves now use the new coercion system. #33525 #33576

## Cryptography

Optimizations to `SBox`. #25633

## Package upgrades

For a list of all packages and their versions, see
* https://repology.org/projects/?inrepo=sagemath_stable

### Python 3.10

Sage 9.6 continues to support system Python 3.7.x to 3.10.x. If no suitable version of Python is installed in the system, Sage will install its own copy of Python. Sage now ships Python 3.10.3 for this purpose. #30767, #33512

### FLINT 2.8.x and arb 2.22.x

[FLINT](https://flintlib.org/) has been upgraded from 2.7.1 to 2.8.4.#32211

The FLINT 2.8 series brings major new algorithms and general speedups ([release notes](https://github.com/wbhart/flint2/blob/flint-2.8/NEWS#L1262)).

Note that Sage accepts system installations of FLINT >= 2.6.x. Users on older distributions who want to benefit from the speed ups in FLINT 2.8.x may want to use `./configure --without-system-flint`.

Meta-ticket #31408 tracks the effort to make use of new features added in recent FLINT releases in the Sage library.

[arb](https://arblib.org/) has been upgraded from 2.19.0 to 2.22.1. #32211, #33189

The 2.20, 2.21, and 2.22 series have brought major new algorithms and other improvements ([changelog](https://arblib.org/history.html#version-2-22-1)).

### igraph 0.9.x

The `igraph` library and its Python interface (now also just called `igraph`) have been upgraded to versions 0.9.7/0.9.9. #32510, #33526

## For developers: Refactoring and modularization

See also [Meta-ticket #29705](https://github.com/sagemath/sage/issues/29705)

### sage.features.Executable.absolute_filename()

The Sage library interfaces to some external non-Python packages by running an executable program in a separate process. The package may either be available from a system installation, or the Sage distribution may have installed the package in the `SAGE_LOCAL` prefix hierarchy. The main `sage` script sets up various environment variables before starting the Python interpreter; in particular, it sets `PATH` to include `SAGE_LOCAL/bin`, which ensures that the installed executables are found.

In Sage 9.6, we have changed most calls to executables so that they no longer depend on the environment variable `PATH` being set in this way. Every executable program is represented by an instance of `sage.features.Executable`. Its method `absolute_filename` explicitly searches inside `SAGE_LOCAL/bin` (in installations with `SAGE_LOCAL`) before it depends on `PATH`.
#31292,
#31296,
#32645,
#32893,
#33440,
#33465,
#33467

### Preparations for PEP 420 implicit namespace packages

The Sage doctester is now prepared for [namespace packages](https://doc.sagemath.org/html/en/developer/packaging_sage_library.html#ordinary-packages-vs-implicit-namespace-packages). #33033

To [reduce runtime dependencies](https://doc.sagemath.org/html/en/developer/packaging_sage_library.html#module-level-runtime-dependencies), many imports from `sage.graphs.all`, `sage.interfaces.all`, `sage.misc.all`, `sage.libs.all`, `sage.rings.all` have been replaced by more specific imports; and module-level imports from `sage.plot` have been changed to either use `lazy_import` or have been moved inside methods.
#30582,
#32847,
#32989,
#32999,
#33000,
#33007,
#33146,
#33199,
#33466,
#33468

### Lazy imports of classes now support "isinstance"

No Python object is an instance of a class that cannot be imported from the module that defines it.
The new special method `LazyImport.__instancecheck__` now just returns `False` in this case. #33017

This provides a convenient pattern for writing modularized code when [creating an abstract base class for "isinstance" testing](https://wiki.sagemath.org/ReleaseTours/sage-9.5#Abstract_base_classes_for_.22isinstance.22_testing) is not justified.

```
sage: from sage.schemes.generic.scheme import Scheme
sage: sZZ = Scheme(ZZ)
sage: lazy_import('xxxx_does_not_exist', 'Pluffe')
sage: isinstance(sZZ, (Scheme, Pluffe))
True
sage: isinstance(ZZ, (Scheme, Pluffe))
False
```
Likewise, no class is a subclass of a class that cannot be imported from the module that defines it;
so the new special method `LazyImport.__subclasscheck__` implements the same logic.

### sage.geometry.polyhedron.base reorganized

The module `sage.geometry.polyhedron.base` has been split into several modules, grouping the methods of class `Polyhedron_base` according to their topic and runtime dependencies on other parts of Sage. #32651

## New developer tools

### Pre-built Docker containers on ghcr.io

Our portability CI on GitHub Actions builds [Docker images](https://github.com/orgs/sagemath/packages?tab=packages&q=with-targets-optional) for all tested Linux platforms (and system package configurations) and makes them available on GitHub Packages (ghcr.io). #30933

Since 9.6.beta1, the image version corresponding to the latest development release receives the additional Docker tag `dev`, see for example the Docker image for [ubuntu-impish-standard](https://github.com/sagemath/sage/pkgs/container/sage%2Fsage-docker-ubuntu-impish-standard-with-targets-optional). Thus, for example, the following command will work:

```
$ docker run -it ghcr.io/sagemath/sage/sage-docker-ubuntu-impish-standard-with-targets-optional:dev bash
```

Images whose names end with the suffix `-with-targets-optional` are the results of full builds and a run of `make ptest`. They also contain a copy of the source tree and the full logs of the build and test. 

[Smaller images corresponding to earlier build stages](https://github.com/orgs/sagemath/packages?tab=packages&q=sage-docker-debian-bullseye-standard) are also available: 

* `-with-system-packages` provides a system installation with system packages installed, no source tree,

* `-configured` contains a partial source tree and has completed bootstrap and the `configure`,

* `-with-targets-pre` contains the full source tree and a full installation of all non-Python packages,

* `-with-targets` contains the full source tree and a full installation of Sage, including the HTML documentation, but `make ptest` has not been run yet.

### Sage development in the cloud with Gitpod

[Gitpod](https://www.gitpod.io/) is a service that provides a development environment in the cloud based on VS Code. It is free to use for up to 50 hours per month. Sage now includes a configuration for Gitpod; see the new section [Setting up your workspace](https://doc.sagemath.org/html/en/developer/workspace.html#section-gitpod) in the Sage Developer's Guide. 
#33103, #33589

<img src="ReleaseTours sage-9.6/gitpod_badge.png" width=116px>

To launch Gitpod on a branch of a Trac ticket, you can use the new badge  in the ticket box.

Alternatively, prepend any repository URL with `https://gitpod.io/#`; for example, https://gitpod.io/#https://github.com/sagemath/sagetrac-mirror/tree/develop opens a development environment containing a prebuilt copy of Sage corresponding to the `develop` branch.

### Builds and checks of ticket branches on [GitHub](GitHub) Actions

Next to the familiar patchbot badges, each ticket now has badges linking to tests that run on GitHub Actions.

<img src="ReleaseTours sage-9.6/ticket_badges.png" width=547px>

#### Linting workflow (pycodestyle, relint)

A [linting workflow](https://github.com/sagemath/sage/blob/develop/.github/workflows/lint.yml) on GitHub Actions runs on all pushes to a branch on Trac. It checks that the code of the current branch adheres to the style guidelines using [pycodestyle](https://doc.sagemath.org/html/en/developer/tools.html#pycodestyle) (in the `pycodestyle-minimal` configuration) and [relint](https://doc.sagemath.org/html/en/developer/tools.html#relint). 

In order to see details when it fails, you can click on the badge and then select the most recent workflow run.

Sage 9.6 includes again many improvements to the [coding style checked by pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes). #32978, #32979, #33095, #33102, ...

Consequently, the `pycodestyle-minimal` configuration has been extended to enforce `E111`, `E401`, `E701`, `E702`, `E703`, `W605`, `E711`, `E712`, `E713`, `E721`, `E722`.

#### Incremental build and test

The [build & test workflow](https://github.com/sagemath/sage/blob/develop/.github/workflows/build.yml) on GitHub Actions builds Sage for the current branch (incrementally on top of the system packages of the develop branch) and runs the test. 

Details are again available by clicking on the badge.

Note that in contrast to the patchbot, the ticket branch is not merged into the current beta version.

#### Documentation build

The [build documentation workflow](https://github.com/sagemath/sage/blob/develop/.github/workflows/doc-build.yml) on GitHub Actions builds the HTML documentation for the current branch. 

If you click on the badge, you get the HTML output of the successful run. The idea is to use this to easily inspect changes to the documentation without the need to locally rebuild the docs yourself. If the doc build fails, you can go to [the Actions tab of sagemath/sagetrac-mirror repo](https://github.com/sagemath/sagetrac-mirror/actions/workflows/doc-build.yml) and choose the particular branch to see what went wrong.

The idea is that these three status badges complement the existing patchbots (and maybe even replace them in the future). In particular, they are supposed to always be green.

#### Test coverage analysis with codecov

A detailed coverage analysis of the Sage library is now available at [codecov.io](https://app.codecov.io/gh/sagemath/sagetrac-mirror). #33355

### sage --pytest

After the optional package [pytest](https://docs.pytest.org/en/7.1.x/) is installed (`./sage -i pytest`), a new command `./sage --pytest` is available, which runs pytest on the Sage library sources. #33572

Also the Sage doctester (`./sage -t` or `./sage -tox -e doctest`) invokes `pytest`. This functionality has been improved in Sage 9.6. #31924, #32975, #33560

### sage -t --baseline-stats-path

#33233

### Sage patchbot on [GitHub](GitHub) Actions

The [Sage patchbot can now be run on GitHub Actions](patchbot#Running_the_patchbot_on_GitHub_Actions),
on top of any of the Linux platforms for which we have prebuilt Docker images.#33253

### New trac.sagemath.org front page

[The front page of trac.sagemath.org](https://trac.sagemath.org/) has been reorganized. #33725

## Availability of Sage 9.6 and installation help

Sage 9.6 was released on 2022-05-15.

**Please read the [updated SageMath installation guide](https://doc.sagemath.org/html/en/installation/index.html)** 

* It now provides a decision tree that guides users and developers to a type of installation suitable for their system and their needs.
* The [section on conda-forge](https://doc.sagemath.org/html/en/installation/conda.html) has been updated and now includes (still experimental) instructions for **Sage development on top of conda-forge**.

### Sources

The Sage source code is available in the [sage git repository](https://github.com/sagemath/sage/tree/develop).

SageMath 9.6 supports all [platforms that were supported by Sage 9.5](https://wiki.sagemath.org/ReleaseTours/sage-9.5#Sources) and **adds support for building on distributions that use the [GCC 12](https://gcc.gnu.org/gcc-12/changes.html) series** (`fedora-36`). #33187

* **Linux 64-bit** (x86_64) - see [CI runs](https://groups.google.com/g/sage-release/c/GOGWk66zaCQ/m/dBQww8WNAAAJ)
  * ubuntu-{[trusty](https://launchpad.net/ubuntu/trusty)⁺,[xenial](https://launchpad.net/ubuntu/xenial),[bionic](https://launchpad.net/ubuntu/bionic),[focal](https://launchpad.net/ubuntu/focal),[hirsute](https://launchpad.net/ubuntu/hirsute),[impish](https://launchpad.net/ubuntu/impish),[jammy](https://launchpad.net/ubuntu/jammy)} 
  * debian-{[stretch](https://wiki.debian.org/DebianStretch), [buster](https://wiki.debian.org/DebianBuster),[bullseye](https://wiki.debian.org/DebianBullseye),[bookworm](https://wiki.debian.org/DebianBookworm),[sid](https://wiki.debian.org/DebianUnstable)}
  * linuxmint-{[17](https://www.linuxmint.com/edition.php?id=158)⁺,[18](https://www.linuxmint.com/edition.php?id=217),[19](https://linuxmint.com/rel_tara_cinnamon.php),[19.3](https://linuxmint.com/rel_tricia_cinnamon.php),[20.1](https://www.linuxmint.com/rel_ulyssa_cinnamon_whatsnew.php),[20.2](https://linuxmint.com/rel_uma_cinnamon.php),[20.3](https://linuxmint.com/rel_una_cinnamon.php)}
  * fedora-{[26](https://docs.fedoraproject.org/en-US/fedora/f26/release-notes/),[27](https://docs.fedoraproject.org/en-US/fedora/f27/release-notes/),[28](https://docs.fedoraproject.org/en-US/fedora/f28/release-notes/),[29](https://docs.fedoraproject.org/en-US/fedora/f29/release-notes/),[30](https://docs.fedoraproject.org/en-US/fedora/f30/release-notes/),[31](https://docs.fedoraproject.org/en-US/fedora/f31/release-notes/),[32](https://docs.fedoraproject.org/en-US/fedora/f32/release-notes/),[33](https://docs.fedoraproject.org/en-US/fedora/f33/release-notes/),[34](https://docs.fedoraproject.org/en-US/fedora/f34/release-notes/),[35](https://docs.fedoraproject.org/en-US/fedora/f35/release-notes/),[36](https://fedoraproject.org/wiki/Releases/36/ChangeSet)}
  * centos-{7⁺,[stream-8](https://www.centos.org/centos-stream/),[stream-9](https://www.centos.org/centos-stream/)}
  * gentoo
  * archlinux
  * opensuse-{15,[15.3](https://doc.opensuse.org/release-notes/x86_64/openSUSE/Leap/15.3/),[tumbleweed](https://get.opensuse.org/tumbleweed/)}
  * slackware-14.2
* **Linux 32-bit** (i386/i686)
  * ubuntu-bionic
  * [manylinux-2_24](https://github.com/pypa/manylinux#manylinux_2_24-debian-9-based)
  * debian-buster
  * centos-7⁺ (but docbuild is broken, #32768)
* **macOS (Intel)** (x86_64) - with [Homebrew](https://brew.sh/) or without
  * macOS 10.15 (Catalina)
  * macOS 11.x (Big Sur)
  * macOS 12.x (Monterey) #32855
* **macOS (Apple Silicon, M1)** #30592
  * Building Sage 9.6 from source on Apple Silicon (M1) requires the use of [Homebrew](https://brew.sh/) (recommended) or conda-forge, which package versions of `gfortran` 11 with necessary changes for this platform that are not in a released upstream version of GCC. (The `gfortran` package that comes with Sage is not suitable for the M1.)
  * Make sure that `/usr/local` does not contain an old copy of homebrew (or other software) for x86_64 that you may have copied from an old machine. Homebrew for the M1 is installed in `/opt/homebrew`, not `/usr/local`.
  * Be sure to follow the [README](https://github.com/sagemath/sage/blob/develop/README.md) and the instructions that the `./configure` command issues regarding the installation of system packages from Homebrew or conda.
* **Cygwin** (x86_64) - see [notes from CI run](https://groups.google.com/g/sage-release/c/GOGWk66zaCQ/m/M_jQiOjaAAAJ)

(On platforms marked with the superscript ⁺, installing optional packages
is not supported in Sage 9.6; and support for these platforms will be removed in Sage 9.7; see #32074. Upgrade to a newer version of the distribution or at least upgrade  the toolchain (gcc, binutils).)

### Availability as binaries

* The easiest way to install Sage 9.6 on Linux is through a distribution that provides it, see [repology.org: sagemath](https://repology.org/project/sagemath/versions).

* [Binary package for 9.6 on macOS](https://github.com/3-manifolds/Sage_macOS/releases) from the 3-manifolds project
  * separate disk images for Intel (x86_64) and Apple Silicon (M1, arm64)
  * also includes many optional Sage packages

* [CoCalc-Docker](https://github.com/sagemathinc/cocalc-docker#readme) from the [CoCalc project](https://cocalc.com)
  * A large image that has Sage, Jupyter, Pluto.jl, VS Code, a web-based X11 server, LaTeX, SageTeX, a new collaborative Whiteboard with Sage code cells
  * But it's big -- 6GB compressed (and 25GB uncompressed) -- so may or may not be of use depending on what you're doing...


### Help

See [README.md](https://github.com/sagemath/sage/blob/9.6/README.md) in the source distribution for installation instructions.

* See [sage-devel](https://groups.google.com/forum/#!forum/sage-devel) for development discussions and [sage-release](https://groups.google.com/forum/#!forum/sage-release) for announcements of beta versions and release candidates.

## More details

* [Trac tickets with milestone 9.6](https://trac.sagemath.org/query?milestone=sage-9.6&groupdesc=1&group=status&max=1500&col=id&col=summary&col=author&col=reviewer&col=time&col=changetime&col=component&col=keywords&order=component)

* [Diff from 9.5](https://github.com/sagemath/sage/compare/9.5...9.6#files_bucket)

* [Changelog for Sage 9.6](https://www.sagemath.org/changelogs/sage-9.6.txt)


---

Attachments:
 * [editor.png](ReleaseTours sage-9.6/editor.png)
 * [ticket_badges.png](ReleaseTours sage-9.6/ticket_badges.png)
 * [gitpod_badge.png](ReleaseTours sage-9.6/gitpod_badge.png)
