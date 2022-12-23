# Issue 1101: new gap_packages*

Issue created by migration from https://trac.sagemath.org/ticket/1101

Original creator: wdj

Original creation time: 2007-11-04 22:01:06

Assignee: wdj

I made a new optional gap_packages* at
http://sage.math.washington.edu/home/wdj/patches/gap_packages-4.4.10_2.spkg

Summary:

This directory contains several "official" and "undeposited"
GAP packages available from 
http://www.gap-system.org/Packages/packages.html. They are
all released under the GPL with the following exception:
(*) grape contains Brendon McKay's nauty program. 

To load a package, for example grape, into SAGE type

sage: gap('LoadPackage("grape")')

All these packages come with documentation in the
doc or htm subdirectory (e.g., for grape, it would be in
SAGEHOME/local/lib/gap-4.4.10/pkg/grape/htm). After loading all
the packages, you can type gap_reset_workspace()
so you don't have to reload them again.

A brief description of each package follows:

braid is a GAP package for computing with braids, covering curves, 
and Hurwitz spaces.
(Authors: K. Magaard, S. Shpectorov and H. Voelklein)

crime - package to compute the cohomology ring of finite
p-groups, induced maps, and Massey products.
(Author: Marcus Bishop)

cryst - Computing with crystallographic groups
(Authors: Bettina Eick, Franz Gähler, Werner Nickel)

CTblLib - The GAP Character Table Library
(Author: Thomas Breuer)

DESIGN is a package for classifying, partitioning and studying block designs.
(Author: Leonard H. Soicher)

FactInt is a package providing routines for factoring integers, in particular:
    * Pollard's p-1
    * Williams' p+1
    * Elliptic Curves Method (ECM)
    * Continued Fraction Algorithm (CFRAC)
    * Multiple Polynomial Quadratic Sieve (MPQS)
(Author: Stefan Kohl)

GAPDoc is a package containing a definition of a structure for 
GAP documentation, based on XML. It also contains conversion 
programs for producing text-, DVI-, PDF- or HTML-versions of such 
documents, with hyperlinks if possible.
(Authors: Frank Luebeck, Max Neunhoeffer)

GRAPE is a package for computing with graphs and groups, and is primarily 
designed for constructing and analysing graphs related to groups, 
finite geometries, and designs.
(Author: Leonard H. Soicher)

HAP (Homological Algebra Programming) is a GAP package 
providing some functions for group cohomology computation. 
(Author: Graham Ellis)

HAPcryst - an extension package for HAP, which allows for
group cohomology computation for a wider class of groups.
(Author: Marc Roeder)

LAGUNA - this package provides functionality for calculation of the 
normalized unit group of the modular group algebra of the finite 
p-group and for investigation of Lie algebra associated with group 
algebras and other associative algebras.
(Authors :Victor Bovdi, Alexander Konovalov, Richard Rossmanith, 
Csaba Schneider)

polymake - an interface with the (standalone) polymake program
used by HAPcryst. 
(Author: Marc Roeder)

SONATA ("System Of Nearrings And Their Applications") is a package 
which constructs finite nearrings and related objects.
(Authors: Erhard Aichinger, Franz Binder, Jürgen Ecker, Peter Mayr, 
Christof Noebauer)

TORIC is a GAP package for computing with toric varieties.
(Author: David Joyner)



---

Comment by was created at 2007-11-04 22:06:29

NOTE to self: when putting this package into the optional repo, be sure
to modify spkg-install to touch $SAGE_LOCAL/bin/gap_stamp


---

Comment by mabshoff created at 2007-12-22 15:14:36

Resolution: fixed


---

Comment by mabshoff created at 2007-12-22 15:14:36

The optional spkg has been put in the repo and mirrored out.
