[This is the Trac macro *PageOutline* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PageOutline-macro)

# Sage 9.8 Release Tour

Current development cycle (2022)

## Linear algebra

### Submodules of tensor modules with prescribed symmetries

The method `FiniteRankFreeModule.tensor_module` now accepts optional arguments `sym`, `antisym`; if given, a submodule of the tensor module spanned by the tensors with these prescribed symmetries is created. [#30229](https://trac.sagemath.org/ticket/30229)

The new methods `symmetric_power` and `dual_symmetric_power` provide two important special cases. 

### Free module isomorphisms corresponding to fixed standard bases of tensor modules

Standard bases of tensor modules (and of their new submodules) are now explicit objects.  The `basis` method now works for tensor modules, not just the base module, and returns an instance of a new class `TensorFreeSubmoduleBasis_sym`, which represents the standard basis of a tensor module associated with a basis of the base module. [#30229](https://trac.sagemath.org/ticket/30229)

The method [FiniteRankFreeModule.isomorphism_with_fixed_basis](https://doc.sagemath.org/html/en/reference/tensor_free_modules/sage/tensor/modules/finite_rank_free_module.html?highlight=isomorphism_with#sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule.isomorphism_with_fixed_basis) now also works for tensor modules (and their submodules). [#34427](https://trac.sagemath.org/ticket/34427)

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
[#31664](https://trac.sagemath.org/ticket/31664), [#33734](https://trac.sagemath.org/ticket/33734), [#34519](https://trac.sagemath.org/ticket/34519)

In particular:

* The `groebner_basis` method of polynomial ideals now supports using msolve to compute Gröbner bases over prime fields (with some cardinality constraints).
* The `variety` method supports computing real or complex solutions of zero-dimensional polynomial systems over the rational numbers using msolve.

(Some of these features use probabilistic algorithms.)

## Polyhedral geometry

The `Polyhedron` constructor offers a new option `backend='number_field'`. [#34479](https://trac.sagemath.org/ticket/34479)

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

The `Polyhedron` constructor now can also convert from convex polyhedra represented by some other classes. [#14222](https://trac.sagemath.org/ticket/14222)

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

* `CRT_list()` now uses a binary tree instead of folding the input from one side, which can be much faster. [#34512](https://trac.sagemath.org/ticket/34512)

## New packages and package upgrades

The new optional package [msolve](https://github.com/algebraic-solving/msolve) is an open source C library implementing computer algebra algorithms for solving polynomial systems (with rational coefficients or coefficients in a prime field) using Gröbner bases. `msolve` has been initiated in 2019 and is mainly authored by Jérémy Berthomieu, Christian Eder, and Mohab Safey El Din. The optional package provides version 0.4.4 of `msolve`. [#31664](https://trac.sagemath.org/ticket/31664), [#34519](https://trac.sagemath.org/ticket/34519)	

[Normaliz](https://www.normaliz.uni-osnabrueck.de/), the package for computations in affine monoids, vector configurations, lattice polytopes, and rational cones, has been upgraded to version 3.9.4, which brings new algorithms and many improvements ([release notes](https://github.com/Normaliz/Normaliz/releases)). For computations with algebraic polyhedra, Normaliz uses [e-antic](https://github.com/flatsurf/e-antic/), a library for real embedded number fields, which has been upgraded to the 1.x series. The new version of e-antic has been refactored and now depends on [ANTIC](https://github.com/wbhart/antic), an algebraic number theory library. [#31588](https://trac.sagemath.org/ticket/31588)

[TOPCOM](https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM/index.html), the package for computing triangulations of point configurations and oriented matroids, has been upgraded to 1.1.2. [#31531](https://trac.sagemath.org/ticket/31531)

[NumPy](https://numpy.org/) has been updated from 1.22.x to 1.23.3 ([release notes for 1.23](https://numpy.org/devdocs/release/1.23.0-notes.html)). [#34110](https://trac.sagemath.org/ticket/34110)	

[SciPy](https://scipy.org/) has been updated from 1.8.1 to 1.9.2 ([release notes for 1.9](https://scipy.github.io/devdocs/release.1.9.0.html)). [#34081](https://trac.sagemath.org/ticket/34081)

Update sympy to 1.11.1, [#34118](https://trac.sagemath.org/ticket/34118)

Update igraph, python_igraph to 0.10.x. [#34491](https://trac.sagemath.org/ticket/34491), [#34498](https://trac.sagemath.org/ticket/34498), [#34680](https://trac.sagemath.org/ticket/34680)

The `rpy2` package has been upgraded to version 3.4.5. It provides an interface to a suitable system installation of [R](https://www.r-project.org/), versions 3.5 or newer. Sage 9.8 no longer offers a package for installing R itself from source. [#34268](https://trac.sagemath.org/ticket/34268)

Python has been upgraded to 3.10.8; Sage continues to support system Python 3.8.x, 3.9.x, 3.10.x. [#34271](https://trac.sagemath.org/ticket/34271)

`Sphinx` has been upgraded from 4.4.x to 5.2.3. [#34615](https://trac.sagemath.org/ticket/34615)

For a list of all packages and their versions, see
 * https://repology.org/projects/?inrepo=sagemath_develop


## New tools for developers

### `tox -e docker-...-incremental`

This does an incremental build of Sage on top of a prebuilt image published at ghcr.io (​https://github.com/orgs/sagemath/packages?tab=packages). [#34228](https://trac.sagemath.org/ticket/34228)

For example:
```
$ tox -e docker-fedora-31-standard-incremental
```

### `./configure --enable-wheels`

This new option ensures that `venv/var/lib/sage/wheels/` contains up-to-date wheels for all Python packages, including *sagemath-standard* (the Sage library). [#32874](https://trac.sagemath.org/ticket/32874)

The option can be used with or without `--disable-editable`, so there are now 4 modes of installation:

- `./configure` (or `./configure --enable-editable --disable-wheels`): The Sage library (sagemath-standard) and other [distribution packages whose source trees are part of the Sage monorepo](https://github.com/sagemath/sage/tree/develop/pkgs) (sage-conf, sage-docbuild, sage-setup, sage-sws2rst) are installed in [editable mode](https://wiki.sagemath.org/ReleaseTours/sage-9.3#Editable_.28.22in-place.22.2C_.22develop.22.29_installs_of_the_Sage_library). Changes to Python source files take immediate effect after restarting Sage. Running `sage -b` or `make build` is only necessary if you make changes (or switch to a branch that makes changes) to Cython sources or external packages. No wheels are available for these distributions; to build wheels once, use `make wheels`.

- `./configure --enable-wheels`: When running `sage -b` or `make build`, in addition to updating the editable install, Sage also builds/updates wheels for sagemath-standard and the other distribution packages whose source trees are part of the Sage monorepo.

- `./configure --disable-editable`: Sage installs sagemath-standard using the legacy `setup.py install` command. For any source changes to take effect, use `sage -b` or `make build`. No wheel is available; to build a wheel once, use `make wheels`.

- `./configure --disable-editable --enable-wheels`: Sage builds a wheel for sagemath-standard and installs the wheel. 


### `make -j list-broken-packages`

When Sage is installed from source, it will make use of various system packages; in particular, it will link to shared libraries provided by the system. Indiscriminate upgrades of system packages can break a Sage installation.

This can always be fixed by a full rebuild (`make distclean && make build`), but this time-consuming step can often be avoided by just reinstalling a few packages. The new command `make -j list-broken-packages` assists with this. [#34203](https://trac.sagemath.org/ticket/34203)
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

Sage 9.8 now requires GCC >= 8 (or a recent version of clang). This enables upgrades of various packages to versions that require C++17 language or library features. Developers can now also use C++17 features in the Sage library (this requires use of the directive `# distutils: extra_compile_args = -std=c++17`). [#34266](https://trac.sagemath.org/ticket/34266)

Users of older Linux distributions (in particular, `ubuntu-xenial`
or older, `debian-stretch` or older, `linuxmint-18` or older, `fedora-28` or older)
should upgrade their systems before attempting to install Sage from
source.  

Users of `ubuntu-bionic`, `linuxmint-19.x`, and
`opensuse-15.x` can install a versioned `gcc` system package
and then use `./configure CC=gcc-8 CXX=g++-8 FC=gfortran-8`
or similar. See [SAGE_ROOT/build/pkgs/](https://github.com/sagemath/sage/tree/develop/build/pkgs)_gcc8, _gcc9, ... for  distribution-specific information.

Users on `ubuntu` can also install a modern compiler
toolchain [using the ubuntu-toolchain-r ppa](https://askubuntu.com/questions/1140183/install-gcc-9-on-ubuntu-18-04/1149383[#11493](https://trac.sagemath.org/ticket/11493)83).
On `ubuntu-trusty`, also the package `binutils-2.26` is required;
after installing it, make it available using `export PATH="/usr/lib/binutils-2.26/bin:$PATH"`.  

Instead of upgrading their distribution, users of `centos-7` or RHEL can install a modern compiler
toolchain [using Redhat's devtoolset](https://stackoverflow.com/a/67212990/557937).

On other old distributions, if an upgrade to a newer distribution is not possible, users can try to use `./configure --without-system-gcc`. Then Sage will attempt to build its own copy of GCC using the available system GCC. We no longer test such system configurations, so this may or may not work.

### Native support for Apple Silicon (M1/M2)

Sage 9.8 ships a copy of GCC 12.x with Apple Silicon support, so it can now be built from source on macOS systems without Homebrew. [#33816](https://trac.sagemath.org/ticket/33816)


## Availability of Sage 9.8 and installation help

The first development release, 9.8.beta0, was tagged on 2022-09-25. The current development release is 9.8.beta4, tagged on 2022-11-21.

### Sources

The Sage source code is available in the [sage git repository](https://github.com/sagemath/sage/tree/develop).

## More details

 * [Trac tickets with milestone 9.8](https://trac.sagemath.org/query?milestone=sage-9.8&groupdesc=1&group=status&max=1500&col=id&col=summary&col=author&col=reviewer&col=time&col=changetime&col=component&col=keywords&order=component)

 * [Diff from 9.7](https://github.com/sagemath/sage/compare/9.7...develop#files_bucket)

