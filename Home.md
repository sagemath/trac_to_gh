
```

# 🚨 BROADCAST 🚨

For maintenance, the **trac server will be switched off on Saturday** 10 / 09 / 2022 from 7:00 to 23:00 (Paris Time).

Sorry for the inconvenience, and thanks for your patience. Please go relax again.

The trac server is currently running in **slightly degraded mode**. Some advanced features are not yet working.
```

# Moving to Github!

Sage development will soon move from Trac to Github! This was decided in a [vote on sage-devel](https://groups.google.com/g/sage-devel/c/7h5JoRgHpxY) that closed on Oct 5, 2022. The migration work is coordinated in #30363.


# Welcome to the SageMath Development Organization Page

[SageMath](https://www.sagemath.org) is free and open software that supports  research and teaching in algebra, geometry, number theory, cryptography, etc.  Both the SageMath development model and the technology in SageMath itself are  distinguished by an extremely strong emphasis on openness, community,  cooperation, and collaboration: we are building the car, not reinventing the wheel.
View our [Code of Conduct](https://github.com/sagemath/sage/blob/develop/CODE_OF_CONDUCT.md).

The Sage Trac server (this web page) manages *tickets*, the equivalents of Issues and Pull Requests (PRs).  In addition to bug reports, also ideas for features to add to SageMath are appropriate as tickets. 


## Getting started

To create tickets, add comments on tickets, and edit wiki pages on this site, you need either a GitHub account or a legacy sage-trac account.

*Users with GitHub accounts* should use the [GitHub Login](https://trac.sagemath.org/github/login) link. (If you do not have an account on GitHub yet, choose a user name and
[create a GitHub account](https://github.com).)

*Users with legacy sage-trac accounts* (account names not starting with "gh-") should use the [Login](https://trac.sagemath.org/login) link. Do _not_ to use GitHub login, as it will be treated as a separate user from their original account (unless you actively prefer to switch).

The [[TracGuide|Help/Guide]] link in the top right corner provides help with the Trac server.


## Reporting a bug

Please help SageMath development by [reporting bugs that you encounter](https://doc.sagemath.org/html/en/developer/trac.html#reporting-bugs), no matter how trivial.
If you need to open a ticket, please use the ``` and ``` tags to add code snippets and SageMath session transcripts. For example:

|= Markup =|= Displays as =|
|----------|---------------|
|\
```
{{{
{{{
sage: 1 + 2
3
```
}}}
}}}
```
{{{
sage: 1 + 2
3
```
}}}
You can also use backticks (```) to demarcate inline code snippets, etc. This is useful around names like `DiGraph` to avoid an automatic wikilink (DiGraph), like so: ``DiGraph``.

SageMath makes use of many upstream projects, which have their own bug tracking pages. A selection: [Cython](https://github.com/cython/cython), [fflas-ffpack](https://github.com/linbox-team/fflas-ffpack/issues), [GAP](https://github.com/gap-system/gap/issues), [GCC](https://gcc.gnu.org/bugzilla/) ([instructions](https://gcc.gnu.org/bugs/)), [Givaro](https://github.com/linbox-team/givaro/issues), [JMol](https://sourceforge.net/p/jmol/bugs/), [LinBox](https://github.com/linbox-team/linbox/issues), [Maxima](https://sourceforge.net/p/maxima/bugs/), [Numpy](https://github.com/numpy/numpy/issues), [PARI/GP](https://pari.math.u-bordeaux.fr/Bugs/) ([instructions](https://pari.math.u-bordeaux.fr/Bugs/Reporting.html)), [Python](https://bugs.python.org/), [Singular](https://www.singular.uni-kl.de:8002/trac/).


## Following the pulse of development

Follow the [Trac development timeline](https://trac.sagemath.org/timeline) or [active tickets by time](https://trac.sagemath.org/report/92), or view [[ticket reports](./TicketReports|other)].

Help by reviewing [Tickets needing review](https://trac.sagemath.org/report/75) (see  [checklist](https://doc.sagemath.org/html/en/developer/reviewer_checklist.html)).

Catch up on [Open tickets you've participated in](https://trac.sagemath.org/report/51) or make a [Custom query](http://trac.sagemath.org/sage_trac/query).

Contribute to the [Release notes for the current development series](https://wiki.sagemath.org/ReleaseTours) by collaborative editing.

Explore the [Open meta-tickets on larger tasks](https://trac.sagemath.org/report/95) or topical pages on [Algebra](./algebra), [Coding Theory](./SageCodingRoadMap), [Combinatorics](./SageCombinatRoadMap), [Manifolds](https://trac.sagemath.org/ticket/30525), [Optimization](https://trac.sagemath.org/ticket/20302), [Polyhedral Geometry](./SagePolyhedralGeometry), [Symbolics](./symbolics).

Discuss in [sage-devel](https://groups.google.com/g/sage-devel) or one of [our other development groups](https://www.sagemath.org/development-groups.html).


## Contributing by working on tickets

Our [FAQ on contributing to SageMath](https://doc.sagemath.org/html/en/faq/faq-contribute.html) will take you to sections [Working on tickets](https://doc.sagemath.org/html/en/developer/trac.html#working-on-tickets) and [Working with git](https://doc.sagemath.org/html/en/developer/manual_git.html) in the [Developer's Guide](https://www.sagemath.org/doc/developer/).
Make sure you understand the review process, and the procedures for opening and closing tickets. 

When opening a ticket to make a feature request or to plan a project, you may find our [Feature request guidelines](https://wiki.sagemath.org/feature_request_guidelines) helpful.

![](ticket_badges.png, 547px)

After pushing a branch to a ticket, the ticket will show badges linking to results of automated tests that run on the [[patchbot]] and other [tests that run on GitHub Actions](https://trac.sagemath.org/wiki/ReleaseTours/sage-9.6#Newdevelopertools).


## Surveying the mathematical software landscape

The SageMath project is a major integrating force in the math software landscape. Follow the ticket numbers to see how you can help; for example, by surveying software, building or extending interfaces, or contributing to distribution packaging.

|                                    |= *In the SageMath distribution*         =|= Not in the SageMath distribution =|
|------------------------------------|------------------------------------------|------------------------------------|
|=Unused math software              =| [SymEngine](https://doc.sagemath.org/html/en/reference/spkg/symengine.html), [cocoalib](https://doc.sagemath.org/html/en/reference/spkg/cocoalib.html), [isl](https://doc.sagemath.org/html/en/reference/spkg/isl.html), [CyLP](https://doc.sagemath.org/html/en/reference/spkg/cylp.html), ... #33773                 | [sagemath.org links](https://www.sagemath.org/links.html), [Open-source CAS](https://wiki.sagemath.org/OSCAS), [SoftwareToIntegrate](https://wiki.sagemath.org/devel/SoftwareToIntegrate), [SoftwareSurveys](https://wiki.sagemath.org/devel/SoftwareSurveys) #33725, [Python optimization packages](https://trac.sagemath.org/ticket/26511) #26511, [polyhedral geometry packages](https://wiki.sagemath.org/OptiPolyGeom), [swMATH.org](https://swmath.org/), math databases #30914
|=[[Upstream]] non-Python math software =|[Packages](https://doc.sagemath.org/html/en/reference/spkg/): [GMP](https://doc.sagemath.org/html/en/reference/spkg/gmp.html), [FLINT](https://doc.sagemath.org/html/en/reference/spkg/flint.html) #31408, [arb](https://doc.sagemath.org/html/en/reference/spkg/arb.html), [Singular](https://doc.sagemath.org/html/en/reference/spkg/singular.html), [GAP](https://doc.sagemath.org/html/en/reference/spkg/gap.html), [PARI](https://doc.sagemath.org/html/en/reference/spkg/pari.html), [Maxima](https://doc.sagemath.org/html/en/reference/spkg/maxima.html), [R](https://doc.sagemath.org/html/en/reference/spkg/r.html), [FPLLL](https://doc.sagemath.org/html/en/reference/spkg/fplll.html), [LinBox](https://doc.sagemath.org/html/en/reference/spkg/linbox.html), [GSL](https://doc.sagemath.org/html/en/reference/spkg/gsl.html),  [polymake](https://doc.sagemath.org/html/en/reference/spkg/polymake.html), ... | [Free software that Sage interfaces to](https://wiki.sagemath.org/Interfaces#Interfaces_to_other_software_in_SageMath): Macaulay2, Octave, ...; [Non-free software that Sage interfaces to](https://wiki.sagemath.org/Interfaces#Interfaces_to_other_software_in_SageMath): Magma, Maple, Mathematica, CPLEX, Gurobi, SCIP, ...
|=[[Upstream]] Python math software     =|[Packages](https://doc.sagemath.org/html/en/reference/spkg/): [NumPy](https://doc.sagemath.org/html/en/reference/spkg/numpy.html), [SciPy](https://doc.sagemath.org/html/en/reference/spkg/scipy.html), [SymPy](https://doc.sagemath.org/html/en/reference/spkg/sympy.html), [CVXOPT](https://doc.sagemath.org/html/en/reference/spkg/cvxopt.html), [NetworkX](https://doc.sagemath.org/html/en/reference/spkg/networkx.html), ...
|=[[Upstream]] distributions            =| | [Distributions providing system packages](https://wiki.sagemath.org/ReleaseTours/sage-9.1#Portability_improvements.2C_increased_use_of_system_packages): homebrew, conda-forge, archlinux, ... #27330
|= Absorbed libraries=| [GiNaC/Pynac](https://trac.sagemath.org/ticket/32386) #33401, [giacpy](https://trac.sagemath.org/ticket/29171), [sage_brial](https://trac.sagemath.org/ticket/30332) |    |
|= *[SageMath library](https://doc.sagemath.org/html/en/reference/index.html)*=| [Source](https://github.com/sagemath/sage/tree/develop/src/sage): [sage.algebras.*](https://github.com/sagemath/sage/tree/develop/src/sage/algebras), [sage.categories.*](https://github.com/sagemath/sage/tree/develop/src/sage/categories), [sage.combinat.*](https://github.com/sagemath/sage/tree/develop/src/sage/combinat),  [sage.crypto.*](https://github.com/sagemath/sage/tree/develop/src/sage/crypto),  [sage.geometry.*](https://github.com/sagemath/sage/tree/develop/src/sage/geometry), [sage.graphs.*](https://github.com/sagemath/sage/tree/develop/src/sage/graphs), [sage.groups.*](https://github.com/sagemath/sage/tree/develop/src/sage/groups), [sage.manifolds.*](https://github.com/sagemath/sage/tree/develop/src/sage/manifolds),  [sage.modular.*](https://github.com/sagemath/sage/tree/develop/src/sage/modular), [sage.rings.*](https://github.com/sagemath/sage/tree/develop/src/sage/rings), [sage.schemes.*](https://github.com/sagemath/sage/tree/develop/src/sage/schemes), [sage.symbolic.*](https://github.com/sagemath/sage/tree/develop/src/sage/symbolic), [sage.tensor.*](https://github.com/sagemath/sage/tree/develop/src/sage/tensor), [sage.topology.*](https://github.com/sagemath/sage/tree/develop/src/sage/topology), ...
|= Absorbed SageMath extensions=| [Sage-Combinat](https://wiki.sagemath.org/combinat), [SageManifolds](https://sagemanifolds.obspm.fr/) | |
|=Downstream software               =| [SageTeX](https://doc.sagemath.org/html/en/reference/spkg/sagetex), [In-distribution Sage user packages](https://trac.sagemath.org/ticket/31164): [admcycles](https://doc.sagemath.org/html/en/reference/spkg/admcycles), [sage-flatsurf](https://doc.sagemath.org/html/en/reference/spkg/sage_flatsurf), ...     | [External Sage user packages](https://wiki.sagemath.org/SageMathExternalPackages) #31164, [GAP-homalg](https://wiki.sagemath.org/Interfaces#Interfaces_to_SageMath_in_other_software)
|=User interfaces                   =| Jupyter, JupyterLab #30399            | [Emacs sage-shell-mode](https://wiki.sagemath.org/Emacs), [Interfaces](https://wiki.sagemath.org/Interfaces#Interfaces_to_SageMath_in_other_software), [IDEs](https://trac.sagemath.org/ticket/30500) #30500
|=Downstream distributions          =| SageMath distribution #33774, [Sage Docker images](https://trac.sagemath.org/wiki/Distribution#Dockerimages), modularized distributions on PyPI #29705, wheels #31251  | [[Distribution#Packagemanagers|Distributions carrying SageMath]]: conda-forge, archlinux, debian/ubuntu, fedora, [sage-on-gentoo](https://github.com/cschwan/sage-on-gentoo), nix, voidlinux, ... #33775; [Third-party Docker images](https://trac.sagemath.org/wiki/Distribution#Dockerimages)
|=Downstream deployments            =| [Gitpod](https://trac.sagemath.org/wiki/ReleaseTours/sage-9.6#SagedevelopmentinthecloudwithGitpod) #33113 | [Running SageMath in the cloud](https://doc.sagemath.org/html/en/installation/): [CoCalc](https://cocalc.com/?utm_source=trac.sagemath.org), [SageCell](https://sagecell.sagemath.org/), [Binder](https://github.com/sagemath/sage-binder-env)
|=Downstream of downstream          =| Devcontainers #33671, #34363

This table is being moved to the Sage developer's guide in #34526; do not edit.


## Maintaining the social and technical infrastructure

Participate in or help organize [Workshops and other activities](https://wiki.sagemath.org/), or [contribute to the Sage community by answering questions](https://wiki.sagemath.org/contribute/AnswerQuestions).

You can also help maintain the [Technical project infrastructure](./Infrastructure).


## Additional formatting hints

You can enable syntax highlighting in these code snippets by using a hashbang (`#!`) followed by the name of the syntax. This also makes inline diff viewers if you choose the syntax name `diff`.
|= Markup =|= Displays as =|
|----------|---------------|
|\
```
{{{
{{{
#!python
def spam ():
    eggs = 3
    return 1
pine_for_fjords()
```
}}}
}}}
```
{{{
#!python
def spam ():
    eggs = 3
    return 1
pine_for_fjords()
```
}}}
|
|
|\
```
{{{
{{{
#!diff
foo

diff --git a/bar b/bar
--- a/bar
+++ b/bar
`@``@` -1,2 +1,3 `@``@`
 baz
 quux
+xyzzy
```
}}}
}}}
```
{{{
#!diff
foo

diff --git a/bar b/bar
--- a/bar
+++ b/bar
`@``@` -1,2 +1,3 `@``@`
 baz
 quux
+xyzzy
```
}}}
To avoid an automatic wikilink for non-code names like GitHub, prepend it with an exclamation mark: `GitHub`. See WikiFormatting for more information.


## Account Names Mapped to Real Names

The list of over 600 account holders in Sage's Trac that was here is now merged to the  [contributors.xml](https://github.com/sagemath/website/blob/master/conf/contributors.xml) through [Github PR](https://github.com/sagemath/website/pull/311). The merged developers list is at [SageMath developer world map](https://www.sagemath.org/development-map.html). 

== Legacy sage-trac Account Request == #legacy-account-request

If you cannot create a GitHub account, need to edit the SageMath Wiki, or have other special needs, you may request a local account on this site, by reading the [trac guidelines](https://www.sagemath.org/doc/developer/trac.html), then sending an email to sage-trac-account AT googlegroups DOT com that contains *all* of the following:

 * your full name
 * the default username is the first letter of the name followed by the family name (i.e. mjohnson for Mike Johnson). If you really want something else you can make a reasonable suggestion [some examples](https://trac.sagemath.org/#AccountNamesMappedtoRealNames)
 * contact email
 * and reason for needing a trac account.

---

Attachments:
 * [ticket_badges.png](Home/ticket_badges.png)
