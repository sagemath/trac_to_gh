# Sage 9.8 Release Tour

Current development cycle (2022–2023)

## Linear algebra

### Submodules of tensor modules with prescribed symmetries

The method `FiniteRankFreeModule.tensor_module` now accepts optional arguments `sym`, `antisym`; if given, a submodule of the tensor module spanned by the tensors with these prescribed symmetries is created. #30229

The new methods `symmetric_power` and `dual_symmetric_power` provide two important special cases. 

### Free module isomorphisms corresponding to fixed standard bases of tensor modules

Standard bases of tensor modules (and of their new submodules) are now explicit objects.  The `basis` method now works for tensor modules, not just the base module, and returns an instance of a new class `TensorFreeSubmoduleBasis_sym`, which represents the standard basis of a tensor module associated with a basis of the base module. #30229

The method [FiniteRankFreeModule.isomorphism_with_fixed_basis](https://doc.sagemath.org/html/en/reference/tensor_free_modules/sage/tensor/modules/finite_rank_free_module.html?highlight=isomorphism_with#sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule.isomorphism_with_fixed_basis) now also works for tensor modules (and their submodules). #34427

For example, we can now send (1,1)-tensors to matrices:

```
sage: V = FiniteRankFreeModule(QQ, 3, start_index=1); V
3-dimensional vector space over the Rational Field
sage: basis = e = V.basis("e"); basis
Basis (e_1,e_2,e_3) on the 3-dimensional vector space over the Rational Field
sage: T11 = V.tensor_module(1, 1); T11
Free module of type-(1,1) tensors on the 3-dimensional vector space over the Rational Field
sage: e_T11 = T11.basis("e"); e_T11
Standard basis on the
 Free module of type-(1,1) tensors on the 3-dimensional vector space over the Rational Field
 induced by Basis (e_1,e_2,e_3) on the 3-dimensional vector space over the Rational Field
sage: W = MatrixSpace(QQ, 3)
sage: phi_e_T11 = T11.isomorphism_with_fixed_basis(e_T11, codomain=W); phi_e_T11
Generic morphism:
From: Free module of type-(1,1) tensors on the 3-dimensional vector space over the Rational Field
To:   Full MatrixSpace of 3 by 3 dense matrices over Rational Field
sage: t = T11.an_element(); t.display()
1/2 e_1⊗e^1
sage: phi_e_T11(t)
[1/2   0   0]
[  0   0   0]
[  0   0   0]
```
Or we can send symmetric bilinear forms to matrices:

```
sage: V = FiniteRankFreeModule(QQ, 3, start_index=1); V
3-dimensional vector space over the Rational Field
sage: basis = e = V.basis("e"); basis
Basis (e_1,e_2,e_3) on the 3-dimensional vector space over the Rational Field
sage: T02 = V.tensor_module(0, 2); T02
Free module of type-(0,2) tensors on the 3-dimensional vector space over the Rational Field
sage: e_T02 = T02.basis("e"); e_T02
Standard basis on the
 Free module of type-(0,2) tensors on the 3-dimensional vector space over the Rational Field
 induced by Basis (e_1,e_2,e_3) on the 3-dimensional vector space over the Rational Field
sage: W = MatrixSpace(QQ, 3)
sage: phi_e_T02 = T02.isomorphism_with_fixed_basis(e_T02, codomain=W); phi_e_T02
Generic morphism:
From: Free module of type-(0,2) tensors on the 3-dimensional vector space over the Rational Field
To:   Full MatrixSpace of 3 by 3 dense matrices over Rational Field

sage: a = V.sym_bilinear_form()
sage: a[1,1], a[1,2], a[1,3] = 1, 2, 3
sage: a[2,2], a[2,3] = 4, 5
sage: a[3,3] = 6
sage: a.display()
e^1⊗e^1 + 2 e^1⊗e^2 + 3 e^1⊗e^3 + 2 e^2⊗e^1 + 4 e^2⊗e^2 + 5 e^2⊗e^3 + 3 e^3⊗e^1 + 5 e^3⊗e^2 + 6 e^3⊗e^3
sage: phi_e_T02(a)
[1 2 3]
[2 4 5]
[3 5 6]
```

## Commutative algebra

### Solving polynomial systems using msolve

A new interface to the [msolve](https://msolve.lip6.fr/) library (now available as an optional package) provides efficient tools for solving large polynomial systems.
#31664, #33734, #34519

In particular:

* The `groebner_basis` method of polynomial ideals now supports using msolve to compute Gröbner bases over prime fields (with some cardinality constraints).
* The `variety` method supports computing real or complex solutions of zero-dimensional polynomial systems over the rational numbers using msolve.

(Some of these features use probabilistic algorithms.)

### Lazy power series ring

The lazy power series ring has now been replaced by what was previously known as the lazy Taylor series ring. #32367
This now supports multiple variables with many other features that are also available for lazy Laurent series.

```
sage: R.<a,b,c,d> = LazyPowerSeriesRing(QQ)
sage: (1 - c + d) / (1 + a*b)
1 + (-c+d) + (-a*b) + (a*b*c-a*b*d) + a^2*b^2 + (-a^2*b^2*c+a^2*b^2*d) + (-a^3*b^3) + O(a,b,c,d)^7
sage: exp(a + b/(1 - c))
1 + (a+b) + (1/2*a^2+a*b+1/2*b^2+b*c) + (1/6*a^3+1/2*a^2*b+1/2*a*b^2+1/6*b^3+a*b*c+b^2*c+b*c^2) + ... + O(a,b,c,d)^7
sage: U = R.undefined()
sage: U.define(a + b * U + c*U^2)
sage: U
a + a*b + (a*b^2+a^2*c) + (a*b^3+3*a^2*b*c) + (a*b^4+6*a^2*b^2*c+2*a^3*c^2) + (a*b^5+10*a^2*b^3*c+10*a^3*b*c^2) + O(a,b,c,d)^7
sage: U(d,d,d,d)
d + d^2 + 2*d^3 + 4*d^4 + 9*d^5 + 21*d^6 + O(a,b,c,d)^7
sage: [c.lc() for c in U(d,d,d,d)[:15]]  # The Motzkin numbers
[1, 1, 2, 4, 9, 21, 51, 127, 323, 835, 2188, 5798, 15511, 41835]
```
The ability to compute a (infinite) q-Pochhammer `(z; q)_{\infty}` has been added: #34381

```
sage: q = ZZ['q'].fraction_field().gen()
sage: P.<x,y> = LazyPowerSeriesRing(q.parent())
sage: x.q_pochhammer(q)
1 + ((-1/(-q+1))*x) + ((q/(q^3-q^2-q+1))*x^2) + ((-q^3/(-q^6+q^5+q^4-q^2-q+1))*x^3) + ... + O(x,y)^7
sage: (x+y).q_pochhammer(q)
1 + ((-1/(-q+1))*x+(-1/(-q+1))*y) + ((q/(q^3-q^2-q+1))*x^2+(2*q/(q^3-q^2-q+1))*x*y+(q/(q^3-q^2-q+1))*y^2) + ... + O(x,y)^7

sage: L.<z> = LazyLaurentSeriesRing(q.parent())
sage: L.q_pochhammer(q)
1 + (-1/(-q + 1))*z + (q/(q^3 - q^2 - q + 1))*z^2 + (-q^3/(-q^6 + q^5 + q^4 - q^2 - q + 1))*z^3 + ... + O(z^7)
sage: L.q_pochhammer(q) / (z*q^3).q_pochhammer(q)
1 + (-q^2 - q - 1)*z + (q^3 + q^2 + q)*z^2 - q^3*z^3 + O(z^7)
```
Taking powers in the lazy series rings is now (much) faster. ##34350

### Free resolution

Free resolutions of modules over polynomial rings are directly accessible from the module. #34379

```
sage: S.<x,y,z,w> = PolynomialRing(QQ)
sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
sage: from sage.homology.free_resolution import FreeResolution
sage: FreeResolution(I)
S^1 <-- S^3 <-- S^2 <-- 0
sage: FreeResolution(I, graded=True)
S(0) <-- S(-2)⊕S(-2)⊕S(-2) <-- S(-3)⊕S(-3) <-- 0
sage: I.free_resolution()
S^1 <-- S^3 <-- S^2 <-- 0
sage: I.graded_free_resolution()
S(0) <-- S(-2)⊕S(-2)⊕S(-2) <-- S(-3)⊕S(-3) <-- 0
```

### Miscellaneous

* Tensor products of commutative algebras now know they are commutative. #34453

## Algebra

* Fixed a multiplication bug in the exterior algebra. #34707
* We can construct the ring of `q`-commuting polynomials: #34412

```
sage: q = ZZ['q'].fraction_field().gen()
sage: R.<x,y> = algebras.qCommutingPolynomials(q)
sage: x * y
x*y
sage: y * x
q*x*y
sage: f = (x + y)^10
sage: all(f[b] == q_binomial(10, b.list()[0]) for b in f.support())  # the q-binomial theorem
True
```
These can also be constructed with respect to any skew-symmetric matrix:

```
sage: B = matrix([[0,1,2],[-1,0,3],[-2,-3,0]])
sage: B
[ 0  1  2]
[-1  0  3]
[-2 -3  0]
sage: q = ZZ['q'].gen()
sage: R.<x,y,z> = algebras.qCommutingPolynomials(q, B)
sage: y * x
q*x*y
sage: z * x
q^2*x*z
sage: z * y
q^3*y*z
```

* All tensor products of modules now must implement a `tensor_factors()` method. #34393
* Minimal polynomials are now computed using NTL's `MinPolyMod()` in important special cases. #34906
* All finite fields now implement `.to_integer()` and `.from_integer()` methods, generalizing the (now deprecated) `.fetch_int()` and `.integer_representation()` methods. #33941
* `BinaryQF` and `QuadraticForm` objects can now be initialized from a polynomial. #34863
* A generic `ProductTree` class is now available in `sage.rings.generic`. #34791

## Combinatorics

More constructions of Hadamard matrices, general and skew, were added. #34807

Sage now is able to construct a Hadamard matrix for all orders 4n < 668.
(668 is the first order for which the existence of a Hadamard matrix is open.)

A similar effort for skew Hadamard matrices is underway. #34848


## Polyhedral geometry

The `Polyhedron` constructor offers a new option `backend='number_field'`. #34479

It accepts any input data that Sage can convert to a common real embedded algebraic number field.
The new backend uses this embedded number field internally for the polyhedral representation conversion,
but the results are converted back to the (common) base ring of the input.

```
sage: polytopes.icosahedron(exact=True, backend='number_field')
A 3-dimensional polyhedron
 in (Number Field in sqrt5 with defining polynomial x^2 - 5
     with sqrt5 = 2.236067977499790?)^3
 defined as the convex hull of 12 vertices

sage: x = polygen(ZZ); P = Polyhedron(
....:     vertices=[[sqrt(2)], [AA.polynomial_root(x^3-2, RIF(0,3))]],
....:     backend='number_field')
sage: P
A 1-dimensional polyhedron
 in (Symbolic Ring)^1 defined as the convex hull of 2 vertices
sage: P.vertices()
(A vertex at (sqrt(2)), A vertex at (2^(1/3)))
```
The same was previously only possible with `backend='normaliz'`. The new backend does not require the installation of an optional package; but note that `backend='normaliz'` is much faster than `backend='number_field'`.

The `Polyhedron` constructor now can also convert from convex polyhedra represented by some other classes. #14222

For example:

```
sage: quadrant = Cone([(1,0), (0,1)])
sage: Polyhedron(quadrant)
A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 rays
sage: Polyhedron(quadrant, base_ring=QQ)
A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex and 2 rays

sage: H.<x,y> = HyperplaneArrangements(QQ)
sage: h = x + y - 1; h
Hyperplane x + y - 1
sage: Polyhedron(h, base_ring=ZZ)
A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
sage: Polyhedron(h)
A 1-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex and 1 line
```


## Number theory

* `CRT_list()` now uses a binary tree instead of folding the input from one side, which can be much faster. #34512

## Elliptic curves

* Frobenius isogenies (in particular, endomorphisms) are now available as `EllipticCurveHom` objects. #33915
* Scalar multiplications are now available as `EllipticCurveHom` objects. #32826
* Isomorphisms are now sorted in such a way that identity and negation morphisms come first. #34728
* The extent of copying cached orders through isogenies has been extended. #34732

## New packages and package upgrades

### SCIP Optimization Suite 8.0

[SCIP](https://www.scipopt.org/), one of the fastest non-commercial solvers for mixed integer programming (MIP) and mixed integer nonlinear programming (MINLP), was relicensed from a non-free academic license to a permissive open source license (Apache 2.0) on the occasion of the [20th anniversary](https://www.scipopt.org/20years/) of the SCIP project in December 2022.

Sage now provides up-to-date packages from the SCIP Optimization Suite: 
- [SoPlex](https://soplex.zib.de/) 6.0.x, a high performance LP solver using the revised simplex method, with special support for computing high-precision solutions and for the exact solution of LPs with rational input data. #34742
- [SCIP](https://github.com/scipopt/scip) 8.0.x, the mixed integer (linear and nonlinear) programming solver and constraint programming framework. #31329
- [PaPILO](https://github.com/scipopt/papilo), providing parallel presolve routines for (mixed integer) linear programming problems, including support for exact rational arithmetic. #34726
In addition, Sage provides:
- [SCIP-SDP](http://www.opt.tu-darmstadt.de/scipsdp/), an extension of SCIP for solving mixed integer semidefinite programs. A new optional package provides the SDP solver [DSDP](http://www.mcs.anl.gov/hs/software/DSDP/). #34749
- [https://github.com/scipopt/PySCIPOpt](https://github.com/scipopt/PySCIPOpt), a Cython interface to the SCIP library. #21003

A new `MixedIntegerLinearProgram` backend using PySCIPOpt provides access to the solver. Use the keyword argument `solver="SCIP"`. This keyword argument can also be passed to various methods that use `MixedIntegerLinearProgram` internally.

```
sage: g = graphs.PetersenGraph()
sage: g.pathwidth(solver='SCIP')
5
```

### msolve: polynomial system solver

The new optional package [msolve](https://github.com/algebraic-solving/msolve) is an open source C library implementing computer algebra algorithms for solving polynomial systems (with rational coefficients or coefficients in a prime field) using Gröbner bases. `msolve` has been initiated in 2019 and is mainly authored by Jérémy Berthomieu, Christian Eder, and Mohab Safey El Din. The optional package provides version 0.4.4 of `msolve`. #31664, #34519	

### Kissat SAT Solver

The new optional package [kissat](http://fmv.jku.at/kissat/) provides an additional SAT solver. #34909, #34911

### Python 3.11

Python has been upgraded to 3.11.1. The Python 3.11 series brings [many improvements](https://docs.python.org/3/whatsnew/3.11.html), including [fine-grained error locations in tracebacks](https://docs.python.org/3/whatsnew/3.11.html#pep-657-fine-grained-error-locations-in-tracebacks) and major speed improvements over Python 3.10. Sage continues to support system Python 3.8.x, 3.9.x, 3.10.x, and now also supports system Python 3.11.x.  #34271, #33842

### Other package upgrades

PARI has been upgraded to version 2.15.2. #34537

[Normaliz](https://www.normaliz.uni-osnabrueck.de/), the package for computations in affine monoids, vector configurations, lattice polytopes, and rational cones, has been upgraded to version 3.9.4, which brings new algorithms and many improvements ([release notes](https://github.com/Normaliz/Normaliz/releases)). For computations with algebraic polyhedra, Normaliz uses [e-antic](https://github.com/flatsurf/e-antic/), a library for real embedded number fields, which has been upgraded to the 1.x series. The new version of e-antic has been refactored and now depends on [ANTIC](https://github.com/wbhart/antic), an algebraic number theory library. #31588

[TOPCOM](https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM/index.html), the package for computing triangulations of point configurations and oriented matroids, has been upgraded to 1.1.2. #31531

[NumPy](https://numpy.org/) has been updated from 1.22.x to 1.23.5 ([release notes for 1.23](https://numpy.org/devdocs/release/1.23.0-notes.html)). #34110, #34658	

[SciPy](https://scipy.org/) has been updated from 1.8.1 to 1.9.3 ([release notes for 1.9](https://scipy.github.io/devdocs/release.1.9.0.html)). #34081, #34658

[SymPy](https://www.sympy.org/en/index.html) has been updated to 1.11.1 ([release notes for 1.11](https://github.com/sympy/sympy/wiki/release-notes-for-1.11)). #34118

Updated igraph, python_igraph to 0.10.x. #34491, #34498, #34680

Matplotlib has been updated to 3.6. #34796

The `rpy2` package has been upgraded to version 3.4.5. It provides an interface to a suitable system installation of [R](https://www.r-project.org/), versions 3.5 or newer. Sage 9.8 no longer offers a package for installing R itself from source. #34268

`Sphinx` has been upgraded from 4.4.x to 5.2.3. #34615

For a list of all packages and their versions, see
* https://repology.org/projects/?inrepo=sagemath_develop


## New tools for developers

### `tox -e docker-...-incremental`

This does an incremental build of Sage on top of a prebuilt image published at ghcr.io (​https://github.com/orgs/sagemath/packages?tab=packages). #34228

For example:

```
$ tox -e docker-fedora-31-standard-incremental
```

### `./configure --enable-wheels`

This new option ensures that `venv/var/lib/sage/wheels/` contains up-to-date wheels for all Python packages, including **sagemath-standard** (the Sage library). #32874

The option can be used with or without `--disable-editable`, so there are now 4 modes of installation:

- `./configure` (or `./configure --enable-editable --disable-wheels`): The Sage library (sagemath-standard) and other [distribution packages whose source trees are part of the Sage monorepo](https://github.com/sagemath/sage/tree/develop/pkgs) (sage-conf, sage-docbuild, sage-setup, sage-sws2rst) are installed in [editable mode](https://wiki.sagemath.org/ReleaseTours/sage-9.3#Editable_.28.22in-place.22.2C_.22develop.22.29_installs_of_the_Sage_library). Changes to Python source files take immediate effect after restarting Sage. Running `sage -b` or `make build` is only necessary if you make changes (or switch to a branch that makes changes) to Cython sources or external packages. No wheels are available for these distributions; to build wheels once, use `make wheels`.

- `./configure --enable-wheels`: When running `sage -b` or `make build`, in addition to updating the editable install, Sage also builds/updates wheels for sagemath-standard and the other distribution packages whose source trees are part of the Sage monorepo.

- `./configure --disable-editable`: Sage installs sagemath-standard using the legacy `setup.py install` command. For any source changes to take effect, use `sage -b` or `make build`. No wheel is available; to build a wheel once, use `make wheels`.

- `./configure --disable-editable --enable-wheels`: Sage builds a wheel for sagemath-standard and installs the wheel. 

### `make -j list-broken-packages`

When Sage is installed from source, it will make use of various system packages; in particular, it will link to shared libraries provided by the system. Indiscriminate upgrades of system packages can break a Sage installation.

This can always be fixed by a full rebuild (`make distclean && make build`), but this time-consuming step can often be avoided by just reinstalling a few packages. The new command `make -j list-broken-packages` assists with this. #34203

```
$ make -j list-broken-packages
make --no-print-directory auditwheel_or_delocate-no-deps
...
# Checking .../local/var/lib/sage/installed/bliss-0.73+debian-1+sage-2016-08-02.p0
...
Checking shared library file '.../local/lib/libumfpack.dylib'
Checking shared library file '.../local/var/tmp/sage/build/suitesparse-5.10.1/src/lib/libsliplu.1.0.2.dylib'
Error during installcheck of 'suitesparse': .../local/var/tmp/sage/build/suitesparse-5.10.1/src/lib/libsliplu.1.0.2.dylib
...
Uninstall broken packages by typing:

    make lcalc-SAGE_LOCAL-uninstall;
    make ratpoints-SAGE_LOCAL-uninstall;
    make r-SAGE_LOCAL-uninstall;
    make suitesparse-SAGE_LOCAL-uninstall;

real	2m25.787s
user	4m54.270s
sys	4m0.796s
```

## Configuration changes

### Support for GCC < 8 dropped; C++17 features now available

Sage 9.8 now requires GCC >= 8 (or a recent version of clang). This enables upgrades of various packages to versions that require C++17 language or library features. Developers can now also use C++17 features in the Sage library (this requires use of the directive `# distutils: extra_compile_args = -std=c++17`). #34266

Users of older Linux distributions (in particular, `ubuntu-xenial`
or older, `debian-stretch` or older, `linuxmint-18` or older, `fedora-28` or older)
should upgrade their systems before attempting to install Sage from
source.  

Users of `ubuntu-bionic`, `linuxmint-19.x`, and
`opensuse-15.x` can install a versioned `gcc` system package
and then use `./configure CC=gcc-8 CXX=g++-8 FC=gfortran-8`
or similar. See [SAGE_ROOT/build/pkgs/](https://github.com/sagemath/sage/tree/develop/build/pkgs)_gcc8, _gcc9, ... for  distribution-specific information.

Users on `ubuntu` can also install a modern compiler
toolchain [using the ubuntu-toolchain-r ppa](https://askubuntu.com/questions/1140183/install-gcc-9-on-ubuntu-18-04/1149383#1149383).
On `ubuntu-trusty`, also the package `binutils-2.26` is required;
after installing it, make it available using `export PATH="/usr/lib/binutils-2.26/bin:$PATH"`.  

Instead of upgrading their distribution, users of `centos-7` or RHEL can install a modern compiler
toolchain [using Redhat's devtoolset](https://stackoverflow.com/a/67212990/557937).

On other old distributions, if an upgrade to a newer distribution is not possible, users can try to use `./configure --without-system-gcc`. Then Sage will attempt to build its own copy of GCC using the available system GCC. We no longer test such system configurations, so this may or may not work.

### Native support for Apple Silicon (M1/M2)

Sage 9.8 ships a copy of GCC 12.x with Apple Silicon support, so it can now be built from source on macOS systems without Homebrew. #33816


## Availability of Sage 9.8 and installation help

The first development release, 9.8.beta0, was tagged on 2022-09-25. The first release candidate, 9.8.rc0, was tagged on 2023-01-29.

### Sources

The Sage source code is available in the [sage git repository](https://github.com/sagemath/sage/tree/develop).

Sage builds successfully on the following platforms:
* **Linux 64-bit** (x86_64)
  * ubuntu-{[trusty](https://launchpad.net/ubuntu/trusty)-toolchain-gcc_9,[xenial](https://launchpad.net/ubuntu/xenial)-toolchain-gcc_9,[bionic](https://launchpad.net/ubuntu/bionic)-gcc_8-python3.8,[focal](https://launchpad.net/ubuntu/focal),[jammy](https://launchpad.net/ubuntu/jammy), [kinetic](https://launchpad.net/ubuntu/kinetic)} 
  * debian-{[buster](https://wiki.debian.org/DebianBuster),[bullseye](https://wiki.debian.org/DebianBullseye),[bookworm](https://wiki.debian.org/DebianBookworm),[sid](https://wiki.debian.org/DebianUnstable)}
  * linuxmint-{[19](https://linuxmint.com/rel_tara_cinnamon.php)-gcc_8-python3.8,[19.3](https://linuxmint.com/rel_tricia_cinnamon.php)-gcc_8-python3.8,[20.1](https://www.linuxmint.com/rel_ulyssa_cinnamon_whatsnew.php),[20.2](https://linuxmint.com/rel_uma_cinnamon.php),[20.3](https://linuxmint.com/rel_una_cinnamon.php),[21](https://linuxmint.com/rel_vanessa_cinnamon.php)}
  * fedora-{[29](https://docs.fedoraproject.org/en-US/fedora/f29/release-notes/),[30](https://docs.fedoraproject.org/en-US/fedora/f30/release-notes/),[31](https://docs.fedoraproject.org/en-US/fedora/f31/release-notes/),[32](https://docs.fedoraproject.org/en-US/fedora/f32/release-notes/),[33](https://docs.fedoraproject.org/en-US/fedora/f33/release-notes/),[34](https://docs.fedoraproject.org/en-US/fedora/f34/release-notes/),[35](https://docs.fedoraproject.org/en-US/fedora/f35/release-notes/),[36](https://docs.fedoraproject.org/en-US/fedora/f36/release-notes/),[37](https://fedoraproject.org/wiki/Releases/37/ChangeSet)}
  * centos-{7-devtoolset-gcc_11,[stream-8](https://www.centos.org/centos-stream/)-python3.9,[stream-9](https://www.centos.org/centos-stream/)-python3.9}
  * gentoo
  * archlinux
  * opensuse-{[15.3](https://doc.opensuse.org/release-notes/x86_64/openSUSE/Leap/15.3/),[15.4](https://doc.opensuse.org/release-notes/x86_64/openSUSE/Leap/15.4/),[tumbleweed](https://get.opensuse.org/tumbleweed/)}
  * conda-forge
* **Linux 32-bit** (i386/i686)
  * ubuntu-bionic-gcc_8
  * debian-buster
* **macOS (Intel)** (x86_64) - with [Homebrew](https://brew.sh/) or without
  * macOS 11.x (Big Sur)
  * macOS 12.x (Monterey)
  * macOS 13.x (Ventura)
* **macOS (Apple Silicon, M1/M2)**  - with [Homebrew](https://brew.sh/) or without
  * Make sure that `/usr/local` does not contain an old copy of homebrew (or other software) for x86_64 that you may have copied from an old machine. Homebrew for the M1/M2 is installed in `/opt/homebrew`, not `/usr/local`.
  * Be sure to follow the [README](https://github.com/sagemath/sage/blob/develop/README.md) and the instructions that the `./configure` command issues regarding the installation of system packages from Homebrew or conda.

You can also [build Sage on top of conda-forge](https://doc.sagemath.org/html/en/installation/conda.html) on Linux and macOS.

**Known issues and workarounds:**

* If your system [singular](https://doc.sagemath.org/html/en/reference/spkg/singular.html#spkg-singular) package is very new (>= 4.3.1p3), then sagelib will fail to build. Workaround: Use `./configure --without-system-singular`. #34851

**Sage 9.8 does not support Cygwin; use Windows Subsystem for Linux instead.** 
Because of unresolved problems with standard packages GIAC (#34269), ECL (#34127), Maxima (#30796), and the rebasing facility (#34223), Sage 9.8 does not support Cygwin. Users on Windows 10 and 11 can migrate to using [WSL as described in our installation guide](https://doc.sagemath.org/html/en/installation//index.html#windows). A convenient way to use such an installation of Sage is via VS Code's WSL remote. #34301, #30484


## More details

* [Trac tickets with milestone 9.8](https://trac.sagemath.org/query?milestone=sage-9.8&groupdesc=1&group=status&max=1500&col=id&col=summary&col=author&col=reviewer&col=time&col=changetime&col=component&col=keywords&order=component)

* [Diff from 9.7](https://github.com/sagemath/sage/compare/9.7...develop#files_bucket)


