[This is the Trac macro *PageOutline* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PageOutline-macro)

# Sage 9.7 Release Tour

Sage 9.7 was released on September 19, 2022.

A total of 92 people were involved as authors or reviewers of code contributions to Sage 9.7.

Here is an overview of some of the main changes in this version.

## Documentation

Sage comes with comprehensive documentation in HTML and PDF formats.

In Sage 9.7, the [HTML documentation](https://doc.sagemath.org/html/en/reference/index.html) has been updated to use the Furo theme, which uses a responsive design and offers a choice between dark mode, light mode, and a high-contrast mode. [#33601](https://trac.sagemath.org/ticket/33601), [#33833](https://trac.sagemath.org/ticket/33833), [#34092](https://trac.sagemath.org/ticket/34092), [#34252](https://trac.sagemath.org/ticket/34252), [#34262](https://trac.sagemath.org/ticket/34262), [#34265](https://trac.sagemath.org/ticket/34265), [#34267](https://trac.sagemath.org/ticket/34267), [#34450](https://trac.sagemath.org/ticket/34450)

## Basic arithmetic

* Sage's `Integer` has a new `.bit_length()` method (to increase compatibility with Python's `int`). [#33676](https://trac.sagemath.org/ticket/33676)
* The `divmod()` function now also works for rings which implement `%` despite not being marked as Euclidean. [#33704](https://trac.sagemath.org/ticket/33704)
* Finite-field elements now support indexing (and iteration) to access the coefficients of the representing polynomial. [#33748](https://trac.sagemath.org/ticket/33748)
* The three-argument form of `pow()` now returns an integer rather than an `IntegerMod`. [#34143](https://trac.sagemath.org/ticket/34143)

## Combinatorics

* Permutations now enjoy a much faster algorithm to compute the `longest_increasing_subsequences` as well as a new function that only count them `longest_increasing_subsequence_number`. [#31451](https://trac.sagemath.org/ticket/31451), [#34218](https://trac.sagemath.org/ticket/34218), [#34214](https://trac.sagemath.org/ticket/34214)
* Cartesian products of infinite enumerated sets now have a working iterator. [#34374](https://trac.sagemath.org/ticket/34374)
* `ImageSet`s can now be equipped with an inverse function for the purpose of membership testing. [#34377](https://trac.sagemath.org/ticket/34377)

## Polyhedral geometry

[Triangulation](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/triangulation/element.html#sage.geometry.triangulation.element.Triangulation)s of point configurations (and thus of polyhedra and cones) are now linked to geometric polyhedral complexes. The new methods [Triangulation.polyhedral_complex](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/triangulation/element.html#sage.geometry.triangulation.element.Triangulation.polyhedral_complex) and [boundary_polyhedral_complex](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/triangulation/element.html#sage.geometry.triangulation.element.Triangulation.boundary_polyhedral_complex) return a `PolyhedralComplex`. Also, `Triangulation` provides a new method [boundary_simplicial_complex](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/triangulation/element.html#sage.geometry.triangulation.element.Triangulation.boundary_simplicial_complex), which returns an abstract `SimplicialComplex`. [#33586](https://trac.sagemath.org/ticket/33586)

Abstract `SimplicialComplex`es now provide a method `is_subcomplex`, which was previously only available for `PolyhedralComplex`es. [#34294](https://trac.sagemath.org/ticket/34294)

The new option [PolyhedralComplex.plot](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/polyhedral_complex.html#sage.geometry.polyhedral_complex.PolyhedralComplex.plot)`(explosion_factor=1)` plots a 2-dimensional or 3-dimensional polyhedral complex, setting its cells apart proportionally to their distance from a center point. There is also a new option `color="rainbow"`, which assigns a different color to every maximal cell. [#33596](https://trac.sagemath.org/ticket/33596)

The method [affine_hull_projection](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/polyhedron/base6.html#sage.geometry.polyhedron.base6.Polyhedron_base6.affine_hull_projection) is now available also for unbounded polyhedra, not only polytopes. [#34326](https://trac.sagemath.org/ticket/34326)	

[RealSet](https://doc.sagemath.org/html/en/reference/sets/sage/sets/real_set.html?highlight=realset#sage.sets.real_set.RealSet)s (finite unions of intervals) now have faster `intersection`, `difference`, `symmetric_difference` and `are_pairwise_disjoint` methods. [#32181](https://trac.sagemath.org/ticket/32181)

## Number theory

* Square roots modulo powers of two are now computed in polynomial time. [#33961](https://trac.sagemath.org/ticket/33961)
* Definite binary quadratic forms can now be reduced including transformation matrix. [#34229](https://trac.sagemath.org/ticket/34229)
* Factoring polynomials modulo prime powers is now supported. [#34371](https://trac.sagemath.org/ticket/34371)

## Elliptic curves

* Elliptic curves can now be transformed into a Montgomery model `y² = x³ + Ax² + x`. [#33707](https://trac.sagemath.org/ticket/33707), [#33708](https://trac.sagemath.org/ticket/33708)
* Computing ℓ‑division fields of elliptic curves has been generalized to finite fields. [#33939](https://trac.sagemath.org/ticket/33939)
* Discrete logarithms on "anomalous" elliptic curves with #E(𝔽ₚ)=p are now computed in polynomial time. [#34253](https://trac.sagemath.org/ticket/34253)
* Elliptic-curve isogenies can now be computed in square-root time using the [√élu](https://velusqrt.isogeny.org) algorithm. [#34303](https://trac.sagemath.org/ticket/34303)

## Algebra

* The exterior algebra has changed its indexing set to `FrozenBitset` for speed [#32369](https://trac.sagemath.org/ticket/32369) and now has its own ideal class that can compute Gröbner bases over any field [#34138](https://trac.sagemath.org/ticket/34138).
* Cubic Hecke algebras are implemented [#29717](https://trac.sagemath.org/ticket/29717).
* General implementation of modules over an integral domain [#33868](https://trac.sagemath.org/ticket/33868).
* (Graded) Finite free resolutions of modules over multivariate polynomials can be computed via Singular [#33950](https://trac.sagemath.org/ticket/33950).

```
sage: from sage.homology.free_resolution import FreeResolution 
sage: R.<x,y,z,w> = QQ[]
sage: I = R.ideal([y*z - x*w, y^3 - x^2*z, x*z^2 - y^2*w, z^3 - y*w^2])
sage: r = FreeResolution(I)
sage: r
S^1 <-- S^4 <-- S^4 <-- S^1 <-- 0
sage: len(r)
3
sage: r.differential(2)
Free module morphism defined as left-multiplication by the matrix
[-z^2 -x*z  y*w -y^2]
[   y    0   -x    0]
[  -w    y    z    x]
[   0    w    0    z]
Domain: Ambient free module of rank 4 over the integral domain Multivariate Polynomial Ring in x, y, z, w over Rational Field
Codomain: Ambient free module of rank 4 over the integral domain Multivariate Polynomial Ring in x, y, z, w over Rational Field
sage: from sage.homology.graded_resolution import GradedFreeResolution
sage: S.<x,y,z,w> = PolynomialRing(QQ)
sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
sage: r = GradedFreeResolution(I)
sage: r
S(0) <-- S(-2)⊕S(-2)⊕S(-2) <-- S(-3)⊕S(-3) <-- 0
```

* The quantum Clifford algebra works for an arbitrary parameter `q` [#34147](https://trac.sagemath.org/ticket/34147).
* Multivariate formal power series that are computed lazily (and exactly) have been implemented [#32324](https://trac.sagemath.org/ticket/32324).

## Knot theory

* Links-Gould polynomial invariant for links [#33798](https://trac.sagemath.org/ticket/33798).

## Manifolds

### Tensor products of free modules of finite rank

Free modules of finite rank, which are used to represent the sets of tensor fields on parallelizable manifolds, have been endowed with a `tensor_product` method ([#31276](https://trac.sagemath.org/ticket/31276)):

```
sage: M = Manifold(2, 'M')
sage: X.<x,y> = M.chart()  # makes M parallelizable
sage: XM = M.vector_field_module(); XM
Free module X(M) of vector fields on the 2-dimensional differentiable manifold M
sage: XM.tensor_product(XM)
Free module T^(2,0)(M) of type-(2,0) tensors fields on the 2-dimensional differentiable manifold M
sage: XM.tensor_product(XM) is M.tensor_field_module((2, 0))
True
```


### Vector bases endowed with dictionary methods

Bases of free modules of finite rank now inherit from [AbstractFamily](https://doc.sagemath.org/html/en/reference/sets/sage/sets/family.html#sage.sets.family.AbstractFamily), so that they are endowed with methods `keys`, `values` and `items` ([#30300](https://trac.sagemath.org/ticket/30300)). In particular, this regards vector frames on manifolds:

```
sage: M = Manifold(2, 'M')
sage: X.<x,y> = M.chart()
sage: f = X.frame(); f
Coordinate frame (M, (∂/∂x,∂/∂y))
sage: f.keys()
<generator object FiniteRankFreeModule.irange at 0x7fb2b4b16120>
sage: list(f.keys())
[0, 1]
sage: f.values()
(Vector field ∂/∂x on the 2-dimensional differentiable manifold M,
 Vector field ∂/∂y on the 2-dimensional differentiable manifold M)
sage: f.items()
<zip object at 0x7fb2a1c17fc0>
sage: list(f.items())
[(0, Vector field ∂/∂x on the 2-dimensional differentiable manifold M),
 (1, Vector field ∂/∂y on the 2-dimensional differentiable manifold M)]
```


### Internal code improvements and bug fixes

Various code improvements have been performed: [#30235](https://trac.sagemath.org/ticket/30235), [#34424](https://trac.sagemath.org/ticket/34424), [#34428](https://trac.sagemath.org/ticket/34428),
and some bugs have been corrected: [#33957](https://trac.sagemath.org/ticket/33957), [#34158](https://trac.sagemath.org/ticket/34158).  

See the [changelog](https://sagemanifolds.obspm.fr/changelog.html) for more details. 

## Package upgrades

[IPython](https://ipython.readthedocs.io/en/stable/index.html#), providing the interactive shell of Sage, has been upgraded from 7.x to 8.4.0. This upgrade (including upgrades of many of its dependencies) brings [many improvements](https://ipython.readthedocs.io/en/stable/whatsnew/version8.html#featured-changes), most notably [autosuggestions](https://ipython.readthedocs.io/en/stable/whatsnew/version8.html#autosuggestions). [#33530](https://trac.sagemath.org/ticket/33530) 

NumPy has been upgraded from 1.21.x to version 1.22.4, see the [release notes](https://numpy.org/devdocs/release/1.22.0-notes.html). [#32423](https://trac.sagemath.org/ticket/32423)

SciPy has been upgraded from 1.7.x to version 1.8.1, see the [release notes](https://scipy.github.io/devdocs/release.1.8.0.html). [#32423](https://trac.sagemath.org/ticket/32423)

[NetworkX](https://networkx.org/), the Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks, has been upgraded to version 2.8.4, see the [release notes for 2.7](https://networkx.org/documentation/stable/release/release_2.7.html) and [2.8](https://networkx.org/documentation/stable/release/release_2.8.html). [#32423](https://trac.sagemath.org/ticket/32423)

The CAS kernel [Giac](https://www-fourier.ujf-grenoble.fr/~parisse/giac.html) has been upgraded to version 1.9.0-15. [#31563](https://trac.sagemath.org/ticket/31563)

[Singular](https://www.singular.uni-kl.de/), the CAS for polynomial computations, with special emphasis on commutative and non-commutative algebra, algebraic geometry, and singularity theory, has been upgraded to version 4.3.1p1. [#33160](https://trac.sagemath.org/ticket/33160)

polymake has been upgraded to version 4.7. [#34222](https://trac.sagemath.org/ticket/34222)

The SAT solver `cryptominisat` has been upgraded to version 5.8.0 ([release notes](https://github.com/msoos/cryptominisat/releases/tag/5.8.0)). [#25374](https://trac.sagemath.org/ticket/25374)

SageTeX has been upgraded to version 3.6.1 (making its way to CTAN, too). [#32887](https://trac.sagemath.org/ticket/32887)

The optional `FriCAS` package has been upgraded to version 1.3.8 [#34051](https://trac.sagemath.org/ticket/34051).

For a list of all packages and their versions, see
 * https://repology.org/projects/?inrepo=sagemath_stable

## New tools for developers

### Visual Studio Code dev containers

The Sage source tree now contains sample [devcontainer.json](https://code.visualstudio.com/docs/remote/containers) configuration files for several purposes. [#33671](https://trac.sagemath.org/ticket/33671)

- For using (or trying out) Sage as it is packaged in a distribution, without compiling it: `downstream-archlinux-latest`, `downstream-conda-forge-latest`
- For using (or trying out) Sage as it is provided in a published Docker image: `downstream-docker-cocalc`, `downstream-docker-computop`
- For doing Sage development on top of a published Docker image: `develop-docker-computop`
- For portability testing on top of a Docker image prebuilt by our portability suite on GH Actions: `portability-ubuntu-jammy-standard`

See the [two new sections in the developer's guide](https://doc.sagemath.org/html/en/developer/portability_testing.html#using-our-pre-built-docker-images-published-on-ghcr-io) for more information.


### Validating docstring with `./sage -tox -e rst`

The new command `./sage -tox -e rst -- FILES-OR-DIRECTORIES-TO-CHECK...` checks that docstrings use correct [ReST markup](https://doc.sagemath.org/html/en/developer/coding_basics.html#documentation-strings). [#34157](https://trac.sagemath.org/ticket/34157), [#30448](https://trac.sagemath.org/ticket/30448), [#34156](https://trac.sagemath.org/ticket/34156), [#34158](https://trac.sagemath.org/ticket/34158), [#34159](https://trac.sagemath.org/ticket/34159), [#34160](https://trac.sagemath.org/ticket/34160), [#34161](https://trac.sagemath.org/ticket/34161), [#34162](https://trac.sagemath.org/ticket/34162), [#34163](https://trac.sagemath.org/ticket/34163), [#34164](https://trac.sagemath.org/ticket/34164), [#34165](https://trac.sagemath.org/ticket/34165), [#34166](https://trac.sagemath.org/ticket/34166), [#34168](https://trac.sagemath.org/ticket/34168), [#34169](https://trac.sagemath.org/ticket/34169), [#34172](https://trac.sagemath.org/ticket/34172), [#34288](https://trac.sagemath.org/ticket/34288)

This is faster than rebuilding the documentation and also checks the docstrings of [private functions](https://doc.sagemath.org/html/en/developer/coding_basics.html#private-functions) (functions whose names start with an underscore). 

The new check also runs automatically for each ticket as part of the [Lint workflow](https://trac.sagemath.org/wiki/ReleaseTours/sage-9.6#BuildsandchecksofticketbranchesonGitHubActions).

### Doctesting with `sage -t --optional='sage,!FEATURE'`

Doctests that are conditional on the presence of a feature using an `# optional - FEATURE` annotation can now be explicitly disabled. This is useful for checking that `# optional` annotations are used consistently in a source file. [#33823](https://trac.sagemath.org/ticket/33823)

`sage -t` now prints some additional information about the build when it starts up. [#33967](https://trac.sagemath.org/ticket/33967)

### Debugging on macOS with `sage --lldb`

Also the Sage doctester can be run under control of the LLDB debugger, using `sage -t --lldb`. These new commands mirror those for using the GDB debugger on Linux systems, `sage --gdb` and `sage -t --gdb`. [#33627](https://trac.sagemath.org/ticket/33627), [#31568](https://trac.sagemath.org/ticket/31568)

### Testing modularized distributions

The new command `make pypi-wheels` builds wheels for the modularized distribution packages sagemath-objects, sagemath-categories, sagemath-environment, sagemath-repl and runs tests in virtual environments set up using `tox`. [#33817](https://trac.sagemath.org/ticket/33817)

A build error indicates that a change introduces a modularization regression, which needs to be fixed before the ticket can be merged.

This new check also runs automatically on GitHub Actions as part of the [Build&Test workflow](https://trac.sagemath.org/wiki/ReleaseTours/sage-9.6#Incrementalbuildandtest).

### Gitpod now based on conda-forge, provides a Docker client

We have updated our [Gitpod configuration](https://trac.sagemath.org/wiki/ReleaseTours/sage-9.6#SagedevelopmentinthecloudwithGitpod) to use conda-forge instead of a large pre-built Docker image. Starting a Gitpod instance is much faster now. It also provides `docker` now and works correctly in forked repositories. [#33739](https://trac.sagemath.org/ticket/33739), [#34255](https://trac.sagemath.org/ticket/34255), [#34270](https://trac.sagemath.org/ticket/34270)

## Modularization changes

The work on modularizing the Sage library has continued in Sage 9.7; see Meta-ticket [#29705](https://trac.sagemath.org/ticket/29705) for all details.

### New distribution sagemath-environment

The Sage library contains a [runtime feature discovery system](https://doc.sagemath.org/html/en/reference/misc/index.html#features) in the namespace `sage.features`.

It is now available as the separately installable, pure Python distribution package [sagemath-environment](https://pypi.org/project/sagemath-environment/). Also included: `sage.env` and [some modules](https://github.com/sagemath/sage/blob/develop/pkgs/sagemath-environment/MANIFEST.in) of `sage.misc`. [#29941](https://trac.sagemath.org/ticket/29941)

### Wheels for modularized distributions

As part of our GH Actions workflows, we now build [binary wheels for the distributions  sagemath-objects](https://pypi.org/project/sagemath-objects/9.7rc0/#files) and [sagemath-categories](https://pypi.org/project/sagemath-categories/9.7rc0/#files), and make them available on PyPI. [#34296](https://trac.sagemath.org/ticket/34296)

### Packages `sage`, `sage.rings`, ... are now namespaces

As a major modularization milestone, 
`__init__.py` files have been removed from the packages
`sage`,
`sage.arith`,
`sage.categories`,
`sage.ext`,
`sage.graphs`,
`sage.graphs.graph_decompositions`,
`sage.interfaces`,
`sage.libs`,
`sage.matrix`,
`sage.misc`,
`sage.numerical`, 
`sage.numerical.backends`,
`sage.rings`,
`sage.sets`.
They are now [PEP 420 implicit namespace packages](https://doc.sagemath.org/html/en/developer/packaging_sage_library.html#ordinary-packages-vs-implicit-namespace-packages). [#33011](https://trac.sagemath.org/ticket/33011), [#33754](https://trac.sagemath.org/ticket/33754), [#34187](https://trac.sagemath.org/ticket/34187)

This means that several distribution packages ("pip-installable distributions") can now provide portions of these namespaces. The distributions	[sagemath-objects](https://pypi.org/project/sagemath-objects/9.7b5/) and [sagemath-categories](https://pypi.org/project/sagemath-categories/9.7b5/) have been changed to do this. [#28925](https://trac.sagemath.org/ticket/28925)

*Downstream packages that use Cython and `cimport` Sage modules need to activate PEP 420 namespace package support* in Cython. This is standard in the upcoming Cython 3  ([#29863](https://trac.sagemath.org/ticket/29863)). When using a Cython release from the stable 0.29.x series, use `with cython_namespace_package_support()`, as is done in https://github.com/sagemath/sage/blob/develop/src/setup.py#L106 for sagelib. Making this change is an opportunity to also check whether your package is compatible with the upcoming Cython 3.

The Sage distribution uses a patched version of Cython 0.29.x with a backport of the Cython 3 namespace package support. [#34221](https://trac.sagemath.org/ticket/34221)

## Configuration changes

### Editable installation is now the default

By the new default, the Sage library (sagemath-standard) and other [distribution packages whose source trees are part of the Sage monorepo](https://github.com/sagemath/sage/tree/develop/pkgs) (sage-conf, sage-docbuild, sage-setup, sage-sws2rst) are now installed in [editable mode](https://wiki.sagemath.org/ReleaseTours/sage-9.3#Editable_.28.22in-place.22.2C_.22develop.22.29_installs_of_the_Sage_library). [#32406](https://trac.sagemath.org/ticket/32406)

This means that changes to Python source files take immediate effect after restarting Sage. Running `sage -b` or `make build` is only necessary if you make changes (or switch to a branch that makes changes) to Cython sources or external packages.

To go back to the previous default, use `./configure --disable-editable`.

If you need wheels for all packages, for example when you want to create a separate venv, you can use the command `make wheels`. [#33817](https://trac.sagemath.org/ticket/33817)


### Support for system Python 3.7 dropped, `ensurepip` required

It is still possible to build the Sage distribution on systems with older Python versions, but Sage will build its own copy of Python 3.10.5 in this case. [#32937](https://trac.sagemath.org/ticket/32937), [#34090](https://trac.sagemath.org/ticket/34090)

The Sage distribution now also requires that the system Python includes the standard [ensurepip](https://docs.python.org/3/library/ensurepip.html) module. On Debian and Ubuntu, it is missing if only `python3-minimal` is installed; the package [python3-venv](https://packages.debian.org/search?keywords=python3-venv) provides it. [#33822](https://trac.sagemath.org/ticket/33822)

### Support for system GCC older than 6.3 dropped

Building Sage from source now requires a system installation of GCC >= 6.3 (except on macOS, where the compilers from an up-to-date Xcode or Xcode CLT installation should be used). An alternative is to use a sufficiently recent version of clang (LLVM). [#33316](https://trac.sagemath.org/ticket/33316)

Users of older Linux distributions (`ubuntu-trusty`, `ubuntu-xenial`, `linuxmint-17`, `linuxmint-18`, `slackware-14.2`) should upgrade their systems before attempting to install Sage from source.

Alternatively, users on `ubuntu-trusty` and `ubuntu-xenial` can install a modern compiler toolchain [using the ubuntu-toolchain-r ppa](https://askubuntu.com/questions/1140183/install-gcc-9-on-ubuntu-18-04/1149383[#11493](https://trac.sagemath.org/ticket/11493)83). On `ubuntu-trusty`, also the package `binutils-2.26` is required; after installing it, make it available using `export PATH="/usr/lib/binutils-2.26/bin:$PATH"`.

Instead of upgrading their distribution, users of `centos-7` can install a modern compiler toolchain [using Redhat's devtoolset](https://stackoverflow.com/a/67212990/557937).

On other old distributions, if an upgrade to a newer distribution is not possible, users can try to use `./configure --without-system-gcc`. Then Sage will attempt to build its own copy of GCC 11.3.0 using the available system GCC. We no longer test such system configurations, so this may or may not work.

### Uninstalling SPKGs using `make SPKG-uninstall`

This command replaces `make SPKG-clean`, which is now deprecated. [#29097](https://trac.sagemath.org/ticket/29097)

When an incremental build of the documentation fails, it is once again sufficient to use `make doc-clean`, followed by `make doc-html`. To uninstall the entire installation of the documentation, use `make doc-uninstall`. [#33705](https://trac.sagemath.org/ticket/33705)


## Availability of Sage 9.7 and installation help

Sage 9.7 was released on September 19, 2022.

*Please read the [updated SageMath installation guide](https://doc.sagemath.org/html/en/installation/index.html)*. 
It provides a decision tree that guides users and developers to a type of installation suitable for their system and their needs.

### Sources

The Sage source code is available in the [sage git repository](https://github.com/sagemath/sage/tree/develop).

Sage builds successfully on the following platforms:
 * *Linux 64-bit* (x86_64) - https://github.com/sagemath/sage/actions/runs/2960673965
   * ubuntu-{[trusty](https://launchpad.net/ubuntu/trusty)-toolchain-gcc_9,[xenial](https://launchpad.net/ubuntu/xenial)-toolchain-gcc_9,[bionic](https://launchpad.net/ubuntu/bionic),[focal](https://launchpad.net/ubuntu/focal),[jammy](https://launchpad.net/ubuntu/jammy), [kinetic](https://launchpad.net/ubuntu/kinetic)} 
   * debian-{[stretch](https://wiki.debian.org/DebianStretch), [buster](https://wiki.debian.org/DebianBuster),[bullseye](https://wiki.debian.org/DebianBullseye),[bookworm](https://wiki.debian.org/DebianBookworm),[sid](https://wiki.debian.org/DebianUnstable)}
   * linuxmint-{[19](https://linuxmint.com/rel_tara_cinnamon.php),[19.3](https://linuxmint.com/rel_tricia_cinnamon.php),[20.1](https://www.linuxmint.com/rel_ulyssa_cinnamon_whatsnew.php),[20.2](https://linuxmint.com/rel_uma_cinnamon.php),[21](https://linuxmint.com/rel_vanessa_cinnamon.php)}
   * fedora-{[26](https://docs.fedoraproject.org/en-US/fedora/f26/release-notes/),[27](https://docs.fedoraproject.org/en-US/fedora/f27/release-notes/),[28](https://docs.fedoraproject.org/en-US/fedora/f28/release-notes/),[29](https://docs.fedoraproject.org/en-US/fedora/f29/release-notes/),[30](https://docs.fedoraproject.org/en-US/fedora/f30/release-notes/),[31](https://docs.fedoraproject.org/en-US/fedora/f31/release-notes/),[32](https://docs.fedoraproject.org/en-US/fedora/f32/release-notes/),[33](https://docs.fedoraproject.org/en-US/fedora/f33/release-notes/),[34](https://docs.fedoraproject.org/en-US/fedora/f34/release-notes/),[35](https://docs.fedoraproject.org/en-US/fedora/f35/release-notes/),[36](https://docs.fedoraproject.org/en-US/fedora/f36/release-notes/),[37](https://fedoraproject.org/wiki/Releases/37/ChangeSet)}
   * centos-{7-devtoolset-gcc_11,[stream-8](https://www.centos.org/centos-stream/),[stream-9](https://www.centos.org/centos-stream/)}
   * gentoo
   * archlinux
   * opensuse-{[15.3](https://doc.opensuse.org/release-notes/x86_64/openSUSE/Leap/15.3/),[15.4](https://doc.opensuse.org/release-notes/x86_64/openSUSE/Leap/15.4/),[tumbleweed](https://get.opensuse.org/tumbleweed/)}
   * conda-forge
 * *Linux 32-bit* (i386/i686) - https://github.com/sagemath/sage/actions/runs/2960673965
   * ubuntu-bionic
   * [manylinux-2_24](https://github.com/pypa/manylinux#manylinux_2_24-debian-9-based)
   * debian-buster
 * *macOS (Intel)* (x86_64) - with [Homebrew](https://brew.sh/) or without
   * macOS 10.15 (Catalina)
   * macOS 11.x (Big Sur)
   * macOS 12.x (Monterey)
 * *macOS (Apple Silicon, M1/M2)*
   * Building Sage from source on Apple Silicon (M1/M2) requires the use of [Homebrew](https://brew.sh/) (recommended) or conda-forge, which package versions of `gfortran` 11/12 with necessary changes for this platform that are not in a released upstream version of GCC. (The `gfortran` package that comes with Sage is not suitable for the M1/M2.)
   * Make sure that `/usr/local` does not contain an old copy of homebrew (or other software) for x86_64 that you may have copied from an old machine. Homebrew for the M1/M2 is installed in `/opt/homebrew`, not `/usr/local`.
   * Be sure to follow the [README](https://github.com/sagemath/sage/blob/develop/README.md) and the instructions that the `./configure` command issues regarding the installation of system packages from Homebrew or conda.

You can also [build Sage on top of conda-forge](https://doc.sagemath.org/html/en/installation/conda.html) on Linux and macOS.

*Known issues and workarounds:*

 * If your system [pari](https://doc.sagemath.org/html/en/reference/spkg/pari.html#spkg-pari) package is very new (>= 2.15) but there is no suitable system [giac](https://doc.sagemath.org/html/en/reference/spkg/giac.html#spkg-giac) package, then `giac` will fail to build. Workaround: Use `./configure --without-system-pari`. [#34537](https://trac.sagemath.org/ticket/34537)

*Sage 9.7 does not support Cygwin; use Windows Subsystem for Linux instead.* 
Because of unresolved problems with standard packages GIAC ([#34269](https://trac.sagemath.org/ticket/34269)), ECL ([#34127](https://trac.sagemath.org/ticket/34127)), Maxima ([#30796](https://trac.sagemath.org/ticket/30796)), and the rebasing facility ([#34223](https://trac.sagemath.org/ticket/34223)), Sage 9.7 does not support Cygwin. Users on Windows 10 and 11 can migrate to using [WSL as described in our installation guide](https://doc.sagemath.org/html/en/installation//index.html#windows). A convenient way to use such an installation of Sage is via VS Code's WSL remote. [#34301](https://trac.sagemath.org/ticket/34301), [#30484](https://trac.sagemath.org/ticket/30484)

### Binaries

 * The easiest way to install Sage 9.7 on Linux is through a distribution that provides it, see [repology.org: sagemath](https://repology.org/project/sagemath/versions).

### Help

See [README.md](https://github.com/sagemath/sage/blob/develop/README.md) in the source distribution for installation instructions.

Visit [sage-support](https://groups.google.com/forum/#!forum/sage-support) for installation help.

## More details

 * [Trac tickets with milestone 9.7](https://trac.sagemath.org/query?milestone=sage-9.7&groupdesc=1&group=status&max=1500&col=id&col=summary&col=author&col=reviewer&col=time&col=changetime&col=component&col=keywords&order=component)

 * [Diff from 9.6](https://github.com/sagemath/sage/compare/9.6...9.7#files_bucket)

 * [Changelog for Sage 9.7](https://www.sagemath.org/changelogs/sage-9.7.txt)

