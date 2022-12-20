# Roadmap and status report for Coding Theory in Sage

See also the page on [https://wiki.sagemath.org/Coding_Theory](https://wiki.sagemath.org/Coding_Theory).

This page is meant to provide an overview of developments for Coding Theory in
Sage. This includes existing trac tickets, with or without code, as well as
wish-lists or long-term goals from interested developers.

Feel free to edit this page by adding trac tickets, more wish-lists, and add
your names for topics you contributed to or would be interested in contributing
to (this helps knowing who does what and who to contact for further
collaborations).

# Topics

## Representing Codes

* Linear codes and category framework [#18150](https://trac.sagemath.org/ticket/18150)
* Deprecate support for finite rings in `LinearCode`  [#20387](https://trac.sagemath.org/ticket/20387)

The following is some wishes:

* Non-linear codes
  * Support multilinear codes (i.e. a code over `GF(q^m)` which is linear over `GF(q)`). Examples include Interleaved linear codes, Folded RS codes and Multiplicity codes.
  * Support codes over rings (see [#20387](https://trac.sagemath.org/ticket/20387) for admitting that we currently don't support this).
* Explicit class for binary codes, possibly building on the current Cython implementation.
  Remove all binary code-specific methods from `AbstractLinearCode`. 

## Algebraic Code Families

* Reed--Muller codes
  * Decoding algorithm for low-order q-ary or binary Reed-Muller codes [#20938](https://trac.sagemath.org/ticket/20938)
* Goppa codes would be extremely nice to have.
* AG codes
  To support Algebraic Geomety codes in Sage, we need the following building blocks:
  * Representation of algebraic curves. Done: `Curve` and `AffineSpace`/`ProjectiveSpace`.
  * Representation of divisors. Done: see `Curve.divisor`.
  * Computation of Riemann-Roch space bases [#22982](https://trac.sagemath.org/ticket/22982)


## Other Code Families

* Open a ticket for your favourite code family and add it here.

## Algorithms for generic codes

* Information set decoder [#20138](https://trac.sagemath.org/ticket/20138)
* Non-guava implementation for `covering_radius` [#19913](https://trac.sagemath.org/ticket/19913)
* Bounds and optimal codes: Not very easy, no support yet. What to do with [http://codetables.de](http://codetables.de)?
* Representing automorphisms of codes. 
  Sage is reasonably good at computing automorphisms of codes with the methods
  `automorphisms_group_gens`, ` permutation_automorphism_group`, and the related
  method `canonical_representative`. These use an efficient C implementation
  written by Thomas Feuler, based on his PhD thesis. However, the
  representations of such automorphisms is very lacking. For instance, the
  "groups" returned by the above methods are simply a list of generators, with
  no group methods attached to them. And one cannot take an element of this
  group and apply it to e.g. a codeword or a whole code. Using a nice, Sage-wide
  algebraic representation would also make it much easier to implement the
  automorphism groups of special families for which it is known, e.g.
  Reed-Solomon codes. In `sage.schemes` there has been some recent development
  in automorphism groups of curves. Perhaps this can serve as a base?
* TestSet decoding algorithm [#21339](https://trac.sagemath.org/ticket/21339)

## Code Testing, Plotting and Benchmarking

* Benchmarking tool for codes [#20526](https://trac.sagemath.org/ticket/20526), [#20684](https://trac.sagemath.org/ticket/20684), [#20786](https://trac.sagemath.org/ticket/20786). After discussions at
  SageDays75, Miguel Marco and Johan Rosenkilde started the stand-alone Python
  project [Bleachermark](https://github.com/miguelmarco/bleachermark) directly
  inspired by the work in these tickets. That project is meant to supersede
  these tickets.

## Documentation

* Improve coding theory thematic tutorial on writing new structures  [#21361](https://trac.sagemath.org/ticket/21361)
* Improve the documentation for `HammingCode`  [#21305](https://trac.sagemath.org/ticket/21305)

## General algebra in Sage that is important for coding theory

* Link to advanced fast polynomial arithmetic library functions such as multi-point evaluation and Lagrange interpolation.
* Link to fast `GF(2)[x]` library (currently used is NTL generic `GF(p)[x]`).
* Ring extension support (related to e.g. subfield subcodes) [#21413](https://trac.sagemath.org/ticket/21413)
* Submodules of `(ZZ/nZZ)^r` (prerequisite for codes over `ZZ/nZZ`) [#6452](https://trac.sagemath.org/ticket/6452)

## Cleanup, Restructuring, Misc bugs

* Clean `LinearCodeFromCheckMatrix` [#19975](https://trac.sagemath.org/ticket/19975) 

## GSoC 2016: Rank metric codes
Arpit Merchant was the student for this project, with David Lucas and Johan Rosenkilde as mentors.

* Advanced skew polynomial methods and optimised implementation for finite field
  base rings [#21088](https://trac.sagemath.org/ticket/21088), [#21259](https://trac.sagemath.org/ticket/21259), [#21262](https://trac.sagemath.org/ticket/21262), [#21264](https://trac.sagemath.org/ticket/21264). Perhaps these should be closed as wont-fix:
  Xavier Caruso has expressed a wish to rewrite all this.
* Gabidulin codes  [#20970](https://trac.sagemath.org/ticket/20970)
* Abstract class for rank-metric codes  [#21226](https://trac.sagemath.org/ticket/21226)
