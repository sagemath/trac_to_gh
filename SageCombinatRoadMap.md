# Roadmap and status report for Sage-Combinat

This page is an attempt at drawing a road map for
[Sage-Combinat](http://combinat.sagemath.org), starting with the migration from [MuPAD-Combinat](http://mupad-combinat.sf.net/).

Please feel free to edit this page to add more items, or add your
names for topics you contributed to or would be interested in
contributing to (this helps knowing who does what and who to contact
for further collaborations).

## Overview

[All Sage-Combinat tickets](https://trac.sagemath.org/query?groupdesc=1&group=status&cc=~sage-combinat&max=103&col=id&col=summary&col=type&col=status&col=priority&col=milestone&col=)

## Progress of the migration from MuPAD to Sage

|                                  |        |                               |
|----------------------------------|--------|-------------------------------|
| Topic                            |Progress| Comments                      |
| Basic enumerative combinatorics  | 75%    | 2007-08 by Mike               |
| Decomposable objects / Species   | 75%    | #10662                        |
| Trees                            | 30%    |                               |
| Posets                           |100%    |                               |
| Words                            |100%    |                               |
| Symmetric functions              | 90%    |                               |
| k-Schur & the like               | 90%    |                               |
| Root systems / ...               | 90%    |                               |
| Crystals                         | 90%    |                               |
| Category framework               |100%    |                               |
| Hopf algebra framework           | 80%    |                               |
| Free modules & such              | 80%    |                               |
| Algebra (desosseur, ...)         | 50%    |                               |
| Operads                          | 15%    | #15633, #15634                |
| Linbox interface                 |100%    | (compares to 10% in MuPAD)    |
| GAP interface                    | 80%    | (compares to  1% in MuPAD)    |
| Interface for fast Gröbner basis |100%    | (compares to  0% in MuPAD)    |
| Nauty                            |100%    | (compares to 50% in MuPAD     |
| Symmetrica                       | 60%    |                               |
| lrcalc                           | 95%    | #10333, #11563, #14107        |
| GLIP                             | 50%    | #6812                         |
| graphviz / dot2tex               | 80%    | #7004, #10518                 |
| Database access                  |100%    |                               |
| MachineIntegerListsLex           |  0%    | Will be easy via cython       |
| Basic abstract data structures   |100%    | (fast stacks, AVL, dancing links) compares to just the basic ones in MuPAD + no real way to implement some with serious speed ourselves     |

## Road map

* Hopf algebras, Symmetric functions, and generalizations
  * Symmetric Functions
    * #10554: Better support for casual usage of symmetric functions
    * Replace Symmetrica by lrcalc whenever possible
    * #10930 (prototype): specializations for symmetric functions (Martin Rubey, ???)
    * #9558: Make `is_symmetric` method for polynomials or where else useful
  * Multisymmetric Functions (Paul Bryan, Emmanuel Briand)
  * #11979 (prototype): Divided power algebras (Bruce)
  * #6629 (prototype) Implement Schubert polynomials (Viviane Pons, AdrienBoussicault, Nicolas Borie)
  * #6889 (prototype): Invariant rings of permutation group (Nicolas Borie)
  * Implement more generic algorithms:
    * Antipode defined recursively
    * Product and coproduct defined by duality
    * Group like elements from primitive idempotents
  * #14901 (prototype): Lie algebras, Kac-Moody algebras, quantum groups (Travis Scrimshaw)
  * Planar algebras
  * Operads (#15633, #15634, basic support, partially depends on #10662) (FlorentHivert, FredericChapoton)

* Monoids, algebras, and their representation theory:
  * Finite dimensional algebras:
    * Decomposition of the center, construction of minimal idempotents (as in MuPAD-Combinat)
    * Quiver, Cartan matrix, radical filtration (as in MuPAD-Combinat)
  * Finite monoids and semigroups
    * #12914 (prototype): Representation theory of finite semigroups
      (Franco, Tom, Anne, Florent, Nicolas)
    * #8360 (needs finalization) interface to Jean-Éric Pin's Semigroupe package
    * #12915: Interfaces to the GAP packages KBMag (and to Monoids, Citrus, ...)
  * Calculus on modules (direct sums, tensor products, induction, restriction, quotients, radical, ...)
    (in progress for semigroups)
  * Tower of algebras: representations, Grothendieck rings, ...
  * Group algebras:
    * #10305: Add rings for the center of the symmetric group algebras
      Mathieu Guay-Paquet, Valentin Feray
  * Quivers and path algebras:
    * #9889 (prototype): A new module implementing Monomial Algebras (Quimey Vivas)
    * Interface to QPA in GAP?
      http://sourceforge.net/projects/quiverspathalg/
      Authors: Green, Solberg, ...
      Based on Gröbner package GBNP by Cohen and Knopper
  * Experiment with KBMAG / PLURAL / Letterplace (see #4539) to easily implement
    algebras like affine nilCoxeter algebra, affine nilTemperley Lieb
    algebra, affine local plactic algebra).

* Root systems, Coxeter groups, Hecke algebras:
  * #8906 (needs finalization): Optional package for gap3
  * Integrate/interface PyCox
  * Root systems:
    * Constructing a root/coroot lattice realization from a pair of matrices
      Christian Stump
  * Coxeter groups, reflection groups:
    * #11187 (prototype): Implementation of finite reflection groups
    * #11109 (prototype): Stable grothendieck polynomials in type A affine (Nicolas Thiéry)
  * Automatic finite Coxeter/(affine)Weyl type recognition, using graph
    isomorphism with predefined cartan types (complex reflection group is harder)
  * Representations of Coxeter groups and Hecke algebras (through pyCox, ...)
    Geck, Franco,
    * Port over the character tables
    * Representations/character tables of the Hecke algebras
    * Port Specht (AndrewMathas)
    * Implement data structures for character tables / use it systematically in Sage (Volunteers? Nicolas has some design notes about this):
      * of groups in Sage / GAP
      * of semi-simple algebras (in Sage / GAP)
      * of a coset
      * See also #7555: fix Cayley tables, add operation tables
  * Further improve root systems, Coxeter groups and the like,
    getting features, inspiration, code, doc, tests, developers from Chevie (...)

* Crystals:
  * Implement more models of Crystals?

* Cluster algebras (Christian Stump, Gregg Musiker, Hugh Thomas):
  * #10819: Implementation of the cluster complex
  * #11010: Implementation of the SubwordComplex as defined by Knutson and Miller

  The complete implementation of the core features are merged in Sage-5.9 . A further road map can be found at http://wiki.sagemath.org/combinat/clusteralgebras.

* Modules and vector spaces:
  * #10673: Roadmap for (Combinatorial)FreeModule
  * Tensor products over an algebra, and application to representation theory
  * #9280 graded algebras
  * Graded morphisms of modules (inverse, adjoint, ...)

* Categories & coercion:
  See also the [Categories Road Map](http://trac.sagemath.org/sage_trac/wiki/CategoriesRoadMap)
  * #10668, #10667: Cleanup support for morphisms
   Nicolas Thiéry, Simon King
  * (prototype) Implement multiparameter morphisms
   This could be extracted and finalized without much work
   Nicolas 
  * #8900 (prototype): Implement multiparameter overloaded functions, with explicit registration
   Nicolas Thiery

* Analytic combinatorics:
  * #10669: MacMahon partition analysis, aka Omega operator (Jason Bandlow, Greg Musiker)
  * #10519 (needs review): Computation of asymptotics for multivariate rational fractions
  * #11515: guessing formulas for sequences (Martin Rubey?)
  * automatic summation (Burcin Erocal)

* Posets:
  * Support for lazy/infinite posets

* Enumerative combinatorics
  * #10662: Improve combinatorial species / decomposable classes
  * Refactoring
    * #12955, #12956: let categories override `__getitem__` and `__len__`
    * #12957: Categories for finite (enumerated) sets
    * #12913: Deprecate CombinatorialClass in favor of the EnumeratedSet's categories
    * #5268: Further cleanup of Enumerated sets
    * #10194 (needs review): Set factories (Florent Hivert)
    * Fix everything from: http://wiki.sagemath.org/combinat/Weirdness
      In particular cleanup permutations!!!!
  * Optimization
    * use ClonableIntArray and friends for all combinatorial object: permutations, partitions, compositions...
  * Trees (Florent Hivert):
    * #13987 Combinatorial m-ary trees

* Dynamics (Vincent Delecroix)
  * Rauzy fractals, ...
  * Flat surfaces, origamis
  * Interval exchange transforms

* Words and languages (Vincent Delecroix, Thierry Monteil, ...):
  * Languages
  * Categorification

* Automorphic Forms, Combinatorial Representation Theory, and Multiple Dirichlet Series
  ICERM http://icerm.brown.edu/sp-s13/
* Tutorials
  * Merge in Sage as many of our tutorials
    * Notebook and help (is this a tutorial or a primer?)
    * Programming in Sage and Python
    * Calculus and Linear algebra
    * Combinatorics (to be taken from «Calcul Mathématique Avec Sage»)
      NicolasThiery and Hugh Thomas

* Sage-Combinat workflow:
  * Write down the properties we want our workflow to have, and improve it!

## History

* 2014-2015:
  * Modules & vector spaces:
    * #11111: More support for finite dimensional free modules and algebras
    * #8678: module morphisms (tensor products, inverses, ...)
  * Categories & coercion:
    * #10963: More functorial constructions (Nicolas Thiéry)
  * Quivers and path algebras:
    * #12630: Representations of quivers and quiver algebras (Jim Stark)
  * Refactoring:
    * #10534: Optimizations for the generation of subwords, subsets, and set partitions (VincentDelecroix)
  * Posets:
    * #12916: Dedekind-MacNeille completion of finite posets
  * Trees:
    * #11529: Rooted_trees
    * #14498: trees and binary trees
    * #14564: BinaryTree().graph()

* 2013:
  * Symmetric functions and generalizations:
    * #9194: Expose and extend the thematic tutorial on symmetric functions
    * #7980: Refactor SymmetricFunctions using «multiple realizations» and deprecate SFASchur and friends
    * #11563: Make lrcalc a standard package
    * #12924: SchubertPolynomialRing causes symmetrica and Sage to crash on bad input
    * #12525: SFAHomogeneous does not work with RealField
  * #11929: Implement quasi-symmetric functions (JasonBandlow, Franco Saliola, Chris Berg, Mike Zabrocki)
  * #8899: Implement Non Commutative Symmetric Functions (JasonBandlow, Franco Saliola, Chris Berg, LenniTevlin, MikeZabrocki)
  * #15150: Implement NCSym (Travis Scrimshaw, Mike Zabrocki, Franco Saliola)
  * Monoids, algebras, and their representation theory:
    * #6654: new features in group algebra category Valentin Feray
    * Free monoids, free groups (#12339), free algebras (see #7797)
    * #7797: Full interface to letterplace from singular
  * Root systems, Coxeter groups, and Hecke algebras:
    * Root systems:
      * #12882: Allows a generalized Cartan matrix as input for Dynkin diagrams
        Christian Stump
      * Constructing a root/coroot lattice realization from a pair of matrices
        Christian Stump
      * #12838: Root poset should treat type A1 properly
        Christian Stump
    * Coxeter groups, reflection groups:
      * Computation of reflection degrees from positive roots (easy)
      * #8359: permutation representation of a Coxeter group, using GAP3
      * #12912: Interface to Coxeter 3 from Fokko Ducloux (MikeHansen)
      * #12774: various enhancements for Coxeter and Weyl groups
    * #8327: implement the universal cyclotomic field, using the Zumbroich basis (Christian Stump)
    * #14261: Implement the many realizations of the Hecke algebra (Brant Jones, Andrew Mathas)
  * Crystals:
    * #11305: Bijection between Rigged Configurations and Crystal Paths (Travis Scrimshaw)
    * #12251: Implementation of Littelmann path model for crystals (Anne Schilling, Mark Shimozono, Reda Chhaibi)
    * #13872: All affine type bijections between rigged configurations and tensor products of KR tableaux (Travis Scrimshaw)
    * #14130: Implementation of generalized Young wall model for affine type A crystals (Lucas Roesler, Ben Salisbury, Travis Scrimshaw)
    * #14192: Implementation of marginally large Young tableaux model for crystals of type A, B, C, D, and G (Ben Salisbury, Travis Scrimshaw)
    * #14413: Implementation of elementary crystals (Ben Salisbury)
    * #14759: Implementation of modified Nakajima monomial model for crystals (Arthur Lubovsky, Ben Salisbury)
  * Cluster algebras (Christian Stump, Gregg Musiker, Hugh Thomas):
    * #13425: Implementation of mutation type checking
    * #13424: Implementation of mutation classes
    * #13369: Implementation of the class ClusterSeed (reviewed by Salvatore Stella)
    * #10538: Implementation of the class ClusterQuiver (reviewed by Dylan Rupel)
    * #10527: Implementation of the class QuiverMutationType
    * #12587: Simplicial complexes lack hash function
    * #11523: Implementation of Cohen-Macaulay test for simplicial complexes
  * Categories and coercion:
    * #7420: Use breath-first-search or Dijkstra in coercion, as discussed (Nicolas Thiery)
    * #11935: Make parent/element classes independent of base rings (SimonKing, NicolasThiery)
  * Analytic combinatorics:
    * #11641 (prototype): guesser of combinatorial statistics, http://www.findstat.org (Chris Berg, Franco Saliola, Christian Stump)
    * #10358 (needs_finalization): The sloane_find command is now completely broken (Thierry Monteil)
  * Posets:
    * #12848: Bug in order_ideal_complement_generators: 'down' (Franco, Anne)
    * #13240 poset polynomials
  * Enumerative combinatorics:
    * #11407: Add normalization to clonable lists (Florent Hivert)
    * #8703: Improve Trees (Florent Hivert)
    * #10193: graded/... enumerated sets
    * #6538: Reimplement from scratch IntegerListsLex, fixing its 8-year old bugs
    * #6812: Enumerate integer vectors modulo to the action of a Permutation Group (Nicolas Borie)
    * #12250: Combinatorics of k-tableaux and the like (Anne Schilling, Mike Zabrocki)
    * #14141: Implementation of Knutson-Tao puzzles (Franco Saliola, Anne Schilling, Allen Knutson, Avi Dalal)
  * #11688 graded modules
  * Trees:
    * #15121 (a quick way to create trees)

* 2012:
  * Optimizations:
    * #11115: Rewrite cached_method in Cython
  * Symmetric functions and generalizations:
    * #10333: An interface to Anders Buch's Littlewood-Richardson Calculator ``lrcalc``
  * Categories: #9469, #8119, #12527, #12877, #11943
  * #4539: Plural wrapper for skew commutative Gröbner bases
  * Coercion: #11250, #11257
  * Enumerated sets: #11118
  * Posets: #10998 (Categorification), #12476, #12677, #10670, #11382,
    #12536 (Linear extensions), #12831 (products)
  * Modules and vector spaces: #12464, #12484, #12489, #12528
  * Root systems:
    * #12667: RootLatticeRealizations: infinite loops while trying to reflect to the positive chamber
    * #10817: Generalized associahedron as a polyhedral complex
    * #6588: Categorification of root systems
  * Quivers: #10349, #10347
  * Sphinx, Documentation: #9128, #12717, #12849, #12490
  * #7980: Implement generic support for parents with (multiple) realizations

* 2011:
  * #8702: Fast datastructure for (combinatorial) objects with prototype (clone) design pattern (Florent Hivert)
  * #11290: Implementation of non-commutative k-Schur functions in the nilCoxeter algebra (Anne Schilling, Chris Berg)
  * Documentation: #11251, #11282
  * Debugging, profiling: #11287
  * Installation: #11296
  * Posets: #10065, #11293
  * Combinatorics: #11300, #11301, #11314
    * #11742, #11700: Cores (Anne Schilling)
    * #10155: Cyclic sieving phenomenon (Christian Stump)
  * Certainly many more!
  * Crystals:
    * #11546: Energy function for Crystals (Anne Schilling)
    * #11183: Stembridge rules (Tom Denton)
    * #10485: Thematic tutorial (Anne Schilling)
    * #10446: Schutzenberger involution, promotion, etc (Anne Schilling)
    * #8442: Lie tutorial (Dan Bump)

* 2010:
  * [The road map in May 2010 (Sage Days 20.5, Toronto)](http://trac.sagemath.org/sage_trac/attachment/wiki/SageCombinatRoadMap/P1050207.JPG)
  * Symmetric functions:
    * #8259: Conversion from symmetric polynomials to basis of monomial symmetric functions
    * #8259, #9755, #12381
  * Root systems, crystals, ...
    * #8984: Implementation of the Lenart--Postnikov alcove path crystal
    * #8380: Interface with GAP3
    * #8911: Categorification of Crystals
    * #8810: Stanley symmetric functions
    * #8811: Translation for elements of a root lattice and related features and fixes
  * Categories, parents, elements:
    * #8001: Stronger category tests
    * #7921: Categories for extension types via `__getattr___`
    * #8044: Categories for finite/permutation/symmetric groups
    * #9138, #9056, #8917, #8913, #8579
    * #8120: UniqueRepresentation and hash value
    * #8028: Improvements to element_wrapper
    * #12645, ...
  * Modules and vector spaces:
    * #8876: Triangular morphisms with domain and codomain having different index sets
    * #7914: Triangular isomorphisms of free modules
    * #7938: swap_term_and_monomial
    * #9651: Addition on CombinatorialFreeModule directly on dictionaries (closed: fixed)
    * #9648: ModulesWithBasis allows module_morphism's to a wider class of ... (closed: fixed)
  * Graphs:
    * #7004: Refactor the graph layout code, and add interface with graphviz for acyclic layout
    * #10723 + massive amount of work by Nathann Cohen
  * Enumerated sets:
    * #8519: NN, NonNegativeIntegers, PositiveIntegers, IntegerRange
      Nicolas Borie
    * #6655: Cleanups and new features about corners and cells in partition and tableau
    * #6775: Disjoint set data structure
  * Words:
    * words bug : #8095 (word morphism is primitive), #8140 (sturmian words definition), #8186 (length handling), #8215 (empty word), #8232 (cmp bug), #7520 (word construction)
    * words enhancement : #8187 (equality of words), #8268 (speed up christoffel words), #8287 (_check function), #8289 (word morphism call function), #7619 (pickle for word defined by callable or iterator), #8233 (concatenation), #8266 (documentation)
    * words new functions : #8093, #8127, #8227
    * #8595, #8618, #8574, #8673 and #8674 (misc defect fixes)
    * #8429 (Split word.py file into 4 files)
    * #8604 (Add a class for factor-enumerable words)
    * #8407 and #8670 (new methods for word paths)
    * #8287 (_check makes it slower)
    * #8431 (Rauzy fractal (discrete planes and broken lines)

* 2009:
  * Category framework (#5891, #7251, #7443) (NicolasThiéry, ...)
  * Cleanup and refactoring of root systems and Coxeter groups (#4326, #4327, #4608, #7753, #7754), Weyl characters (#5794) and crystals (#4311,#5729,#3663, #5002, #5729, #5879) (AnneSchilling, DanBump, NicolasBorie, StevenPon, NicolasThiéry, ...)
  * Cleanup and refactoring of combinatorics (#4549, #5200, #5308, #5487, #5534, #5551, #5781, #5600, #6000, #7403, #7395, #7396, #7397) (FlorentHivert, NicolasThiéry, ...)
  * #6136: Implementation of FreeModule / Hopf algebra framework
  * Refactoring of symmetric functions (#5457, #6137, #7777) (NicolasThiéry, JasonBandlow)
  * #6138: Refactoring of the SymmetricGroupAlgebra to use categories and free modules
  * Words, ...
  * Families: #5538, #7208, ... (FlorentHivert)
  * TestSuites: #6097, #6809, #6343, #7478 (NicolasThiéry)
  * Technical patches:  #5120, #5405, #5449, #5598, #5783,  #5843, #5920,
    #5967, #5979, #5985, #5986, #5991, #6000, #6097, #7420, #7421, #7776, #7928, #7842 (NicolasThiéry, ...)
  * Partial support for Iwahori Hecke algebras for all types: #7729 (DanielBump, AnneSchilling, NicolasThiéry)
  * July: [FPSAC'09](http://wiki.sagemath.org/combinat/FPSAC09) (RISC, Linz, Austria)
    * Goal: Most features ported
    * Goal: Most of the research done with Sage-Combinat
  * Goal: All new users can start directly with Sage

* 2008: Switching to Sage!
  * October: Sage Days 10 (Nancy, France)
  * Get the core MuPAD-Combinat developers started with Sage
  * Design, prioritization, planning
  * Design of the categories and (Hopf) algebra framework using the new coercion system

  * September: announcement that Sciface is purchased by Mathworks (Matlab).
  * MuPAD does not qualify anymore as a "reasonably priced high quality computer algebra system".
  * Sciface cancels its formerly liberal licence policy for MuPAD-Combinat developers.
  * Plan for a final stable release of MuPAD-Combinat dropped.

  * Port of decomposable objects (from MuPAD-combinat) / species (from aldor-combinat) by Mike Hansen, funded by Google Summer of Code
  * June 24th, FPSAC (Valparaiso, Chile):
  * Official announcement of the migration
  * Goal: elementary combinatorics users can start directly with Sage

  * June 19th: Visit of Florent to Davis. Final decision to migrate!

  * May: Fixed several of the Weirdness issues (#3286, JasonBandlow)

  * Spring, in particular at MSRI (Berkeley, USA):
  * Long discussions within the community about the opportunity to switch
  * Port of root systems (#2808, #2809, #2864, #2868, #2874, #2964, #3660, #3664, NicolasThiéry, DanBump, JustinWalker, MikeHansen, TomDenton)
  * Further port and extensions to the crystals library (#2868,#3032,#3417,#3418,#3660, AnneSchilling, DanBump, JustinWalker, BrantJones)
  * Basic setup for FreeModule's
  * Posets (FrancoSaliola)
  * Created the '[Weirdness](http://wiki.sagemath.org/combinat/Weirdness)' web page

  * February: Sage Days 7 (Los Angeles)
  * Technical experimentation with Sage to see how fit it is for our purposes.
  * Partial port of the crystals library (#2742, AnneSchilling and NicolasThiéry)
  * Implementation of Xin's Omega algorithm by Jason and Greg #10669

  * January: presentation of MuPAD-Combinat at the AMS meeting in San-Diego; meeting and discussions with the Sage team
* 2007: Early contacts with Sage
  * June: design discussions between Nicolas and Mike at the Axiom Workshop 2007

  * February: First contact with Mike Hansen who wanted to port some features of MuPAD-Combinat, which we very much encouraged.
    In the following month,  Mike translated 30k lines of code, which accounts for most of the basic combinatorics (tableaux, permutations, ...), and symmetric functions.
* 2006-2008: Aldor-Combinat
  * Species (Martin Rubey, Ralf Hemmecke)
* 2000-2008: 100k lines of code in MuPAD-Combinat, 20 contributers, 25+ papers
  * Symmetric functions (François Descouens, NicolasThiery, ...)
  * NCSF, QSym, Hopf algebras, Kac algebras (Florent Hivert, NicolasThiery)
  * Operads (Frédéric Chapoton)
  * Quivers and path algebras (Patrick Le Meur)
  * Crystals (Anne Schilling, ...)
  * Root systems, Weyl groups (NicolasThiery, ...)
  * Representation theory of algebras (Florent Hivert, ...)
  * Enumerative combinatorics (tableaux, compositions, integer vectors, trees, ...)
  * Decomposable classes/species (NicolasThiery, FlorentHivert, Sébastien Cellier, Paul Zimmermann...)
  * Coercion system (NicolasThiery)
  * Categories for algebraic combinatorics (NicolasThiery)
  * Graph & Graphviz (Teresa Gomez Diaz)
* December 2000: Birth of [MuPAD-Combinat](http://mupad-combinat.sf.net/)
---

Attachments:
 * [P1050207.JPG](SageCombinatRoadMap/P1050207.JPG)
